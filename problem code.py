import pulp
import pandas as pd

def get_patterns_for_stock(s_width, widths, min_w):
    valid_patterns = []
    def find_combos(idx, current_sum, counts):
        if idx == len(widths):
            waste = s_width - current_sum
            if 0 <= waste < min_w:
                valid_patterns.append(tuple(counts))
            return
        max_c = (s_width - current_sum) // widths[idx]
        for c in range(max_c + 1):
            find_combos(idx + 1, current_sum + c * widths[idx], counts + [c])
    find_combos(0, 0, [])
    return valid_patterns

def run_interactive_solver():
    print("---  Cutting Stock Solver (Terminal Version) ---")
    
    try:
        # 1. USER INPUTS
        stock_raw = input("Enter Master Roll Widths (comma separated, e.g., 20, 22): ")
        stock_options = [int(s.strip()) for s in stock_raw.split(",")]

        items_raw = input("Enter Required Item Widths (comma separated, e.g., 9, 8, 7): ")
        items = [int(i.strip()) for i in items_raw.split(",")]

        demands = {}
        print("\nEnter Demands for each width:")
        for w in items:
            demands[w] = int(input(f"  How many pieces of {w} inch? "))

        min_width = min(items)
        all_results = []

        # 2. OPTIMIZATION LOGIC
        for s_width in stock_options:
            patterns = get_patterns_for_stock(s_width, items, min_width)
            prob = pulp.LpProblem(f"Minimize_{s_width}", pulp.LpMinimize)
            x = pulp.LpVariable.dicts("P", range(len(patterns)), lowBound=0, cat='Integer')
            
            prob += pulp.lpSum([x[i] for i in range(len(patterns))])
            
            for i, width in enumerate(items):
                prob += pulp.lpSum([patterns[j][i] * x[j] for j in range(len(patterns))]) >= demands[width]
            
            prob.solve(pulp.PULP_CBC_CMD(msg=0))
            
            if pulp.LpStatus[prob.status] == 'Optimal':
                res_details = []
                for i, p in enumerate(patterns):
                    qty = pulp.value(x[i])
                    if qty and qty > 0:
                        waste = s_width - sum(p[j] * items[j] for j in range(len(items)))
                        res_details.append({"Pattern": dict(zip(items, p)), "Rolls": int(qty), "Waste": waste})
                
                all_results.append({
                    'Stock': s_width,
                    'Total_Rolls': int(pulp.value(prob.objective)),
                    'Total_Material': int(pulp.value(prob.objective) * s_width),
                    'Details': res_details
                })

        # 3. DISPLAY RESULTS
        if all_results:
            print("\n" + "="*60)
            print("RESULTS SUMMARY")
            df = pd.DataFrame(all_results).drop(columns=['Details'])
            print(df.to_string(index=False))

            winner = min(all_results, key=lambda x: x['Total_Material'])
            print(f"\n BEST OPTION: {winner['Stock']} inch stock")
            print("-" * 30)
            print(pd.DataFrame(winner['Details']).to_string(index=False))
        else:
            print("\n No valid solution found. Make sure master rolls are wider than items.")

    except ValueError:
        print("\n Invalid Input! Please enter numbers only.")

if __name__ == "__main__":
    run_interactive_solver()