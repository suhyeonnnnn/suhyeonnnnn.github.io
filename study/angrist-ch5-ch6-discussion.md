---
layout: default
title: "Econometrics Study Discussion Guide"
lang: en
---

# Econometrics Study Discussion Guide
## Chapter 5 & 6: Fixed Effects, DD, and RD

---

## Discussion 1: 가정의 검증 가능성

### 토론 주제
> **"Parallel Trends와 Continuity 가정은 둘 다 직접 검증이 불가능하다. 그렇다면 DD와 RD 연구의 credibility는 어디서 오는가?"**

### 토론 포인트

| | DD (Parallel Trends) | RD (Continuity) |
|---|---|---|
| **가정** | 처치 없었으면 같은 추세 | E[y₀\|x]가 cutoff에서 연속 |
| **검증 불가 이유** | Counterfactual 관측 불가 | Cutoff 양쪽에서 동일 x 없음 |
| **간접 검증** | Pre-trends, Leads=0 | McCrary, Covariate balance |

**생각해볼 질문**:
- Pre-trends가 평행해도 parallel trends가 위배될 수 있는가?
- McCrary test 통과해도 manipulation이 있을 수 있는가?
- 어떤 상황에서 DD가 RD보다 credible한가? 그 반대는?

---

## Discussion 2: Robustness vs Precision

### 토론 주제
> **"모든 인과추론 방법에는 robustness와 precision 사이의 tradeoff가 있다. 연구자는 어떻게 균형을 잡아야 하는가?"**

### 각 방법론의 Tradeoff

| 방법 | Robustness ↑ | Precision ↑ |
|------|-------------|-------------|
| **FE** | 더 많은 fixed effects | 더 적은 fixed effects |
| **DD** | State-specific trends 추가 | 단순 two-way FE |
| **RD** | 좁은 bandwidth | 넓은 bandwidth |
| **IV** | 강한 1단계 | - |

**생각해볼 질문**:
- Angrist & Lavy (1999)에서 full sample과 ±3 window 중 어느 추정치를 믿어야 하는가?
- Besley & Burgess (2004)에서 state trends 추가 후 효과가 사라졌다면, 원래 효과가 없던 것인가?
- 결과가 specification에 따라 달라지면 어떻게 보고해야 하는가?

---

## Discussion 3: LATE의 한계

### 토론 주제
> **"IV와 Fuzzy RD는 LATE를 추정한다. LATE가 policy-relevant한가?"**

### Complier 문제

| 연구 | Compliers는 누구? | 일반화 가능? |
|------|------------------|-------------|
| **Angrist & Evans (1998)** | 쌍둥이/동성 때문에 자녀 더 가진 부모 | 모든 부모에게? |
| **Angrist & Lavy (1999)** | Maimonides rule 때문에 작은 학급 배정된 학생 | 모든 학생에게? |
| **Lee (2008)** | 아슬아슬하게 당선된 후보 | 압도적 승리 후보에게? |

**생각해볼 질문**:
- Twins compliers와 Same-sex compliers의 LATE가 다른 것은 문제인가?
- RD의 "double locality" (compliers at cutoff)가 external validity를 얼마나 제한하는가?
- Policy maker에게 ATE와 LATE 중 무엇이 더 유용한가?

---

## Discussion 4: 방법론 선택

### 토론 주제
> **"동일한 연구 질문에 여러 방법론이 적용 가능할 때, 어떤 기준으로 선택해야 하는가?"**

### 사례: "학급 규모가 학업 성취에 미치는 영향"

| 방법 | 적용 방식 | 장점 | 단점 |
|------|----------|------|------|
| **RCT** | Tennessee STAR | Gold standard | 비용, 윤리 |
| **RD** | Maimonides Rule | 자연실험 | Local effect |
| **FE** | 학교 고정효과 | 학교 특성 통제 | Time-varying 못 잡음 |
| **DD** | 정책 변화 전후 | 자연실험 | Parallel trends |

**생각해볼 질문**:
- Angrist & Lavy RD 추정치(−0.25)와 STAR 실험 결과가 유사한 것은 우연인가?
- 여러 방법론의 결과가 일치하면 더 credible한가?
- 결과가 다르면 어느 것을 믿어야 하는가?

---

## Discussion 5: FE vs LDV 논쟁

### 토론 주제
> **"Selection이 time-invariant인지 time-varying인지 모를 때, FE와 LDV 중 무엇을 써야 하는가?"**

### Bracketing의 실무적 함의

```
FE 추정치: +0.15
LDV 추정치: +0.05
True effect: 0.05 ~ 0.15 사이 어딘가
```

**생각해볼 질문**:
- 두 추정치의 중간값을 보고하는 것이 합리적인가?
- Training program에서 Ashenfelter's dip이 있으면 FE를 아예 쓰면 안 되는가?
- Nickell bias를 피하면서 둘을 동시에 고려할 방법은?

---

## Discussion 6: Manipulation과 윤리

### 토론 주제
> **"Running variable manipulation이 가능한 상황에서 RD를 사용해도 되는가?"**

### 실제 사례들

| 사례 | Manipulation 가능성 | 대응 |
|------|-------------------|------|
| **선거 결과** (Lee 2008) | 2000 Florida 재검표 | McCrary test |
| **시험 점수** | 채점 재량, 부정행위 | Covariate balance |
| **소득 기준** | 소득 과소보고 | 행정 데이터 사용 |

**생각해볼 질문**:
- Manipulation이 "약간" 있어도 RD가 유효한가?
- Cutoff를 미리 발표하면 manipulation 유인이 생기는가?
- 연구자가 cutoff를 사후적으로 선택하면 문제인가?

---

## 종합 토론: 인과추론의 한계

### 토론 주제
> **"어떤 방법론도 완벽하지 않다. 실증 연구자는 이 한계를 어떻게 다뤄야 하는가?"**

### 각 방법론의 핵심 한계

| 방법 | 핵심 한계 |
|------|----------|
| **FE** | Time-varying confounders, 측정오차 심화 |
| **DD** | Parallel trends 검증 불가 |
| **RD** | Local effect, bandwidth 의존성 |
| **IV** | Exclusion restriction 검증 불가, LATE |

**최종 토론 질문**:
1. "No perfect method" 상황에서 연구의 가치는 어디서 오는가?
2. 여러 방법론의 결과를 종합하는 것이 best practice인가?
3. Robustness check의 결과를 어떻게 해석하고 보고해야 하는가?
4. 방법론의 한계를 인정하면서도 policy recommendation을 할 수 있는가?

---

## 토론 진행 가이드

### 권장 형식
1. **개인 준비** (5분): 각자 입장 정리
2. **소그룹 토론** (10분): 2-3명씩 의견 교환
3. **전체 토론** (15분): 주요 논점 공유
4. **정리** (5분): 합의점과 열린 질문 정리

### 평가 기준
- 개념의 정확한 이해
- 논리적 근거 제시
- 실제 연구 사례 활용
- 다양한 관점 고려
- 실무적 함의 도출

---

## 핵심 질문 요약

### Chapter 5 핵심 질문

**Q1. Parallel Trends 가정**
- 수식: E[y₀ᵢₛₜ \| s, t] = γₛ + λₜ
- 직접 검증 불가 (counterfactual 관측 불가)
- 간접 검증: Pre-trends, Leads 검정, Placebo test

**Q2. FE의 측정오차 문제**
- Attenuation bias ∝ Var(noise) / Var(signal)
- FE에서 signal(상태 변화) 분산 작음, noise 비슷 → bias 심화
- Union status: 실제 변화 드물고, 측정오차는 매년 발생

**Q3. Bracketing Property**
- True effect는 FE와 LDV 추정치 사이
- LDV true → FE 과대추정 / FE true → LDV 과소추정
- 둘 다 추정해서 비교하는 것이 best practice

### Chapter 6 핵심 질문

**Q1. Sharp RD vs Fuzzy RD**
- Sharp: d_i = 1(x_i ≥ x₀), OLS로 추정, ATE at cutoff
- Fuzzy: P(d_i=1) jumps, 2SLS로 추정, LATE for compliers
- Fuzzy RD = IV (cutoff 통과 여부가 instrument)

**Q2. RD의 핵심 가정과 타당성 검정**
- Continuity: E[y₀\|x]가 cutoff에서 연속
- McCrary test: manipulation (bunching) 검정
- Covariate balance: RCT의 balance check와 동일한 논리

**Q3. Bandwidth Tradeoff**
- 좁은 BW: robustness↑, precision↓
- 넓은 BW: precision↑, robustness↓
- Robustness check: 여러 BW에서 추정치 안정적이어야 함

---

*Based on Angrist & Pischke, "Mostly Harmless Econometrics" Chapters 5-6*
