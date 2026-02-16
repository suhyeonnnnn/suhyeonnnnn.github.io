---
layout: minimal_base
title: "Angrist Ch.5 - 고정효과, DD, 패널 데이터"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Chapter 5: 고정효과, 이중차분, 패널 데이터</h2>
            <a href="/study/angrist-ch5" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">English</a>
        </div>
        <div class="section-content">
            <p><em>Angrist & Pischke, Mostly Harmless Econometrics — Chapter 5</em></p>
            <p style="color: #6b7280; font-style: italic;">"평행 우주에 대해 처음 깨달아야 할 것은... 그것들이 평행하지 않다는 것이다." — Douglas Adams</p>
        </div>
    </section>

    <!-- 핵심 메시지 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">핵심 메시지</h2>
        <div class="section-content">
            <blockquote style="border-left: 4px solid #2563eb; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                중요한 교란요인이 <strong>관측되지 않지만 시간에 걸쳐 고정</strong>되어 있을 때, 패널 데이터 전략으로 이를 제거할 수 있다: <strong>고정효과</strong>(개인 내 변동) 또는 <strong>이중차분</strong>(평행 추세 가정). 이 방법들은 "수준 비교를 포기"하면서 반사실적 추세가 동일할 것을 요구한다.
            </blockquote>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>지금까지의 식별 도구:</strong></p>
                <ul>
                    <li><strong>3장:</strong> <em>관측된</em> 교란요인 통제 (회귀, 매칭)</li>
                    <li><strong>4장:</strong> 교란요인이 <em>관측되지 않을</em> 때 도구변수 사용</li>
                    <li><strong>5장:</strong> 교란요인이 관측되지 않지만 고정일 때 <em>시간/코호트 차원</em> 활용</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- 5.1 개인 고정효과 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">5.1 개인 고정효과</h2>
        <div class="section-content">

            <h3>동기: 노조 임금 프리미엄</h3>
            <p>노동경제학의 고전적 질문: 단체교섭으로 임금이 결정되는 근로자가 더 많이 버는 것이 단체교섭 <em>때문</em>인가, 아니면 어차피 더 많이 벌 사람들인가(더 숙련되고 경험이 많아서)?</p>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <strong style="color: #92400e;">문제:</strong> 관측되지 않는 근로자 능력 A<sub>i</sub>가 노조 가입과 임금 모두에 영향. 더 능력 있는 근로자가 노조에 가입할 확률이 높다면, OLS는 노조 효과를 과대추정.
            </div>

            <h3>고정효과 설정</h3>
            <p>y<sub>it</sub> = 근로자 i의 t기 로그 임금, d<sub>it</sub> = 노조 상태라 하자. 가정:</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                <p><strong>조건부 독립성:</strong></p>
                <p style="text-align: center;">E(y<sub>0it</sub> | A<sub>i</sub>, X<sub>it</sub>, t, d<sub>it</sub>) = E(y<sub>0it</sub> | A<sub>i</sub>, X<sub>it</sub>, t)</p>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">관측되지 않는 능력 A<sub>i</sub>, 관측된 공변량 X<sub>it</sub>, 시간에 <em>조건부로</em> 노조 상태가 무작위 배정과 같음.</p>
            </div>

            <p><strong>핵심 가정:</strong> 관측되지 않는 A<sub>i</sub>가 선형 모형에서 <strong>시간 첨자 없이</strong> 등장:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                E(y<sub>0it</sub> | A<sub>i</sub>, X<sub>it</sub>, t) = α + λ<sub>t</sub> + A'<sub>i</sub>γ + X<sub>it</sub>β
            </div>

            <p>상수적, 가법적 처치효과 ρ와 함께:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                E(y<sub>1it</sub> | A<sub>i</sub>, X<sub>it</sub>, t) = E(y<sub>0it</sub> | A<sub>i</sub>, X<sub>it</sub>, t) + ρ
            </div>

            <p>이로부터 <strong>고정효과 모형</strong>이 도출:</p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center; font-size: 1.1rem;">
                y<sub>it</sub> = α<sub>i</sub> + λ<sub>t</sub> + ρd<sub>it</sub> + X<sub>it</sub>β + ε<sub>it</sub>
            </div>
            <p>여기서 α<sub>i</sub> ≡ α + A'<sub>i</sub>γ가 <strong>개인 고정효과</strong>(추정할 모수로 취급), λ<sub>t</sub>는 <strong>연도 효과</strong>(시간 더미의 계수).</p>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <strong style="color: #92400e;">참고:</strong> 이 가정들은 3장보다 <em>더 제약적</em>이다. 도구변수 없이 패널 데이터로 관측되지 않는 교란요인 문제를 해결하려면 선형, 가법적 함수 형태가 필요하다.
            </div>

            <h3>추정 전략 1: 평균으로부터의 편차</h3>
            <p>패널 데이터(동일 개인에 대한 반복 관측)로 α<sub>i</sub>를 제거할 수 있다. 먼저 개인 평균 계산:</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                ȳ<sub>i</sub> = α<sub>i</sub> + λ̄ + ρd̄<sub>i</sub> + X̄<sub>i</sub>β + ε̄<sub>i</sub>
            </div>

            <p>원래 식에서 빼면:</p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                (y<sub>it</sub> − ȳ<sub>i</sub>) = (λ<sub>t</sub> − λ̄) + ρ(d<sub>it</sub> − d̄<sub>i</sub>) + (X<sub>it</sub> − X̄<sub>i</sub>)β + (ε<sub>it</sub> − ε̄<sub>i</sub>)
            </div>

            <p><strong>고정효과 α<sub>i</sub>가 제거됨!</strong> 이를 <strong>"within 추정량"</strong> 또는 <strong>"공분산 분석"</strong>이라 함.</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>왜 대수적으로 같은가?</strong></p>
                <p>회귀 해부 공식(3.1.3)에 의해, 개인 더미 전체 집합에 대한 회귀 잔차는 정확히 개인 평균으로부터의 편차이다.</p>
            </div>

            <h3>추정 전략 2: 1차 차분</h3>
            <p>평균 편차의 대안:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                Δy<sub>it</sub> = Δλ<sub>t</sub> + ρΔd<sub>it</sub> + ΔX<sub>it</sub>β + Δε<sub>it</sub>
            </div>

            <p>여기서 Δy<sub>it</sub> = y<sub>it</sub> − y<sub>it−1</sub>.</p>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">방법</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">평균 편차</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">1차 차분</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">T = 2일 때</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;" colspan="2" align="center">대수적으로 동일</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">T > 2일 때</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">ε<sub>it</sub>가 등분산 & 계열 비상관이면 더 효율적</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">더 편리할 수 있음; Δε<sub>it</sub>는 계열 상관됨에 주의</td>
                </tr>
            </table>

            <h3>고정효과 vs. 확률효과</h3>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>확률효과(Random effects)</strong>는 α<sub>i</sub>가 회귀변수와 <em>비상관</em>이라고 가정. 그러면 α<sub>i</sub>는 잔차의 일부가 됨(무시해도 OVB 없음), 단 동일인의 잔차가 기간 간 상관됨.</p>
                <p style="margin-top: 0.5rem;"><strong>저자들의 선호:</strong> 확률효과 하 GLS보다 고정효과 OLS + 강건 표준오차. GLS는 더 강한 가정(선형 CEF, 등분산)이 필요하고 효율성 이득은 보통 미미함.</p>
            </div>

            <h3>예시: 노조 임금 효과 (Freeman 1984)</h3>
            <p>Freeman은 네 개의 패널 데이터셋으로 노조 임금 효과 추정:</p>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">조사</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">횡단면</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">고정효과</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">May CPS, 1974-75</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.19</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.09</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">NLS Young Men, 1970-78</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.28</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.19</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Michigan PSID, 1970-79</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.23</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.14</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">QES, 1973-77</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.14</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.16</td>
                </tr>
            </table>

            <p><strong>패턴:</strong> FE 추정치(0.09–0.19)가 일반적으로 횡단면 추정치(0.14–0.28)보다 작음. 이는 횡단면에서 <strong>양의 선택 편의</strong> 시사 — 더 능력 있는 근로자가 노조에 가입하<em>고</em> 더 많이 번다.</p>

            <h3>주의 1: 측정 오차</h3>
            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>FE 추정치는 감쇠 편의에 매우 취약:</strong></p>
                <ul>
                    <li>노조 상태 같은 경제 변수는 <strong>지속적</strong>인 경향(올해 노조원이면 내년에도 노조원일 가능성 높음)</li>
                    <li>측정 오차는 종종 <strong>매년 변동</strong>(올해 노조 상태가 잘못 보고되어도 내년에는 아닐 수 있음)</li>
                    <li>→ 어떤 한 해에 잘못 분류되는 근로자는 적지만, 관측된 연간 노조 상태 <em>변화</em>는 대부분 노이즈일 수 있음</li>
                    <li>→ d<sub>it</sub>보다 Δd<sub>it</sub>에서 측정 오차가 더 큼 → FE 추정치가 0 방향으로 편향</li>
                </ul>
            </div>

            <p><strong>가능한 해결책:</strong></p>
            <ul>
                <li><strong>IV:</strong> 형제간 교차 보고를 도구변수로 사용 (Ashenfelter & Krueger 1994)</li>
                <li><strong>외부 검증:</strong> 검증 조사의 측정 오차율을 사용해 추정치 조정 (Card 1996)</li>
            </ul>

            <h3>주의 2: 좋은 변동 제거 (쌍둥이 예시)</h3>
            <p>차분/평균 편차는 좋은 변동과 나쁜 변동을 <em>모두</em> 제거. 변환이 OVB라는 더러운 물은 버리지만 유용한 정보인 아기도 함께 버릴 수 있음.</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>쌍둥이와 교육 수익률:</strong></p>
                <p>Ashenfelter & Krueger (1994), Ashenfelter & Rouse (1998)는 쌍둥이를 사용해 가족 고정효과(공통 가족/유전적 배경)를 통제하며 교육 수익률 추정.</p>
                <p style="margin-top: 0.5rem;"><strong>놀라운 결과:</strong> 가족 내 추정치가 OLS보다 <em>더 큼</em>!</p>
                <p style="margin-top: 0.5rem;"><strong>Bound & Solon (1999) 비판:</strong></p>
                <ul>
                    <li>쌍둥이도 작은 차이가 있음: 첫째가 보통 출생 체중과 IQ가 더 높음</li>
                    <li>쌍둥이 내 차이는 작지만, 그들의 교육 차이도 작음</li>
                    <li>→ 작은 양의 관측되지 않는 능력 차이가 상당한 편의를 야기할 수 있음</li>
                </ul>
            </div>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <strong style="color: #92400e;">결론:</strong> 고정효과 추정치를 해석할 때 지나치게 강한 주장은 피해야 한다. 관측되지 않는 변수의 정확한 성격은 보통 다소 불분명하게 남는다.
            </div>
        </div>
    </section>

    <!-- 5.2 이중차분 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">5.2 이중차분 (DD)</h2>
        <div class="section-content">

            <h3>처치가 그룹 수준에서 변동할 때</h3>
            <p>FE는 <em>동일 개인</em>에 대한 반복 관측이 있는 패널 데이터가 필요. 그러나 종종 처치가 더 집계된 수준(주, 코호트)에서만 변동. 예:</p>
            <ul>
                <li>임산부 건강 보험에 대한 주 정책</li>
                <li>주별 최저임금</li>
                <li>고용법에 대한 법원 판결</li>
            </ul>
            <p>OVB의 원천은 따라서 <strong>주 및 연도 수준</strong>의 관측되지 않는 변수여야 함.</p>

            <h3>고전적 예시: Card & Krueger (1994) — 최저임금</h3>
            <p>고전적 질문: 경쟁적 노동시장에서 최저임금 인상은 고용을 감소시켜야 함(하향 경사 수요곡선을 따라 이동). 실제로 그런가?</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>자연실험:</strong></p>
                <ul>
                    <li><strong>1992년 4월 1일:</strong> 뉴저지가 주 최저임금을 $4.25에서 $5.05로 인상</li>
                    <li><strong>펜실베이니아:</strong> $4.25 유지 (연방 최저임금)</li>
                    <li><strong>데이터:</strong> NJ와 동부 PA의 패스트푸드 레스토랑(버거킹, 웬디스 등) 고용</li>
                    <li><strong>시점:</strong> 1992년 2월 (이전)과 1992년 11월 (이후)</li>
                </ul>
            </div>

            <h3>DD 모형</h3>
            <p>잠재적 결과 정의:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                y<sub>1ist</sub> = 높은 최저임금일 때 고용<br>
                y<sub>0ist</sub> = 낮은 최저임금일 때 고용
            </div>

            <p><strong>핵심 가정 — 처치 부재 시 평행 추세:</strong></p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center; font-size: 1.1rem;">
                E(y<sub>0ist</sub> | s, t) = γ<sub>s</sub> + λ<sub>t</sub>
            </div>

            <p>이 말은: 최저임금 변화가 없으면, 고용은 다음의 합으로 결정:</p>
            <ul>
                <li><strong>γ<sub>s</sub>:</strong> 시간불변 주 효과 (개인 FE에서 α<sub>i</sub>의 역할)</li>
                <li><strong>λ<sub>t</sub>:</strong> 주 간 공통인 연도 효과</li>
            </ul>

            <p>상수 처치효과 δ와 함께:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                y<sub>ist</sub> = γ<sub>s</sub> + λ<sub>t</sub> + δd<sub>st</sub> + ε<sub>ist</sub>
            </div>
            <p>여기서 d<sub>st</sub>는 높은 최저임금 주-기간에 대한 더미이고 E(ε<sub>ist</sub> | s, t) = 0.</p>

            <h3>DD 추정량 도출</h3>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                <p><strong>통제 주 (PA):</strong></p>
                <p style="padding-left: 1rem;">E[y|PA, 11월] − E[y|PA, 2월] = λ<sub>11월</sub> − λ<sub>2월</sub></p>
                
                <p style="margin-top: 0.5rem;"><strong>처치 주 (NJ):</strong></p>
                <p style="padding-left: 1rem;">E[y|NJ, 11월] − E[y|NJ, 2월] = λ<sub>11월</sub> − λ<sub>2월</sub> + δ</p>
                
                <p style="margin-top: 0.5rem;"><strong>이중차분:</strong></p>
                <p style="padding-left: 1rem;">[E[y|NJ, 11월] − E[y|NJ, 2월]] − [E[y|PA, 11월] − E[y|PA, 2월]] = <strong>δ</strong></p>
            </div>

            <h3>Card & Krueger 결과</h3>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">FTE 고용</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">PA (통제)</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">NJ (처치)</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">NJ − PA</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">이전 (2월)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">23.33 (1.35)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">20.44 (0.51)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−2.89 (1.44)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">이후 (11월)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">21.17 (0.94)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">21.03 (0.52)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.14 (1.07)</td>
                </tr>
                <tr style="background: #f0fdf4;">
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>변화</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>−2.16</strong> (1.25)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>+0.59</strong> (0.54)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; background: #dcfce7;"><strong>+2.76</strong> (1.36)</td>
                </tr>
            </table>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>해석:</strong></p>
                <ul>
                    <li>PA 고용은 점포당 2.16명 감소</li>
                    <li>NJ 고용은 점포당 0.59명 증가</li>
                    <li><strong>DD = +2.76</strong> — 표준 예측과 반대!</li>
                    <li>최저임금 인상이 고용을 감소시키지 않음; 오히려 약간 증가</li>
                </ul>
            </div>

            <h3>시각적 표현</h3>
            <div style="background: #f9f9f9; padding: 1.5rem; border-radius: 8px; margin: 1rem 0; text-align: center;">
                <pre style="font-family: monospace; font-size: 0.85rem; text-align: left; display: inline-block;">
고용
    │
    │                    ●───────● 처치군 (관측됨)
    │                   ╱         
    │                  ╱  ← 처치효과 (δ)
    │                 ╱           
    │                ●─ ─ ─ ─ ─ ●  반사실
    │               ╱               (통제군과 평행)
    │              ╱
    │  ●─────────●  통제군 (관측됨)
    │
    └────────────────────────────── 시간
              이전        이후

핵심 통찰: 반사실은 절대 관측되지 않는다.
평행 추세 가정이 통제군의 변화를 
반사실의 대리변수로 사용하게 해준다.
                </pre>
            </div>

            <h3>평행 추세 검정</h3>
            <p>식별 가정은 <strong>여러 처치 전 기간</strong>으로 조사 가능. 처치 전에 처치군과 통제군이 비슷한 추세를 따르는가?</p>

            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Card & Krueger (2000) 후속 연구:</strong></p>
                <p>NJ와 PA 레스토랑의 여러 해 행정 급여 데이터:</p>
                <ul>
                    <li>1992년 2-11월: 약간의 PA 감소, NJ 거의 변화 없음 (원래 조사와 일치)</li>
                    <li>하지만: 다른 기간에 상당한 연간 변동</li>
                    <li>고용 변동이 주 간에 종종 크게 다름</li>
                    <li>1992-1995년에 PA 고용이 NJ 대비 하락, 대부분 1996년 연방 최저임금 인상 <em>전</em>에</li>
                </ul>
                <p style="margin-top: 0.5rem;"><strong>우려:</strong> PA가 NJ의 반사실 고용을 잘 측정하지 못할 수 있음.</p>
            </div>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>더 나은 예시: Pischke (2007) — 독일 학기 기간</strong></p>
                <ul>
                    <li>1960년대까지: 독일 주들(바이에른 제외)이 봄에 학교 시작</li>
                    <li>1966-67: 비바이에른 주들이 가을 시작으로 전환</li>
                    <li>전환을 위해 <strong>두 번의 짧은 학년</strong> 필요 (37주 대신 24주)</li>
                    <li>결과: 2학년의 유급률</li>
                </ul>
                <p style="margin-top: 0.5rem;"><strong>결과:</strong></p>
                <ul>
                    <li>바이에른 (통제): 1966년 이후 유급률 ~2.5%로 평탄</li>
                    <li>처치 주: 더 높은 기준선 (~4-4.5%), 영향받은 코호트에서 ~1%p 상승, 이후 기준선 복귀</li>
                    <li>→ 평행 추세 + 일시적 처치효과의 강력한 시각적 증거</li>
                </ul>
            </div>

            <h3>5.2.1 회귀 DD</h3>
            <p>DD는 회귀로 추정 가능. NJ<sub>s</sub> = NJ 더미, d<sub>t</sub> = 11월 더미라 하면:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center; font-size: 1.05rem;">
                y<sub>ist</sub> = α + γ·NJ<sub>s</sub> + λ·d<sub>t</sub> + <strong>δ·(NJ<sub>s</sub> × d<sub>t</sub>)</strong> + ε<sub>ist</sub>
            </div>

            <p><strong>모수 해석:</strong></p>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">모수</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">의미</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">α</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">E[y | PA, 2월] = γ<sub>PA</sub> + λ<sub>2월</sub></td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">γ</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">E[y | NJ, 2월] − E[y | PA, 2월] = γ<sub>NJ</sub> − γ<sub>PA</sub></td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">λ</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">E[y | PA, 11월] − E[y | PA, 2월] = λ<sub>11월</sub> − λ<sub>2월</sub></td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;"><strong>δ</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>DD 추정치</strong> = {E[y|NJ,11월] − E[y|NJ,2월]} − {E[y|PA,11월] − E[y|PA,2월]}</td>
                </tr>
            </table>

            <p>이는 <strong>포화 모형</strong>: E(y|s,t)의 4개 가능한 값, 4개 모수.</p>

            <h4>회귀 DD의 장점:</h4>

            <p><strong>1. 주/기간 추가 용이:</strong> 더미만 더 추가. 일반화된 모형은 각 주와 기간에 대한 더미 포함.</p>

            <p><strong>2. 처치 강도 변동:</strong> on/off 처치 대신 연속 측정치 사용 가능.</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>예시: Card (1992) — 연방 최저임금</strong></p>
                <p>1990년 연방 최저임금이 $3.35에서 $3.80으로 인상. 영향은 주마다 다름(고임금 코네티컷에서는 무관, 저임금 미시시피에서는 큰 영향).</p>
                <div style="font-family: 'Times New Roman', serif; text-align: center; margin: 0.5rem 0;">
                    y<sub>ist</sub> = γ<sub>s</sub> + λ<sub>t</sub> + δ·(fa<sub>s</sub> × d<sub>t</sub>) + ε<sub>ist</sub>
                </div>
                <p>여기서 fa<sub>s</sub> = s주에서 $3.80 미만으로 버는 청소년의 기준선 비율 (처치 강도).</p>
            </div>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">결과</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Δ 평균 로그임금</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Δ 고용/인구 비율</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">영향받은 비율 (fa<sub>s</sub>)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.15 (0.03)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.02 (0.03)</td>
                </tr>
            </table>
            <p>최저임금이 더 영향력 있는 주에서 임금이 더 많이 상승(0.15), 하지만 고용은 영향받은 비율과 거의 무관(0.02 ≈ 0).</p>

            <p><strong>3. 공변량 추가 용이:</strong> 시간 변동 주 특성 X<sub>st</sub> 통제(예: 주 경제 상황의 대리변수로 성인 고용).</p>

            <h3>Granger 스타일 인과성 검정: 선행과 후행</h3>
            <p>표본이 여러 해를 포함하고 처치 시점이 주마다 다를 때, "원인이 결과보다 먼저 발생"하는지 검정 가능:</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                y<sub>ist</sub> = γ<sub>s</sub> + λ<sub>t</sub> + Σ<sub>τ=0</sub><sup>m</sup> δ<sub>−τ</sub>d<sub>s,t−τ</sub> + Σ<sub>τ=1</sub><sup>q</sup> δ<sub>+τ</sub>d<sub>s,t+τ</sub> + X<sub>ist</sub>β + ε<sub>ist</sub>
            </div>

            <ul>
                <li><strong>후행(Lags)</strong> (δ<sub>−τ</sub>): 처치 후 효과 — 효과가 시간에 따라 어떻게 진화?</li>
                <li><strong>선행(Leads)</strong> (δ<sub>+τ</sub>): 처치 전 "효과" — 처치가 인과적이면 0이어야!</li>
            </ul>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>예시: Autor (2003) — 고용 보호 & 파견 근로</strong></p>
                <p>"부당 해고" 소송을 허용하는 주 법원 판결 → 기업이 파견 근로자를 더 많이 사용?</p>
                <p style="margin-top: 0.5rem;"><strong>추정된 선행/후행 패턴:</strong></p>
                <ul>
                    <li><strong>2년 전, 1년 전:</strong> 효과 없음 (선행 ≈ 0) ✓</li>
                    <li><strong>채택 연도:</strong> 작은 양의 효과</li>
                    <li><strong>1-3년 후:</strong> 급격히 증가하는 효과</li>
                    <li><strong>4년 이상 후:</strong> 효과가 영구적으로 높은 수준에서 평탄화</li>
                </ul>
                <p style="margin-top: 0.5rem;">이 패턴은 인과적 해석과 일관: 예측 없음, 점진적 조정.</p>
            </div>

            <h3>주별 추세</h3>
            <p>대안적 강건성 검정: 처치군과 통제군이 다른 <em>선형</em> 추세를 따르도록 허용:</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                y<sub>ist</sub> = γ<sub>0s</sub> + γ<sub>1s</sub>·t + λ<sub>t</sub> + δd<sub>st</sub> + X<sub>ist</sub>β + ε<sub>ist</sub>
            </div>

            <p>이는 추세의 제한된 이질성을 허용. 결과가 살아남으면 고무적, 아니면 낙담.</p>

            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>예시: Besley & Burgess (2004) — 인도 노동 규제</strong></p>
                <table style="width:100%; border-collapse: collapse; margin: 0.5rem 0; font-size: 0.9rem;">
                    <tr style="background: #f5f5f5;">
                        <th style="padding: 0.5rem; border: 1px solid #ddd;">설정</th>
                        <th style="padding: 0.5rem; border: 1px solid #ddd;">노동 규제 효과</th>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">DD만</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.186 (0.064)</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">DD + 주 수준 통제</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.104 (0.039)</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>DD + 주별 추세</strong></td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>0.0002 (0.02)</strong></td>
                    </tr>
                </table>
                <p style="margin-top: 0.5rem;"><strong>해석:</strong> 추세 없이 노동 규제가 생산량을 줄이는 것처럼 보임. 주 추세를 넣으면 효과 사라짐 → 규제는 생산량이 <em>이미 하락 중인</em> 주에서 증가함.</p>
            </div>

            <h3>통제군 선택: 구성 변화</h3>
            <p>DD는 암묵적 처치-통제 비교를 설정. 잠재적 함정: 처치의 결과로 <strong>구성 변화</strong>.</p>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>예시: 복지 혜택과 노동 공급</strong></p>
                <p>관대한 복지를 제공하는 주가 어차피 노동력 연계가 약한 가난한 사람들을 유인하면(프로그램 유발 이동), DD는 관대한 복지가 노동 공급에 실제보다 더 나빠 보이게 만듦.</p>
                <p style="margin-top: 0.5rem;"><strong>해결:</strong> 출생 주 또는 이전 거주지 사용(처치에 의해 변하지 않지만 현재 위치와 상관). IV 전략으로 구현 가능.</p>
            </div>

            <h3>삼중차분 (DDD)</h3>
            <p>처치가 세 차원(주 × 시간 × 연령)에서 변동할 때, 고차 대비 사용:</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                y<sub>iast</sub> = γ<sub>st</sub> + λ<sub>at</sub> + μ<sub>as</sub> + δd<sub>ast</sub> + X<sub>iast</sub>β + ε<sub>iast</sub>
            </div>

            <p>통제하는 효과:</p>
            <ul>
                <li>γ<sub>st</sub>: 주 × 시간 효과 (연령 그룹 간 공통)</li>
                <li>λ<sub>at</sub>: 연령 × 시간 효과 (주 간 공통)</li>
                <li>μ<sub>as</sub>: 주 × 연령 효과 (시간 간 공통)</li>
            </ul>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>예시: Yelowitz (1995) — Medicaid 확대</strong></p>
                <p>Medicaid 적격성이 한때 AFDC(현금 복지)에 연계됨. 1980년대에 일부 주가 AFDC 부적격 가족의 아동에게 적용 범위 확대.</p>
                <p style="margin-top: 0.5rem;">처치가 주, 시간, <em>그리고</em> 자녀 연령에 따라 변동. DDD는 세 차원 모두에서 비교하여 표준 DD보다 더 설득력 있는 통제 제공.</p>
            </div>
        </div>
    </section>

    <!-- 5.3 FE vs LDV -->
    <section class="section fade-in-delay">
        <h2 class="section-title">5.3 고정효과 대 종속변수 시차</h2>
        <div class="section-content">

            <h3>딜레마</h3>
            <p>FE와 DD는 <strong>시간불변 누락변수</strong>에 기반. 그러나 많은 질문에서 이 가정은 그럴듯해 보이지 않음.</p>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>예시: 훈련 프로그램 평가</strong></p>
                <p>정부 훈련 프로그램 참가자들은 종종 최근 충격(실직)을 경험함. 많은 프로그램이 명시적으로 그런 사람들을 대상.</p>
                <p style="margin-top: 0.5rem;"><strong>Ashenfelter (1978), Ashenfelter & Card (1985):</strong> 훈련 참가자들이 <strong>프로그램 전 소득 하락(dip)</strong>을 보임.</p>
                <p style="margin-top: 0.5rem;">과거 소득은 시간불변 α<sub>i</sub>에 포함될 수 없는 <em>시간 변동</em> 교란요인.</p>
            </div>

            <h3>두 경쟁 모형</h3>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;"></th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">고정효과</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">종속변수 시차</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>선택 기반</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">시간불변 비관측변수 (α<sub>i</sub>)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">과거 결과 (y<sub>it−h</sub>)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>CIA</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif; font-size: 0.9rem;">E(y<sub>0it</sub>|α<sub>i</sub>, X<sub>it</sub>, d<sub>it</sub>) = E(y<sub>0it</sub>|α<sub>i</sub>, X<sub>it</sub>)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif; font-size: 0.9rem;">E(y<sub>0it</sub>|y<sub>it−h</sub>, X<sub>it</sub>, d<sub>it</sub>) = E(y<sub>0it</sub>|y<sub>it−h</sub>, X<sub>it</sub>)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>모형</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif; font-size: 0.9rem;">y<sub>it</sub> = α<sub>i</sub> + λ<sub>t</sub> + ρd<sub>it</sub> + X<sub>it</sub>β + ε<sub>it</sub></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif; font-size: 0.9rem;">y<sub>it</sub> = θ + γy<sub>it−h</sub> + λ<sub>t</sub> + ρd<sub>it</sub> + X<sub>it</sub>β + ε<sub>it</sub></td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>적절한 경우</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">영구적 비관측 능력/선호가 선택 주도</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">최근 충격/변화가 선택 주도 (훈련 프로그램)</td>
                </tr>
            </table>

            <h3>둘 다 포함할 수 있나?</h3>
            <p>α<sub>i</sub>와 y<sub>it−1</sub> 모두 있는 모형을 추정하고 싶은 유혹:</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                y<sub>it</sub> = α<sub>i</sub> + γy<sub>it−1</sub> + λ<sub>t</sub> + ρd<sub>it</sub> + X<sub>it</sub>β + ε<sub>it</sub>
            </div>

            <p>α<sub>i</sub>를 제거하기 위해 차분:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                Δy<sub>it</sub> = γΔy<sub>it−1</sub> + Δλ<sub>t</sub> + ρΔd<sub>it</sub> + ΔX<sub>it</sub>β + Δε<sub>it</sub>
            </div>

            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Nickell (1981) 문제:</strong></p>
                <p>Δy<sub>it−1</sub> = y<sub>it−1</sub> − y<sub>it−2</sub>에 ε<sub>it−1</sub> 포함</p>
                <p>Δε<sub>it</sub> = ε<sub>it</sub> − ε<sub>it−1</sub>에도 ε<sub>it−1</sub> 포함</p>
                <p style="margin-top: 0.5rem;">→ <strong>회귀변수가 오차와 상관!</strong> OLS가 비일치.</p>
            </div>

            <p><strong>가능한 해결:</strong> y<sub>it−2</sub>를 Δy<sub>it−1</sub>의 도구변수로 사용. 하지만 필요 조건:</p>
            <ul>
                <li>최소 3기간의 데이터</li>
                <li>ε<sub>it</sub>가 계열 비상관 (가능성 낮음 — 소득은 매우 지속적)</li>
            </ul>

            <h3>괄호(Bracketing) 성질</h3>
            <p>FE와 LDV 모형은 <strong>중첩되지 않음</strong>. 결합 모형(추정하기 어려움)만이 둘 다 포함. 그러나 유용한 <strong>괄호 성질</strong>이 있음:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <table style="width:100%; border-collapse: collapse; margin: 0;">
                    <tr style="background: #059669; color: white;">
                        <th style="padding: 0.75rem; border: 1px solid #ddd;">진정한 모형이...</th>
                        <th style="padding: 0.75rem; border: 1px solid #ddd;">그런데 추정은...</th>
                        <th style="padding: 0.75rem; border: 1px solid #ddd;">편의 방향</th>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">LDV (y<sub>it−1</sub>에 의한 선택)</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">FE (차분)</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>상향</strong> — 추정치 너무 큼</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">FE (α<sub>i</sub>에 의한 선택)</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">LDV (y<sub>it−1</sub> 통제)</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>하향</strong> — 추정치 너무 작음</td>
                    </tr>
                </table>
            </div>

            <p><strong>함의:</strong> FE와 LDV 추정치가 진정한 인과효과를 <strong>괄호로 묶음</strong>. 경계를 제공한다고 생각할 수 있음.</p>

            <h3>부록: 왜 괄호가 작동하는가</h3>

            <details style="margin: 1rem 0; padding: 1rem; background: #f9f9f9; border-radius: 8px;">
                <summary style="cursor: pointer; font-weight: 600; color: #2563eb;">클릭하여 펼치기: 수학적 도출</summary>
                <div style="margin-top: 1rem;">
                    <p><strong>경우 1: LDV가 맞는데 FE 사용</strong></p>
                    <p>진정한 모형 (단순화, 공변량/시간효과 없음, d<sub>it−1</sub> = 0):</p>
                    <div style="font-family: 'Times New Roman', serif; padding: 0.5rem; background: white; border-radius: 4px; margin: 0.5rem 0;">
                        y<sub>it</sub> = α<sub>i</sub> + ρd<sub>it</sub> + ε<sub>it</sub>
                    </div>
                    <p>여기서 ε<sub>it</sub>는 계열 비상관이고 α<sub>i</sub>, d<sub>it</sub>와 비상관.</p>
                    
                    <p>y<sub>it−1</sub> = α<sub>i</sub> + ε<sub>it−1</sub>을 잘못 통제. α<sub>i</sub> = y<sub>it−1</sub> − ε<sub>it−1</sub>을 대입:</p>
                    <div style="font-family: 'Times New Roman', serif; padding: 0.5rem; background: white; border-radius: 4px; margin: 0.5rem 0;">
                        y<sub>it</sub> = y<sub>it−1</sub> + ρd<sub>it</sub> + ε<sub>it</sub> − ε<sub>it−1</sub>
                    </div>
                    
                    <p>LDV 추정량이 얻는 것:</p>
                    <div style="font-family: 'Times New Roman', serif; padding: 0.5rem; background: white; border-radius: 4px; margin: 0.5rem 0;">
                        ρ + σ²<sub>ε</sub> / V(d̃<sub>it</sub>)
                    </div>
                    
                    <p>훈련생은 낮은 y<sub>it−1</sub>을 가지므로, d<sub>it</sub>와 y<sub>it−1</sub>의 상관은 음수 (π < 0). 편의 항은 양수 → <strong>LDV 추정치가 너무 작음</strong>.</p>

                    <hr style="margin: 1rem 0;">

                    <p><strong>경우 2: FE가 맞는데 LDV 사용</strong></p>
                    <p>진정한 모형:</p>
                    <div style="font-family: 'Times New Roman', serif; padding: 0.5rem; background: white; border-radius: 4px; margin: 0.5rem 0;">
                        y<sub>it</sub> = θ + γy<sub>it−1</sub> + ρd<sub>it</sub> + ε<sub>it</sub>
                    </div>
                    <p>여기서 ε<sub>it</sub>는 계열 비상관이고 0 < γ < 1 (정상성).</p>
                    
                    <p>잘못 차분 (FE). y<sub>it−1</sub>을 빼면:</p>
                    <div style="font-family: 'Times New Roman', serif; padding: 0.5rem; background: white; border-radius: 4px; margin: 0.5rem 0;">
                        y<sub>it</sub> − y<sub>it−1</sub> = θ + (γ−1)y<sub>it−1</sub> + ρd<sub>it</sub> + ε<sub>it</sub>
                    </div>
                    
                    <p>차분 추정량이 얻는 것:</p>
                    <div style="font-family: 'Times New Roman', serif; padding: 0.5rem; background: white; border-radius: 4px; margin: 0.5rem 0;">
                        ρ + (γ−1) × Cov(y<sub>it−1</sub>, d<sub>it</sub>) / V(d<sub>it</sub>)
                    </div>
                    
                    <p>γ < 1이므로 (γ−1 < 0) 훈련생이 낮은 y<sub>it−1</sub>을 가지면 (음의 상관), 편의 항은 양수 → <strong>FE 추정치가 너무 큼</strong>.</p>
                </div>
            </details>

            <h3>실용적 조언</h3>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <ol>
                    <li><strong>강건성 검토:</strong> FE와 LDV 모형 둘 다 추정. 비슷한 결과면 더 확신할 수 있음.</li>
                    <li><strong>경계로 해석:</strong> 결과가 다르면 진실은 아마 그 사이(양의 효과에서 FE 상한, LDV 하한).</li>
                    <li><strong>선택에 대해 생각:</strong> 선택이 영구적 특성(FE)에 더 그럴듯하게 기반하는가 최근 이력(LDV)에 기반하는가?</li>
                </ol>
                <p style="margin-top: 0.5rem;"><strong>예시:</strong> Guryan (2004)는 법원 명령 버스 통학이 흑인 고등학교 졸업률에 미치는 효과 연구에서 이 괄호 추론 사용.</p>
            </div>
        </div>
    </section>

    <!-- 요약 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Chapter 5 요약</h2>
        <div class="section-content">
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">개념</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">핵심 포인트</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>고정효과</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">단위 내 변동을 사용해 시간불변 비관측 교란요인 제거</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>FE 추정</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">평균 편차 또는 1차 차분 (T=2일 때 동일)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>FE 한계</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">측정 오차 증폭; 좋은 변동과 나쁜 변동 모두 제거</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>DD</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">집계 데이터용 FE: (Δ처치군) − (Δ통제군)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>평행 추세</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">핵심 DD 가정 — 처치 부재 시 처치군과 통제군이 같은 추세</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>회귀 DD</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">주 + 시간 더미 + 교호작용; 처치 강도 변동, 공변량 허용</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>DD 검정</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">사전 추세, 선행/후행 (Granger), 주별 추세, 삼중차분</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>FE vs. LDV</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">다른 가정; 중첩 안 됨; 추정치가 진정한 효과를 괄호로 묶음</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>괄호</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">LDV 참이면 FE 너무 큼; FE 참이면 LDV 너무 작음 → 인과효과의 경계</td>
                </tr>
            </table>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>실용적 체크리스트:</strong></p>
                <ol>
                    <li>✓ FE/DD는 <strong>단위 내 시간에 걸친 변동</strong> 활용 — 수준 비교 포기</li>
                    <li>✓ 가능하면 항상 처치 전 데이터로 <strong>평행 추세 검정</strong></li>
                    <li>✓ <strong>측정 오차</strong> 효과 검토 (FE가 감쇠될 수 있음)</li>
                    <li>✓ <strong>선행/후행</strong> 설정 실행 — 선행은 0이어야</li>
                    <li>✓ 강건성 검정으로 <strong>주별 추세</strong> 시도</li>
                    <li>✓ <strong>FE와 LDV 둘 다</strong> 고려 — 진실을 괄호로 묶음</li>
                    <li>✓ 처치/통제 그룹의 <strong>구성 변화</strong> 주시</li>
                </ol>
            </div>
        </div>
    </section>

    <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee; display: flex; justify-content: space-between;">
        <a href="/study/angrist-ch4-part3-ko" style="color: #666;">← Ch 4-3: IV 상세</a>
        <a href="/study/angrist-ch6-ko" style="color: #9ca3af;">Ch 6: RDD →</a>
    </div>

    <div style="margin-top: 2rem; padding: 1rem; background: #f9fafb; border-radius: 8px; font-size: 0.8rem; color: #6b7280;">
        <em>이 노트는 LLM (Claude)의 도움을 받아 작성되었습니다.</em>
    </div>
</div>
