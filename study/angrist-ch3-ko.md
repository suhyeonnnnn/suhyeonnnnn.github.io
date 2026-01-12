---
layout: minimal_base
title: "Angrist Ch.3 - Making Regression Make Sense"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Chapter 3: Making Regression Make Sense</h2>
            <a href="/study/angrist-ch3" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">English</a>
        </div>
        <div class="section-content">
            <p><em>Angrist & Pischke, Mostly Harmless Econometrics</em></p>
        </div>
    </section>

    <!-- 핵심 메시지 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">핵심 메시지</h2>
        <div class="section-content">
            <blockquote style="border-left: 4px solid #2563eb; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                회귀분석은 <strong>조건부 기댓값 함수(CEF)</strong>에 대한 최선의 선형 근사를 제공하기 때문에 유용하다. 회귀분석이 <em>언제</em> 인과적인지는 <strong>조건부 독립 가정(CIA)</strong>에 달려 있다.
            </blockquote>
            
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>이 장의 핵심 질문들:</strong></p>
                <ol>
                    <li>회귀분석은 <strong>무엇을</strong> 추정하는가? → CEF (또는 그 근사)</li>
                    <li>회귀분석은 <strong>언제</strong> 인과관계를 말해주는가? → CIA가 성립할 때</li>
                    <li>통제변수를 추가하면 <strong>어떻게</strong> 되는가? → OVB 공식</li>
                    <li><strong>어떤</strong> 변수를 통제해야 하는가? → Bad control 문제</li>
                </ol>
            </div>
        </div>
    </section>

    <!-- 3.1 회귀분석의 기초 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">3.1 회귀분석의 기초</h2>
        <div class="section-content">
            
            <h3>3.1.1 조건부 기댓값 함수 (CEF)</h3>
            
            <h4>정의</h4>
            <p>CEF는 X<sub>i</sub>가 주어졌을 때 Y<sub>i</sub>의 기댓값:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                E[Y<sub>i</sub> | X<sub>i</sub>]
            </div>
            
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>직관:</strong> "X가 특정 값일 때, Y의 평균은 얼마인가?"</p>
                <ul>
                    <li>X = 교육 연수 12년인 사람들의 평균 임금</li>
                    <li>X = 교육 연수 16년인 사람들의 평균 임금</li>
                    <li>이런 점들을 모두 연결한 함수가 CEF</li>
                </ul>
            </div>
            
            <p><strong>예시:</strong> 교육 연수별 로그 임금의 CEF</p>
            <ul>
                <li>교육을 더 받은 사람이 평균적으로 더 많이 번다</li>
                <li>연간 약 10% 수익률 (Mincer equation)</li>
                <li>이 관계가 선형인지, 비선형인지는 별개의 문제</li>
            </ul>

            <h4>반복 기댓값의 법칙 (Law of Iterated Expectations)</h4>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p>무조건부 기댓값은 CEF의 기댓값과 같다:</p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    E[Y<sub>i</sub>] = E{ E[Y<sub>i</sub> | X<sub>i</sub>] }
                </div>
                <p style="margin-top: 1rem;"><strong>직관:</strong> 전체 평균 = (각 그룹 평균의) 가중평균</p>
            </div>
            
            <p><strong>수학적 유도:</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                E[Y<sub>i</sub>] = Σ<sub>x</sub> E[Y<sub>i</sub> | X<sub>i</sub> = x] · P(X<sub>i</sub> = x)<br><br>
                = E<sub>X</sub>[ E[Y<sub>i</sub> | X<sub>i</sub>] ]
            </div>

            <h4>CEF의 세 가지 핵심 성질</h4>
            
            <p><strong>성질 1: CEF 분해 (CEF Decomposition Property)</strong></p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    Y<sub>i</sub> = E[Y<sub>i</sub> | X<sub>i</sub>] + ε<sub>i</sub>
                </div>
                <p style="margin-top: 1rem;">여기서 ε<sub>i</sub> ≡ Y<sub>i</sub> − E[Y<sub>i</sub> | X<sub>i</sub>]</p>
            </div>
            
            <p><strong>ε<sub>i</sub>의 두 가지 중요한 특성:</strong></p>
            <ol>
                <li><strong>평균 독립 (Mean Independence):</strong> E[ε<sub>i</sub> | X<sub>i</sub>] = 0</li>
                <li><strong>직교성:</strong> ε<sub>i</sub>는 X<sub>i</sub>의 모든 함수 h(X<sub>i</sub>)와 상관 없음</li>
            </ol>
            
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>증명 (평균 독립):</strong></p>
                <p style="font-family: 'Times New Roman', serif;">
                    E[ε<sub>i</sub> | X<sub>i</sub>] = E[Y<sub>i</sub> − E[Y<sub>i</sub> | X<sub>i</sub>] | X<sub>i</sub>]<br>
                    = E[Y<sub>i</sub> | X<sub>i</sub>] − E[Y<sub>i</sub> | X<sub>i</sub>] = 0
                </p>
            </div>

            <p>→ 모든 확률변수는 "X로 설명되는 부분"(CEF)과 직교하는 잔차로 분해 가능</p>

            <p><strong>성질 2: CEF 예측 (CEF Prediction Property)</strong></p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    E[Y<sub>i</sub> | X<sub>i</sub>] = arg min<sub>m(X)</sub> E[(Y<sub>i</sub> − m(X<sub>i</sub>))²]
                </div>
                <p style="margin-top: 1rem;">CEF는 X가 주어졌을 때 Y의 <strong>최소 평균제곱오차(MMSE)</strong> 예측자</p>
            </div>
            
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>직관:</strong></p>
                <ul>
                    <li>X만 알고 Y를 예측해야 한다면?</li>
                    <li>어떤 함수 m(X)를 써야 예측 오차가 최소?</li>
                    <li>정답: CEF! (어떤 다른 함수도 CEF보다 잘 예측 못함)</li>
                </ul>
            </div>

            <p><strong>성질 3: ANOVA 정리 (ANOVA Variance Decomposition)</strong></p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    V(Y<sub>i</sub>) = V(E[Y<sub>i</sub> | X<sub>i</sub>]) + E[V(Y<sub>i</sub> | X<sub>i</sub>)]
                </div>
                <p style="margin-top: 1rem; text-align: center;">
                    <strong>총 분산 = X로 설명되는 분산 + 잔차 분산</strong>
                </p>
            </div>
            
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>유도:</strong></p>
                <p style="font-family: 'Times New Roman', serif;">
                    V(Y<sub>i</sub>) = E[Y<sub>i</sub>²] − (E[Y<sub>i</sub>])²<br><br>
                    Y<sub>i</sub> = E[Y<sub>i</sub>|X<sub>i</sub>] + ε<sub>i</sub> 이고 ε<sub>i</sub> ⊥ E[Y<sub>i</sub>|X<sub>i</sub>] 이므로<br><br>
                    V(Y<sub>i</sub>) = V(E[Y<sub>i</sub>|X<sub>i</sub>]) + V(ε<sub>i</sub>)<br><br>
                    = V(E[Y<sub>i</sub>|X<sub>i</sub>]) + E[V(Y<sub>i</sub>|X<sub>i</sub>)]
                </p>
            </div>
            
            <p>→ 이것이 <strong>R²</strong>의 이론적 기초!</p>

            <h3>3.1.2 선형 회귀와 CEF</h3>
            
            <h4>모집단 회귀함수</h4>
            <p>모집단 회귀계수는 다음 최소화 문제의 해:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif;">
                β = arg min<sub>b</sub> E[(Y<sub>i</sub> − X<sub>i</sub>'b)²]
            </div>
            
            <p><strong>1차 조건 (FOC):</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                ∂/∂b E[(Y<sub>i</sub> − X<sub>i</sub>'b)²] = 0<br><br>
                E[−2X<sub>i</sub>(Y<sub>i</sub> − X<sub>i</sub>'b)] = 0<br><br>
                E[X<sub>i</sub>Y<sub>i</sub>] = E[X<sub>i</sub>X<sub>i</sub>']b
            </div>
            
            <p><strong>해:</strong></p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                β = E[X<sub>i</sub>X<sub>i</sub>']<sup>−1</sup> E[X<sub>i</sub>Y<sub>i</sub>]
            </div>
            
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>이변량 회귀의 특수 경우:</strong></p>
                <div style="text-align: center; font-family: 'Times New Roman', serif;">
                    β = Cov(X<sub>i</sub>, Y<sub>i</sub>) / V(X<sub>i</sub>)
                </div>
                <p style="margin-top: 0.5rem;">→ 익숙한 공식!</p>
            </div>

            <h4>회귀 해부학 (Regression Anatomy / Frisch-Waugh-Lovell)</h4>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p>다변량 회귀에서 k번째 회귀변수의 계수:</p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    β<sub>k</sub> = Cov(Y<sub>i</sub>, x̃<sub>ki</sub>) / V(x̃<sub>ki</sub>)
                </div>
                <p style="margin-top: 0.5rem;">여기서 x̃<sub>ki</sub>는 x<sub>ki</sub>를 다른 모든 공변량에 회귀시킨 <strong>잔차</strong></p>
            </div>
            
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Frisch-Waugh-Lovell 정리 (단계별):</strong></p>
                <p>Y<sub>i</sub> = β<sub>0</sub> + β<sub>1</sub>x<sub>1i</sub> + β<sub>2</sub>x<sub>2i</sub> + e<sub>i</sub> 에서 β<sub>1</sub>을 구하려면:</p>
                <ol>
                    <li><strong>Step 1:</strong> x<sub>1</sub>을 x<sub>2</sub>에 회귀: x<sub>1i</sub> = γ<sub>0</sub> + γ<sub>1</sub>x<sub>2i</sub> + x̃<sub>1i</sub></li>
                    <li><strong>Step 2:</strong> 잔차 x̃<sub>1i</sub> 저장 ("x<sub>2</sub>로 설명 안 되는 x<sub>1</sub>의 변이")</li>
                    <li><strong>Step 3:</strong> Y를 x̃<sub>1</sub>에 회귀: Y<sub>i</sub> = α + β<sub>1</sub>x̃<sub>1i</sub> + error</li>
                    <li>이 β<sub>1</sub>이 원래 다변량 회귀의 β<sub>1</sub>과 동일!</li>
                </ol>
            </div>

            <p><strong>해석:</strong> 다변량 회귀의 각 계수는 다른 변수들을 "제거(partialling out)"한 후의 이변량 기울기</p>

            <h4>회귀분석을 정당화하는 세 가지 정리</h4>
            
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">정리</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">내용</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">적용 조건</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>1. 선형 CEF 정리</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">CEF가 선형이면, 회귀함수 = CEF</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">결합 정규분포, 포화 모형</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>2. 최선 선형 예측자</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">X'β는 Y의 최선 선형 예측자 (MMSE)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">항상</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>3. 회귀-CEF 정리</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">X'β는 E[Y|X]에 대한 최선의 선형 근사</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">항상 (CEF가 비선형이어도)</td>
                </tr>
            </table>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>정리 1 상세: 선형 CEF</strong></p>
                <p>CEF가 선형인 두 가지 경우:</p>
                <ol>
                    <li><strong>결합 정규분포:</strong> (Y<sub>i</sub>, X<sub>i</sub>)가 결합 정규분포이면 E[Y<sub>i</sub>|X<sub>i</sub>]는 X<sub>i</sub>에서 선형</li>
                    <li><strong>포화 모형:</strong> X가 이산형이고 모든 상호작용을 포함하면 회귀 = CEF</li>
                </ol>
            </div>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>정리 3 상세: 회귀-CEF 정리 (가장 중요!)</strong></p>
                <div style="text-align: center; font-family: 'Times New Roman', serif;">
                    β = arg min<sub>b</sub> E[(E[Y<sub>i</sub>|X<sub>i</sub>] − X<sub>i</sub>'b)²]
                </div>
                <p style="margin-top: 1rem;"><strong>의미:</strong> CEF가 비선형이더라도, 회귀분석은 그것에 대한 <strong>최선의 선형 근사</strong>를 제공한다!</p>
            </div>
            
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>핵심 통찰:</strong> 이것이 회귀분석 사용의 가장 일반적인 정당화!</p>
                <ul>
                    <li>CEF가 실제로 선형인지 몰라도 됨</li>
                    <li>회귀분석은 항상 CEF에 대한 좋은 요약을 제공</li>
                    <li>특히 평균 효과(average effects)에 관심 있을 때 유용</li>
                </ul>
            </div>

            <h3>3.1.3 점근적 OLS 추론</h3>
            
            <h4>OLS 추정량</h4>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                β̂ = (Σ<sub>i</sub> X<sub>i</sub>X<sub>i</sub>')<sup>−1</sup> Σ<sub>i</sub> X<sub>i</sub>Y<sub>i</sub><br><br>
                = (X'X)<sup>−1</sup>X'Y
            </div>

            <h4>핵심 점근 결과</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">결과</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">수식</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">의미</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">대수의 법칙 (LLN)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">(1/n)Σ X<sub>i</sub>X<sub>i</sub>' →<sup>p</sup> E[X<sub>i</sub>X<sub>i</sub>']</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">표본 적률 → 모집단 적률</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">중심극한정리 (CLT)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">√n(β̂ − β) →<sup>d</sup> N(0, V)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">점근 정규성</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">슬러츠키 정리</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">-</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">확률 수렴 → 상수 대체 가능</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">연속 사상 정리</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">-</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">확률 극한은 연속 함수 통과</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">델타 방법</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">-</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">점근 정규 변수의 함수도 점근 정규</td>
                </tr>
            </table>

            <h4>OLS의 일치성 증명</h4>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                β̂ = (X'X/n)<sup>−1</sup>(X'Y/n)<br><br>
                
                X'Y/n = (1/n) Σ X<sub>i</sub>Y<sub>i</sub> →<sup>p</sup> E[X<sub>i</sub>Y<sub>i</sub>] (by LLN)<br><br>
                X'X/n = (1/n) Σ X<sub>i</sub>X<sub>i</sub>' →<sup>p</sup> E[X<sub>i</sub>X<sub>i</sub>'] (by LLN)<br><br>
                
                ∴ β̂ →<sup>p</sup> E[X<sub>i</sub>X<sub>i</sub>']<sup>−1</sup> E[X<sub>i</sub>Y<sub>i</sub>] = β
            </div>

            <h4>이분산-강건 표준오차 (Robust SE)</h4>
            
            <p><strong>점근 분산:</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif;">
                Avar(β̂) = E[X<sub>i</sub>X<sub>i</sub>']<sup>−1</sup> <span style="color: #dc2626;">E[X<sub>i</sub>X<sub>i</sub>'e<sub>i</sub>²]</span> E[X<sub>i</sub>X<sub>i</sub>']<sup>−1</sup>
            </div>
            <p style="text-align: center;"><span style="color: #dc2626;">"Meat" (샌드위치의 고기)</span></p>
            
            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>왜 강건 SE를 쓰는가?</strong></p>
                <ul>
                    <li>CEF가 비선형이면, 잔차가 X에 따라 변함 → <strong>이분산은 자연스러움</strong></li>
                    <li>기본(동분산) SE는 E[e<sub>i</sub>² | X<sub>i</sub>] = σ² (상수) 가정</li>
                    <li>강건 SE는 이 가정 없이도 유효</li>
                    <li><strong>Eicker-Huber-White</strong> 표준오차라고도 불림</li>
                </ul>
            </div>

            <p><strong>동분산 가정 하의 단순화:</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p>E[e<sub>i</sub>² | X<sub>i</sub>] = σ² 이면:</p>
                <div style="text-align: center; font-family: 'Times New Roman', serif;">
                    Avar(β̂) = σ² · E[X<sub>i</sub>X<sub>i</sub>']<sup>−1</sup>
                </div>
                <p style="margin-top: 0.5rem;">→ 이게 Stata/SAS가 기본으로 보고하는 SE</p>
            </div>

            <h3>3.1.4 포화 모형 (Saturated Models)</h3>
            
            <h4>정의</h4>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>포화 모형:</strong> X가 취할 수 있는 모든 값에 대해 별도의 파라미터를 갖는 모형</p>
                <p>→ 가능한 셀의 수 = 파라미터의 수</p>
            </div>
            
            <p><strong>예: 두 개의 더미 (x<sub>1</sub> = 대졸, x<sub>2</sub> = 여성):</strong></p>
            
            <p>비포화 (가산) 모형:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                Y<sub>i</sub> = α + β·x<sub>1i</sub> + γ·x<sub>2i</sub> + ε<sub>i</sub>
            </div>
            
            <p>포화 모형:</p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                Y<sub>i</sub> = α + β·x<sub>1i</sub> + γ·x<sub>2i</sub> + <span style="color: #dc2626;">δ·(x<sub>1i</sub>·x<sub>2i</sub>)</span> + ε<sub>i</sub>
            </div>
            
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">그룹</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">x<sub>1</sub></th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">x<sub>2</sub></th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">가산 모형</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">포화 모형</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">비대졸 남성</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">α</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">α</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">대졸 남성</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">1</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">α + β</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">α + β</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">비대졸 여성</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">1</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">α + γ</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">α + γ</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">대졸 여성</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">1</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">1</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">α + β + γ</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">α + β + γ + <span style="color: #dc2626;">δ</span></td>
                </tr>
            </table>
            
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">항</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">명칭</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">해석</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">β, γ</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">주효과 (Main effects)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">각 변수의 개별 효과</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">δ</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">상호작용 항 (Interaction)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">대졸 효과가 성별에 따라 어떻게 다른지</td>
                </tr>
            </table>
            
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>핵심:</strong> 포화 모형은 CEF를 완벽하게 적합시킨다. 왜냐하면 이산형 X에 대해 CEF는 더미 회귀변수에서 <strong>선형</strong>이기 때문.</p>
            </div>

            <p><strong>모형 계층:</strong></p>
            <ul>
                <li>✅ 포화 모형 → CEF와 완벽히 일치</li>
                <li>⚠️ 상호작용 없는 가산 모형 → CEF의 근사 (제약을 부과)</li>
                <li>❌ 주효과 없이 상호작용만 포함 → 해석 어려움!</li>
            </ul>
        </div>
    </section>

    <!-- 3.2 회귀와 인과관계 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">3.2 회귀와 인과관계</h2>
        <div class="section-content">
            
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>핵심 질문:</strong> 회귀분석이 언제 인과적 해석을 가지는가?</p>
                <p><strong>답:</strong> 회귀가 근사하는 CEF가 인과적일 때, 즉 <strong>조건부 독립 가정(CIA)</strong>이 성립할 때.</p>
            </div>

            <h3>3.2.1 조건부 독립 가정 (CIA)</h3>
            
            <h4>설정: 잠재적 결과</h4>
            <p>교육 연수 s에 대해:</p>
            <ul>
                <li>Y<sub>si</sub> = f<sub>i</sub>(s): 개인 i가 s년 교육을 받았을 때의 잠재적 소득</li>
                <li>s<sub>i</sub>: 실제 교육 연수</li>
                <li>관측된 소득: Y<sub>i</sub> = f<sub>i</sub>(s<sub>i</sub>)</li>
            </ul>
            
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>CIA (Conditional Independence Assumption):</strong></p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.2rem; margin: 1rem 0;">
                    {Y<sub>0i</sub>, Y<sub>1i</sub>, ..., Y<sub>si</sub>, ...} ⊥ s<sub>i</sub> | X<sub>i</sub>
                </div>
                <p style="text-align: center;">"잠재적 결과는 X가 주어지면 실제 교육 연수와 독립"</p>
            </div>

            <h4>CIA의 다른 이름들</h4>
            <ul>
                <li><strong>Selection on observables</strong> (관측 가능 변수에 의한 선택)</li>
                <li><strong>Unconfoundedness</strong> (무교란성)</li>
                <li><strong>Ignorability</strong> (무시가능성)</li>
                <li><strong>Exogeneity</strong> (외생성)</li>
            </ul>

            <h4>CIA의 의미</h4>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>핵심 직관:</strong></p>
                <ul>
                    <li>X<sub>i</sub>가 교육과 잠재적 결과가 상관되는 <strong>모든 이유</strong>를 포착</li>
                    <li>X가 주어지면, 교육은 "<strong>무작위 배정된 것과 같다</strong>"</li>
                    <li>X가 같은 사람들 중에서는 교육 수준이 잠재적 결과와 무관</li>
                </ul>
            </div>
            
            <p><strong>예시:</strong></p>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">X에 포함</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">왜?</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">부모 교육 수준</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">자녀 교육과 능력 모두에 영향</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">가구 소득</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">교육 기회와 네트워크에 영향</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">IQ / 능력 점수</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">교육 선택과 소득 잠재력에 영향</td>
                </tr>
            </table>

            <h4>CIA의 함의</h4>
            <p>CIA가 성립하면, 조건부 비교는 인과적:</p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                E[Y<sub>i</sub> | X<sub>i</sub>, s<sub>i</sub> = s] − E[Y<sub>i</sub> | X<sub>i</sub>, s<sub>i</sub> = s−1]<br><br>
                = E[Y<sub>si</sub> | X<sub>i</sub>, s<sub>i</sub> = s] − E[Y<sub>s-1,i</sub> | X<sub>i</sub>, s<sub>i</sub> = s−1]<br><br>
                = E[Y<sub>si</sub> | X<sub>i</sub>] − E[Y<sub>s-1,i</sub> | X<sub>i</sub>] <span style="color: #666;">(by CIA)</span><br><br>
                = E[Y<sub>si</sub> − Y<sub>s-1,i</sub> | X<sub>i</sub>] <span style="color: #2563eb;">(인과효과!)</span>
            </div>
            <p>→ 교육 수준 간 평균 소득 차이가 <strong>인과적 해석</strong>을 가짐!</p>

            <h4>CIA에서 회귀로</h4>
            <p><strong>Step 1:</strong> 선형 상수 효과 모형 가정</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                f<sub>i</sub>(s) = α + ρs + η<sub>i</sub>
            </div>
            <p>여기서:</p>
            <ul>
                <li>ρ = 교육 1년의 인과효과 (모든 사람에게 동일)</li>
                <li>η<sub>i</sub> = 잠재적 소득의 랜덤 부분 (개인별 이질성)</li>
            </ul>
            
            <p><strong>Step 2:</strong> η<sub>i</sub>를 분해</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                η<sub>i</sub> = X<sub>i</sub>'γ + v<sub>i</sub>
            </div>
            <p>여기서:</p>
            <ul>
                <li>X<sub>i</sub>'γ = X로 설명되는 η의 부분</li>
                <li>v<sub>i</sub> = 설명 안 되는 나머지</li>
            </ul>
            
            <p><strong>Step 3:</strong> 인과적 회귀 모형</p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                Y<sub>i</sub> = α + ρs<sub>i</sub> + X<sub>i</sub>'γ + v<sub>i</sub>
            </div>
            
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>CIA가 성립하면:</strong></p>
                <ul>
                    <li>E[v<sub>i</sub> | s<sub>i</sub>, X<sub>i</sub>] = 0</li>
                    <li>v<sub>i</sub>는 s<sub>i</sub>와 X<sub>i</sub> 모두와 상관 없음</li>
                    <li>→ <strong>OLS로 추정한 ρ̂가 인과효과!</strong></li>
                </ul>
            </div>

            <h3>3.2.2 누락변수 편의 (OVB) 공식</h3>
            
            <p><strong>설정:</strong></p>
            <p>"긴" 회귀 (능력 A<sub>i</sub>를 통제):</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                Y<sub>i</sub> = α<sup>l</sup> + ρ<sup>l</sup>s<sub>i</sub> + A<sub>i</sub>'γ<sup>l</sup> + ε<sub>i</sub><sup>l</sup>
            </div>
            
            <p>"짧은" 회귀 (A<sub>i</sub> 없음):</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                Y<sub>i</sub> = α<sup>s</sup> + ρ<sup>s</sup>s<sub>i</sub> + ε<sub>i</sub><sup>s</sup>
            </div>

            <h4>OVB 공식</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.2rem;">
                    ρ<sup>s</sup> = ρ<sup>l</sup> + γ<sup>l</sup>'δ<sub>As</sub>
                </div>
                <p style="margin-top: 1rem; text-align: center;">
                    <strong>짧은 = 긴 + (누락변수 효과) × (누락변수의 포함변수에 대한 회귀)</strong>
                </p>
            </div>
            
            <p>여기서 δ<sub>As</sub>는 A<sub>i</sub>를 s<sub>i</sub>에 회귀시킨 계수</p>

            <h4>OVB 공식 유도 (Step by Step)</h4>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Step 1:</strong> 짧은 회귀의 계수 정의</p>
                <p style="font-family: 'Times New Roman', serif; margin-left: 1rem;">
                    ρ<sup>s</sup> = Cov(Y<sub>i</sub>, s<sub>i</sub>) / V(s<sub>i</sub>)
                </p>
                
                <p><strong>Step 2:</strong> Y<sub>i</sub>에 긴 회귀식 대입</p>
                <p style="font-family: 'Times New Roman', serif; margin-left: 1rem;">
                    Y<sub>i</sub> = α<sup>l</sup> + ρ<sup>l</sup>s<sub>i</sub> + γ<sup>l</sup>A<sub>i</sub> + ε<sub>i</sub><sup>l</sup>
                </p>
                
                <p><strong>Step 3:</strong> Cov(Y<sub>i</sub>, s<sub>i</sub>) 계산</p>
                <p style="font-family: 'Times New Roman', serif; margin-left: 1rem;">
                    Cov(Y<sub>i</sub>, s<sub>i</sub>) = Cov(ρ<sup>l</sup>s<sub>i</sub> + γ<sup>l</sup>A<sub>i</sub> + ε<sub>i</sub><sup>l</sup>, s<sub>i</sub>)<br>
                    = ρ<sup>l</sup>·V(s<sub>i</sub>) + γ<sup>l</sup>·Cov(A<sub>i</sub>, s<sub>i</sub>) + 0
                </p>
                
                <p><strong>Step 4:</strong> V(s<sub>i</sub>)로 나누기</p>
                <p style="font-family: 'Times New Roman', serif; margin-left: 1rem;">
                    ρ<sup>s</sup> = ρ<sup>l</sup> + γ<sup>l</sup> · <span style="text-decoration: underline;">Cov(A<sub>i</sub>, s<sub>i</sub>) / V(s<sub>i</sub>)</span><br>
                    <span style="margin-left: 4rem;">↑ = δ<sub>As</sub></span>
                </p>
            </div>

            <h4>OVB의 부호 판단</h4>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>편의 = γ<sup>l</sup> × δ<sub>As</sub></strong></p>
                <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                    <tr style="background: #f5f5f5;">
                        <th style="padding: 0.5rem; border: 1px solid #ddd;"></th>
                        <th style="padding: 0.5rem; border: 1px solid #ddd;">δ<sub>As</sub> > 0</th>
                        <th style="padding: 0.5rem; border: 1px solid #ddd;">δ<sub>As</sub> < 0</th>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>γ<sup>l</sup> > 0</strong></td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd; background: #fee2e2;">양의 편의 (과대추정)</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd; background: #dbeafe;">음의 편의 (과소추정)</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>γ<sup>l</sup> < 0</strong></td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd; background: #dbeafe;">음의 편의 (과소추정)</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd; background: #fee2e2;">양의 편의 (과대추정)</td>
                    </tr>
                </table>
            </div>

            <h4>적용: 교육의 수익률</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">통제변수</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">교육 계수</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">해석</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">없음</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.132</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">-</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">연령 더미</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.131</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">거의 변화 없음</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+ 가족 배경</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.114</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">↓ 감소</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+ AFQT 점수</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.087</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">↓ 크게 감소</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+ 직업 더미</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.066</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">⚠️ Bad control?</td>
                </tr>
            </table>
            <p><em>출처: NLSY 데이터</em></p>
            
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>OVB 공식으로 해석:</strong></p>
                <ul>
                    <li>가족 배경, AFQT를 통제하면 계수 감소</li>
                    <li>왜? γ > 0 (능력 → 임금 ↑) AND δ<sub>As</sub> > 0 (능력 ↔ 교육 양의 상관)</li>
                    <li>→ 짧은 회귀가 과대추정하고 있었음</li>
                </ul>
            </div>

            <h3>3.2.3 나쁜 통제 (Bad Control)</h3>
            
            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>정의:</strong></p>
                <ul>
                    <li><strong>나쁜 통제:</strong> 처치의 <strong>결과(outcome)</strong>인 변수</li>
                    <li><strong>좋은 통제:</strong> 처치 <strong>이전에</strong> 결정된 변수</li>
                </ul>
            </div>

            <h4>예시 1: 직업 통제</h4>
            <p>교육 회귀에서 직업을 통제해야 할까?</p>
            
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>문제:</strong> 대학은 직업 선택에 영향을 미친다!</p>
                <ul>
                    <li>w<sub>i</sub> = 1 (화이트칼라 직업)</li>
                    <li>대학 → 화이트칼라 가능성 ↑</li>
                </ul>
            </div>

            <p><strong>화이트칼라 내에서 대졸 vs 비대졸 비교:</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                E[Y<sub>i</sub> | w<sub>i</sub>=1, c<sub>i</sub>=1] − E[Y<sub>i</sub> | w<sub>i</sub>=1, c<sub>i</sub>=0]<br><br>
                = E[Y<sub>1i</sub> − Y<sub>0i</sub> | w<sub>1i</sub>=1] + <span style="color: #dc2626;">{E[Y<sub>0i</sub> | w<sub>1i</sub>=1] − E[Y<sub>0i</sub> | w<sub>0i</sub>=1]}</span>
            </div>
            <p style="text-align: center;"><span style="color: #dc2626;">↑ 새로운 선택 편의!</span></p>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>왜 편의가 생기나?</strong></p>
                <ul>
                    <li>화이트칼라인 대졸자 = <strong>평범한</strong> 대졸자</li>
                    <li>화이트칼라인 비대졸자 = <strong>예외적인</strong> 비대졸자 (특별히 능력 있음)</li>
                    <li>→ <strong>다른 종류의 사람들</strong>을 비교하는 것!</li>
                </ul>
            </div>

            <h4>예시 2: 대리 통제 문제 (Proxy Control)</h4>
            <p>교육 후에 측정된 "늦은" 능력 변수 (예: 성인 IQ)를 쓰면?</p>
            
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                al<sub>i</sub> = π<sub>0</sub> + π<sub>1</sub>s<sub>i</sub> + π<sub>2</sub>a<sub>i</sub> + u<sub>i</sub>
            </div>
            <p>여기서:</p>
            <ul>
                <li>al<sub>i</sub> = 늦게 측정된 능력</li>
                <li>a<sub>i</sub> = 진짜 능력</li>
                <li>π<sub>1</sub> > 0: 교육이 측정된 능력을 높임</li>
            </ul>
            
            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>결과:</strong> 늦은 능력을 통제하면 교육 계수가 <strong>하향 편의</strong></p>
                <p>왜? 교육의 일부 효과가 al을 통해 전달되는데, al을 통제하면 이 경로가 차단됨</p>
            </div>

            <h4>핵심 원칙</h4>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>타이밍이 중요하다!</strong></p>
                <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                    <tr style="background: #f5f5f5;">
                        <th style="padding: 0.5rem; border: 1px solid #ddd;">통제변수 종류</th>
                        <th style="padding: 0.5rem; border: 1px solid #ddd;">통제?</th>
                        <th style="padding: 0.5rem; border: 1px solid #ddd;">예시</th>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">처치 이전에 측정된 변수</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">✅ 좋은 통제</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">부모 교육, 어린 시절 IQ</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">처치의 결과인 변수</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">❌ 나쁜 통제</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">직업, 결혼 상태</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">처치 이후 측정된 변수</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">⚠️ 주의</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">성인 IQ, 성인 건강</td>
                    </tr>
                </table>
            </div>

            <h4>인과 다이어그램으로 이해</h4>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center;">
                <p><strong>좋은 통제 (X):</strong></p>
                <p style="font-family: monospace;">
                    X → D → Y<br>
                    X → Y
                </p>
                <p>X를 통제하면 D→Y 경로만 남음 ✅</p>
                <br>
                <p><strong>나쁜 통제 (M):</strong></p>
                <p style="font-family: monospace;">
                    D → M → Y<br>
                    D → Y
                </p>
                <p>M을 통제하면 D→M→Y 경로가 차단됨 ❌</p>
            </div>
        </div>
    </section>

    <!-- 요약 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Chapter 3 요약</h2>
        <div class="section-content">
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">개념</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">핵심 포인트</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>CEF</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">E[Y|X] - X가 주어졌을 때 Y의 MMSE 예측자</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>회귀</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">CEF에 대한 최선의 선형 근사 (항상!)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>회귀 해부학</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">β<sub>k</sub> = 다른 X 제거 후 이변량 기울기 (FWL)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>CIA</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Y<sub>s</sub> ⊥ s | X - 회귀를 인과적으로 만듦</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>OVB 공식</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">짧은 = 긴 + (누락 효과) × (누락의 포함에 대한 회귀)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>나쁜 통제</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">처치의 결과인 변수는 통제하지 말 것</td>
                </tr>
            </table>

            <h4>핵심 메시지</h4>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <ol>
                    <li><strong>회귀는 CEF의 근사:</strong> CEF가 비선형이어도 회귀는 유용한 요약</li>
                    <li><strong>인과성은 CIA에 달림:</strong> 관측변수 통제 후 처치가 무작위와 같아야</li>
                    <li><strong>OVB를 이해하라:</strong> 통제변수 추가/제거의 효과를 예측 가능</li>
                    <li><strong>타이밍이 중요:</strong> 처치 이전 변수만 통제할 것</li>
                </ol>
            </div>

            <h4>핵심 공식 정리</h4>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <table style="width:100%; border-collapse: collapse;">
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>CEF 분해</strong></td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">Y<sub>i</sub> = E[Y<sub>i</sub>|X<sub>i</sub>] + ε<sub>i</sub></td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>ANOVA</strong></td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">V(Y) = V(E[Y|X]) + E[V(Y|X)]</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>OLS</strong></td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">β = E[XX']<sup>−1</sup>E[XY]</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>OVB</strong></td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">ρ<sup>s</sup> = ρ<sup>l</sup> + γ'δ</td>
                    </tr>
                </table>
            </div>
        </div>
    </section>

    <!-- 참고문헌 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">참고문헌</h2>
        <div class="section-content">
            <ul style="font-size: 0.9rem;">
                <li>Barnow, B., Cain, G., & Goldberger, A. (1981). Selection on observables. <em>Evaluation Studies Review Annual</em>.</li>
                <li>White, H. (1980). A heteroskedasticity-consistent covariance matrix estimator. <em>Econometrica</em>.</li>
                <li>Frisch, R., & Waugh, F. (1933). Partial time regressions as compared with individual trends. <em>Econometrica</em>.</li>
                <li>Angrist, J. (1998). Estimating the labor market impact of voluntary military service. <em>Econometrica</em>.</li>
                <li>Rosenbaum, P., & Rubin, D. (1983). The central role of the propensity score. <em>Biometrika</em>.</li>
            </ul>
        </div>
    </section>

    <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee; display: flex; justify-content: space-between;">
        <a href="/study/angrist-ch2-ko" style="color: #666;">← Chapter 2: The Experimental Ideal</a>
        <a href="/study" style="color: #2563eb;">Back to Study Notes →</a>
    </div>

    <div style="margin-top: 2rem; padding: 1rem; background: #f9fafb; border-radius: 8px; font-size: 0.8rem; color: #6b7280;">
        <em>이 노트는 LLM(Claude)을 활용하여 작성되었습니다.</em>
    </div>
</div>
