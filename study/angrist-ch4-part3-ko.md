---
layout: minimal_base
title: "Angrist Ch.4-3 - IV 상세"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Chapter 4 Part 3: IV 상세</h2>
            <a href="/study/angrist-ch4-part3" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">English</a>
        </div>
        <div class="section-content">
            <p><em>Angrist & Pischke, Mostly Harmless Econometrics — Section 4.6</em></p>
        </div>
    </section>

    <!-- 핵심 메시지 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">핵심 메시지</h2>
        <div class="section-content">
            <blockquote style="border-left: 4px solid #2563eb; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                이 절은 IV의 실전적 함정들을 다룬다: 수동 2SLS의 흔한 실수, 동료 효과(peer effects) 식별의 어려움, 2SLS와 비선형 모형(이변량 Probit)의 관계, 그리고 도구변수가 많거나 약할 때의 <strong>유한표본 편의</strong>.
            </blockquote>
        </div>
    </section>

    <!-- 4.6.1 2SLS 실수들 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4.6.1 흔한 2SLS 실수들</h2>
        <div class="section-content">

            <h3>실수 1: 공변량 무관심</h3>
            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>실수:</strong> 1단계와 2단계에 서로 다른 공변량을 포함하는 것.</p>
            </div>
            <p>Griliches & Mason (1972)은 2단계에 나이를 포함했지만 1단계에는 포함하지 않았다. 이는 1단계 잔차(s<sub>i</sub> − ŝ<sub>i</sub>)가 1단계에 <em>포함된</em> 변수들과만 비상관이 보장되기 때문에 잘못된 것이다.</p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>규칙:</strong> 항상 양 단계에 동일한 외생 공변량을 포함해야 한다. 2단계에 넣을 만한 공변량이면 1단계에도 넣어야 한다.</p>
            </div>

            <h3>실수 2: 금지된 회귀</h3>
            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>실수:</strong> <em>비선형</em> 1단계 적합값(예: Probit)을 2단계에 대입하는 것.</p>
            </div>

            <p>d<sub>i</sub>가 이진 내생변수라면 "d<sub>i</sub>가 0/1이니 1단계에 OLS 대신 Probit을 쓰자"고 생각할 수 있다.</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>왜 틀린가:</strong> OLS 잔차만이 정규방정식에 의해 적합값 및 공변량과의 비상관성이 보장된다. Probit 잔차는 Probit 모형이 올바르게 설정되지 않는 한 이 성질을 갖지 않으며 — 이를 검증할 수 없다.</p>
            </div>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>올바른 대안:</strong></p>
                <ul>
                    <li><strong>표준 2SLS:</strong> 선형 1단계 사용 (1단계 함수형과 무관하게 항상 일치)</li>
                    <li><strong>비선형 적합값을 도구변수로:</strong> d̂<sup>probit</sup>을 대입이 아닌 <em>도구변수</em>로 사용하여 표준 2SLS 수행. Probit 모형이 좋은 근사이면 효율성 향상 가능</li>
                </ul>
                <p><strong>주의:</strong> 비선형 적합값을 도구변수로 사용하면 암묵적으로 비선형성을 식별 정보로 활용하게 된다. Z<sub>i</sub>가 인과 방정식에 나타나면 모형은 미식별이어야 하지만, 비선형 1단계가 함수형을 통한 "뒷문" 식별을 만드는데 — 이는 의심스럽다.</p>
            </div>

            <h3>실수 3: 금지된 비선형 2단계</h3>
            <p>이차 모형 y<sub>i</sub> = δ'X<sub>i</sub> + ρ₁s<sub>i</sub> + ρ₂s<sub>i</sub>² + ε<sub>i</sub>에서, 하나의 1단계에서 ŝ과 ŝ²을 대입하지 <strong>말 것</strong>. 대신 s<sub>i</sub>와 s<sub>i</sub>²을 각각 별도의 내생변수로 취급하여, 각자의 1단계 방정식을 세우고 적절한 2SLS를 사용해야 한다.</p>
        </div>
    </section>

    <!-- 4.6.2 동료 효과 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4.6.2 동료 효과 (Peer Effects)</h2>
        <div class="section-content">

            <h3>유형 1: 한 변수의 집단 평균이 다른 변수의 개인 결과에 미치는 효과</h3>
            <p>예: 주(州)의 평균 교육연수(S̄<sub>jt</sub>)가 개인 임금에 영향을 미치는가? (Acemoglu & Angrist 2000)</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                Y<sub>ijt</sub> = α<sub>j</sub> + λ<sub>t</sub> + ρs<sub>i</sub> + ψS̄<sub>jt</sub> + u<sub>jt</sub> + ε<sub>ijt</sub>
            </div>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>문제:</strong> OLS와 2SLS(주 더미 사용)가 ρ의 다른 추정치를 내면, 진정한 외부효과 없이도 <em>기계적으로</em> ψ̂ ≠ 0이 된다.</p>
                <ul>
                    <li>2SLS > OLS (예: 측정오차 보정): 허위 <em>양</em>의 외부효과</li>
                    <li>2SLS < OLS (예: 능력 편의 제거): 허위 <em>음</em>의 외부효과</li>
                </ul>
                <p>→ 이런 방정식의 OLS는 동료 효과에 대해 해석하기 매우 어렵다.</p>
            </div>

            <h3>유형 2: 같은 변수의 집단 평균이 개인 변수에 미치는 효과</h3>
            <p>"급우들의 평균 졸업률이 나의 졸업 여부에 영향을 미치는가?"</p>

            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>s<sub>ij</sub>를 S̄<sub>j</sub>에 회귀하면 계수가 항상 1이다.</strong> S̄<sub>j</sub>는 말 그대로 s<sub>ij</sub>를 학교 더미에 회귀한 적합값이기 때문. 이 회귀는 <strong>항진적(tautological)</strong>이며 인과관계에 대해 아무것도 말해주지 않는다.</p>
            </div>

            <p>본인 제외 평균 S̄<sub>(−i)j</sub>를 사용해도, 학교 수준 공통 충격(예: 좋은 교장)이 개인과 동료 결과 사이에 허위 상관을 만들어 문제적이다.</p>

            <h4>더 나은 접근법</h4>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p>결과에 <strong>선행하는 사전적(ex ante) 동료 특성</strong>을 사용:</p>
                <ul>
                    <li><strong>Ammermueller & Pischke (2006):</strong> 동료 가정의 도서 보유량 → 학생 시험 점수 (도서는 사전 결정된 가정 특성)</li>
                    <li><strong>Angrist & Lang (2004):</strong> 통학 버스로 온 저성취 학생 수 → 재학생 시험 점수 (표본 <em>외부의</em> 학생에 의해 결정)</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- 4.6.3 제한 종속변수 재론 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4.6.3 제한 종속변수 재론</h2>
        <div class="section-content">

            <h3>이변량 Probit보다 2SLS를 선호하는 이유</h3>
            <p>종속변수가 이진(예: 취업 여부)일 때, 2SLS 대신 이변량 Probit을 써야 하는가?</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>2SLS를 고수해야 하는 논거:</strong></p>
                <ul>
                    <li>2SLS는 종속변수가 이진이든, 비음이든, 연속이든 상관없이 LATE를 포착</li>
                    <li>2SLS는 분포 가정이 필요 없음</li>
                    <li>2SLS는 인과효과를 <em>직접</em> 추정 — 잠재지수 계수에서 한계효과를 계산할 필요 없음</li>
                    <li>이변량 Probit은 ATE(LATE가 아닌)를 추정 가능하지만, <strong>결합 정규성</strong>이라는 강한 가정 하에서만 가능</li>
                </ul>
            </div>

            <h4>이변량 Probit 설정</h4>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                <strong>1단계:</strong> d<sub>i</sub> = 1[X<sub>i</sub>'δ₀ + δ₁z<sub>i</sub> > v<sub>i</sub>]<br>
                <strong>2단계:</strong> y<sub>i</sub> = 1[X<sub>i</sub>'β₀ + β₁d<sub>i</sub> > ε<sub>i</sub>]<br><br>
                내생성은 Corr(v<sub>i</sub>, ε<sub>i</sub>) ≠ 0에서 발생.<br>
                z<sub>i</sub> ⊥ (v<sub>i</sub>, ε<sub>i</sub>)와 <strong>결합 정규성</strong>을 가정하여 식별.
            </div>

            <h4>실증 비교: 셋째 자녀가 여성 취업에 미치는 효과</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.9rem;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">설정</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">2SLS</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Abadie</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Biprobit MFX</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Biprobit ATE</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">공변량 없음</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.138</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.138</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.138</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.139</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">일부 공변량</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.132</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.132</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.135</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.135</td>
                </tr>
                <tr style="background: #fee2e2;">
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+ 선형 나이 항</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.120</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.121</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>−0.171</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>−0.171</strong></td>
                </tr>
            </table>
            <p>강한 함수형 가정 없이 결과가 거의 동일. 그러나 나이 더미를 선형 항으로 교체하면 이변량 Probit 추정치가 −0.171로 뛰는 반면 2SLS와 Abadie는 안정적. 이는 희소 셀로의 외삽 — 비선형 모형이 도입하는 정확히 그 취약성 — 을 반영한다.</p>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>결론:</strong> 2SLS는 함수형에 강건하다. 이변량 Probit은 LATE 대신 ATE를 줄 수 있지만, 성립하지 않을 수 있는 강한 분포 가정의 대가를 치른다. 실제로는 Probit 모형이 외삽하지 않는 한 두 방법이 보통 일치한다.</p>
            </div>
        </div>
    </section>

    <!-- 4.6.4 2SLS의 편의 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4.6.4 2SLS의 편의</h2>
        <div class="section-content">

            <h3>OLS는 불편, 2SLS는 불편이 아님</h3>
            <p>OLS는 불편추정량(어떤 표본 크기에서도 모집단 계수에 중심). 2SLS는 <strong>일치추정량</strong>일 뿐 — 대표본에서 수렴하지만 유한표본에서 체계적으로 벗어날 수 있다.</p>

            <h3>편의 공식</h3>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    E[β̂<sub>2SLS</sub> − β] ≈ (β̂<sub>OLS 편의</sub>) × 1/(F + 1)
                </div>
                <p style="text-align: center; margin-top: 0.5rem;">여기서 F는 배제된 도구변수에 대한 1단계 F-통계량.</p>
            </div>

            <h4>주요 시사점</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">시나리오</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">2SLS 편의</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">F → ∞ (강한 도구변수)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">편의 → 0 ✓</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">F → 0 (1단계 없음)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">편의 → OLS 편의 (최악의 경우)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">도구변수 수 증가 (q 증가)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">F 하락 → 편의 증가</td>
                </tr>
            </table>

            <h4>편의의 원천</h4>
            <p>편의는 1단계가 알려진 것이 아니라 <em>추정된</em> 것이기 때문에 발생. 적합값 ŝ<sub>i</sub> = Zπ̂는 2단계 오차 ε과 상관된 표본 오차(Pzη)를 포함한다. 도구변수가 약할 때 이 표본 상관이 지배적이 되어 2SLS를 OLS 쪽으로 끌어당긴다.</p>

            <h3>LIML: 편의 감소 대안</h3>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>LIML (Limited Information Maximum Likelihood)</strong>은 과대식별에서도 근사적으로 <strong>중앙값-불편</strong>이며, 2SLS와 동일한 대표본 분포를 가진다.</p>
                <ul>
                    <li>LIML은 본질적으로 OLS와 2SLS의 편의 보정된 선형 결합</li>
                    <li>Stata와 SAS에서 사용 가능</li>
                    <li>몬테카를로 증거 (Flores-Lagunes 2007)가 다양한 시나리오에서 LIML 지지</li>
                </ul>
            </div>

            <h4>몬테카를로 증거</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">설정 (참 β=1)</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">OLS 중앙값</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">2SLS 중앙값</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">LIML 중앙값</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">q=2 (유용 1개 + 무용 1개)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">~1.79</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">1.07</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">~1.0</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">q=20 (유용 1개 + 무용 19개)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">~1.79</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">1.53</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">~1.0</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">q=20 (모두 무용)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">~1.79</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">~1.79</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">매우 분산</td>
                </tr>
            </table>
            <p>LIML은 약한 도구변수가 많아도 β=1에 중심을 유지하는 반면, 2SLS는 OLS 쪽으로 끌린다. 도구변수가 모두 무관련이면 LIML의 넓은 분포가 정보 부재를 올바르게 반영한다.</p>

            <h3>실용적 권고사항</h3>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <ol>
                    <li><strong>1단계를 보고하라.</strong> 부호, 크기, 타당성을 확인.</li>
                    <li><strong>F-통계량을 보고하라.</strong> 배제된 도구변수에 대한 것. 경험법칙: F > 10이면 안전 (Stock, Wright & Yogo 2002). 다만 절대적 정리는 아님.</li>
                    <li><strong>적정식별 추정치를 보고하라.</strong> 가장 좋은 단일 도구변수로. 적정식별 IV는 중앙값-불편이며 과다 도구변수 문제에 면역.</li>
                    <li><strong>2SLS와 LIML을 비교하라.</strong> 일치하면 안심. 불일치하면 우려 — 더 강한 도구변수를 찾아야 한다.</li>
                    <li><strong>축약형을 확인하라.</strong> 축약형 회귀(y를 z에)는 OLS이므로 불편. 축약형에서 인과관계가 보이지 않으면 아마 없는 것이다.</li>
                </ol>
            </div>

            <h4>적용: Angrist & Krueger (1991) 재검토</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.9rem;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">도구변수</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">q</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">F-통계량</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">2SLS</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">LIML</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">3개 QOB 더미</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">3</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">32.3</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.105 (0.020)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.106 (0.020)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">QOB×YOB 교호작용</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">30</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">4.9</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.089 (0.016)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.093 (0.018)</td>
                </tr>
                <tr style="background: #fef3c7;">
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+ QOB×SOB 교호작용</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">180</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">2.6</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.093 (0.009)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.091 (0.011)</td>
                </tr>
            </table>
            <p>도구변수 3개에 F=32일 때 2SLS와 LIML이 근접하게 일치. 도구변수 180개에 F=2.6일 때 F-통계량은 낮지만 LIML이 여전히 2SLS와 일치하여, 경험법칙에도 불구하고 편의가 치명적이지 않을 수 있음을 시사한다.</p>
        </div>
    </section>

    <!-- 요약 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Part 3 요약</h2>
        <div class="section-content">
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">주제</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">핵심 교훈</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>공변량 무관심</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">양 단계에 동일한 공변량; 그렇지 않으면 잔차가 적합값과 상관</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>금지된 회귀</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">비선형 적합값을 2단계에 대입하지 말 것; 대신 도구변수로 사용</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>동료 효과 (유형 1)</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">외부효과의 OLS 추정은 사적 수익의 OLS-IV 차이와 혼동</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>동료 효과 (유형 2)</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">같은 결과의 집단 평균에 회귀는 항진적; 사전적 동료 특성 사용</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>2SLS vs. 이변량 Probit</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">2SLS는 강건; Biprobit은 정규성 필요하고 공변량에 민감</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>2SLS 편의</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">편의 ≈ OLS 편의 / (F+1); 많고 약한 도구변수 → OLS 쪽으로 편의</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>LIML</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">2SLS의 중앙값-불편 대안; 강건성 검증용</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>F > 10 규칙</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">도구변수 강도의 경험법칙; 절대적 정리는 아님</td>
                </tr>
            </table>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>5가지 IV 점검 목록:</strong></p>
                <ol>
                    <li>1단계를 보고하고 점검하라</li>
                    <li>F-통계량을 보고하라 (10 이상 목표)</li>
                    <li>가장 좋은 도구변수로 적정식별 추정치를 보고하라</li>
                    <li>2SLS와 LIML을 비교하라</li>
                    <li>축약형을 확인하라 — 거기서 인과효과가 보이지 않으면 아마 실재하지 않는다</li>
                </ol>
            </div>
        </div>
    </section>

    <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee; display: flex; justify-content: space-between;">
        <a href="/study/angrist-ch4-part2-ko" style="color: #666;">← Part 2: LATE & 이질적 효과</a>
        <a href="/study" style="color: #2563eb;">학습 노트로 돌아가기 →</a>
    </div>

    <div style="margin-top: 2rem; padding: 1rem; background: #f9fafb; border-radius: 8px; font-size: 0.8rem; color: #6b7280;">
        <em>이 노트는 LLM (Claude)의 도움을 받아 작성되었습니다.</em>
    </div>
</div>
