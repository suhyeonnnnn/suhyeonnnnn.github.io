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

    <!-- 적용 사례: Angrist & Evans (1998) -->
    <section class="section fade-in-delay">
        <h2 class="section-title">적용: Angrist & Evans (1998) — 출산과 노동공급</h2>
        <div class="section-content">
            <p><strong>연구 질문:</strong> 셋째 자녀 출산이 여성의 노동공급을 인과적으로 감소시키는가?</p>

            <h3>식별 문제</h3>
            <p>자녀 2명 vs 3명 이상인 어머니의 단순 OLS 비교는 인과관계와 선택을 혼동: 자녀가 많은 여성은 본래 가정 중심적 선호가 강할 수 있어 자녀 수와 노동공급 <em>모두</em>에 영향.</p>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <strong style="color: #92400e;">핵심 문제:</strong> 출산은 내생적 — 관찰 불가능한 선호가 자녀 수와 노동공급 결정을 동시에 주도.
            </div>

            <h3>셋째 자녀를 위한 두 가지 도구변수</h3>
            <p>자녀가 2명 이상인 어머니를 대상으로, 두 가지 외생적 변동 활용:</p>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;"></th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">둘째 출산 시 쌍둥이</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">첫 두 자녀 동성</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>논리</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">쌍둥이가 기계적으로 자녀 ≥3명을 만듦</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">부모가 성별 다양성을 선호 → 셋째 시도 확률 ↑</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>1단계</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.625 (매우 강함)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.067 (약함)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>타당성</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">쌍둥이 출산은 본질적으로 무작위</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">자녀 성별 구성은 무작위</td>
                </tr>
            </table>

            <h3>추정 결과</h3>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">결과변수</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">OLS</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Twins IV</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Same-sex IV</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">취업 여부</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.167</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.083</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.135</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">연간 근로주수</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−8.05</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−3.83</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−6.23</td>
                </tr>
            </table>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <strong style="color: #92400e;">핵심 관찰:</strong> |OLS| > |Same-sex IV| > |Twins IV|. 같은 처치, 같은 결과변수인데 추정치가 다르다. 왜?
            </div>

            <h3>추정치가 다른 이유: 순응자가 다르다</h3>
            <p>각 도구변수는 서로 다른 <strong>순응자 하위집단</strong>의 효과를 식별:</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Twins 순응자</strong> = 쌍둥이가 아니었으면 셋째를 낳지 <em>않았을</em> 어머니들</p>
                <ul>
                    <li>나이 많고, 교육 수준 높고, 커리어 확립</li>
                    <li>2명만 계획 → 쌍둥이로 강제 3명</li>
                    <li>→ 노동공급 감소가 <strong>작음</strong> (커리어 애착이 충격을 완충)</li>
                </ul>
            </div>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Same-sex 순응자</strong> = 성별 다양성 선호로 셋째를 낳게 된 어머니들</p>
                <ul>
                    <li>젊고, 교육 수준 낮고, 커리어 초기 단계</li>
                    <li>가족 구성에 대한 강한 선호</li>
                    <li>→ 노동공급 감소가 <strong>큼</strong> (낮은 커리어 애착, 높은 기회비용)</li>
                </ul>
            </div>

            <h3>ATE / ATT / ITT / LATE 관점에서의 매핑</h3>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">추정량</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">정의</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">이 연구에서</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong style="color: #dc2626;">ATE</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">E[Y(1)−Y(0)], 전체 모집단</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">2자녀 <em>모든</em> 어머니가 셋째를 낳으면 — 직접 관측 불가</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong style="color: #059669;">ATT</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">E[Y(1)−Y(0)|D=1], 처치자</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><em>실제로</em> 셋째를 낳은 어머니 — OLS(−0.167)가 추정 시도하나 선택 편의</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong style="color: #d97706;">ITT</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">E[Y|Z=1]−E[Y|Z=0], 할당별</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">쌍둥이/동성에 "배정"된 것의 효과 — 축약형, 항상 불편</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong style="color: #7c3aed;">LATE</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">E[Y(1)−Y(0)|순응자]</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Twins: −0.083 | Same-sex: −0.135 — 다른 순응자 → 다른 LATE</td>
                </tr>
            </table>

            <h3>수학적 관계</h3>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                <p><strong>ATE</strong> = E[Y₁−Y₀|C]·π<sub>C</sub> + E[Y₁−Y₀|AT]·π<sub>AT</sub> + E[Y₁−Y₀|NT]·π<sub>NT</sub></p>
                <p><strong>ATT</strong> = E[Y₁−Y₀|C]·π<sub>C</sub>/(π<sub>C</sub>+π<sub>AT</sub>) + E[Y₁−Y₀|AT]·π<sub>AT</sub>/(π<sub>C</sub>+π<sub>AT</sub>)</p>
                <p><strong>ITT</strong> = LATE × π<sub>C</sub>  (항상 불편, |ITT| ≤ |LATE|)</p>
                <p><strong>LATE</strong> = E[Y₁−Y₀ | 순응자] = ITT / 1단계</p>
            </div>

            <h4>크기 관계 요약</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">관계</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">조건</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">|ITT| &lt; |LATE|</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">항상 (순응률 &lt; 1일 때)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">ATT ≥ ATE (보통)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">효과 큰 사람이 선택적으로 참여</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">LATE = ATT</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">항상-처치자 없음 (Bloom 1984)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">LATE₁ ≠ LATE₂</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">다른 IV → 다른 순응자 (Angrist & Evans)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">LATE = ATE</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">동질적 처치효과 (모든 사람에게 효과 동일)</td>
                </tr>
            </table>

            <h4>방법론 → 추정량 연결</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">방법론</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">추정하는 효과</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">일반화 범위</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">RCT (완전 순응)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong style="color: #dc2626;">ATE</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">넓음</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">RCT (비순응) + IV</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong style="color: #7c3aed;">LATE</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">순응자 한정</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">DID / Matching / PSM</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong style="color: #059669;">ATT</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">처치군과 비슷한 집단</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">RDD</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong style="color: #7c3aed;">LATE at cutoff</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Cutoff 근처 한정</td>
                </tr>
            </table>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Angrist & Evans의 핵심 교훈:</strong></p>
                <ol>
                    <li><strong>LATE ≠ ATE ≠ ATT.</strong> OLS(−0.167), Twins IV(−0.083), Same-sex IV(−0.135) 모두 같은 연구 질문에 다른 숫자.</li>
                    <li><strong>다른 도구변수 → 다른 순응자 → 다른 LATE.</strong> 도구변수 선택이 <em>누구의</em> 효과를 추정하는지를 결정.</li>
                    <li><strong>순응자 특성이 차이를 설명.</strong> 추정치 차이는 무작위가 아니라 각 순응자 집단의 인구통계학적 구성으로 체계적으로 설명됨.</li>
                    <li><strong>정책적 함의가 달라진다.</strong> 취업 효과 −8% vs −17%는 완전히 다른 보육정책 결론으로 이어짐.</li>
                </ol>
            </div>
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
