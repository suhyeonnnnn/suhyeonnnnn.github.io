---
layout: default
title: "Angrist Chapter 7: Quantile Regression Study Guide"
lang: en
---

# Chapter 7: Quantile Regression Study Guide

---

## 핵심 개념 요약

### 왜 Quantile Regression인가?

> "95%의 응용 계량경제학은 평균에 관한 것이다. 하지만 분포 전체에 무슨 일이 일어나는지 알고 싶다면?"

**OLS의 한계**:
- 평균 효과만 추정
- 분포의 변화 (퍼짐, 압축) 파악 불가
- 불평등 변화 분석 불가

**Quantile Regression의 장점**:
- 분포의 여러 지점 (10분위, 중위수, 90분위 등) 효과 추정
- 불평등 변화 분석 가능
- OLS와 유사하게 공변량 통제 가능

---

## 7.1 Quantile Regression Model

### Conditional Quantile Function (CQF)

**정의**:
```
Q_τ(y_i | X_i) = F_Y^{-1}(τ | X_i)
```

| τ 값 | 의미 |
|------|------|
| τ = 0.10 | 하위 10분위 (lower decile) |
| τ = 0.50 | 중위수 (median) |
| τ = 0.90 | 상위 10분위 (upper decile) |

### CEF vs CQF 비교

| | CEF (OLS) | CQF (Quantile Reg) |
|---|---|---|
| **정의** | E[y_i \| X_i] | Q_τ(y_i \| X_i) |
| **최소화** | E[(y_i - m(X_i))²] | E[ρ_τ(y_i - q(X_i))] |
| **손실함수** | Squared error | Check function ρ_τ |
| **추정** | 조건부 평균 | 조건부 분위수 |

### Check Function (ρ_τ)

```
ρ_τ(u) = u · (τ - 1(u ≤ 0))
       = τ·u        if u > 0
       = (τ-1)·u    if u ≤ 0
```

**직관**: 양수/음수 잔차에 **비대칭 가중치** 부여

| τ 값 | 양수 잔차 가중치 | 음수 잔차 가중치 | 결과 |
|------|-----------------|-----------------|------|
| 0.5 | 0.5 | 0.5 | 중위수 (LAD) |
| 0.9 | 0.9 | 0.1 | 상위 분위수 |
| 0.1 | 0.1 | 0.9 | 하위 분위수 |

### Quantile Regression 추정

**Population 문제**:
```
β_τ = arg min_{b∈R^d} E[ρ_τ(y_i - X_i'b)]
```

**Sample analog**: Linear programming으로 해결 가능

선형 모형 가정:
```
Q_τ(y_i | X_i) = X_i'β_τ
```

---

## Location Shift vs Heteroskedasticity

### Case 1: Location Shift (Homoskedastic)

**모형**:
```
y_i ~ N(X_i'β, σ²)
```

**CQF 유도**:
```
P[y_i - X_i'β < σ·Φ^{-1}(τ) | X_i] = τ
```

따라서:
```
Q_τ(y_i | X_i) = X_i'β + σ·Φ^{-1}(τ)
```

**특징**: 
- 절편만 τ에 따라 변함
- **기울기 β는 모든 분위수에서 동일**
- Within-group inequality 불변

### Case 2: Heteroskedasticity (Linear Location-Scale Model)

**모형**:
```
y_i ~ N(X_i'β, (X_i'γ)²)
```
여기서 γ > 0, X_i'γ > 0

**CQF 유도**:
```
P[y_i - X_i'β < (X_i'γ)·Φ^{-1}(τ) | X_i] = τ
```

따라서:
```
Q_τ(y_i | X_i) = X_i'β + (X_i'γ)·Φ^{-1}(τ)
                = X_i'[β + γ·Φ^{-1}(τ)]
```

**특징**:
- **기울기가 τ에 따라 변함**
- τ > 0.5: 기울기 증가 (상위 분위수)
- τ < 0.5: 기울기 감소 (하위 분위수)
- Within-group inequality가 X에 따라 변함

---

## 실증 예시: 교육의 임금 효과 (Table 7.1.1)

### 데이터
- 1980, 1990, 2000 U.S. Census
- 40-49세 백인/흑인 남성
- 통제변수: 인종, 잠재 경력(age - education - 6)의 이차함수

### 연도별 분위수 회귀 결과

| Census | Mean | SD | 0.10 | 0.25 | 0.50 | 0.75 | 0.90 | OLS |
|--------|------|-----|------|------|------|------|------|-----|
| **1980** | 6.40 | 0.67 | .074 | .074 | .068 | .070 | .079 | .072 |
| **1990** | 6.46 | 0.60 | .112 | .110 | .106 | .111 | .137 | .114 |
| **2000** | 6.50 | 0.75 | .092 | .105 | .111 | .120 | **.157** | .114 |

### 해석

**1980년**: 
- 모든 분위수에서 계수 유사 (~0.07)
- **Location shift** — 교육이 임금 분포를 균등하게 이동
- Within-group inequality 불변

**1990년**:
- 대체로 유사한 패턴 (~0.11)
- 상위 10분위만 약간 높음 (0.137)

**2000년**: 
- **상위 분위수에서 계수 급증** (0.09 → 0.16)
- 하위 10분위: 9.2% vs 상위 10분위: 15.7%
- **Heteroskedasticity** — 교육이 불평등도 증가시킴
- "교육받은 사람 중에서도 부자가 더 부자가 됨"

**정책적 함의**:
- 1980s-1990s: 전반적인 학력 프리미엄 증가
- 2000년: 학력 내 불평등(within-group inequality)도 증가
- 노동시장의 근본적 변화 시사 (Autor, Katz, Kearney 2005; Lemieux 2008)

---

## 7.1.1 Censored Quantile Regression

### 문제 상황

**Censoring**: 일부 데이터가 숨겨짐 (limited가 아님!)
```
y_{i,obs} = y_i · 1[y_i < c]
```

| 유형 | 예시 | 설명 |
|------|------|------|
| **Top-coding** | CPS 고소득 비공개 | 고소득자 프라이버시 보호 |
| **Duration censoring** | 실업 기간 40주 이상 미추적 | 추적 기간 제한 |

**주의**: Limited dependent variable (예: 의료비=0)과 다름!

### 해결책: Powell (1986)

**핵심 아이디어**: Censoring point **아래** 분위수는 영향 없음

예: 상위 10%가 censored → τ ≤ 0.90 추정에 영향 없음

**Censored QR 모형**:
```
Q_τ(y_i | X_i) = min(c, X_i'β_τ)
```

**추정**:
```
β_τ^c = arg min_{b∈R^d} E{1[X_i'β_τ^c < c] · ρ_τ(y_i - X_i'b)}
```

즉, X_i'β < c 인 관측치만 사용

### Buchinsky (1994) 반복 알고리즘

**문제**: 어떤 관측치가 X_i'β < c 인지 미리 모름

**해결**: 반복 추정

```
Step 1: Censoring 무시하고 β̂_τ 추정
Step 2: X_i'β̂_τ < c 인 셀 찾기
Step 3: 해당 셀만으로 β̂_τ 재추정
Step 4: 수렴까지 반복
```

**특징**:
- 수렴 보장 안 되지만 실제로 잘 작동
- Standard errors는 bootstrap으로
- Buchinsky (1994), Chamberlain (1994): CPS topcode 보정 시 교육 수익률 증가

---

## 7.1.2 Quantile Regression Approximation Property

### Theorem 7.1.1 (Angrist, Chernozhukov, Fernandez-Val 2006)

**가정**:
- (i) 조건부 밀도 f_Y(y|X_i) 존재
- (ii) E[y_i], E[Q_τ(y_i|X_i)], E||X_i|| 유한
- (iii) β_τ가 유일한 해

**정리**:
```
β_τ = arg min_{b∈R^d} E[w_τ(X_i, b) · ε_τ²(X_i, b)]
```

여기서:
- **Specification error**: ε_τ(X_i, β) ≡ X_i'β_τ - Q_τ(y_i|X_i)
- **Weight function**: 
```
w_τ(X_i, β) = ∫_0^1 (1-u) · f_{ε(τ)}(u·ε_τ(X_i,β) | X_i) du
```

**근사**:
```
w_τ(X_i, β_τ) ≈ (1/2) · f_Y(Q_τ(y_i|X_i) | X_i)
```

### 직관적 의미

| | OLS | Quantile Regression |
|---|---|---|
| **근사 대상** | E[y_i \| X_i] | Q_τ(y_i \| X_i) |
| **가중치** | Histogram of X_i | w_τ(X_i) × Histogram |
| **강조 영역** | X_i 분포 전체 | CQF 근처에 y_i가 밀집된 X_i |

**핵심**: CQF가 정확히 선형이 아니어도, quantile regression은 **가중 최소제곱 의미에서 최선의 선형 근사** 제공

---

## Figure 7.1.1: QR vs MD vs Nonparametric CQF

### 세 가지 추정량 비교

**1980 Census 데이터, 종속변수: log wages, 독립변수: schooling**

| 추정량 | 방법 | 특징 |
|--------|------|------|
| **CQ (Nonparametric)** | 각 학력 수준에서 직접 분위수 계산 | 비모수적, 대표본 필요 |
| **QR (Quantile Regression)** | ρ_τ 최소화 | 선형 모형 가정, weighted fit |
| **MD (Minimum Distance)** | CQF에 선형 회귀 | Chamberlain (1994), histogram 가중 |

### Minimum Distance (MD) Estimator

**Chamberlain (1994)**:

```
β̃_τ = arg min_{b∈R^d} E[(Q_τ(y_i|X_i) - X_i'b)²]
```

**해석**: Q_τ(y_i|X_i)를 X_i에 회귀 → histogram 가중치 사용

**QR vs MD 차이**:
- QR: w_τ(X_i) × histogram 가중
- MD: histogram만 가중
- 실제로는 매우 유사한 결과

### Figure 해석 (Panels A-C)

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
- 실선 = Quantile Regression
- 점선 = Minimum Distance
- **세 추정량 모두 유사** → 선형 근사 타당

### Figure 해석 (Panels D-F): 가중 함수

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

**관찰**:
- **Importance weights** ≈ **Density weights** ≈ flat
- **Overall QR weights** ≈ schooling histogram
- → 12년, 16년 학력에 가장 높은 가중치 (관측치 많음)

---

## 7.1.3 Tricky Points

### Tricky Point 1: 개인 효과 vs 분포 효과

> **"훈련이 하위 10분위를 올렸다" ≠ "가난했던 사람이 부자가 됐다"**

**Quantile regression이 말해주는 것**:
- 처치 후 분포의 하위 10분위 **위치**

**말해주지 않는 것**:
- 특정 개인의 변화
- 누가 하위 10%인지

**수학적 설명**:
- Q_τ(y₁ᵢ|X) vs Q_τ(y₀ᵢ|X) 비교
- 이것은 **marginal distribution의 분위수** 비교
- **개인 수준 (y₁ᵢ - y₀ᵢ)의 분위수가 아님!**

**Rank Preservation 가정**:
- 처치가 순위를 바꾸지 않는다면 → 개인 효과로 해석 가능
- 하지만 이 가정은 매우 강함

### Tricky Point 2: Conditional vs Marginal Quantiles

**문제**: Conditional quantile ≠ Marginal quantile

**기대값의 경우 (간단)**:
```
E[y_i | X_i] = X_i'β  
⟹  E[y_i] = E[X_i]'β   (by iterated expectations)
```

**분위수의 경우 (복잡)**:
```
Q_τ(y_i | X_i) = X_i'β_τ  
⟹  Q_τ(y_i) ≠ E[X_i]'β_τ   (일반적으로!)
```

**왜?** 분위수는 비선형 연산자

### Extracting Marginal Quantiles: 상세 절차

**Step 1**: 조건부 분위수와 조건부 분포의 관계

```
∫_0^1 1[F_Y^{-1}(τ|X_i) < y] dτ = F_Y(y|X_i)
```

해석: y 아래에 있는 조건부 분위수의 비율 = 조건부 CDF

**Step 2**: 선형 CQF 대입

```
F_Y(y|X_i) = ∫_0^1 1[X_i'β_τ < y] dτ
```

**Step 3**: X_i에 대해 적분 → Marginal CDF

```
F_Y(y) = ∫∫_0^1 1[X_i'β_τ < y] dτ dF_X(x)
```

**Step 4**: Marginal quantile = F_Y(y) 역함수

```
Q_τ(y_i) = inf{y : F_Y(y) ≥ τ}
```

### 실제 추정 (Machado & Mata 2005)

**Sample analog**:
```
F̂_Y(y) = (1/n) Σ_i (1/100) Σ_{τ=0.01}^{1.00} 1[X_i'β̂_τ < y]
```

**절차**:
1. τ = 0.01, 0.02, ..., 0.99에서 100개 분위수 회귀 추정
2. 각 X_i에 대해 100개 예측값 계산
3. 전체 예측값의 경험적 분포 계산
4. 이 분포에서 marginal quantile 추출

**한계**:
- 많은 분위수 회귀 필요
- 분포 이론 복잡 (Melly 2005)

---

## 7.2 Quantile Treatment Effects (QTE)

### 문제: Selection Bias in Quantile Regression

Quantile regression도 **omitted variable bias** 문제 있음

| 방법 | 추정 대상 | Selection bias |
|------|----------|----------------|
| OLS | 평균 효과 | 있음 |
| Quantile Reg | 분위수 효과 | 있음 |
| 2SLS | 평균 인과효과 | 제거 |
| **QTE** | **분위수 인과효과** | **제거** |

### QTE의 아이디어

**LATE 프레임워크를 분위수로 확장** (Abadie, Angrist, Imbens 2002)

**모형**:
```
Q_τ(y_i | X_i, d_i, complier) = α_τ·d_i + X_i'β_τ
```

**해석**:
- α_τ = **compliers의 τ-분위수에 대한 처치 효과**
- 즉: Q_τ(y₁ᵢ|X_i, complier) - Q_τ(y₀ᵢ|X_i, complier) = α_τ

### 중요한 구분

**α_τ가 의미하는 것**:
- Compliers의 y₁과 y₀ **각각의 marginal distribution** 비교
- τ-분위수에서의 차이

**α_τ가 의미하지 않는 것**:
- 개인 처치효과 (y₁ᵢ - y₀ᵢ)의 τ-분위수
- 이건 y₁ᵢ와 y₀ᵢ를 동시에 관측해야 알 수 있음 → 불가능

**좋은 소식**: 
- 평균의 경우: E[y₁-y₀] = E[y₁] - E[y₀] ✓
- 후생 분석에는 marginal distribution만 필요 (Atkinson 1970)

### QTE Estimator: Abadie Kappa

**Kappa 정의**:
```
κ_i = 1 - d_i(1-z_i)/(1-P(z_i=1|X_i)) - (1-d_i)z_i/P(z_i=1|X_i)
```

**속성**: E[κ_i | complier] = 1, E[κ_i | non-complier] = 0

**QTE 추정**:
```
(α_τ, β_τ) = arg min_{a,b} E[κ_i · ρ_τ(y_i - a·d_i - X_i'b)]
```

### QTE 구현의 실제 문제와 해결

#### 문제 1: κ_i가 음수일 수 있음

d_i ≠ z_i 일 때 κ_i < 0 → minimand가 non-convex → LP 불가

**해결**: Iterated expectations 사용

```
E[κ_i · ρ_τ(...)] = E[E[κ_i | y_i, d_i, X_i] · ρ_τ(...)]
```

여기서:
```
E[κ_i | y_i, d_i, X_i] = P[complier | y_i, d_i, X_i] ∈ [0, 1]
```

#### 문제 2: E[κ_i | y_i, d_i, X_i] 추정 필요

**공식**:
```
E[κ_i | y_i, d_i, X_i] = 1 - d_i(1-E[z_i|y_i,d_i=1,X_i])/(1-P(z_i=1|X_i)) 
                          - (1-d_i)E[z_i|y_i,d_i=0,X_i]/P(z_i=1|X_i)
```

### QTE 구현 단계 (Angrist 2001)

```
Step 1: d_i = 1 subsample에서 Probit: z_i ~ y_i, X_i
        → Ê[z_i | y_i, d_i=1, X_i] 저장

Step 2: d_i = 0 subsample에서 Probit: z_i ~ y_i, X_i
        → Ê[z_i | y_i, d_i=0, X_i] 저장

Step 3: 전체 sample에서 Probit: z_i ~ X_i
        → P̂(z_i=1 | X_i) 저장

Step 4: 공식에 대입하여 Ê[κ_i | y_i, d_i, X_i] 계산
        - [0, 1] 범위 벗어나면 trim

Step 5: Stata qreg에서 weight로 사용하여 분위수 회귀

Step 6: 전체 과정 bootstrap → standard errors
```

---

## Standard Errors for Quantile Regression

### Conventional Standard Errors (Stata qreg, robust)

**가정**: CQF가 정확히 선형

**공식**:
```
Var(β̂_τ) = τ(1-τ) · {E[f_u(0|X_i)X_i X_i']}^{-1} · E[X_i X_i'] · {E[f_u(0|X_i)X_i X_i']}^{-1}
```

여기서 f_u(0|X_i) = 잔차의 조건부 밀도 (0에서)

**Homoskedastic case**:
```
Var(β̂_τ) = τ(1-τ)/f_u²(0) · {E[X_i X_i']}^{-1}
```

### Robust Standard Errors (Angrist, Chernozhukov, Fernandez-Val 2006)

- CQF 비선형에도 robust
- 실제로는 conventional과 큰 차이 없는 경우 많음

### Bootstrap

- QTE의 경우 필수 (first-step estimation 때문)
- 전체 과정 (Probit → Kappa → QR) 반복

---

## 실증 예시: JTPA 훈련 프로그램 (Table 7.2.1)

### 배경

| 항목 | 내용 |
|------|------|
| **프로그램** | Job Training Partnership Act (1980s 미국) |
| **대상** | 저소득 노동자 |
| **SDA** | 649개 Service Delivery Areas |
| **표본** | 15,981명 (30개월 소득 데이터) |

### 변수 정의

| 변수 | 정의 |
|------|------|
| y_i | 30개월 누적 소득 |
| d_i | 실제 훈련 참여 여부 |
| z_i | 훈련 제안 (무작위 배정) |
| X_i | 인종, 학력, 결혼, 연령, 과거 근로 등 |

### Compliance 상황

- 제안받은 사람 중 ~60%만 실제 참여
- Control group 중 <2%가 훈련 받음 (few always-takers)
- → Complier 효과 ≈ 처치자 효과

### 결과 비교: Panel A (OLS & QR)

**Selection bias 있음**

| | OLS | τ=0.15 | τ=0.25 | τ=0.50 | τ=0.75 | τ=0.85 |
|---|---|---|---|---|---|---|
| **Training** | 3,754 | 1,187 | 2,510 | 4,420 | 4,678 | 4,806 |
| (s.e.) | (536) | (205) | (356) | (651) | (937) | (1,055) |
| **% Impact** | 21% | **136%** | 75% | 35% | 17% | 13% |

**관찰**: 하위 분위수에서 효과가 **훨씬 커 보임** (136% vs 13%)

### 결과 비교: Panel B (2SLS & QTE)

**Selection bias 제거**

| | 2SLS | τ=0.15 | τ=0.25 | τ=0.50 | τ=0.75 | τ=0.85 |
|---|---|---|---|---|---|---|
| **Training** | 1,593 | **121** | 702 | 1,544 | 3,131 | 3,378 |
| (s.e.) | (895) | (475) | (670) | (1,073) | (1,376) | (1,811) |
| **% Impact** | 9% | **5%** | 12% | 10% | 11% | 9% |

**관찰**: 하위 분위수 효과가 **거의 사라짐!**

### QR vs QTE 비교

| 분위수 | QR 추정치 | QTE 추정치 | 차이 | 해석 |
|--------|-----------|-----------|------|------|
| 0.15 | $1,187 | **$121** | −90% | Selection bias 심각 |
| 0.25 | $2,510 | $702 | −72% | Selection bias 심각 |
| 0.50 | $4,420 | $1,544 | −65% | 중간 |
| 0.75 | $4,678 | $3,131 | −33% | 덜 심각 |
| 0.85 | $4,806 | $3,378 | −30% | 덜 심각 |

### 핵심 발견

**Selection Bias 패턴**:
- 하위 분위수: 심각한 positive selection bias
- 상위 분위수: 덜 심각

**해석**:
- 훈련에 참여한 저소득자 = 더 motivated된 사람
- QR 하위 분위수: 훈련 효과 + motivation 효과 혼재
- QTE로 분리하면 → 하위 분위수 실제 효과 거의 없음

**정책적 함의**:
- JTPA는 **상위 분위수**에서만 효과 있음
- 저소득층 돕겠다는 목표와 괴리
- 상위 분위수 소득 증가가 정책 우선순위였나?

---

## 핵심 질문 3개

### Q1. Quantile Regression vs OLS

**Quantile regression이 OLS와 다른 점은 무엇이며, 언제 사용해야 하는가?**

**답변**:

| 측면 | OLS | Quantile Regression |
|------|-----|---------------------|
| 추정 대상 | 조건부 평균 | 조건부 분위수 |
| 손실함수 | Squared error | Check function (asymmetric) |
| 분포 정보 | 평균만 | 분포 전체 |
| Outlier 민감도 | 높음 | 낮음 (특히 중위수) |

**사용 시점**:
- 불평등 변화 분석 시
- 효과의 이질성 (상위/하위 분위수) 파악 시
- Location shift vs heteroskedasticity 구분 시
- Outlier에 robust한 추정 필요 시

---

### Q2. Location Shift vs Fanning Out

**분위수별 계수가 동일하면 location shift, 다르면 무엇을 의미하는가?**

**답변**:

| 패턴 | 의미 | 수학적 조건 | 예시 |
|------|------|-------------|------|
| **동일한 계수** | Location shift | Homoskedastic | 1980년 교육 효과 |
| **증가하는 계수** | 불평등 증가 (fanning out) | Var(y\|X) 증가 | 2000년 교육 효과 |
| **감소하는 계수** | 불평등 감소 (compression) | Var(y\|X) 감소 | - |

**2000년 해석**: 
- 평균 교육 수익률 ~11%
- 상위 10분위: 15.7% (평균보다 높음)
- 하위 10분위: 9.2% (평균보다 낮음)
- → 교육이 평균 임금도 올리지만, **고학력자 내 불평등도 증가**

---

### Q3. QTE의 필요성

**Quantile regression 추정치에 selection bias가 있을 수 있는 이유와 QTE의 해결 방식을 설명하시오.**

**답변**:

**Selection bias 예시 (JTPA)**:
- 훈련에 참여하는 저소득자 = 더 motivated된 사람
- QR 하위 분위수: 훈련 효과 + motivation 효과 혼재
- → 과대추정

**QTE 해결 방식**:
1. IV 로직을 분위수 회귀에 적용
2. Abadie Kappa로 compliers 가중
3. 무작위 배정(z_i)을 도구변수로 사용
4. Kappa-weighted quantile regression

**JTPA 결과**: 
- 하위 분위수 효과: $1,187 → $121 (90% 감소)
- Selection bias가 얼마나 심각했는지 보여줌

---

## Discussion 질문

### D1. 개인 효과 vs 분포 효과

> "훈련이 하위 10분위를 $1,000 올렸다"는 것은 "가난한 사람이 $1,000 더 벌게 됐다"를 의미하는가?

**토론 포인트**:
- Rank preservation 가정이 필요
- 처치가 순위를 바꿀 수 있음
- E[y₁-y₀]의 분위수 vs Q(y₁)-Q(y₀)의 차이
- 분포 효과 vs 개인 효과의 policy 함의

### D2. Conditional vs Marginal Quantiles

> 교육의 분위수별 효과가 다르면, 전체 불평등에 어떤 영향을 미치는가?

**토론 포인트**:
- Q_τ(y|X) ≠ Q_τ(y) 문제
- Machado & Mata (2005) 방법론
- Counterfactual 분포 구성
- "교육 수준이 전부 대졸이었다면 불평등은?"

### D3. QTE의 한계

> QTE는 LATE처럼 compliers에 대한 효과만 추정한다. 이것이 policy 함의에 어떤 제한을 주는가?

**토론 포인트**:
- Compliers vs always-takers vs never-takers
- JTPA에서 control group의 2%만 always-takers → 문제 적음
- 다른 맥락에서는?
- External validity와 일반화

---

## 실무 체크리스트

### Quantile Regression 수행 시

```
□ 여러 분위수 (0.1, 0.25, 0.5, 0.75, 0.9) 추정
□ 계수가 분위수별로 어떻게 변하는지 확인
□ Location shift vs fanning out 판단
□ Censoring 문제 확인 (topcode 등)
□ Standard errors 보고 (bootstrap 권장)
□ Median ≈ OLS 인지 확인 (대칭 분포 시)
```

### QTE 수행 시

```
□ 도구변수의 타당성 확인 (LATE 가정)
□ First stage 강도 확인
□ Probit으로 E[z|y,d,X] 추정 (d=0, d=1 별도)
□ Probit으로 P(z=1|X) 추정
□ Kappa weights 계산 및 [0,1] trim
□ Kappa-weighted quantile regression
□ QR 추정치와 비교 (selection bias 크기 파악)
□ Bootstrap standard errors
```

### Stata 코드 예시

```stata
* Quantile Regression
qreg y x1 x2, quantile(0.5) vce(robust)

* 여러 분위수
foreach q in 0.1 0.25 0.5 0.75 0.9 {
    qreg y x1 x2, quantile(`q')
}

* QTE (simplified)
* Step 1-3: Probit
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

## 핵심 수식 요약

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

## OLS vs QR vs 2SLS vs QTE 종합 비교

### 2×2 Framework

| | Exogenous d_i | Endogenous d_i |
|---|---|---|
| **평균** | OLS | 2SLS |
| **분위수** | Quantile Regression | **QTE** |

### 상세 비교

| 방법 | 추정 대상 | Selection bias | 분포 정보 | 가정 |
|------|----------|----------------|----------|------|
| OLS | E[y\|X,d] | 있음 | 평균만 | 선형 CEF |
| 2SLS | E[y\|X,d] for compliers | 제거 | 평균만 | LATE 가정 |
| QR | Q_τ(y\|X,d) | 있음 | 분포 전체 | 선형 CQF |
| QTE | Q_τ(y\|X,d) for compliers | 제거 | 분포 전체 | LATE + 선형 CQF |

---

*Based on Angrist & Pischke, "Mostly Harmless Econometrics" Chapter 7*
