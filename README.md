# Bus Fleet Transit Optimization: Multi-Objective Integer Programming

## Project Overview
This project focuses on the strategic reallocation of a 39-bus transit fleet for a student organization. Using **Python** and the **Gurobi**, the system minimized individual service time of each student and then went more in depth, making sure there werent any major trade-offs to complete the task.

### Phase 1: Baseline Efficiency
The primary goal was to minimize the average individual service time for the entire student population across multiple clubs.
* **Mechanism:** Optimized the selection from 78 feasible routing solutions and 5 distinct bus capacities (14, 15, 24, 30, and 66 seats).
* **Implementation:** Developed a model linking binary route selection ($x_r$) with integer bus assignments ($y_{cj}$), ensuring all student demand was met within physical fleet constraints.

### Phase 2: Fairness & Capacity Retention
Recognizing that global optimization can often lead to "losers" at specific hubs, this phase introduced **Multi-Objective Optimization** to ensure equitable service.
* **Minimax Objective:** Introduced an auxiliary variable ($z$) to minimize the **worst-case seat capacity loss** across all clubs.
* **Trade-off Modeling:** Analyzed the sensitivity of the system using a $\beta$ parameter to explore the **Pareto frontier** between system-wide capacity and individual club fairness.
* **Constraint Engineering:** Implemented strict service-time thresholds ($\alpha$) to ensure that "fairness" improvements did not degrade overall system performance beyond acceptable limits.

---

* **Decision Variables:**
    * $x_{r} \in \{0, 1\}$ : Binary variable; 1 if route solution $r$ is selected, 0 otherwise.
    * $y_{cj} \in \mathbb{Z}$ : Integer variable; number of buses of capacity $j$ assigned to club $c$.
    * $z \ge 0$ : Auxiliary variable capturing the maximum localized seat loss.

* **Core Constraints:**
    * **Demand Satisfaction:** Every club must be assigned exactly one feasible routing solution.
    * **Fleet Capacity:** Total buses used cannot exceed the available inventory for each of the five capacity tiers.
    * **Resource Alignment:** Links selected route solutions to the specific bus types required for those routes.

---

## Repository Structure
* `src/`: Jupyter Notebooks covering Phase 1 (Baseline) and Phase 2 (Fairness/Multi-objective).
* `docs/`: Technical reports detailing mathematical proofs and sensitivity analysis results.
* `data/`: Mock data representation

## Contributions
This project was a collaborative effort completed at the **Georgia Institute of Technology** for ISYE 3133 (Optimization).

**My Contributions:**
* **System Modeling:** Defined and formalized the core **decision variables** ($x_r, y_{cj}$) and **objective functions** for both system efficiency and fairness models
* **Constraint Engineering:** Designed and implemented the mathematical **constraint statements** ensuring demand satisfaction, fleet capacity limits, and resource alignment
* **Linearization:** Aided in the translation of  "Minimax" fairness goals into linear constraints ($z$) to ensure model feasibility within the Gurobi solver
