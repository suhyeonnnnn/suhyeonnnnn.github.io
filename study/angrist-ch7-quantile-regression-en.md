---
layout: default
title: "Angrist Chapter 7: Quantile Regression Study Guide"
lang: en
---

# Chapter 7: Quantile Regression Study Guide

---

## Key Concepts Overview

### Why Quantile Regression?

> "95% of applied econometrics is concerned with averages. But what if we want to know what's happening to the entire distribution?"

**Limitations of OLS**:
- Estimates only average effects
- Cannot detect distributional changes (spreading, compression)
- Cannot analyze inequality changes

**Advantages of Quantile Regression**:
- Estimates effects at multiple points (10th percentile, median, 90th percentile, etc.)
- Enables inequality analysis
- Controls for covariates similar to OLS

---

## 7.1 Quantile Regression Model

### Conditional Quantile Function (CQF)

**Definition**:
```
Q_τ(y_i | X_i) = F_Y^{-1}(τ | X_i)
```

| τ value | Meaning |
|---------|---------|
| τ = 0.10 | Lower decile |
| τ = 0.50 | Median |
| τ = 0.90 | Upper decile |

### CEF vs CQF Comparison

| | CEF (OLS) | CQF (Quantile Reg) |
|---|---|---|
| **Definition** | E[y_i \| X_i] | Q_τ(y_i \| X_i) |
| **Minimization** | E[(y_i - m(X_i))²] | E[ρ_τ(y_i - q(X_i))] |
| **Loss function** | Squared error | Check function ρ_τ |
| **Estimates** | Conditional mean | Conditional quantile |

### Check Function (ρ_τ)

```
ρ_τ(u) = u · (τ - 1(u ≤ 0))
       = τ·u        if u > 0
       = (τ-1)·u    if u ≤ 0
```

**Intuition**: Asymmetric weighting on positive/negative residuals

| τ value | Weight on positive | Weight on negative | Result |
|---------|-------------------|-------------------|--------|
| 0.5 | 0.5 | 0.5 | Median (LAD) |
| 0.9 | 0.9 | 0.1 | Upper quantile |
| 0.1 | 0.1 | 0.9 | Lower quantile |

### Quantile Regression Estimation

**Population problem**:
```
β_τ = arg min_{b∈R^d} E[ρ_τ(y_i - X_i'b)]
```

**Sample analog**: Solvable via linear programming

Linear model assumption:
```
Q_τ(y_i | X_i) = X_i'β_τ
```

---

## Location Shift vs Heteroskedasticity

### Case 1: Location Shift (Homoskedastic)

**Model**:
```
y_i ~ N(X_i'β, σ²)
```

**CQF derivation**:
```
P[y_i - X_i'β < σ·Φ^{-1}(τ) | X_i] = τ
```

Therefore:
```
Q_τ(y_i | X_i) = X_i'β + σ·Φ^{-1}(τ)
```

**Characteristics**: 
- Only intercept varies with τ
- **Slope β is identical across all quantiles**
- Within-group inequality unchanged

### Case 2: Heteroskedasticity (Linear Location-Scale Model)

**Model**:
```
y_i ~ N(X_i'β, (X_i'γ)²)
```
where γ > 0, X_i'γ > 0

**CQF derivation**:
```
P[y_i - X_i'β < (X_i'γ)·Φ^{-1}(τ) | X_i] = τ
```

Therefore:
```
Q_τ(y_i | X_i) = X_i'β + (X_i'γ)·Φ^{-1}(τ)
                = X_i'[β + γ·Φ^{-1}(τ)]
```

**Characteristics**:
- **Slope varies with τ**
- τ > 0.5: Slope increases (upper quantiles)
- τ < 0.5: Slope decreases (lower quantiles)
- Within-group inequality varies with X

---

## Empirical Example: Returns to Education (Table 7.1.1)

### Data
- 1980, 1990, 2000 U.S. Census
- White/Black men aged 40-49
- Controls: Race, quadratic in potential experience (age - education - 6)

### Quantile Regression Results by Year

| Census | Mean | SD | 0.10 | 0.25 | 0.50 | 0.75 | 0.90 | OLS |
|--------|------|-----|------|------|------|------|------|-----|
| **1980** | 6.40 | 0.67 | .074 | .074 | .068 | .070 | .079 | .072 |
| **1990** | 6.46 | 0.60 | .112 | .110 | .106 | .111 | .137 | .114 |
| **2000** | 6.50 | 0.75 | .092 | .105 | .111 | .120 | **.157** | .114 |

### Interpretation

**1980**: 
- Coefficients similar across quantiles (~0.07)
- **Location shift** — education shifts wage distribution uniformly
- Within-group inequality unchanged

**1990**:
- Similar pattern (~0.11)
- Only upper decile slightly higher (0.137)

**2000**: 
- **Sharp increase in upper quantile coefficients** (0.09 → 0.16)
- Lower decile: 9.2% vs Upper decile: 15.7%
- **Heteroskedasticity** — education also increases inequality
- "Among the educated, the rich get even richer"

**Policy implications**:
- 1980s-1990s: Overall skill premium increase
- 2000: Within-group inequality also increases
- Suggests fundamental labor market changes (Autor, Katz, Kearney 2005; Lemieux 2008)

---

## 7.1.1 Censored Quantile Regression

### Problem Setting

**Censoring**: Some data is hidden (not the same as limited!)
```
y_{i,obs} = y_i · 1[y_i < c]
```

| Type | Example | Description |
|------|---------|-------------|
| **Top-coding** | CPS high earnings | Privacy protection |
| **Duration censoring** | Unemployment >40 weeks | Follow-up period limit |

**Note**: Different from limited dependent variables (e.g., medical expenditure = 0)!

### Solution: Powell (1986)

**Key insight**: Quantiles **below** censoring point are unaffected

Example: Top 10% censored → Estimation for τ ≤ 0.90 unaffected

**Censored QR model**:
```
Q_τ(y_i | X_i) = min(c, X_i'β_τ)
```

**Estimation**:
```
β_τ^c = arg min_{b∈R^d} E{1[X_i'β_τ^c < c] · ρ_τ(y_i - X_i'b)}
```

Only use observations where X_i'β < c

### Buchinsky (1994) Iterative Algorithm

**Problem**: Don't know which observations have X_i'β < c a priori

**Solution**: Iterative estimation

```
Step 1: Estimate β̂_τ ignoring censoring
Step 2: Find cells with X_i'β̂_τ < c
Step 3: Re-estimate β̂_τ using only those cells
Step 4: Repeat until convergence
```

**Features**:
- Convergence not guaranteed but works in practice
- Bootstrap standard errors
- Buchinsky (1994), Chamberlain (1994): Returns to schooling increase with censoring adjustment

---

## 7.1.2 Quantile Regression Approximation Property

### Theorem 7.1.1 (Angrist, Chernozhukov, Fernandez-Val 2006)

**Assumptions**:
- (i) Conditional density f_Y(y|X_i) exists a.s.
- (ii) E[y_i], E[Q_τ(y_i|X_i)], E||X_i|| are finite
- (iii) β_τ uniquely solves the minimization problem

**Theorem**:
```
β_τ = arg min_{b∈R^d} E[w_τ(X_i, b) · ε_τ²(X_i, b)]
```

where:
- **Specification error**: ε_τ(X_i, β) ≡ X_i'β_τ - Q_τ(y_i|X_i)
- **Weight function**: 
```
w_τ(X_i, β) = ∫_0^1 (1-u) · f_{ε(τ)}(u·ε_τ(X_i,β) | X_i) du
```

**Approximation**:
```
w_τ(X_i, β_τ) ≈ (1/2) · f_Y(Q_τ(y_i|X_i) | X_i)
```

### Intuitive Meaning

| | OLS | Quantile Regression |
|---|---|---|
| **Approximates** | E[y_i \| X_i] | Q_τ(y_i \| X_i) |
| **Weights** | Histogram of X_i | w_τ(X_i) × Histogram |
| **Emphasizes** | Entire X_i distribution | X_i values where y_i is dense near CQF |

**Key point**: Even if CQF is not exactly linear, quantile regression provides the **best linear approximation in a weighted least squares sense**

---

## Figure 7.1.1: QR vs MD vs Nonparametric CQF

### Comparison of Three Estimators

**1980 Census data, dependent variable: log wages, independent variable: schooling**

| Estimator | Method | Features |
|-----------|--------|----------|
| **CQ (Nonparametric)** | Direct quantile computation at each schooling level | Nonparametric, requires large samples |
| **QR (Quantile Regression)** | ρ_τ minimization | Linear model assumption, weighted fit |
| **MD (Minimum Distance)** | Linear regression on CQF | Chamberlain (1994), histogram weighting |

### Minimum Distance (MD) Estimator

**Chamberlain (1994)**:

```
β̃_τ = arg min_{b∈R^d} E[(Q_τ(y_i|X_i) - X_i'b)²]
```

**Interpretation**: Regress Q_τ(y_i|X_i) on X_i → uses histogram weights

**QR vs MD difference**:
- QR: w_τ(X_i) × histogram weighting
- MD: histogram weighting only
- In practice, results are very similar

### Figure Interpretation (Panels A-C)

```
Panel A (τ = 0.10):          Panel B (τ = 0.50):          Panel C (τ = 0.90):
                              
    y│                            y│                            y│
     │    ○○○○                     │      ○○○○                   │        ○○○○
     │  ○○  ──QR                   │    ○○  ──QR                 │      ○○  ──QR
     │○○   ---MD                   │  ○○   ---MD                 │    ○○   ---MD
     │    ○=CQ                     │○○    ○=CQ                   │  ○○    ○=CQ
     └──────────── school          └──────────── school          └──────────── school
```

- ○ = Nonparametric CQF (cell-by-cell)
- Solid line = Quantile Regression
- Dashed line = Minimum Distance
- **All three estimators are similar** → linear approximation is valid

### Figure Interpretation (Panels D-F): Weighting Functions

```
Panel D-F: Weighting functions by schooling

  Weight│
   0.5 │     
       │        ●  ●           ← QR weights (overall)
   0.4 │       ● ●  ●
       │      ●      ●
   0.3 │     ●        ●
       │    ●          ●
   0.2 │   ●            ●
       │  ●              ●
   0.1 │ ●                ●
       │●                  ●
     0 └────────────────────── school
         8  10  12  14  16  18
```

**Observations**:
- **Importance weights** ≈ **Density weights** ≈ flat
- **Overall QR weights** ≈ schooling histogram
- → Highest weights on 12 and 16 years of schooling (most observations)

---

## 7.1.3 Tricky Points

### Tricky Point 1: Individual Effects vs Distributional Effects

> **"Training raised the lower decile" ≠ "Poor people became richer"**

**What quantile regression tells us**:
- Position of the lower decile in the post-treatment distribution

**What it doesn't tell us**:
- Changes for specific individuals
- Who is in the bottom 10%

**Mathematical explanation**:
- We compare Q_τ(y₁ᵢ|X) vs Q_τ(y₀ᵢ|X)
- This compares **quantiles of marginal distributions**
- Not the **quantile of individual treatment effects (y₁ᵢ - y₀ᵢ)**!

**Rank Preservation assumption**:
- If treatment doesn't change ranks → can interpret as individual effects
- But this is a very strong assumption

### Tricky Point 2: Conditional vs Marginal Quantiles

**Problem**: Conditional quantile ≠ Marginal quantile

**For expectations (simple)**:
```
E[y_i | X_i] = X_i'β  
⟹  E[y_i] = E[X_i]'β   (by iterated expectations)
```

**For quantiles (complex)**:
```
Q_τ(y_i | X_i) = X_i'β_τ  
⟹  Q_τ(y_i) ≠ E[X_i]'β_τ   (in general!)
```

**Why?** Quantiles are nonlinear operators

### Extracting Marginal Quantiles: Detailed Procedure

**Step 1**: Relationship between conditional quantiles and conditional distribution

```
∫_0^1 1[F_Y^{-1}(τ|X_i) < y] dτ = F_Y(y|X_i)
```

Interpretation: Proportion of conditional quantiles below y = conditional CDF

**Step 2**: Substitute linear CQF

```
F_Y(y|X_i) = ∫_0^1 1[X_i'β_τ < y] dτ
```

**Step 3**: Integrate over X_i → Marginal CDF

```
F_Y(y) = ∫∫_0^1 1[X_i'β_τ < y] dτ dF_X(x)
```

**Step 4**: Marginal quantile = inverse of F_Y(y)

```
Q_τ(y_i) = inf{y : F_Y(y) ≥ τ}
```

### Practical Estimation (Machado & Mata 2005)

**Sample analog**:
```
F̂_Y(y) = (1/n) Σ_i (1/100) Σ_{τ=0.01}^{1.00} 1[X_i'β̂_τ < y]
```

**Procedure**:
1. Estimate 100 quantile regressions at τ = 0.01, 0.02, ..., 0.99
2. Compute 100 predicted values for each X_i
3. Compute empirical distribution of all predicted values
4. Extract marginal quantiles from this distribution

**Limitations**:
- Requires many quantile regressions
- Complex distribution theory (Melly 2005)

---

## 7.2 Quantile Treatment Effects (QTE)

### Problem: Selection Bias in Quantile Regression

Quantile regression also suffers from **omitted variable bias**

| Method | Estimand | Selection bias |
|--------|----------|----------------|
| OLS | Average effect | Present |
| Quantile Reg | Quantile effect | Present |
| 2SLS | Average causal effect | Removed |
| **QTE** | **Quantile causal effect** | **Removed** |

### QTE Idea

**Extend LATE framework to quantiles** (Abadie, Angrist, Imbens 2002)

**Model**:
```
Q_τ(y_i | X_i, d_i, complier) = α_τ·d_i + X_i'β_τ
```

**Interpretation**:
- α_τ = **Treatment effect on τ-quantile for compliers**
- i.e.: Q_τ(y₁ᵢ|X_i, complier) - Q_τ(y₀ᵢ|X_i, complier) = α_τ

### Important Distinction

**What α_τ means**:
- Comparison of **marginal distributions** of y₁ and y₀ for compliers
- Difference at the τ-quantile

**What α_τ does NOT mean**:
- τ-quantile of individual treatment effects (y₁ᵢ - y₀ᵢ)
- This requires observing both y₁ᵢ and y₀ᵢ simultaneously → impossible

**Good news**: 
- For means: E[y₁-y₀] = E[y₁] - E[y₀] ✓
- Welfare analysis only requires marginal distributions (Atkinson 1970)

### QTE Estimator: Abadie Kappa

**Kappa definition**:
```
κ_i = 1 - d_i(1-z_i)/(1-P(z_i=1|X_i)) - (1-d_i)z_i/P(z_i=1|X_i)
```

**Property**: E[κ_i | complier] = 1, E[κ_i | non-complier] = 0

**QTE estimation**:
```
(α_τ, β_τ) = arg min_{a,b} E[κ_i · ρ_τ(y_i - a·d_i - X_i'b)]
```

### Practical Issues and Solutions for QTE Implementation

#### Problem 1: κ_i can be negative

When d_i ≠ z_i, κ_i < 0 → minimand is non-convex → LP not applicable

**Solution**: Use iterated expectations

```
E[κ_i · ρ_τ(...)] = E[E[κ_i | y_i, d_i, X_i] · ρ_τ(...)]
```

where:
```
E[κ_i | y_i, d_i, X_i] = P[complier | y_i, d_i, X_i] ∈ [0, 1]
```

#### Problem 2: Need to estimate E[κ_i | y_i, d_i, X_i]

**Formula**:
```
E[κ_i | y_i, d_i, X_i] = 1 - d_i(1-E[z_i|y_i,d_i=1,X_i])/(1-P(z_i=1|X_i)) 
                          - (1-d_i)E[z_i|y_i,d_i=0,X_i]/P(z_i=1|X_i)
```

### QTE Implementation Steps (Angrist 2001)

```
Step 1: In d_i = 1 subsample, Probit: z_i ~ y_i, X_i
        → Save Ê[z_i | y_i, d_i=1, X_i]

Step 2: In d_i = 0 subsample, Probit: z_i ~ y_i, X_i
        → Save Ê[z_i | y_i, d_i=0, X_i]

Step 3: In full sample, Probit: z_i ~ X_i
        → Save P̂(z_i=1 | X_i)

Step 4: Compute Ê[κ_i | y_i, d_i, X_i] using formula
        - Trim to [0, 1] range

Step 5: Use as weights in Stata qreg for quantile regression

Step 6: Bootstrap entire procedure → standard errors
```

---

## Standard Errors for Quantile Regression

### Conventional Standard Errors (Stata qreg, robust)

**Assumption**: CQF is exactly linear

**Formula**:
```
Var(β̂_τ) = τ(1-τ) · {E[f_u(0|X_i)X_i X_i']}^{-1} · E[X_i X_i'] · {E[f_u(0|X_i)X_i X_i']}^{-1}
```

where f_u(0|X_i) = conditional density of residual at 0

**Homoskedastic case**:
```
Var(β̂_τ) = τ(1-τ)/f_u²(0) · {E[X_i X_i']}^{-1}
```

### Robust Standard Errors (Angrist, Chernozhukov, Fernandez-Val 2006)

- Robust to nonlinear CQF
- Often similar to conventional in practice

### Bootstrap

- Essential for QTE (due to first-step estimation)
- Repeat entire procedure (Probit → Kappa → QR)

---

## Empirical Example: JTPA Training Program (Table 7.2.1)

### Background

| Item | Description |
|------|-------------|
| **Program** | Job Training Partnership Act (1980s US) |
| **Target** | Disadvantaged workers |
| **SDAs** | 649 Service Delivery Areas |
| **Sample** | 15,981 individuals (30-month earnings data) |

### Variable Definitions

| Variable | Definition |
|----------|------------|
| y_i | 30-month cumulative earnings |
| d_i | Actual training participation |
| z_i | Training offer (randomly assigned) |
| X_i | Race, education, marriage, age, prior work, etc. |

### Compliance Situation

- ~60% of those offered training actually participated
- <2% of control group received training (few always-takers)
- → Complier effect ≈ effect on the treated

### Results Comparison: Panel A (OLS & QR)

**Selection bias present**

| | OLS | τ=0.15 | τ=0.25 | τ=0.50 | τ=0.75 | τ=0.85 |
|---|---|---|---|---|---|---|
| **Training** | 3,754 | 1,187 | 2,510 | 4,420 | 4,678 | 4,806 |
| (s.e.) | (536) | (205) | (356) | (651) | (937) | (1,055) |
| **% Impact** | 21% | **136%** | 75% | 35% | 17% | 13% |

**Observation**: Effect appears **much larger** at lower quantiles (136% vs 13%)

### Results Comparison: Panel B (2SLS & QTE)

**Selection bias removed**

| | 2SLS | τ=0.15 | τ=0.25 | τ=0.50 | τ=0.75 | τ=0.85 |
|---|---|---|---|---|---|---|
| **Training** | 1,593 | **121** | 702 | 1,544 | 3,131 | 3,378 |
| (s.e.) | (895) | (475) | (670) | (1,073) | (1,376) | (1,811) |
| **% Impact** | 9% | **5%** | 12% | 10% | 11% | 9% |

**Observation**: Lower quantile effects **nearly disappear!**

### QR vs QTE Comparison

| Quantile | QR estimate | QTE estimate | Difference | Interpretation |
|----------|-------------|--------------|------------|----------------|
| 0.15 | $1,187 | **$121** | −90% | Severe selection bias |
| 0.25 | $2,510 | $702 | −72% | Severe selection bias |
| 0.50 | $4,420 | $1,544 | −65% | Moderate |
| 0.75 | $4,678 | $3,131 | −33% | Less severe |
| 0.85 | $4,806 | $3,378 | −30% | Less severe |

### Key Findings

**Selection Bias Pattern**:
- Lower quantiles: Severe positive selection bias
- Upper quantiles: Less severe

**Interpretation**:
- Low-income trainees = more motivated individuals
- QR lower quantiles: Training effect + motivation effect combined
- QTE separates these → actual lower quantile effect is nearly zero

**Policy Implications**:
- JTPA only effective at **upper quantiles**
- Disconnected from goal of helping the poor
- Was raising upper-quantile earnings a policy priority?

---

## Three Key Questions

### Q1. Quantile Regression vs OLS

**What distinguishes quantile regression from OLS, and when should it be used?**

**Answer**:

| Aspect | OLS | Quantile Regression |
|--------|-----|---------------------|
| Estimand | Conditional mean | Conditional quantile |
| Loss function | Squared error | Check function (asymmetric) |
| Distribution info | Mean only | Entire distribution |
| Outlier sensitivity | High | Low (especially median) |

**When to use**:
- Analyzing inequality changes
- Detecting effect heterogeneity (upper/lower quantiles)
- Distinguishing location shift vs heteroskedasticity
- When robust estimation against outliers is needed

---

### Q2. Location Shift vs Fanning Out

**If coefficients are identical across quantiles, it's a location shift. What does it mean when they differ?**

**Answer**:

| Pattern | Meaning | Mathematical condition | Example |
|---------|---------|------------------------|---------|
| **Identical coefficients** | Location shift | Homoskedastic | 1980 education effect |
| **Increasing coefficients** | Inequality increase (fanning out) | Var(y\|X) increases | 2000 education effect |
| **Decreasing coefficients** | Inequality decrease (compression) | Var(y\|X) decreases | - |

**2000 interpretation**: 
- Average return to education ~11%
- Upper decile: 15.7% (above average)
- Lower decile: 9.2% (below average)
- → Education raises average wages but also **increases inequality among the educated**

---

### Q3. Need for QTE

**Explain why quantile regression estimates can have selection bias and how QTE addresses this.**

**Answer**:

**Selection bias example (JTPA)**:
- Low-income trainees = more motivated individuals
- QR lower quantiles: Training effect + motivation effect combined
- → Overestimation

**How QTE solves this**:
1. Apply IV logic to quantile regression
2. Weight by Abadie Kappa for compliers
3. Use random assignment (z_i) as instrument
4. Kappa-weighted quantile regression

**JTPA result**: 
- Lower quantile effect: $1,187 → $121 (90% reduction)
- Shows how severe selection bias was

---

## Discussion Questions

### D1. Individual Effects vs Distributional Effects

> Does "training raised the lower decile by $1,000" mean "poor people earned $1,000 more"?

**Discussion points**:
- Rank preservation assumption needed
- Treatment can change ranks
- Quantile of E[y₁-y₀] vs Q(y₁)-Q(y₀) difference
- Policy implications of distributional vs individual effects

### D2. Conditional vs Marginal Quantiles

> If education effects differ by quantile, what does this imply for overall inequality?

**Discussion points**:
- Q_τ(y|X) ≠ Q_τ(y) problem
- Machado & Mata (2005) methodology
- Constructing counterfactual distributions
- "What would inequality be if everyone were college educated?"

### D3. Limitations of QTE

> QTE only estimates effects for compliers, like LATE. What limitations does this impose on policy implications?

**Discussion points**:
- Compliers vs always-takers vs never-takers
- In JTPA, only 2% of control group were always-takers → minor issue
- What about other contexts?
- External validity and generalization

---

## Practical Checklist

### When Running Quantile Regression

```
□ Estimate multiple quantiles (0.1, 0.25, 0.5, 0.75, 0.9)
□ Check how coefficients vary across quantiles
□ Determine location shift vs fanning out
□ Check for censoring issues (topcode, etc.)
□ Report standard errors (bootstrap recommended)
□ Verify median ≈ OLS (for symmetric distributions)
```

### When Running QTE

```
□ Verify instrument validity (LATE assumptions)
□ Check first stage strength
□ Estimate E[z|y,d,X] via Probit (separately for d=0, d=1)
□ Estimate P(z=1|X) via Probit
□ Compute kappa weights and trim to [0,1]
□ Run kappa-weighted quantile regression
□ Compare with QR estimates (assess selection bias magnitude)
□ Bootstrap standard errors
```

### Stata Code Example

```stata
* Quantile Regression
qreg y x1 x2, quantile(0.5) vce(robust)

* Multiple quantiles
foreach q in 0.1 0.25 0.5 0.75 0.9 {
    qreg y x1 x2, quantile(`q')
}

* QTE (simplified)
* Steps 1-3: Probit
probit z y x1 x2 if d==1
predict pz_d1
probit z y x1 x2 if d==0  
predict pz_d0
probit z x1 x2
predict pz

* Step 4: Kappa
gen kappa = 1 - d*(1-pz_d1)/(1-pz) - (1-d)*pz_d0/pz
replace kappa = 0 if kappa < 0
replace kappa = 1 if kappa > 1

* Step 5: Weighted QR
qreg y d x1 x2 [pw=kappa], quantile(0.5)
```

---

## Key Formulas Summary

### Check Function
```
ρ_τ(u) = u·(τ - 1(u ≤ 0))
```

### Quantile Regression
```
β_τ = arg min E[ρ_τ(y_i - X_i'b)]
```

### Location Shift Model
```
Q_τ(y_i | X_i) = X_i'β + σ·Φ^{-1}(τ)
```

### Heteroskedastic Model (Location-Scale)
```
Q_τ(y_i | X_i) = X_i'[β + γ·Φ^{-1}(τ)]
```

### Abadie Kappa
```
κ_i = 1 - d_i(1-z_i)/(1-p(X_i)) - (1-d_i)z_i/p(X_i)
```
where p(X_i) = P(z_i=1|X_i)

### QTE Estimator
```
(α_τ, β_τ) = arg min E[κ_i · ρ_τ(y_i - α·d_i - X_i'b)]
```

### Conditional → Marginal Quantile
```
F_Y(y) = ∫∫_0^1 1[X_i'β_τ < y] dτ dF_X(x)
Q_τ(y) = F_Y^{-1}(τ)
```

---

## Comprehensive Comparison: OLS vs QR vs 2SLS vs QTE

### 2×2 Framework

| | Exogenous d_i | Endogenous d_i |
|---|---|---|
| **Mean** | OLS | 2SLS |
| **Quantile** | Quantile Regression | **QTE** |

### Detailed Comparison

| Method | Estimand | Selection bias | Distribution info | Assumption |
|--------|----------|----------------|-------------------|------------|
| OLS | E[y\|X,d] | Present | Mean only | Linear CEF |
| 2SLS | E[y\|X,d] for compliers | Removed | Mean only | LATE assumptions |
| QR | Q_τ(y\|X,d) | Present | Entire distribution | Linear CQF |
| QTE | Q_τ(y\|X,d) for compliers | Removed | Entire distribution | LATE + Linear CQF |

---

*Based on Angrist & Pischke, "Mostly Harmless Econometrics" Chapter 7*
