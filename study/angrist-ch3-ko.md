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
            
            <p>이 장은 두 가지 핵심 질문을 다룬다:</p>
            <ol>
                <li><strong>회귀분석의 기계적 성질:</strong> CEF와 회귀의 관계 (인과성과 무관)</li>
                <li><strong>회귀분석의 인과적 해석:</strong> 언제 회귀계수가 인과효과인가?</li>
            </ol>
        </div>
    </section>

    <!-- 3.1 회귀분석의 기초 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">3.1 회귀분석의 기초</h2>
        <div class="section-content">
            
            <h3>3.1.1 조건부 기댓값 함수 (CEF)</h3>
            
            <h4>CEF의 정의</h4>
            <p>종속변수 Y<sub>i</sub>가 주어지고 k×1 공변량 벡터 X<sub>i</sub>가 있을 때, CEF는:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                E[Y<sub>i</sub> | X<sub>i</sub>] = X<sub>i</sub>를 고정했을 때 Y<sub>i</sub>의 모집단 평균
            </div>
            
            <p><strong>수학적 정의 (연속 변수):</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                E[Y<sub>i</sub> | X<sub>i</sub> = x] = ∫ t · f<sub>Y</sub>(t | X<sub>i</sub> = x) dt
            </div>
            
            <p><strong>예시: 교육과 임금</strong></p>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p>1980년 센서스 데이터에서 40-49세 백인 남성의 교육 연수별 로그 주급:</p>
                <ul>
                    <li>교육 4년: 평균 로그 임금 ≈ 5.8</li>
                    <li>교육 8년: 평균 로그 임금 ≈ 6.2</li>
                    <li>교육 12년: 평균 로그 임금 ≈ 6.6</li>
                    <li>교육 16년: 평균 로그 임금 ≈ 7.0</li>
                </ul>
                <p>→ 교육 1년당 평균 임금 상승 ≈ <strong>10%</strong></p>
            </div>
            
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>⚠️ 중요:</strong> 교육을 많이 받은 사람이 더 많이 번다는 사실이 교육이 임금을 <em>인과적으로</em> 높인다는 것을 의미하지는 않는다. 이 장의 핵심 주제!</p>
            </div>

            <h4>반복 기댓값의 법칙 (Law of Iterated Expectations)</h4>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>정리:</strong></p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    E[Y<sub>i</sub>] = E{ E[Y<sub>i</sub> | X<sub>i</sub>] }
                </div>
                <p style="margin-top: 0.5rem;">"무조건부 기댓값 = CEF의 기댓값 (X<sub>i</sub>의 분포에 대해)"</p>
            </div>
            
            <p><strong>증명 (연속 변수):</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; font-size: 0.95rem;">
                E{E[Y<sub>i</sub>|X<sub>i</sub>]} = ∫ E[Y<sub>i</sub>|X<sub>i</sub>=u] · g<sub>X</sub>(u) du<br><br>
                = ∫∫ t · f<sub>Y</sub>(t|X<sub>i</sub>=u) dt · g<sub>X</sub>(u) du<br><br>
                = ∫∫ t · f<sub>Y</sub>(t|X<sub>i</sub>=u) · g<sub>X</sub>(u) du dt<br><br>
                = ∫ t · g<sub>Y</sub>(t) dt = E[Y<sub>i</sub>]
            </div>

            <h4>CEF의 세 가지 핵심 성질</h4>
            
            <h5>성질 1: CEF 분해 정리 (Theorem 3.1.1)</h5>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>정리:</strong></p>
                <div style="font-family: 'Times New Roman', serif; font-size: 1.1rem; text-align: center;">
                    Y<sub>i</sub> = E[Y<sub>i</sub> | X<sub>i</sub>] + ε<sub>i</sub>
                </div>
                <p style="margin-top: 0.5rem;">여기서:</p>
                <ul>
                    <li>(i) ε<sub>i</sub>는 X<sub>i</sub>에 대해 <strong>평균 독립</strong>: E[ε<sub>i</sub> | X<sub>i</sub>] = 0</li>
                    <li>(ii) 따라서 ε<sub>i</sub>는 X<sub>i</sub>의 <strong>모든 함수</strong>와 상관 없음</li>
                </ul>
            </div>
            
            <p><strong>증명:</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                (i) E[ε<sub>i</sub> | X<sub>i</sub>] = E[Y<sub>i</sub> − E[Y<sub>i</sub>|X<sub>i</sub>] | X<sub>i</sub>]<br>
                &nbsp;&nbsp;&nbsp;= E[Y<sub>i</sub>|X<sub>i</sub>] − E[Y<sub>i</sub>|X<sub>i</sub>] = 0<br><br>
                (ii) h(X<sub>i</sub>)를 X<sub>i</sub>의 임의의 함수라 하면,<br>
                &nbsp;&nbsp;&nbsp;E[h(X<sub>i</sub>)ε<sub>i</sub>] = E{h(X<sub>i</sub>) · E[ε<sub>i</sub>|X<sub>i</sub>]} = E{h(X<sub>i</sub>) · 0} = 0
            </div>
            
            <p><strong>직관:</strong> 모든 확률변수 Y<sub>i</sub>는 "X로 설명되는 부분"(CEF)과 "X로 설명 안 되는 부분"(잔차)으로 분해 가능. 잔차는 X의 어떤 함수와도 상관 없음.</p>

            <h5>성질 2: CEF 예측 정리 (Theorem 3.1.2)</h5>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>정리:</strong> m(X<sub>i</sub>)를 X<sub>i</sub>의 임의의 함수라 하면,</p>
                <div style="font-family: 'Times New Roman', serif; font-size: 1.1rem; text-align: center;">
                    E[Y<sub>i</sub> | X<sub>i</sub>] = arg min<sub>m(X)</sub> E[(Y<sub>i</sub> − m(X<sub>i</sub>))²]
                </div>
                <p style="margin-top: 0.5rem;">→ CEF는 <strong>최소 평균제곱오차(MMSE)</strong> 예측자</p>
            </div>
            
            <p><strong>증명:</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                (Y<sub>i</sub> − m(X<sub>i</sub>))² = ((Y<sub>i</sub> − E[Y<sub>i</sub>|X<sub>i</sub>]) + (E[Y<sub>i</sub>|X<sub>i</sub>] − m(X<sub>i</sub>)))²<br><br>
                = (Y<sub>i</sub> − E[Y<sub>i</sub>|X<sub>i</sub>])² + 2(E[Y<sub>i</sub>|X<sub>i</sub>] − m(X<sub>i</sub>))(Y<sub>i</sub> − E[Y<sub>i</sub>|X<sub>i</sub>]) + (E[Y<sub>i</sub>|X<sub>i</sub>] − m(X<sub>i</sub>))²<br><br>
                • 첫째 항: m(X<sub>i</sub>)를 포함하지 않음<br>
                • 둘째 항: h(X<sub>i</sub>)ε<sub>i</sub> 형태 → 기댓값 0 (CEF 분해 성질)<br>
                • 셋째 항: m(X<sub>i</sub>) = E[Y<sub>i</sub>|X<sub>i</sub>]일 때 0으로 최소화
            </div>

            <h5>성질 3: ANOVA 정리 (Theorem 3.1.3)</h5>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>정리:</strong></p>
                <div style="font-family: 'Times New Roman', serif; font-size: 1.1rem; text-align: center;">
                    V(Y<sub>i</sub>) = V(E[Y<sub>i</sub> | X<sub>i</sub>]) + E[V(Y<sub>i</sub> | X<sub>i</sub>)]
                </div>
                <p style="margin-top: 0.5rem;">총 분산 = 그룹 간 분산 + 그룹 내 분산</p>
            </div>
            
            <p><strong>증명:</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                CEF 분해에서: Y<sub>i</sub> = E[Y<sub>i</sub>|X<sub>i</sub>] + ε<sub>i</sub><br><br>
                ε<sub>i</sub>와 E[Y<sub>i</sub>|X<sub>i</sub>]는 상관 없으므로:<br>
                V(Y<sub>i</sub>) = V(E[Y<sub>i</sub>|X<sub>i</sub>]) + V(ε<sub>i</sub>)<br><br>
                V(ε<sub>i</sub>) = E[ε<sub>i</sub>²] = E[E[ε<sub>i</sub>²|X<sub>i</sub>]] = E[V(Y<sub>i</sub>|X<sub>i</sub>)]
            </div>

            <h3>3.1.2 선형 회귀와 CEF</h3>
            
            <h4>모집단 회귀계수의 정의</h4>
            <p>k×1 회귀계수 벡터 β는 다음 최소화 문제의 해:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                β = arg min<sub>b</sub> E[(Y<sub>i</sub> − X<sub>i</sub>'b)²]
            </div>
            
            <p><strong>1차 조건:</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                E[X<sub>i</sub>(Y<sub>i</sub> − X<sub>i</sub>'b)] = 0
            </div>
            
            <p><strong>해:</strong></p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                β = E[X<sub>i</sub>X<sub>i</sub>']<sup>−1</sup> E[X<sub>i</sub>Y<sub>i</sub>]
            </div>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>중요:</strong> 정의에 의해 E[X<sub>i</sub>(Y<sub>i</sub> − X<sub>i</sub>'β)] = 0</p>
                <p>즉, 모집단 잔차 e<sub>i</sub> = Y<sub>i</sub> − X<sub>i</sub>'β는 회귀변수와 <strong>정의상</strong> 상관 없다.</p>
                <p>이것은 경제적 가정이 아니라 β의 정의에서 나온다!</p>
            </div>

            <h4>회귀 해부학 공식 (Regression Anatomy)</h4>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>공식 (Frisch-Waugh, 1933):</strong></p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    β<sub>k</sub> = Cov(Y<sub>i</sub>, x̃<sub>ki</sub>) / V(x̃<sub>ki</sub>)
                </div>
                <p style="margin-top: 0.5rem;">여기서 <strong>x̃<sub>ki</sub></strong>는 x<sub>ki</sub>를 다른 모든 공변량에 회귀시킨 <strong>잔차</strong></p>
            </div>
            
            <p><strong>해석:</strong> 다변량 회귀의 각 계수는 다른 변수들을 "제거(partialling out)"한 후의 이변량 기울기</p>
            
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>직관적 이해:</strong></p>
                <ol>
                    <li>x<sub>k</sub>를 다른 모든 X에 회귀 → 잔차 x̃<sub>k</sub> 얻음</li>
                    <li>x̃<sub>k</sub>는 "다른 X로 설명 안 되는 x<sub>k</sub>의 변동"</li>
                    <li>Y를 x̃<sub>k</sub>에 단순 회귀 → 기울기가 β<sub>k</sub>!</li>
                </ol>
                <p><strong>시각화:</strong> ỹ<sub>k</sub> vs x̃<sub>k</sub> 산점도의 기울기 = 다변량 회귀의 β<sub>k</sub></p>
            </div>
            
            <p><strong>검증:</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                Y<sub>i</sub> = β<sub>0</sub> + β<sub>1</sub>x<sub>1i</sub> + ... + β<sub>k</sub>x<sub>ki</sub> + ... + e<sub>i</sub>를 대입하면:<br><br>
                Cov(Y<sub>i</sub>, x̃<sub>ki</sub>) = Cov(β<sub>k</sub>x<sub>ki</sub> + ..., x̃<sub>ki</sub>)<br><br>
                • x̃<sub>ki</sub>는 e<sub>i</sub>와 상관 없음 (회귀변수의 선형결합이므로)<br>
                • x̃<sub>ki</sub>는 다른 공변량과 상관 없음 (잔차이므로)<br>
                • Cov(x<sub>ki</sub>, x̃<sub>ki</sub>) = V(x̃<sub>ki</sub>)<br><br>
                ∴ Cov(Y<sub>i</sub>, x̃<sub>ki</sub>) = β<sub>k</sub> · V(x̃<sub>ki</sub>)
            </div>

            <h4>회귀분석을 정당화하는 세 가지 정리</h4>
            
            <h5>정리 1: 선형 CEF 정리 (Theorem 3.1.4)</h5>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>정리:</strong> CEF가 선형이면, 모집단 회귀함수가 곧 CEF다.</p>
                <p style="font-family: 'Times New Roman', serif;">E[Y<sub>i</sub>|X<sub>i</sub>] = X<sub>i</sub>'α 이면 → β = α</p>
            </div>
            
            <p><strong>증명:</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                CEF 분해 성질에서: E[X<sub>i</sub>(Y<sub>i</sub> − E[Y<sub>i</sub>|X<sub>i</sub>])] = 0<br><br>
                E[Y<sub>i</sub>|X<sub>i</sub>] = X<sub>i</sub>'α를 대입하면:<br>
                E[X<sub>i</sub>(Y<sub>i</sub> − X<sub>i</sub>'α)] = 0<br><br>
                이는 β의 1차 조건과 동일 → β = α
            </div>
            
            <p><strong>CEF가 선형인 경우:</strong></p>
            <ul>
                <li><strong>결합 정규분포:</strong> (Y<sub>i</sub>, X<sub>i</sub>')'가 다변량 정규 → Galton(1886)의 고전적 설정</li>
                <li><strong>포화 모형:</strong> 모든 가능한 X 조합에 별도 파라미터 → 항상 선형</li>
            </ul>

            <h5>정리 2: 최선 선형 예측자 정리 (Theorem 3.1.5)</h5>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>정리:</strong> X<sub>i</sub>'β는 Y<sub>i</sub>의 <strong>최선 선형 예측자</strong> (MMSE 의미에서)</p>
            </div>
            <p><strong>증명:</strong> β는 E[(Y<sub>i</sub> − X<sub>i</sub>'b)²]를 최소화하는 b로 정의됨</p>

            <h5>정리 3: 회귀-CEF 정리 (Theorem 3.1.6) ⭐</h5>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>정리:</strong> X<sub>i</sub>'β는 E[Y<sub>i</sub>|X<sub>i</sub>]에 대한 <strong>최선의 선형 근사</strong></p>
                <div style="font-family: 'Times New Roman', serif; font-size: 1.1rem; text-align: center; margin: 1rem 0;">
                    β = arg min<sub>b</sub> E{(E[Y<sub>i</sub>|X<sub>i</sub>] − X<sub>i</sub>'b)²}
                </div>
            </div>
            
            <p><strong>증명:</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                (Y<sub>i</sub> − X<sub>i</sub>'b)² = {(Y<sub>i</sub> − E[Y<sub>i</sub>|X<sub>i</sub>]) + (E[Y<sub>i</sub>|X<sub>i</sub>] − X<sub>i</sub>'b)}²<br><br>
                = (Y<sub>i</sub> − E[Y<sub>i</sub>|X<sub>i</sub>])² + (E[Y<sub>i</sub>|X<sub>i</sub>] − X<sub>i</sub>'b)²<br>
                &nbsp;&nbsp;+ 2(Y<sub>i</sub> − E[Y<sub>i</sub>|X<sub>i</sub>])(E[Y<sub>i</sub>|X<sub>i</sub>] − X<sub>i</sub>'b)<br><br>
                • 첫째 항: b를 포함하지 않음<br>
                • 셋째 항: 기댓값 0 (CEF 분해 성질 (ii))<br><br>
                ∴ E[(Y<sub>i</sub> − X<sub>i</sub>'b)²]와 E[(E[Y<sub>i</sub>|X<sub>i</sub>] − X<sub>i</sub>'b)²]는 같은 해를 가짐
            </div>
            
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>핵심 통찰 (저자들의 선호):</strong></p>
                <p>CEF가 비선형이더라도, 회귀분석은 그것에 대한 최선의 선형 근사를 제공한다!</p>
                <p>→ 회귀는 Y<sub>i</sub>를 예측하는 것이 아니라 E[Y<sub>i</sub>|X<sub>i</sub>]를 근사하는 것으로 보는 게 더 적절</p>
            </div>

            <h4>그룹 데이터 회귀</h4>
            <p>회귀-CEF 정리의 함의: β는 Y<sub>i</sub> 대신 E[Y<sub>i</sub>|X<sub>i</sub>]를 종속변수로 써도 얻을 수 있다!</p>
            
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                β = E[X<sub>i</sub>X<sub>i</sub>']<sup>−1</sup> E[X<sub>i</sub>Y<sub>i</sub>] = E[X<sub>i</sub>X<sub>i</sub>']<sup>−1</sup> E[X<sub>i</sub> · E(Y<sub>i</sub>|X<sub>i</sub>)]
            </div>
            
            <p><strong>실용적 의미:</strong> 마이크로 데이터 없이 그룹 평균만으로도 동일한 계수 추정 가능</p>
            <p><strong>예시:</strong> 교육 연수별 평균 임금 (21개 그룹)으로 회귀 → 개인 데이터 (409,435명)와 동일한 계수 (0.0674)</p>

            <h3>3.1.3 점근적 OLS 추론</h3>
            
            <h4>OLS 추정량</h4>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                β̂ = (Σ X<sub>i</sub>X<sub>i</sub>')<sup>−1</sup> Σ X<sub>i</sub>Y<sub>i</sub>
            </div>
            <p>= 적률추정량 = 각 기댓값을 표본 합으로 대체</p>

            <h4>핵심 점근 결과들</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">정리</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">내용</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">의미</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>대수의 법칙</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">표본 적률 →<sup>p</sup> 모집단 적률</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">일치성</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>중심극한정리</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">√N(표본적률 − 모집단적률) →<sup>d</sup> N(0, Σ)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">점근 정규성</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>슬러츠키 정리</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">확률 수렴 → 상수로 대체 가능</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">분포 유도에 사용</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>연속 사상 정리</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">plim h(b<sub>N</sub>) = h(plim b<sub>N</sub>)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">함수의 확률 극한</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>델타 방법</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">함수의 점근 분포 = ∇h'Σ∇h</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">비선형 함수의 분산</td>
                </tr>
            </table>

            <h4>β̂의 점근 분포 유도</h4>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                <p><strong>Step 1:</strong> Y<sub>i</sub> = X<sub>i</sub>'β + e<sub>i</sub>를 대입</p>
                β̂ = β + (ΣX<sub>i</sub>X<sub>i</sub>')<sup>−1</sup> ΣX<sub>i</sub>e<sub>i</sub><br><br>
                
                <p><strong>Step 2:</strong> √N(β̂ − β)의 분포</p>
                √N(β̂ − β) = (N<sup>−1</sup>ΣX<sub>i</sub>X<sub>i</sub>')<sup>−1</sup> · N<sup>−1/2</sup>ΣX<sub>i</sub>e<sub>i</sub><br><br>
                
                <p><strong>Step 3:</strong> 슬러츠키 정리 적용</p>
                ≈ E[X<sub>i</sub>X<sub>i</sub>']<sup>−1</sup> · N<sup>−1/2</sup>ΣX<sub>i</sub>e<sub>i</sub><br><br>
                
                <p><strong>Step 4:</strong> CLT 적용 (E[X<sub>i</sub>e<sub>i</sub>] = 0이므로)</p>
                N<sup>−1/2</sup>ΣX<sub>i</sub>e<sub>i</sub> →<sup>d</sup> N(0, E[X<sub>i</sub>X<sub>i</sub>'e<sub>i</sub>²])
            </div>

            <h4>점근 분산</h4>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>이분산-강건 분산 (Robust/White/Eicker-White):</strong></p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    V(β̂) = E[X<sub>i</sub>X<sub>i</sub>']<sup>−1</sup> E[X<sub>i</sub>X<sub>i</sub>'e<sub>i</sub>²] E[X<sub>i</sub>X<sub>i</sub>']<sup>−1</sup>
                </div>
                <p style="margin-top: 0.5rem;">"샌드위치 추정량" - 가운데에 E[X<sub>i</sub>X<sub>i</sub>'e<sub>i</sub>²]이 끼어있음</p>
            </div>
            
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>동분산 가정 하의 단순화:</strong></p>
                <p>E[e<sub>i</sub>²|X<sub>i</sub>] = σ² (상수)이면:</p>
                <div style="text-align: center; font-family: 'Times New Roman', serif;">
                    E[X<sub>i</sub>X<sub>i</sub>'e<sub>i</sub>²] = E[X<sub>i</sub>X<sub>i</sub>' · E[e<sub>i</sub>²|X<sub>i</sub>]] = σ² · E[X<sub>i</sub>X<sub>i</sub>']
                </div>
                <p style="margin-top: 0.5rem;">→ V(β̂) = σ² · E[X<sub>i</sub>X<sub>i</sub>']<sup>−1</sup> (기본 SE)</p>
            </div>

            <h4>왜 이분산이 자연스러운가?</h4>
            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p>CEF가 비선형이면:</p>
                <div style="font-family: 'Times New Roman', serif;">
                    E[(Y<sub>i</sub> − X<sub>i</sub>'β)²|X<sub>i</sub>] = V[Y<sub>i</sub>|X<sub>i</sub>] + (E[Y<sub>i</sub>|X<sub>i</sub>] − X<sub>i</sub>'β)²
                </div>
                <p>→ V[Y<sub>i</sub>|X<sub>i</sub>]가 상수여도, 회귀선과 CEF의 간격이 X에 따라 다르면 잔차 분산이 X에 따라 달라짐!</p>
            </div>
            
            <p><strong>선형확률모형(LPM)의 예:</strong></p>
            <ul>
                <li>Y<sub>i</sub> ∈ {0, 1}인 더미 변수</li>
                <li>포화 모형이라 CEF가 선형</li>
                <li>하지만 V[Y<sub>i</sub>|X<sub>i</sub>] = P[Y<sub>i</sub>|X<sub>i</sub>](1 − P[Y<sub>i</sub>|X<sub>i</sub>])</li>
                <li>→ LPM은 항상 이분산! (상수만 있는 경우 제외)</li>
            </ul>
            
            <p><strong>실증적 조언:</strong></p>
            <ul>
                <li>Robust SE와 기본 SE 차이가 보통 작음 (예: 0.00034 vs 0.00030)</li>
                <li>30% 이상 차이나면 → 코딩 오류나 다른 문제 의심</li>
                <li>Robust SE < 기본 SE → 유한표본 편의 의심</li>
            </ul>

            <h3>3.1.4 포화 모형 (Saturated Models)</h3>
            
            <h4>정의</h4>
            <p><strong>포화 모형:</strong> 설명변수가 취할 수 있는 모든 값에 대해 별도의 파라미터를 가진 모형</p>
            
            <p><strong>예 1: 단일 더미 (대졸 여부)</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                Y<sub>i</sub> = β<sub>0</sub> + β<sub>1</sub> · 1[대졸] + ε<sub>i</sub>
            </div>
            <p>→ 2개 값, 2개 파라미터 = 포화</p>
            
            <p><strong>예 2: 다값 변수 (교육 연수 s<sub>i</sub> = 0, 1, ..., τ)</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                Y<sub>i</sub> = β<sub>0</sub> + Σ<sub>j=1</sub><sup>τ</sup> β<sub>j</sub> · 1[s<sub>i</sub>=j] + ε<sub>i</sub>
            </div>
            <p>β<sub>j</sub> = E[Y<sub>i</sub>|s<sub>i</sub>=j] − E[Y<sub>i</sub>|s<sub>i</sub>=0] ("j년 교육 효과")</p>

            <h4>두 개의 더미: 주효과와 상호작용</h4>
            <p>x<sub>1i</sub> = 대졸, x<sub>2i</sub> = 여성일 때, CEF는 4개 값:</p>
            
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">x<sub>1</sub></th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">x<sub>2</sub></th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">CEF</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">파라미터화</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">E[Y|x<sub>1</sub>=0, x<sub>2</sub>=0]</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">α</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">1</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">E[Y|x<sub>1</sub>=1, x<sub>2</sub>=0]</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">α + β</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">1</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">E[Y|x<sub>1</sub>=0, x<sub>2</sub>=1]</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">α + γ</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">1</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">1</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">E[Y|x<sub>1</sub>=1, x<sub>2</sub>=1]</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">α + β + γ + δ</td>
                </tr>
            </table>
            
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                Y<sub>i</sub> = α + β·x<sub>1i</sub> + γ·x<sub>2i</sub> + δ·(x<sub>1i</sub>·x<sub>2i</sub>) + ε<sub>i</sub>
            </div>
            
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

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>모형 계층:</strong></p>
                <ol>
                    <li><strong>포화 모형</strong> (주효과 + 상호작용) → CEF와 완벽히 일치</li>
                    <li><strong>가산 모형</strong> (주효과만) → 상호작용이 작으면 좋은 근사</li>
                    <li><strong>⚠️ 상호작용만</strong> (주효과 없음) → 해석 불가! 피해야 함</li>
                </ol>
            </div>
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
            
            <h4>잠재적 결과 표기법</h4>
            <p>대학 진학(c<sub>i</sub>)의 효과를 생각해보자:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                잠재적 결과 = { Y<sub>1i</sub> if c<sub>i</sub> = 1 (대학 감)<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ Y<sub>0i</sub> if c<sub>i</sub> = 0 (대학 안 감)
            </div>
            
            <p><strong>관측 결과:</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                Y<sub>i</sub> = Y<sub>0i</sub> + (Y<sub>1i</sub> − Y<sub>0i</sub>) · c<sub>i</sub>
            </div>
            <p>→ Y<sub>1i</sub>와 Y<sub>0i</sub> 중 하나만 관측 가능 (근본적 인과추론 문제)</p>

            <h4>선택 편의</h4>
            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <div style="font-family: 'Times New Roman', serif;">
                    E[Y<sub>i</sub>|c<sub>i</sub>=1] − E[Y<sub>i</sub>|c<sub>i</sub>=0]<br><br>
                    = <span style="color: #059669;">E[Y<sub>1i</sub> − Y<sub>0i</sub>|c<sub>i</sub>=1]</span> + <span style="color: #dc2626;">E[Y<sub>0i</sub>|c<sub>i</sub>=1] − E[Y<sub>0i</sub>|c<sub>i</sub>=0]</span>
                </div>
                <p style="margin-top: 0.5rem;">
                    <span style="color: #059669;">■ ATT (처치받은 자의 평균 처치효과)</span><br>
                    <span style="color: #dc2626;">■ 선택 편의 (대학 간 사람이 원래 더 많이 벌었을 것)</span>
                </p>
            </div>
            <p>→ 선택 편의가 양수이면, 단순 비교는 대학 효과를 <strong>과대추정</strong></p>

            <h4>CIA의 정의</h4>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>조건부 독립 가정 (이항 처치):</strong></p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem; margin: 1rem 0;">
                    {Y<sub>0i</sub>, Y<sub>1i</sub>} ⊥ c<sub>i</sub> | X<sub>i</sub>
                </div>
                <p>"잠재적 결과는 X가 주어지면 처치와 독립"</p>
            </div>
            
            <p><strong>CIA의 함의:</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                E[Y<sub>i</sub>|X<sub>i</sub>, c<sub>i</sub>=1] − E[Y<sub>i</sub>|X<sub>i</sub>, c<sub>i</sub>=0] = E[Y<sub>1i</sub> − Y<sub>0i</sub>|X<sub>i</sub>]
            </div>
            <p>→ X를 통제하면 조건부 비교가 <strong>인과효과</strong>를 준다!</p>

            <h4>다값 처치로 확장</h4>
            <p>교육 연수 s<sub>i</sub>가 여러 값을 가질 때:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                Y<sub>si</sub> ≡ f<sub>i</sub>(s) = 개인 i가 s년 교육을 받았을 때의 잠재적 소득
            </div>
            
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>일반화된 CIA:</strong></p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    Y<sub>si</sub> ⊥ s<sub>i</sub> | X<sub>i</sub>
                </div>
            </div>
            
            <p><strong>CIA가 성립하면:</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                E[Y<sub>i</sub>|X<sub>i</sub>, s<sub>i</sub>=s] − E[Y<sub>i</sub>|X<sub>i</sub>, s<sub>i</sub>=s−1] = E[f<sub>i</sub>(s) − f<sub>i</sub>(s−1)|X<sub>i</sub>]
            </div>
            <p>→ 예: 고졸(s=12)과 중퇴(s=11) 비교는 고졸의 인과효과</p>

            <h4>CIA에서 회귀로: 선형 상수 효과 모형</h4>
            <p><strong>가정:</strong> 잠재적 결과가 선형이고 모든 사람에게 동일</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                f<sub>i</sub>(s) = α + ρs + η<sub>i</sub>
            </div>
            <p>여기서 η<sub>i</sub>는 평균 0인 개인별 오차 (미관측 요인)</p>
            
            <p><strong>관측 결과:</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                Y<sub>i</sub> = α + ρs<sub>i</sub> + η<sub>i</sub>
            </div>
            <p>⚠️ 인과 모형이므로 s<sub>i</sub>와 η<sub>i</sub>가 상관될 수 있음!</p>
            
            <p><strong>CIA 적용:</strong> η<sub>i</sub>를 분해</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                η<sub>i</sub> = X<sub>i</sub>'γ + v<sub>i</sub>, 여기서 E[η<sub>i</sub>|X<sub>i</sub>] = X<sub>i</sub>'γ
            </div>
            
            <p><strong>인과적 회귀 모형:</strong></p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                Y<sub>i</sub> = α + ρs<sub>i</sub> + X<sub>i</sub>'γ + v<sub>i</sub>
            </div>
            <p>CIA가 성립하면:</p>
            <ul>
                <li>E[f<sub>i</sub>(s)|X<sub>i</sub>, s<sub>i</sub>] = E[f<sub>i</sub>(s)|X<sub>i</sub>] = α + ρs + X<sub>i</sub>'γ</li>
                <li>v<sub>i</sub>는 s<sub>i</sub>, X<sub>i</sub>와 상관 없음</li>
                <li><strong>ρ가 인과효과!</strong></li>
            </ul>

            <h3>3.2.2 누락변수 편의 (OVB) 공식</h3>
            
            <h4>설정</h4>
            <p><strong>긴 회귀</strong> (능력 A<sub>i</sub> 통제):</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                Y<sub>i</sub> = α + ρs<sub>i</sub> + A<sub>i</sub>'γ + ε<sub>i</sub>
            </div>
            
            <p><strong>짧은 회귀</strong> (A<sub>i</sub> 없음):</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                Y<sub>i</sub> = α̃ + ρ̃s<sub>i</sub> + ε̃<sub>i</sub>
            </div>

            <h4>OVB 공식</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.2rem;">
                    ρ̃ = ρ + γ'δ<sub>As</sub>
                </div>
                <p style="margin-top: 1rem; text-align: center; font-size: 1.1rem;">
                    <strong>짧은 = 긴 + (누락변수 효과) × (누락의 포함에 대한 회귀)</strong>
                </p>
            </div>
            
            <p>여기서 δ<sub>As</sub>는 A<sub>i</sub>를 s<sub>i</sub>에 회귀시킨 계수 벡터</p>

            <h4>OVB 공식 유도</h4>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Step 1:</strong> 짧은 회귀 계수의 정의</p>
                <div style="font-family: 'Times New Roman', serif; margin-left: 1rem;">
                    ρ̃ = Cov(Y<sub>i</sub>, s<sub>i</sub>) / V(s<sub>i</sub>)
                </div>
                
                <p><strong>Step 2:</strong> 긴 회귀를 대입</p>
                <div style="font-family: 'Times New Roman', serif; margin-left: 1rem;">
                    Cov(Y<sub>i</sub>, s<sub>i</sub>) = Cov(α + ρs<sub>i</sub> + A<sub>i</sub>'γ + ε<sub>i</sub>, s<sub>i</sub>)<br>
                    = ρ·V(s<sub>i</sub>) + γ'·Cov(A<sub>i</sub>, s<sub>i</sub>)
                </div>
                
                <p><strong>Step 3:</strong> V(s<sub>i</sub>)로 나눔</p>
                <div style="font-family: 'Times New Roman', serif; margin-left: 1rem;">
                    ρ̃ = ρ + γ' · Cov(A<sub>i</sub>, s<sub>i</sub>) / V(s<sub>i</sub>)<br>
                    = ρ + γ'δ<sub>As</sub>
                </div>
            </div>

            <h4>OVB의 방향</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">γ (누락변수→Y)</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">δ<sub>As</sub> (누락↔포함)</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">편의 방향</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">예시</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>과대추정</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">능력↑ → 임금↑, 능력↑ → 교육↑</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">과소추정</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">동기↑ → 임금↑, but 교육 기회비용↑</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">과소추정</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">-</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">과대추정</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">-</td>
                </tr>
            </table>

            <h4>실증 예시: NLSY 교육 수익률</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">통제변수</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">교육 계수</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">SE</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">없음</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.132</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(0.007)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">연령 더미</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.131</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(0.007)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+ 부모 교육, 인종, 지역</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.114</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(0.007)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+ AFQT 점수</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.087</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(0.009)</td>
                </tr>
                <tr style="background: #fee2e2;">
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+ 직업 더미 ⚠️</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.066</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(0.010)</td>
                </tr>
            </table>
            
            <p><strong>해석:</strong></p>
            <ul>
                <li>0.132 → 0.114: 가족 배경이 임금, 교육 모두와 양의 상관</li>
                <li>0.114 → 0.087: 능력(AFQT)이 임금, 교육 모두와 양의 상관</li>
                <li>0.087 → 0.066: ⚠️ 주의 필요! (나쁜 통제 문제)</li>
            </ul>

            <h4>CIA가 그럴듯한 경우</h4>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>1. 조건부 무작위 배정:</strong></p>
                <ul>
                    <li>Black et al. (2003): 재취업 훈련 프로그램</li>
                    <li>자격 조건이 관측 변수로 결정</li>
                    <li>훈련 기회는 자격자 중 추첨으로 배정</li>
                </ul>
                
                <p><strong>2. 상세한 제도적 지식:</strong></p>
                <ul>
                    <li>Angrist (1998): 자원 군복무의 효과</li>
                    <li>군대가 지원자를 관측 가능 변수로 선발</li>
                    <li>마지막에 "탈락"하는 것은 거의 무작위</li>
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

            <h4>예시 1: 직업 통제 문제</h4>
            <p><strong>상황:</strong> 대학 졸업(c<sub>i</sub>)이 임금(Y<sub>i</sub>)에 미치는 효과</p>
            <p>직업(w<sub>i</sub> = 화이트칼라 여부)도 대학의 영향을 받음</p>
            
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                Y<sub>i</sub> = c<sub>i</sub>·Y<sub>1i</sub> + (1−c<sub>i</sub>)·Y<sub>0i</sub><br>
                w<sub>i</sub> = c<sub>i</sub>·w<sub>1i</sub> + (1−c<sub>i</sub>)·w<sub>0i</sub>
            </div>
            
            <p><strong>c<sub>i</sub>가 무작위 배정되었다고 가정:</strong></p>
            <ul>
                <li>E[Y<sub>i</sub>|c<sub>i</sub>=1] − E[Y<sub>i</sub>|c<sub>i</sub>=0] = E[Y<sub>1i</sub> − Y<sub>0i</sub>] ✓ 인과효과</li>
                <li>E[w<sub>i</sub>|c<sub>i</sub>=1] − E[w<sub>i</sub>|c<sub>i</sub>=0] = E[w<sub>1i</sub> − w<sub>0i</sub>] ✓ 인과효과</li>
            </ul>
            
            <p><strong>하지만 직업 내 비교는?</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                E[Y<sub>i</sub>|w<sub>i</sub>=1, c<sub>i</sub>=1] − E[Y<sub>i</sub>|w<sub>i</sub>=1, c<sub>i</sub>=0]<br><br>
                = E[Y<sub>1i</sub>|w<sub>1i</sub>=1] − E[Y<sub>0i</sub>|w<sub>0i</sub>=1]<br><br>
                = <span style="color: #059669;">E[Y<sub>1i</sub> − Y<sub>0i</sub>|w<sub>1i</sub>=1]</span> + <span style="color: #dc2626;">{E[Y<sub>0i</sub>|w<sub>1i</sub>=1] − E[Y<sub>0i</sub>|w<sub>0i</sub>=1]}</span>
            </div>
            
            <p><span style="color: #dc2626;"><strong>선택 편의:</strong></span> 대학이 화이트칼라 풀의 구성을 바꿈!</p>
            <ul>
                <li>w<sub>1i</sub>=1 인 사람: 대졸로서 화이트칼라 = 평범한 대졸자</li>
                <li>w<sub>0i</sub>=1 인 사람: 비대졸로서 화이트칼라 = <strong>예외적인</strong> 비대졸자</li>
                <li>→ 서로 다른 종류의 사람을 비교!</li>
            </ul>

            <h4>예시 2: 대리 통제 문제 (Proxy Control)</h4>
            <p><strong>상황:</strong> 8학년 때 측정한 능력(a<sub>i</sub>)을 통제하고 싶지만, 데이터 없음</p>
            <p>대신 교육 후 측정한 "늦은 능력"(al<sub>i</sub>)이 있음</p>
            
            <p><strong>원하는 회귀:</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                Y<sub>i</sub> = α + ρs<sub>i</sub> + γa<sub>i</sub> + ε<sub>i</sub>
            </div>
            
            <p><strong>늦은 능력의 구조:</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                al<sub>i</sub> = π<sub>0</sub> + π<sub>1</sub>s<sub>i</sub> + π<sub>2</sub>a<sub>i</sub>
            </div>
            <p>→ 교육이 측정된 능력을 높임 (π<sub>1</sub> > 0)</p>
            
            <p><strong>a<sub>i</sub>를 al<sub>i</sub>로 대체하면:</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                a<sub>i</sub> = (al<sub>i</sub> − π<sub>0</sub> − π<sub>1</sub>s<sub>i</sub>) / π<sub>2</sub> 를 대입<br><br>
                Y<sub>i</sub> = (α − γπ<sub>0</sub>/π<sub>2</sub>) + (ρ − γπ<sub>1</sub>/π<sub>2</sub>)s<sub>i</sub> + (γ/π<sub>2</sub>)al<sub>i</sub> + ε<sub>i</sub>
            </div>
            
            <p><strong>결과:</strong> 교육 계수가 ρ − γπ<sub>1</sub>/π<sub>2</sub></p>
            <ul>
                <li>γ, π<sub>1</sub>, π<sub>2</sub> 모두 양수이면</li>
                <li>→ 계수가 ρ보다 <strong>작아짐</strong> (하향 편의)</li>
            </ul>
            
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>대리 통제의 딜레마:</strong></p>
                <ul>
                    <li>직업 통제: 완전히 잘못됨 (결과를 통제)</li>
                    <li>대리 통제: 의도는 좋지만, 정확한 효과를 주지 않음</li>
                    <li>그래도 아무것도 안 하는 것보다 나을 수 있음</li>
                    <li>진정한 효과는 두 추정치 사이에 있을 가능성</li>
                </ul>
            </div>

            <h4>핵심 원칙</h4>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>타이밍이 중요하다!</strong></p>
                <ul>
                    <li>✅ 처치 <strong>이전에</strong> 결정된 변수 → 좋은 통제</li>
                    <li>❌ 처치 <strong>이후에</strong> 결정된 변수 → 잠재적으로 나쁜 통제</li>
                </ul>
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
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>CEF 분해</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Y = E[Y|X] + ε, E[ε|X] = 0</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>회귀</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">CEF에 대한 최선의 선형 근사 (CEF가 비선형이어도!)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>회귀 해부학</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">β<sub>k</sub> = Cov(Y, x̃<sub>k</sub>)/V(x̃<sub>k</sub>) (다른 X 제거 후)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Robust SE</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">이분산 하에서도 유효한 표준오차</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>CIA</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Y<sub>s</sub> ⊥ s | X - 회귀를 인과적으로 만듦</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>OVB 공식</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">짧은 = 긴 + γ'δ</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>나쁜 통제</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">처치의 결과인 변수는 통제하지 말 것</td>
                </tr>
            </table>

            <h4>핵심 메시지</h4>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <ol>
                    <li><strong>회귀는 CEF의 근사:</strong> CEF가 비선형이어도 회귀는 최선의 선형 근사 제공</li>
                    <li><strong>인과성은 별개 문제:</strong> 회귀의 기계적 성질 vs 인과적 해석은 다른 질문</li>
                    <li><strong>CIA가 핵심:</strong> 관측변수 통제 후 처치가 "무작위와 같아야" 인과적 해석 가능</li>
                    <li><strong>OVB를 이해하라:</strong> 통제변수 추가/제거 효과를 예측하고 해석할 수 있음</li>
                    <li><strong>타이밍이 중요:</strong> 처치 이전 변수만 통제, 처치 이후 변수는 나쁜 통제</li>
                </ol>
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
                <li>Black, D., Smith, J., Berger, M., & Noel, B. (2003). Is the threat of reemployment services more effective than the services themselves? <em>American Economic Review</em>.</li>
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
