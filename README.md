# 🏭 Industrial-Cutting-Slitting-Optimizer

🌐 **Live Application:** https://cuttingstock.streamlit.app/

---

## 📌 Project Overview

This project was developed after studying the production planning and slitting operations of a small-scale manufacturing industry. During the industrial study, it was observed that cutting patterns for master reels were generated manually using spreadsheets and operator experience.

While the existing process was able to satisfy customer demand, generating and evaluating cutting patterns required significant manual effort, especially when multiple slit widths and order quantities were involved.

To simplify this process, a web-based **Industrial Cutting & Slitting Optimization System** was developed. The application automatically generates feasible cutting patterns and identifies an optimized production plan using **Integer Linear Programming (ILP)** and the **CBC Solver**.

The system acts as a decision-support tool that helps planners evaluate alternatives quickly, reduce manual calculations, and make production planning decisions more efficiently.

---

## 🎯 Problem Statement

Manufacturing industries that convert large master reels into smaller slit widths must satisfy customer demand while minimizing trim loss.

In many small and medium-scale industries, production planners:

* Generate cutting patterns manually
* Use spreadsheet-based calculations
* Rely on practical experience for pattern selection
* Compare master reel options manually

As the number of slit widths and order quantities increases, evaluating all feasible cutting combinations becomes time-consuming.

This project automates that planning process by generating feasible cutting patterns and recommending optimized reel allocations through mathematical optimization.

---

## 🏭 Industrial Context

The project is inspired by real industrial operations where:

* Large master reels are procured from suppliers.
* Customer orders require different slit widths.
* Production planners manually evaluate cutting patterns.
* Multiple master reel options must be compared before production.

The objective is to determine:

> Which master reel width should be selected, and how should it be cut to satisfy customer demand efficiently?

Rather than replacing production expertise, the system assists planners by automating calculations and optimization tasks.

---

## 🚀 Live Demo

### Streamlit Application

🔗 https://cuttingstock.streamlit.app/

Users can directly test different:

* Master reel widths
* Customer slit sizes
* Demand quantities

and instantly receive optimized production recommendations.

---

## 🛠 Technologies Used

| Technology | Purpose                     |
| ---------- | --------------------------- |
| Python     | Core Development            |
| Streamlit  | Web Application             |
| PuLP       | Optimization Modeling       |
| CBC Solver | Integer Programming Solver  |
| Pandas     | Data Processing & Reporting |

---

## ⚙️ Methodology

### 1. Input Collection

The planner enters:

* Available Master Reel Widths
* Customer Slit Widths
* Demand Quantity

Example:

```text
Master Reel Widths:
20 mm, 22 mm

Customer Sizes:
9 mm, 8 mm, 7 mm, 6 mm

Demand:
9 mm → 511
8 mm → 301
7 mm → 263
6 mm → 383
```

---

### 2. Cutting Pattern Generation

A recursive backtracking algorithm generates all feasible cutting patterns for a given master reel width.

Example:

```text
(0,0,2,1)
(0,1,0,2)
(2,0,0,0)
```

Each tuple represents the number of slits of each customer width produced from a single master reel.

---

### 3. Industrial Feasibility Validation

A cutting pattern is accepted only when:

```text
Remaining Scrap < Minimum Slit Width
```

This ensures that no additional valid slit can be produced from the remaining material.

Benefits:

* Eliminates impractical patterns
* Improves pattern quality
* Ensures realistic production recommendations

---

### 4. Optimization Using ILP

The problem is formulated as an **Integer Linear Programming (ILP)** model.

#### Objective

Minimize:

* Total reels required
* Material consumption
* Trim loss

#### Constraints

* Customer demand must be satisfied
* Reel allocations must be integers
* Only feasible cutting patterns can be selected

---

### 5. CBC Solver

The optimization model is solved using the **CBC Branch-and-Cut Solver**.

Benefits:

* Evaluates thousands of possible allocations
* Produces optimized reel allocations
* Reduces manual trial-and-error calculations
* Provides consistent planning recommendations

---

## 📊 Output Dashboard

For each master reel option, the application provides:

### Total Reels Needed

Number of reels required to satisfy customer demand.

### Gross Material Consumption

```text
Total Reels × Reel Width
```

### Net Trim Loss

Total scrap generated during production.

### Pattern Allocation Table

Displays:

* Cutting Pattern
* Scrap per Reel
* Total Run Scrap
* Reel Set Count

---

## 📈 Sample Result

### 20 mm Master Reel

| Metric         | Value    |
| -------------- | -------- |
| Total Reels    | 601      |
| Gross Material | 12020 mm |
| Trim Loss      | 865 mm   |

### 22 mm Master Reel

| Metric         | Value    |
| -------------- | -------- |
| Total Reels    | 532      |
| Gross Material | 11704 mm |
| Trim Loss      | 544 mm   |

### Recommendation

✅ **22 mm Master Reel**

Because it provides:

* Lower material consumption
* Lower trim loss
* Better reel utilization

---

## 💡 Key Features

### Automatic Pattern Generation

Generates feasible cutting patterns automatically.

### Industrial Feasibility Filter

Rejects inefficient cutting combinations.

### Optimization-Based Planning

Uses mathematical optimization to determine reel allocations.

### Pattern Explosion Safety Brake

To prevent excessive computation:

```text
Maximum Pattern Limit = 50,000
```

If the limit is exceeded, optimization stops and alerts the user.

### Master Reel Comparison

Allows planners to compare multiple master reel widths and select the most suitable option.

---

## 📉 Business Impact

The developed system helps industries:

* Reduce planning effort
* Automate cutting pattern generation
* Save time during production planning
* Reduce manual calculations
* Improve consistency in decision-making
* Compare alternative master reel options quickly

---

## 📜 Conclusion

This project demonstrates how **Operations Research**, **Industrial Engineering**, and **Optimization Techniques** can be applied to automate a real-world production planning task.

By replacing manual pattern generation and evaluation with an optimization-driven decision-support system, production planners can generate feasible cutting plans faster, compare multiple reel options efficiently, and make more informed planning decisions.
