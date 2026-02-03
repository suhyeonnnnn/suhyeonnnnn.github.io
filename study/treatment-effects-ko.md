---
layout: minimal_base
title: "Treatment Effects 가이드 - ATE, ATT, ITT, LATE"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Treatment Effects: ATE, ATT, ITT, LATE</h2>
            <a href="/study/treatment-effects" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">English</a>
        </div>
        <div class="section-content">
            <p><em>Angrist & Evans (1998) 사례 연구를 중심으로 — MHE Chapter 4 보충 자료</em></p>
        </div>
    </section>

    <!-- 핵심 메시지 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">핵심 메시지</h2>
        <div class="section-content">
            <blockquote style="border-left: 4px solid #2563eb; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                "효과가 얼마인가?"가 아니라 <strong>"누구에 대한 효과인가?"</strong>가 핵심이다 — 같은 처치라도 대상 집단에 따라 다른 추정치(ATE, ATT, ITT, LATE)가 도출된다. 어떤 추정량을 식별하는지 이해하는 것이 올바른 해석과 정책 설계의 출발점이다.
            </blockquote>
        </div>
    </section>

    <!-- 1부: 정의 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">1. Treatment Effect 추정량</h2>
        <div class="section-content">

            <!-- ATE -->
            <div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1.5rem 0;">
                <h3 style="margin-top: 0;"><span style="background: #dc2626; color: white; padding: 0.2rem 0.5rem; border-radius: 4px; font-family: monospace; font-size: 0.85rem;">ATE</span> Average Treatment Effect (평균 처치효과)</h3>
                <p><strong>전체 모집단</strong>에서 처치를 받았을 때와 받지 않았을 때의 평균적 결과 차이.</p>
                <div style="background: white; border: 1px solid #fecaca; padding: 1rem; border-radius: 6px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    ATE = E[Y<sub>i</sub>(1) − Y<sub>i</sub>(0)]
                </div>
                <ul>
                    <li>모든 개인이 처치를 받았다면 vs 모두 받지 않았다면의 비교</li>
                    <li><strong>보편적 정책</strong>(예: 전 국민 의무 프로그램)을 고려할 때 관련됨</li>
                    <li>반사실(counterfactual)이 관측 불가 → 강한 가정이나 완벽한 RCT 필요</li>
                </ul>
            </div>

            <!-- ATT -->
            <div style="background: #ecfdf5; border-left: 4px solid #059669; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1.5rem 0;">
                <h3 style="margin-top: 0;"><span style="background: #059669; color: white; padding: 0.2rem 0.5rem; border-radius: 4px; font-family: monospace; font-size: 0.85rem;">ATT</span> Average Treatment Effect on the Treated (처치자 평균 처치효과)</h3>
                <p><strong>실제로 처치를 받은 집단</strong>에서의 평균 인과효과.</p>
                <div style="background: white; border: 1px solid #a7f3d0; padding: 1rem; border-radius: 6px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    ATT = E[Y<sub>i</sub>(1) − Y<sub>i</sub>(0) | D<sub>i</sub> = 1]
                </div>
                <ul>
                    <li>처치자의 실제 결과 vs 만약 처치를 받지 않았다면의 결과 비교</li>
                    <li><strong>자발적 프로그램</strong> 평가에서 관련됨</li>
                    <li>효과가 큰 사람이 선택적으로 참여하면 보통 <strong>ATT > ATE</strong></li>
                </ul>
            </div>

            <div style="background: #fef3c7; border: 1px solid #fcd34d; padding: 1rem 1.5rem; border-radius: 6px; margin: 1.5rem 0; font-size: 0.95rem;">
                <strong style="color: #92400e;">ATE vs ATT:</strong> 이질적 처치효과와 자기선택이 있으면 둘은 다르다. 처치 혜택이 큰 사람들이 선택적으로 참여하면 <strong>ATT > ATE</strong>.
            </div>

            <!-- ITT -->
            <div style="background: #fffbeb; border-left: 4px solid #d97706; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1.5rem 0;">
                <h3 style="margin-top: 0;"><span style="background: #d97706; color: white; padding: 0.2rem 0.5rem; border-radius: 4px; font-family: monospace; font-size: 0.85rem;">ITT</span> Intent-to-Treat (처치 의도 효과)</h3>
                <p>실제 처치 수령 여부와 무관하게, 처치에 <strong>배정</strong>된 것의 효과.</p>
                <div style="background: white; border: 1px solid #fde68a; padding: 1rem; border-radius: 6px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    ITT = E[Y<sub>i</sub> | Z<sub>i</sub> = 1] − E[Y<sub>i</sub> | Z<sub>i</sub> = 0]
                </div>
                <ul>
                    <li>Z는 처치 할당, D는 실제 처치 수령</li>
                    <li><strong>항상 불편추정치</strong> — 비순응이 있어도 무작위화를 보존</li>
                    <li>프로그램을 <strong>제공하는 것</strong>의 현실적 효과 반영 (비참여 포함)</li>
                    <li>|ITT| ≤ |LATE| — ITT = LATE × 순응률이므로</li>
                </ul>
            </div>

            <!-- LATE -->
            <div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1.5rem 0;">
                <h3 style="margin-top: 0;"><span style="background: #7c3aed; color: white; padding: 0.2rem 0.5rem; border-radius: 4px; font-family: monospace; font-size: 0.85rem;">LATE</span> Local Average Treatment Effect (국소 평균 처치효과)</h3>
                <p>도구변수에 의해 처치 상태가 바뀌는 <strong>순응자(compliers)</strong>에 대한 평균 인과효과.</p>
                <div style="background: white; border: 1px solid #c4b5fd; padding: 1rem; border-radius: 6px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    LATE = Cov(Y, Z) / Cov(D, Z) = ITT / 1단계
                </div>
                <ul>
                    <li><strong>순응자에만</strong> 적용 — 항상-처치자와 비순응자 제외</li>
                    <li><strong>단조성(monotonicity)</strong> 가정 필요 (거역자 없음)</li>
                    <li>다른 도구변수 → 다른 순응자 → 다른 LATE</li>
                    <li>RDD도 cutoff 근처 순응자에 대한 LATE로 해석 가능</li>
                </ul>
            </div>

            <!-- 요약 테이블 -->
            <h3>핵심 비교</h3>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">추정량</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">대상 집단</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">주요 상황</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">방법론</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #dc2626; font-weight: 500;">ATE</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">전체 모집단</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">보편적 정책 효과</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">RCT (완전 순응)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #059669; font-weight: 500;">ATT</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">처치 받은 집단</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">자발적 프로그램 평가</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">DID, Matching/PSM</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #d97706; font-weight: 500;">ITT</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">할당받은 집단</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">비순응 있는 RCT</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">축약형(Reduced form)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #7c3aed; font-weight: 500;">LATE</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">순응자(Compliers)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">IV / RDD 추정</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">2SLS, Wald 추정량</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- 2부: Angrist & Evans -->
    <section class="section fade-in-delay">
        <h2 class="section-title">2. 사례 연구: Angrist & Evans (1998)</h2>
        <div class="section-content">
            <p><strong>연구 질문:</strong> 셋째 자녀 출산이 여성의 노동공급을 인과적으로 감소시키는가?</p>

            <h3>식별 문제</h3>
            <p>자녀 2명 vs 3명 이상인 어머니의 단순 OLS 비교는 인과관계와 선택을 혼동한다: 자녀가 많은 여성은 본래 가정 중심적 선호가 강할 수 있어 자녀 수와 노동공급 <em>모두</em>에 영향을 미친다.</p>

            <div style="background: #fef3c7; border: 1px solid #fcd34d; padding: 1rem 1.5rem; border-radius: 6px; margin: 1rem 0;">
                <strong style="color: #92400e;">핵심 문제:</strong> 출산은 내생적 — 관찰 불가능한 선호가 자녀 수와 노동공급 결정을 동시에 주도한다.
            </div>

            <h3>셋째 자녀를 위한 두 가지 도구변수</h3>
            <p>자녀가 2명 이상인 어머니를 대상으로, 셋째 자녀 출산(D) 확률에 대한 두 가지 외생적 변동 활용:</p>

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

            <div style="background: #fef3c7; border: 1px solid #fcd34d; padding: 1rem 1.5rem; border-radius: 6px; margin: 1rem 0;">
                <strong style="color: #92400e;">핵심 관찰:</strong> |OLS| > |Same-sex IV| > |Twins IV|. 같은 처치, 같은 결과변수인데 추정치가 다르다. 왜?
            </div>

            <h3>추정치가 다른 이유: 순응자가 다르다</h3>
            <p>각 도구변수는 서로 다른 <strong>순응자 하위집단</strong>의 효과를 식별한다:</p>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #7c3aed; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">특성</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">표본 평균</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Twins 비율</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Same-sex 비율</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">첫 출산 시 30세 이상</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.003</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>1.39</strong> (과대대표)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">1.00 (평균적)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">대졸 이상</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.132</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>1.14</strong> (과대대표)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>0.70</strong> (과소대표)</td>
                </tr>
            </table>
            <p style="font-size: 0.9rem; color: #6b7280;"><em>비율 > 1이면 해당 특성이 순응자 집단에서 과대대표됨을 의미.</em></p>

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

            <h3>Treatment Effect 관점에서의 매핑</h3>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">추정량</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">이 연구에서의 해석</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">값 / 상태</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #dc2626; font-weight: 500;">ATE</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">2자녀 <em>모든</em> 어머니가 셋째를 낳으면</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">직접 관측 불가; 두 LATE 사이 어딘가</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #059669; font-weight: 500;">ATT</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><em>실제로</em> 셋째를 낳은 어머니에 대한 효과</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">OLS(−0.167)가 추정 시도하나 선택 편의로 편향</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #d97706; font-weight: 500;">ITT</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">쌍둥이/동성에 "배정"된 것의 효과</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">축약형: 예) 쌍둥이 RF 취업효과 = −0.052</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #7c3aed; font-weight: 500;">LATE</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">도구변수 <em>때문에</em> 셋째를 낳은 어머니</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Twins: −0.083 | Same-sex: −0.135</td>
                </tr>
            </table>

            <h3>이 연구의 핵심 교훈</h3>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <ol>
                    <li><strong>LATE ≠ ATE ≠ ATT.</strong> OLS(−0.167), Twins IV(−0.083), Same-sex IV(−0.135) 모두 같은 연구 질문에 다른 숫자를 제시.</li>
                    <li><strong>다른 도구변수 → 다른 순응자 → 다른 LATE.</strong> 도구변수 선택이 <em>누구의</em> 효과를 추정하는지를 결정.</li>
                    <li><strong>순응자 특성이 차이를 설명.</strong> 추정치 차이는 무작위가 아니라 각 순응자 집단의 인구통계학적 구성으로 체계적으로 설명됨.</li>
                    <li><strong>정책적 함의가 달라진다.</strong> 취업 효과 −8% vs −17%는 완전히 다른 보육정책 결론으로 이어짐.</li>
                </ol>
            </div>
        </div>
    </section>

    <!-- 3부: 수학적 관계 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">3. 수학적 관계</h2>
        <div class="section-content">

            <h3>단조성 하 모집단 하위집단</h3>
            <p>도구변수는 모집단을 세 그룹으로 분할 (거역자 없음 가정):</p>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">그룹</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">정의</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">비율</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>순응자 (C)</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">d<sub>1i</sub> = 1, d<sub>0i</sub> = 0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">π<sub>C</sub> = E[D|Z=1] − E[D|Z=0] = 1단계</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>항상-처치자 (AT)</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">d<sub>1i</sub> = d<sub>0i</sub> = 1</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">π<sub>AT</sub> = E[D|Z=0]</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>비순응자 (NT)</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">d<sub>1i</sub> = d<sub>0i</sub> = 0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">π<sub>NT</sub> = 1 − E[D|Z=1]</td>
                </tr>
            </table>

            <h3>각 추정량의 분해</h3>

            <div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1.5rem 0;">
                <h4 style="margin-top: 0; color: #dc2626;">ATE: 전체 그룹의 가중평균</h4>
                <div style="background: white; border: 1px solid #fecaca; padding: 1rem; border-radius: 6px; margin: 0.5rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.05rem;">
                    ATE = E[Y₁−Y₀|C]·π<sub>C</sub> + E[Y₁−Y₀|AT]·π<sub>AT</sub> + E[Y₁−Y₀|NT]·π<sub>NT</sub>
                </div>
            </div>

            <div style="background: #ecfdf5; border-left: 4px solid #059669; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1.5rem 0;">
                <h4 style="margin-top: 0; color: #059669;">ATT: 순응자 + 항상-처치자</h4>
                <div style="background: white; border: 1px solid #a7f3d0; padding: 1rem; border-radius: 6px; margin: 0.5rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.05rem;">
                    ATT = E[Y₁−Y₀|C] · π<sub>C</sub>/(π<sub>C</sub>+π<sub>AT</sub>) + E[Y₁−Y₀|AT] · π<sub>AT</sub>/(π<sub>C</sub>+π<sub>AT</sub>)
                </div>
                <p style="font-size: 0.9rem;">처치자 = 순응자 + 항상-처치자. 비순응자는 처치를 안 받으므로 제외.</p>
            </div>

            <div style="background: #fffbeb; border-left: 4px solid #d97706; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1.5rem 0;">
                <h4 style="margin-top: 0; color: #d97706;">ITT: LATE × 순응률</h4>
                <div style="background: white; border: 1px solid #fde68a; padding: 1rem; border-radius: 6px; margin: 0.5rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.05rem;">
                    ITT = LATE × (E[D|Z=1] − E[D|Z=0]) = LATE × π<sub>C</sub>
                </div>
                <p style="font-size: 0.9rem;">항상 불편추정치 (Y를 Z에 OLS). 순응률 < 1이므로 LATE보다 절대값이 작다.</p>
            </div>

            <div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1.5rem 0;">
                <h4 style="margin-top: 0; color: #7c3aed;">LATE: 순응자만</h4>
                <div style="background: white; border: 1px solid #c4b5fd; padding: 1rem; border-radius: 6px; margin: 0.5rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.05rem;">
                    LATE = E[Y₁−Y₀ | 순응자] = ITT / 1단계
                </div>
                <p style="font-size: 0.9rem;">항상-처치자와 비순응자의 효과는 완전히 배제.</p>
            </div>

            <h3>특수한 경우: LATE = ATT (Bloom 1984)</h3>
            <div style="background: #f0fdf4; border: 1px solid #86efac; padding: 1.5rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>항상-처치자가 없는 경우</strong> (일방적 비순응), 즉 E[D|Z=0] = 0:</p>
                <div style="background: white; border: 1px solid #86efac; padding: 1rem; border-radius: 6px; margin: 0.5rem 0; text-align: center; font-family: 'Times New Roman', serif;">
                    항상-처치자 = 0 → 처치자 = 순응자만 → <strong>LATE = ATT</strong>
                </div>
                <p><strong>예시:</strong> JTPA 훈련 실험 — 배정 없이는 훈련 접근 불가, 훈련받은 사람 전원이 순응자. IV = ITT ÷ 순응률 = ATT.</p>
            </div>

            <h3>크기 관계 요약</h3>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">관계</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">조건</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">예시</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">|ITT| &lt; |LATE|</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">항상 (순응률 &lt; 1일 때)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">ITT = LATE × 순응률</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">ATT ≥ ATE (보통)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">효과 큰 사람이 선택적 참여</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">자발적 직업훈련, 대학 진학</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">LATE = ATT</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">항상-처치자 없음</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">JTPA 실험 (Bloom 1984)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">LATE₁ ≠ LATE₂</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">다른 IV → 다른 순응자</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Angrist & Evans: Twins ≠ Same-sex</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">LATE = ATE</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">동질적 처치효과</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">모든 사람에게 효과가 동일한 경우</td>
                </tr>
            </table>

            <h3>방법론 → 추정량 연결</h3>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">방법론</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">추정하는 효과</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">일반화 범위</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">RCT (완전 순응)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #dc2626; font-weight: 500;">ATE</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">넓음</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">RCT (비순응) + IV</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #7c3aed; font-weight: 500;">LATE</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">순응자 한정</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">DID</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #059669; font-weight: 500;">ATT</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">처치군과 비슷한 집단</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">RDD</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #7c3aed; font-weight: 500;">LATE at cutoff</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Cutoff 근처 한정</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Matching / PSM</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #059669; font-weight: 500;">ATT</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">처치군과 비슷한 집단</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- 핵심 요약 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">핵심 요약</h2>
        <div class="section-content">
            <div style="background: #ecfdf5; padding: 1.5rem; border-radius: 8px; margin: 1rem 0;">
                <p>실증 연구를 읽거나 쓸 때 항상 물어야 할 질문:</p>
                <ol>
                    <li><strong>이 방법론이 식별하는 추정량은?</strong> (ATE, ATT, 아니면 LATE?)</li>
                    <li><strong>순응자는 누구인가?</strong> (IV/RDD라면 — 누구의 효과를 배우고 있는가?)</li>
                    <li><strong>추정량이 정책 질문과 맞는가?</strong> (보편 프로그램 → ATE; 자발적 → ATT; 넛지 → LATE)</li>
                    <li><strong>순응자가 의도한 정책 대상과 관련 있는가?</strong> (파일럿 열성 참가자 ≠ 일반 모집단)</li>
                </ol>
            </div>
        </div>
    </section>

    <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee; display: flex; justify-content: space-between;">
        <a href="/study/angrist-ch4-part2-ko" style="color: #666;">← Ch.4 Part 2: LATE & 이질적 효과</a>
        <a href="/study/angrist-ch4-part3-ko" style="color: #2563eb;">Ch.4 Part 3: IV 상세 →</a>
    </div>

    <div style="margin-top: 2rem; padding: 1rem; background: #f9fafb; border-radius: 8px; font-size: 0.8rem; color: #6b7280;">
        <em>이 노트는 LLM (Claude)의 도움을 받아 작성되었습니다.</em>
    </div>
</div>
