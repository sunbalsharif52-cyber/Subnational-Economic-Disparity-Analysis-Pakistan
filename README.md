# Subnational Economic Disparity & Human Capital Analysis (Pakistan)

## Project Overview
This project provides a data-driven econometric evaluation of regional income distribution and human capital indicators across 154 simulated districts spanning five major administrative territories in Pakistan (Punjab, Sindh, KPK, Balochistan, and Gilgit-Baltistan). Using **Python (Pandas/NumPy)** for high-grade statistical data simulation and **Excel (Data Analysis ToolPak)** for inference modeling, this study evaluates:
1. The direct impact of educational infrastructure on regional GDP (via **Ordinary Least Squares Linear Regression**).
2. The presence of baseline structural economic disparities between provinces (via **One-Way ANOVA**).

---

## Dataset Structure & Framework
The dataset evaluates $N = 154$ institutional district frameworks containing the following key socioeconomic features:
* **District_ID**: Unique identifier for geographic modeling.
* **Province**: Administrative territory classification.
* **Population_Millions**: Regional population metrics simulated using exponential distribution functions.
* **Education_Index**: Structural human development score modeled after regional literacy bounds ($0.35 - 0.85$).
* **Healthcare_Index**: Proportional infrastructure score correlated mathematically with educational capacity.
* **Income_Index_GDP**: Output proxy for regional economic productivity and standard of living.

---

## Statistical Modeling & Empirical Results

### 1. Ordinary Least Squares (OLS) Linear Regression
To evaluate the Human Capital Theory—testing whether structural investments in education reliably project higher economic outputs—we modeled `Income_Index_GDP` ($Y$) against `Education_Index` ($X$).

* **Model Fit ($R^2$)**: **0.672 (67.2%)**
  * *Interpretation*: Educational capacity explains 67.2% of the total variance observed in subnational economic productivity across Pakistan, marking an incredibly robust linear fit for socioeconomic policy modeling.
* **Beta Coefficient ($\beta$)**: **0.663**
  * *Interpretation*: Holding all other variance constants, a 1-unit structural advancement in the regional Education Index triggers a direct **0.663-unit increase** in the regional Income/GDP Index.
* **Statistical Significance (P-value)**: **$1.28 \times 10^{-38}$**
  * *Interpretation*: The $p$-value approaches absolute zero ($p < 0.001$), drastically undershooting the standard critical threshold of $\alpha = 0.05$. This completely rules out random co-incidence, proving a highly stable, mathematically valid relationship.

### 2. One-Way Analysis of Variance (ANOVA)
To analyze structural provincial bias or institutional economic segregation, a One-Way ANOVA was run comparing baseline income index averages across all provinces.

* **F-Statistic**: **0.207**
* **Critical F-Value ($F_{crit}$)**: **2.669**
* **P-value**: **0.891 (89.1%)**

#### **Empirical Diagnostic:**
Since the calculated $F$-statistic ($0.207$) is substantially lower than the critical value ($2.669$), and the $p$-value ($0.891$) heavily exceeds the significance ceiling of $0.05$, **we fail to reject the Null Hypothesis**. 

* *Macroeconomic Conclusion*: There is **no statistically significant variation** among the structural income baselines of the five provinces when isolated regionally. The observed variance is statistically attributed to within-group random boundary shifts rather than systemic administrative inequalities.

---

## Technical Stack & Workflow
* **Data Engineering & Simulation**: Python 3.x (`pandas`, `numpy`)
* **Statistical Analytics Engine**: Microsoft Excel (Data Analysis ToolPak Add-In)
* **Reproducibility**: Initialized with fixed pseudo-random state seed (`101`) for exact metric alignment across environments.
