---
layout: minimal_base
title: "Angrist Ch.4-2 - LATE & 이질적 효과"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Chapter 4 Part 2: LATE & 이질적 효과</h2>
            <a href="/study/angrist-ch4-part2" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">English</a>
        </div>
        <div class="section-content">
            <p><em>Angrist & Pischke, Mostly Harmless Econometrics — Sections 4.4–4.5</em></p>
        </div>
    </section>

    <!-- 핵심 메시지 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">핵심 메시지</h2>
        <div class="section-content">
            <blockquote style="border-left: 4px solid #2563eb; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                처치효과가 <strong>이질적</strong>일 때(사람마다 처치 혜택이 다를 때), IV는 <strong>국소 평균 처치효과(LATE)</strong>를 추정한다 — 도구변수에 의해 처치 상태가 바뀌는 하위집단인 <em>순응자(compliers)</em>에 대한 인과효과.
            </blockquote>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>이 파트의 핵심 질문들:</strong></p>
                <ol>
                    <li>이질적 효과에서 IV는 무엇을 추정하는가? → LATE (순응자에 대한 효과)</li>
                    <li>순응자는 누구인가? → 도구변수에 따라 처치가 바뀌는 사람들</li>
                    <li>LATE와 ATE, ATT의 관계는? → 일반적으로 다르지만, 특수한 경우에 일치</li>
                    <li>2SLS는 어떻게 일반화되는가? → 공변량별 LATE의 가중평균</li>
                </ol>
            </div>
        </div>
    </section>

    <!-- 4.4 이질적 잠재적 결과의 IV -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4.4 이질적 잠재적 결과에서의 IV</h2>
        <div class="section-content">

            <h3>이질성이 중요한 이유</h3>
            <p>동질적 효과(y<sub>1i</sub> − y<sub>0i</sub> = ρ, 모든 i)는 비현실적. 사람마다 처치 혜택이 다르다. 이는 두 가지 우려를 제기:</p>
            <ul>
                <li><strong>내적 타당성:</strong> IV가 정확히 무엇을 추정하는가?</li>
                <li><strong>외적 타당성:</strong> 결과가 다른 집단으로 일반화되는가?</li>
            </ul>

            <h3>4.4.1 LATE 정리 (Imbens & Angrist, 1994)</h3>

            <h4>네 가지 가정</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">가정</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">수식</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">직관</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>A1: 독립성</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">{y<sub>i</sub>(d,z), d<sub>1i</sub>, d<sub>0i</sub>} ⊥ z<sub>i</sub></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">도구변수가 무작위 배정과 같음</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>A2: 배제</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">y<sub>i</sub>(d, 0) = y<sub>i</sub>(d, 1)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">도구변수는 처치를 통해서만 결과에 영향</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>A3: 1단계</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">E[d<sub>1i</sub> − d<sub>0i</sub>] ≠ 0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">도구변수가 평균적으로 처치에 영향</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>A4: 단조성</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">d<sub>1i</sub> ≥ d<sub>0i</sub>, 모든 i</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">도구변수가 누구도 처치에서 <em>멀어지게</em> 하지 않음</td>
                </tr>
            </table>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>LATE 정리:</strong></p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem; margin: 0.5rem 0;">
                    [E(y<sub>i</sub>|z<sub>i</sub>=1) − E(y<sub>i</sub>|z<sub>i</sub>=0)] / [E(d<sub>i</sub>|z<sub>i</sub>=1) − E(d<sub>i</sub>|z<sub>i</sub>=0)]
                </div>
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem; margin: 0.5rem 0;">
                    = E[y<sub>1i</sub> − y<sub>0i</sub> | d<sub>1i</sub> > d<sub>0i</sub>]
                </div>
                <p style="text-align: center;">IV 추정량 = <strong>순응자의 평균 인과효과</strong></p>
            </div>

            <h4>증명 스케치</h4>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>분자 (축약형):</strong></p>
                <p style="font-family: 'Times New Roman', serif; padding-left: 1rem;">
                    E[y<sub>i</sub>|z=1] − E[y<sub>i</sub>|z=0] = E[(y<sub>1i</sub>−y<sub>0i</sub>)(d<sub>1i</sub>−d<sub>0i</sub>)]
                </p>
                <p>단조성에 의해 (d<sub>1i</sub>−d<sub>0i</sub>)는 0 또는 1이므로:</p>
                <p style="font-family: 'Times New Roman', serif; padding-left: 1rem;">
                    = E[y<sub>1i</sub>−y<sub>0i</sub> | d<sub>1i</sub>>d<sub>0i</sub>] × P[d<sub>1i</sub>>d<sub>0i</sub>]
                </p>
                <p><strong>분모 (1단계):</strong> E[d<sub>1i</sub>−d<sub>0i</sub>] = P[d<sub>1i</sub>>d<sub>0i</sub>]</p>
                <p>나누면 순응 확률이 소거되어 LATE가 남는다.</p>
            </div>

            <h4>왜 단조성이 필요한가?</h4>
            <p>단조성이 없으면 "거역자(defiers)" (d<sub>1i</sub> < d<sub>0i</sub>)가 존재. 축약형이:</p>
            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                E[(y<sub>1i</sub>−y<sub>0i</sub>)|순응자]·P[순응자] − E[(y<sub>1i</sub>−y<sub>0i</sub>)|거역자]·P[거역자]
            </div>
            <p>양의 효과가 거역자에 의해 상쇄될 수 있어 축약형이 오도적일 수 있다.</p>

            <h3>4.4.2 순응자 하위집단</h3>

            <p>도구변수는 모집단을 세 그룹으로 분할:</p>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">그룹</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">정의</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">징병 추첨 예시</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>순응자</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">d<sub>1i</sub>=1, d<sub>0i</sub>=0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">징병 대상 <em>때문에</em> 복무</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>항상-처치자</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">d<sub>1i</sub>=d<sub>0i</sub>=1</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">어차피 자원입대</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>비순응자</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">d<sub>1i</sub>=d<sub>0i</sub>=0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">어차피 면제/연기</td>
                </tr>
            </table>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>일반적으로 LATE ≠ ATE ≠ ATT:</strong></p>
                <ul>
                    <li><strong>ATT</strong> (처치자에 대한 효과) = 항상-처치자와 순응자 효과의 가중평균</li>
                    <li><strong>ATE</strong> (평균 처치효과) = 세 그룹 모두의 효과 가중평균</li>
                    <li><strong>LATE</strong> = 순응자에 대한 효과만</li>
                </ul>
            </div>

            <h4>특수한 경우</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">시나리오</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">예시</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">이유</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">항상-처치자 없음: E[d|z=0]=0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">JTPA 훈련 실험</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">처치자 = 순응자만 → LATE = ATT</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">비순응자 없음: d<sub>1i</sub>=1, 모든 i</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">쌍둥이 도구변수</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">비처치자 = 순응자만 → LATE = E[y₁−y₀|d=0]</td>
                </tr>
            </table>

            <h3>4.4.3 무작위 실험에서의 IV (Bloom 1984)</h3>

            <p><strong>일방적 비순응</strong>(처치 배정받은 일부가 거부, 통제군은 처치 불가)이 있는 무작위 실험에서:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Bloom의 결과:</strong> E[d<sub>i</sub>|z<sub>i</sub>=0] = 0이면:</p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    ITT / 순응률 = E[y<sub>1i</sub>−y<sub>0i</sub> | d<sub>i</sub>=1] = ATT
                </div>
            </div>

            <h4>예시: JTPA 훈련 실험</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;"></th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">훈련 여부별 (OLS)</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">배정 여부별 (ITT)</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">IV 추정치 (ATT)</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">남성</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">$3,970</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">$1,117</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">$1,825</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">여성</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">$2,133</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">$1,243</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">$1,942</td>
                </tr>
            </table>
            <p>OLS(실제 훈련 여부)는 선택 편의로 과대추정. ITT는 60%만 순응하여 과소추정. IV = ITT ÷ 0.6 = 순응자 인과효과 = ATT.</p>

            <h3>4.4.4 순응자의 크기와 특성 파악</h3>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                순응자 비율: P[d<sub>1i</sub> > d<sub>0i</sub>] = E[d<sub>i</sub>|z<sub>i</sub>=1] − E[d<sub>i</sub>|z<sub>i</sub>=0] = <strong>1단계</strong>
            </div>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>순응자 특성 비율:</strong> 이진 특성 x<sub>1i</sub>에 대해,</p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; margin: 0.5rem 0;">
                    P[x<sub>1i</sub>=1 | 순응자] / P[x<sub>1i</sub>=1] = (x<sub>1i</sub>=1 하위집단의 1단계) / (전체 1단계)
                </div>
                <p>이 비율 > 1이면 순응자가 해당 특성을 가질 확률이 불균형적으로 높다.</p>
            </div>
        </div>
    </section>

    <!-- 4.5 LATE의 일반화 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4.5 LATE의 일반화</h2>
        <div class="section-content">

            <h3>4.5.1 다중 도구변수</h3>
            <p>두 도구변수 z<sub>1i</sub>, z<sub>2i</sub>가 각자의 순응자 그룹을 가질 때, 2SLS는:</p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                ρ<sub>2SLS</sub> = λ·ρ<sub>1</sub> + (1−λ)·ρ<sub>2</sub>
            </div>
            <p>도구변수별 LATE의 가중평균. 1단계가 강한 도구변수에 더 큰 가중치 부여.</p>

            <h3>4.5.2 이질적 효과 모형에서의 공변량</h3>

            <p>도구변수가 공변량 X<sub>i</sub>에 <em>조건부로만</em> 유효할 때:</p>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>조건부 독립성:</strong> {y<sub>1i</sub>, y<sub>0i</sub>, d<sub>1i</sub>, d<sub>0i</sub>} ⊥ z<sub>i</sub> | X<sub>i</sub></p>
            </div>

            <h4>포화 및 가중 정리 (Angrist & Imbens 1995)</h4>
            <p>완전 포화 1단계와 포화 공변량 모형으로 2SLS하면:</p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                ρ<sub>2SLS</sub> = E[ω(X<sub>i</sub>) · LATE(X<sub>i</sub>)]
            </div>
            <p>공변량별 LATE의 가중평균. 도구변수가 처치에 더 많은 변동을 만드는 X 값에 더 큰 가중치.</p>

            <h4>Abadie의 카파 가중 (Abadie 2003)</h4>
            <p>2SLS는 순응자의 인과 반응 함수 E[y<sub>i</sub> | d<sub>i</sub>, X<sub>i</sub>, 순응자]를 근사한다. P(z=1|X)에 선형 모형을 사용하면 Abadie 추정량 = 2SLS.</p>

            <h3>4.5.3 다중값 처치의 평균 인과 반응</h3>

            <p>처치가 다중값(예: 교육연수 s ∈ {0, 1, …, S})일 때:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>ACR 정리 (Angrist & Imbens 1995):</strong></p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.05rem; margin: 0.5rem 0;">
                    IV 추정량 = Σ<sub>s</sub> ω<sub>s</sub> · E[Y<sub>s</sub> − Y<sub>s−1</sub> | s<sub>1i</sub> ≥ s > s<sub>0i</sub>]
                </div>
                <p style="margin-top: 0.5rem;">인과 반응 함수를 따라 단위 인과효과의 가중평균. 가중치는 해당 지점에서의 처치 CDF 이동에 비례.</p>
            </div>

            <h4>적용: 의무교육법</h4>
            <p>Acemoglu & Angrist (2000)는 아동노동법과 의무교육법이 주로 8~12학년 범위에서 교육 분포를 이동시키고, 대학 교육에는 영향이 없음을 보여준다. 따라서 이 도구변수를 사용한 IV는 <strong>고등학교 수준</strong>의 교육 수익률을 포착한다.</p>

            <h4>연속 처치: 평균 미분</h4>
            <p>처치가 연속(예: 가격)이면 IV 추정량은 가중 평균 미분:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                IV = ∫ q'(t) · ω(t) dt
            </div>
            <p>예: Angrist, Graddy & Imbens (2000)는 날씨 도구변수를 사용하여 Fulton 어시장의 수요 탄력성을 추정. 폭풍이 가격을 올리고, IV는 폭풍으로 인한 가격 변동 범위에 걸쳐 평균화된 수요 탄력성을 복원.</p>
        </div>
    </section>

    <!-- 요약 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Part 2 요약</h2>
        <div class="section-content">
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">개념</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">핵심 포인트</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>LATE</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">IV = E[y₁−y₀ | 순응자], 일반적으로 ATE나 ATT와 다름</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>네 가지 가정</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">독립성, 배제, 1단계, 단조성</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>단조성</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">거역자 없음; 영향받는 모든 사람이 같은 방향으로 이동</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Bloom의 결과</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">일방적 비순응 → LATE = ATT</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>다중 도구변수</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">2SLS = 도구변수별 LATE의 가중평균</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>ACR 정리</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">다중값 처치 → 반응 함수를 따른 단위 인과효과의 가중평균</td>
                </tr>
            </table>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>실용적 시사점:</strong> 다른 도구변수는 다른 하위집단에 대한 효과를 추정한다. 순응자가 <em>누구인지</em> 이해하는 것이 IV 추정치의 의미와 일반화 가능성을 해석하는 데 핵심적이다.</p>
            </div>
        </div>
    </section>

    <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee; display: flex; justify-content: space-between;">
        <a href="/study/angrist-ch4-part1-ko" style="color: #666;">← Part 1: IV 기초, Wald & 2SLS</a>
        <a href="/study/angrist-ch4-part3-ko" style="color: #2563eb;">Part 3: IV 상세 →</a>
    </div>

    <div style="margin-top: 2rem; padding: 1rem; background: #f9fafb; border-radius: 8px; font-size: 0.8rem; color: #6b7280;">
        <em>이 노트는 LLM (Claude)의 도움을 받아 작성되었습니다.</em>
    </div>
</div>
