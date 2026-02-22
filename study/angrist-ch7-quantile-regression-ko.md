---
layout: minimal_base
title: "앵그리스트 7장 - 분위수 회귀"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">7장: 분위수 회귀</h2>
            <a href="/study/angrist-ch7-quantile-regression" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">English</a>
        </div>
        <div class="section-content">
            <p><em>앵그리스트 & 피슈케, 대체로 무해한 계량경제학 — 7장</em></p>
            <p style="color: #6b7280; font-style: italic;">"기도문을 하나 알려줄게... 내가 알 필요 없는 것은 모르게 해주세요." — 더글러스 애덤스</p>
        </div>
    </section>

    <!-- 핵심 메시지 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">핵심 메시지</h2>
        <div class="section-content">
            <blockquote style="border-left: 4px solid #2563eb; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                <strong>응용 계량경제학의 95%는 평균에 관한 것이다.</strong> 하지만 많은 변수들은 평균만으로는 알 수 없는 방식으로 변화하는 연속 분포를 가진다 — 분포가 퍼지거나 압축될 수 있다. <strong>분위수 회귀</strong>를 사용하면 평균뿐 아니라 전체 분포를 모형화할 수 있다.
            </blockquote>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>핵심 통찰:</strong> 최소제곱법이 조건부 평균에 선형 모형을 적합하듯이, 분위수 회귀는 조건부 분위수에 선형 모형을 적합한다 — 이를 통해 처치가 분포의 다른 부분에 서로 다른 영향을 미치는지 확인할 수 있다.</p>
            </div>
        </div>
    </section>

    <!-- 7.1 분위수 회귀 모형 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">7.1 분위수 회귀 모형</h2>
        <div class="section-content">

            <h3>조건부 분위수 함수 (CQF)</h3>
            <p>출발점은 <strong>조건부 분위수 함수</strong>이다:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center; font-size: 1.1rem;">
                Q<sub>τ</sub>(y<sub>i</sub> | X<sub>i</sub>) = F<sub>Y</sub><sup>-1</sup>(τ | X<sub>i</sub>)
            </div>

            <table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc;">
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb; text-align: left;">τ 값</th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb; text-align: left;">의미</th>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">τ = 0.10</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">하위 10분위</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">τ = 0.50</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">중위수</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">τ = 0.90</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">상위 10분위</td>
                </tr>
            </table>

            <h3>조건부 기대 함수 vs 조건부 분위수 함수</h3>
            <table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc;">
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;"></th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">조건부 기대 함수 (최소제곱)</th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">조건부 분위수 함수 (분위수 회귀)</th>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;"><strong>최소화</strong></td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">E[(y - m(X))²]</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">E[ρ<sub>τ</sub>(y - q(X))]</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;"><strong>손실 함수</strong></td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">제곱 오차</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">체크 함수 ρ<sub>τ</sub></td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;"><strong>추정 대상</strong></td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">조건부 평균</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">조건부 분위수</td>
                </tr>
            </table>

            <h3>체크 함수</h3>
            <p>체크 함수는 양수와 음수 잔차에 <strong>비대칭 가중치</strong>를 부여한다:</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: monospace;">
                ρ<sub>τ</sub>(u) = u · (τ - 1(u ≤ 0))<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= τ·u &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;만약 u > 0<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= (τ-1)·u &nbsp;만약 u ≤ 0
            </div>

            <table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc;">
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">τ</th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">양수 가중치</th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">음수 가중치</th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">결과</th>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">0.5</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">0.5</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">0.5</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">중위수 (최소절대편차)</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">0.9</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">0.9</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">0.1</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">상위 분위수</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">0.1</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">0.1</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">0.9</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">하위 분위수</td>
                </tr>
            </table>

        </div>
    </section>

    <!-- 위치 이동 vs 이분산성 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">위치 이동 vs 이분산성</h2>
        <div class="section-content">

            <h3>경우 1: 위치 이동 (등분산)</h3>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>모형:</strong> y<sub>i</sub> ~ N(X<sub>i</sub>'β, σ²)</p>
                <p><strong>조건부 분위수 함수:</strong> Q<sub>τ</sub>(y<sub>i</sub> | X<sub>i</sub>) = X<sub>i</sub>'β + σ·Φ<sup>-1</sup>(τ)</p>
                <p><strong>핵심 특징:</strong> 기울기 β는 모든 분위수에서 <em>동일</em>. 절편만 τ에 따라 변함.</p>
            </div>

            <h3>경우 2: 이분산성 (위치-척도 모형)</h3>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>모형:</strong> y<sub>i</sub> ~ N(X<sub>i</sub>'β, (X<sub>i</sub>'γ)²)</p>
                <p><strong>조건부 분위수 함수:</strong> Q<sub>τ</sub>(y<sub>i</sub> | X<sub>i</sub>) = X<sub>i</sub>'[β + γ·Φ<sup>-1</sup>(τ)]</p>
                <p><strong>핵심 특징:</strong> 기울기가 <em>τ에 따라 변함</em>. 상위 분위수에서 계수가 더 큼 → X에 따라 불평등 증가.</p>
            </div>

        </div>
    </section>

    <!-- 실증 예시: 교육 수익률 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">실증 예시: 교육 수익률 (표 7.1.1)</h2>
        <div class="section-content">

            <p><strong>자료:</strong> 1980, 1990, 2000년 미국 인구조사. 40-49세 백인/흑인 남성. 통제변수: 인종, 잠재 경력의 이차함수.</p>

            <table style="width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.9rem;">
                <tr style="background: #1e40af; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">인구조사</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">0.10</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">0.25</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">0.50</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">0.75</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">0.90</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">최소제곱</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;"><strong>1980</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.074</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.074</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.068</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.070</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.079</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.072</td>
                </tr>
                <tr style="background: #f8fafc;">
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;"><strong>1990</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.112</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.110</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.106</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.111</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.137</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.114</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;"><strong>2000</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.092</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.105</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.111</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.120</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb; background: #fef3c7;"><strong>.157</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.114</td>
                </tr>
            </table>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>1980년:</strong> 모든 분위수에서 계수 유사 (~0.07) → <strong>위치 이동</strong></p>
                <p><strong>2000년:</strong> 상위 10분위 (15.7%) >> 하위 10분위 (9.2%) → <strong>부채꼴 패턴</strong></p>
                <p><strong>해석:</strong> "교육받은 사람 중에서도 부자가 더 부자가 됨" — 교육이 평균 임금과 불평등 모두 증가시킴.</p>
            </div>

        </div>
    </section>

    <!-- 절단된 분위수 회귀 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">7.1.1 절단된 분위수 회귀</h2>
        <div class="section-content">

            <p><strong>문제:</strong> 일부 자료가 숨겨짐 (예: 현재인구조사 상한 코딩, 기간 절단).</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>핵심 통찰:</strong> 위에서 절단되어도 절단점 <em>아래</em> 분위수는 영향 없음.</p>
                <p>예: 상위 10%가 절단됨 → τ ≤ 0.90 추정치는 영향 없음.</p>
            </div>

            <p><strong>파월 (1986) 해결책:</strong></p>
            <ul>
                <li>모형: Q<sub>τ</sub>(y | X) = min(c, X'β<sub>τ</sub>)</li>
                <li>X'β < c 인 관측치만 사용</li>
            </ul>

            <p><strong>부친스키 (1994) 반복 알고리즘:</strong></p>
            <ol>
                <li>절단 무시하고 β̂<sub>τ</sub> 추정</li>
                <li>X'β̂<sub>τ</sub> < c 인 셀 찾기</li>
                <li>해당 셀만으로 재추정</li>
                <li>수렴까지 반복</li>
            </ol>

        </div>
    </section>

    <!-- 까다로운 점들 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">7.1.3 까다로운 점들</h2>
        <div class="section-content">

            <h3>까다로운 점 1: 개인 효과 vs 분포 효과</h3>
            <div style="background: #fef2f2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>"훈련이 하위 10분위를 올렸다"</strong> ≠ <strong>"가난한 사람이 부자가 됐다"</strong></p>
                <p>분위수 회귀는 특정 개인이 아닌 <em>분포의 형태</em>를 알려준다. <strong>순위 보존</strong>(처치가 순위를 바꾸지 않음)을 가정해야만 개인 수준으로 해석 가능.</p>
            </div>

            <h3>까다로운 점 2: 조건부 분위수 ≠ 주변 분위수</h3>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>평균의 경우:</strong> E[y | X] = X'β ⟹ E[y] = E[X]'β ✓</p>
                <p><strong>분위수의 경우:</strong> Q<sub>τ</sub>(y | X) = X'β<sub>τ</sub> ⟹ Q<sub>τ</sub>(y) ≠ E[X]'β<sub>τ</sub> ✗</p>
                <p>분위수는 비선형 연산자. 주변 분위수 추출에는 X 분포 전체에 대한 적분 필요 (마차도 & 마타, 2005).</p>
            </div>

        </div>
    </section>

    <!-- 7.2 분위수 처치 효과 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">7.2 분위수 처치 효과 (QTE)</h2>
        <div class="section-content">

            <h3>문제: 선택 편의</h3>
            <p>최소제곱법과 마찬가지로, 분위수 회귀도 처치가 내생적일 때 <strong>누락 변수 편의</strong> 문제가 있다.</p>

            <table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc;">
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;"></th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">외생적 d</th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">내생적 d</th>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;"><strong>평균</strong></td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">최소제곱법</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">2단계 최소제곱법</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;"><strong>분위수</strong></td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">분위수 회귀</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;"><strong>분위수 처치 효과</strong></td>
                </tr>
            </table>

            <h3>분위수 처치 효과: 국소 평균 처치 효과의 분위수 확장</h3>
            <p>아바디, 앵그리스트, 임벤스 (2002)가 국소 평균 처치 효과 프레임워크를 분위수로 확장:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: monospace;">
                Q<sub>τ</sub>(y | X, d, 순응자) = α<sub>τ</sub>·d + X'β<sub>τ</sub>
            </div>

            <p>α<sub>τ</sub> = <strong>순응자</strong>에 대한 τ-분위수 처치 효과</p>

            <h3>아바디 카파</h3>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: monospace;">
                κ<sub>i</sub> = 1 - d<sub>i</sub>(1-z<sub>i</sub>)/(1-p(X<sub>i</sub>)) - (1-d<sub>i</sub>)z<sub>i</sub>/p(X<sub>i</sub>)
            </div>

            <p>속성: E[κ | 순응자] = 1, E[κ | 비순응자] = 0</p>

            <p><strong>분위수 처치 효과 추정량:</strong></p>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: monospace;">
                (α<sub>τ</sub>, β<sub>τ</sub>) = arg min E[κ<sub>i</sub> · ρ<sub>τ</sub>(y<sub>i</sub> - α·d<sub>i</sub> - X<sub>i</sub>'b)]
            </div>

        </div>
    </section>

    <!-- 분위수 처치 효과 구현 단계 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">분위수 처치 효과 구현 단계</h2>
        <div class="section-content">

            <ol>
                <li><strong>1단계:</strong> d=1 하위표본에서 프로빗 z ~ y, X → Ê[z | y, d=1, X] 저장</li>
                <li><strong>2단계:</strong> d=0 하위표본에서 프로빗 z ~ y, X → Ê[z | y, d=0, X] 저장</li>
                <li><strong>3단계:</strong> 전체 표본에서 프로빗 z ~ X → P̂(z=1 | X) 저장</li>
                <li><strong>4단계:</strong> 공식으로 Ê[κ | y, d, X] 계산; [0, 1]로 절단</li>
                <li><strong>5단계:</strong> κ-가중 분위수 회귀 실행</li>
                <li><strong>6단계:</strong> 전체 과정 붓스트랩으로 표준오차 계산</li>
            </ol>

        </div>
    </section>

    <!-- 직업훈련협력법 예시 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">실증 예시: 직업훈련협력법 훈련 (표 7.2.1)</h2>
        <div class="section-content">

            <p><strong>설정:</strong> 직업훈련협력법 (1980년대 미국). z = 무작위 배정된 훈련 제안, d = 실제 참여 (~60%), y = 30개월 소득.</p>

            <h3>패널 A: 최소제곱법 & 분위수 회귀 (선택 편의 있음)</h3>
            <table style="width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.9rem;">
                <tr style="background: #1e40af; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;"></th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">최소제곱</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">τ=0.15</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">τ=0.25</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">τ=0.50</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">τ=0.75</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">τ=0.85</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;"><strong>훈련</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">3,754</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb; background: #fef2f2;">1,187</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">2,510</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">4,420</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">4,678</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">4,806</td>
                </tr>
                <tr style="background: #f8fafc;">
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;"><strong>% 영향</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">21%</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb; background: #fef2f2;"><strong>136%</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">75%</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">35%</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">17%</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">13%</td>
                </tr>
            </table>

            <h3>패널 B: 2단계 최소제곱법 & 분위수 처치 효과 (선택 편의 제거)</h3>
            <table style="width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.9rem;">
                <tr style="background: #1e40af; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;"></th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">2단계최소제곱</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">τ=0.15</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">τ=0.25</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">τ=0.50</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">τ=0.75</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">τ=0.85</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;"><strong>훈련</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">1,593</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb; background: #ecfdf5;"><strong>121</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">702</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">1,544</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">3,131</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">3,378</td>
                </tr>
                <tr style="background: #f8fafc;">
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;"><strong>% 영향</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">9%</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb; background: #ecfdf5;"><strong>5%</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">12%</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">10%</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">11%</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">9%</td>
                </tr>
            </table>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>핵심 발견:</strong> 분위수 회귀는 τ=0.15에서 큰 효과 ($1,187, 136%). 하지만 분위수 처치 효과는 거의 0 ($121, 5%)!</p>
                <p><strong>해석:</strong> 저소득 훈련생들이 더 의욕적임 → 양의 선택 편의가 하위 분위수의 분위수 회귀 추정치를 부풀림. 직업훈련협력법은 실제로 상위 분위수에서만 효과가 있었음.</p>
            </div>

        </div>
    </section>

    <!-- 핵심 질문 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">핵심 질문 3개</h2>
        <div class="section-content">

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <h4 style="margin-top: 0; color: #1e40af;">질문 1. 분위수 회귀 vs 최소제곱법</h4>
                <p><strong>Q:</strong> 분위수 회귀가 최소제곱법과 어떻게 다르며, 언제 사용해야 하는가?</p>
                <p><strong>A:</strong> 최소제곱법은 조건부 평균을 추정하고, 분위수 회귀는 조건부 분위수를 추정한다. 사용 시점: (1) 불평등 분석, (2) 이질적 효과 탐지, (3) 위치 이동 vs 부채꼴 패턴 구분, (4) 이상치에 강건한 추정.</p>
            </div>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <h4 style="margin-top: 0; color: #1e40af;">질문 2. 위치 이동 vs 부채꼴 패턴</h4>
                <p><strong>Q:</strong> 분위수별 계수가 τ에 따라 다르면 무엇을 의미하는가?</p>
                <p><strong>A:</strong> 동일한 계수 → 위치 이동 (분포가 균등하게 이동). 증가하는 계수 → 부채꼴 패턴 (X에 따라 불평등 증가). 2000년 인구조사: 상위 10분위 수익률 (15.7%) >> 하위 10분위 (9.2%) → 교육이 불평등 증가시킴.</p>
            </div>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <h4 style="margin-top: 0; color: #1e40af;">질문 3. 분위수 처치 효과의 필요성</h4>
                <p><strong>Q:</strong> 분위수 회귀 추정치가 편향될 수 있는 이유와 분위수 처치 효과의 해결 방법은?</p>
                <p><strong>A:</strong> 처치가 내생적일 때 분위수 회귀도 선택 편의 문제가 있다. 분위수 처치 효과는 도구변수 논리를 적용: 아바디 카파로 순응자일 확률에 따라 관측치에 가중치 부여. 직업훈련협력법 예시: 분위수 회귀의 하위 분위수 효과가 $1,187에서 $121로 감소 (90% 감소).</p>
            </div>

        </div>
    </section>

    <!-- 종합 비교 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">종합 비교: 최소제곱법 vs 분위수 회귀 vs 2단계 최소제곱법 vs 분위수 처치 효과</h2>
        <div class="section-content">

            <table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #1e40af; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">방법</th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">추정 대상</th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">선택 편의</th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">분포 정보</th>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">최소제곱법</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">E[y|X,d]</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">있음</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">평균만</td>
                </tr>
                <tr style="background: #f8fafc;">
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">2단계 최소제곱법</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">순응자의 E[y|X,d]</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">제거</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">평균만</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">분위수 회귀</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">Q<sub>τ</sub>(y|X,d)</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">있음</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">분포 전체</td>
                </tr>
                <tr style="background: #ecfdf5;">
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;"><strong>분위수 처치 효과</strong></td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">순응자의 Q<sub>τ</sub>(y|X,d)</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;"><strong>제거</strong></td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;"><strong>분포 전체</strong></td>
                </tr>
            </table>

        </div>
    </section>

</div>
