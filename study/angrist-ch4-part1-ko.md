---
layout: minimal_base
title: "Angrist Ch.4-1 - IV 기초, Wald & 2SLS"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Chapter 4 Part 1: IV 기초, Wald & 2SLS</h2>
            <a href="/study/angrist-ch4-part1" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">English</a>
        </div>
        <div class="section-content">
            <p><em>Angrist & Pischke, Mostly Harmless Econometrics — Sections 4.1–4.3</em></p>
        </div>
    </section>

    <!-- 핵심 메시지 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">핵심 메시지</h2>
        <div class="section-content">
            <blockquote style="border-left: 4px solid #2563eb; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                <strong>도구변수(IV)</strong>는 결과에 <em>처치를 통해서만</em> 영향을 미치는 변수(도구변수)를 활용하여 누락변수 편의를 해결한다. IV 추정량은 <strong>축약형</strong>(도구변수 → 결과)을 <strong>1단계</strong>(도구변수 → 처치)로 나눈 비율이다.
            </blockquote>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>이 파트의 핵심 질문들:</strong></p>
                <ol>
                    <li>IV가 유효하려면 어떤 가정이 필요한가? → 배제제약 + 1단계</li>
                    <li>2SLS는 어떻게 작동하는가? → 내생변수를 1단계 적합값으로 대체</li>
                    <li>Wald 추정량이란? → 이진 도구변수를 사용하는 가장 단순한 IV</li>
                    <li>집단 데이터와 2SLS의 관계는? → 더미 도구변수의 2SLS = 집단 평균의 GLS</li>
                </ol>
            </div>
        </div>
    </section>

    <!-- 4.1 IV와 인과관계 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4.1 IV와 인과관계</h2>
        <div class="section-content">

            <h3>IV가 해결하는 문제</h3>
            <p>필요한 모든 통제변수가 포함된 "긴 회귀식(long regression)"이 아래와 같다고 가정하자:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                y<sub>i</sub> = α + ρs<sub>i</sub> + A<sub>i</sub>'γ + v<sub>i</sub>
            </div>
            <p>여기서 A<sub>i</sub>("능력")가 교육연수 s<sub>i</sub>와 v<sub>i</sub>의 상관을 제거한다. A<sub>i</sub>가 <strong>관측 불가능</strong>하면, "짧은 회귀식" y<sub>i</sub> = α + ρ̃s<sub>i</sub> + ε<sub>i</sub>의 OLS는 편의를 가진다. IV는 A<sub>i</sub>를 관측하지 않고도 이 문제를 해결한다.</p>

            <h3>IV 설정 (동질적 효과)</h3>
            <p>도구변수 z<sub>i</sub>는 두 가지 조건을 만족해야 한다:</p>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">조건</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">수식</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">의미</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>관련성</strong> (1단계)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">Cov(s<sub>i</sub>, z<sub>i</sub>) ≠ 0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">도구변수가 실제로 처치에 영향을 미침</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>배제제약</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">Cov(ε<sub>i</sub>, z<sub>i</sub>) = 0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">도구변수는 <em>처치를 통해서만</em> 결과에 영향</td>
                </tr>
            </table>

            <h3>IV 추정량</h3>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.2rem;">
                    ρ = Cov(y<sub>i</sub>, z<sub>i</sub>) / Cov(s<sub>i</sub>, z<sub>i</sub>) = <span style="color: #059669;">축약형</span> / <span style="color: #2563eb;">1단계</span>
                </div>
            </div>
            <p>인과효과는 두 회귀계수의 비율이다:</p>
            <ul>
                <li><strong style="color: #059669;">축약형(Reduced form)</strong>: y<sub>i</sub>를 z<sub>i</sub>에 회귀 (도구변수가 결과에 미치는 영향)</li>
                <li><strong style="color: #2563eb;">1단계(First stage)</strong>: s<sub>i</sub>를 z<sub>i</sub>에 회귀 (도구변수가 처치에 미치는 영향)</li>
            </ul>

            <h3>예시: 출생 분기 (Angrist & Krueger 1991)</h3>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>논리:</strong> 취학연령 규칙 + 의무교육법 → 연초 출생 아동이 약간 <em>적은</em> 교육을 받음.</p>
                <ul>
                    <li><strong>처치:</strong> 교육연수 (s<sub>i</sub>)</li>
                    <li><strong>도구변수:</strong> 출생 분기 (z<sub>i</sub>)</li>
                    <li><strong>결과:</strong> 로그 주급 (y<sub>i</sub>)</li>
                </ul>
                <p><strong>왜 유효한가?</strong> 생년월일은 본질적으로 무작위이며, 교육을 통해서만 소득에 영향을 미친다고 볼 수 있다.</p>
            </div>

            <h4>두 개의 방정식</h4>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                <strong>1단계:</strong> s<sub>i</sub> = X<sub>i</sub>'π<sub>10</sub> + π<sub>11</sub>z<sub>i</sub> + η<sub>1i</sub><br><br>
                <strong>축약형:</strong> y<sub>i</sub> = X<sub>i</sub>'π<sub>20</sub> + π<sub>21</sub>z<sub>i</sub> + η<sub>2i</sub>
            </div>
            <p>IV 추정량은 ρ = π<sub>21</sub> / π<sub>11</sub>이며, 이를 <strong>간접최소제곱(ILS)</strong> 추정량이라고도 한다.</p>

            <h3>4.1.1 2단계 최소제곱법 (2SLS)</h3>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>1단계:</strong> 내생변수를 도구변수와 공변량에 회귀하여 적합값을 구한다.</p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; margin: 0.5rem 0;">
                    ŝ<sub>i</sub> = X<sub>i</sub>'π̂<sub>10</sub> + π̂<sub>11</sub>z<sub>i</sub>
                </div>
                <p><strong>2단계:</strong> 결과변수를 적합값과 공변량에 회귀한다.</p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; margin: 0.5rem 0;">
                    y<sub>i</sub> = δ'X<sub>i</sub> + ρŝ<sub>i</sub> + [ε<sub>i</sub> + (s<sub>i</sub> − ŝ<sub>i</sub>)]
                </div>
            </div>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>왜 작동하는가?</strong></p>
                <ul>
                    <li>ŝ<sub>i</sub>는 도구변수에 의해 발생한 변동<em>만</em> 보존</li>
                    <li>이 준실험적 변동은 오차항과 무상관</li>
                    <li>도구변수가 하나이면, 2SLS = ILS (축약형 ÷ 1단계)</li>
                </ul>
            </div>

            <h4>다중 도구변수</h4>
            <p>세 개의 출생 분기 더미(z<sub>1i</sub>, z<sub>2i</sub>, z<sub>3i</sub>)를 사용하면 1단계는:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                s<sub>i</sub> = X<sub>i</sub>'π<sub>10</sub> + π<sub>11</sub>z<sub>1i</sub> + π<sub>12</sub>z<sub>2i</sub> + π<sub>13</sub>z<sub>3i</sub> + η<sub>1i</sub>
            </div>
            <p>2SLS는 여러 도구변수를 최적으로 결합하여 하나의 적합값을 만든다.</p>

            <h4>결과: 교육의 수익률</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">모형</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">OLS</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">2SLS</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">도구변수</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">통제변수 없음</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.075</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.103 (0.024)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">QOB=1 더미</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">YOB + SOB 더미</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.072</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.108 (0.019)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">QOB 더미 3개</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+ QOB×YOB 교호작용</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.072</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.089 (0.016)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">30개 도구변수</td>
                </tr>
            </table>
            <p>2SLS 추정치가 OLS보다 약간 <em>크므로</em>, 이 경우 능력 편의가 교육-소득 관계를 주도하지 않음을 시사한다.</p>

            <h3>4.1.2 Wald 추정량</h3>

            <p>가장 단순한 IV: <strong>단일 이진 도구변수</strong>, 공변량 없음.</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Wald 공식:</strong></p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.2rem; margin: 0.5rem 0;">
                    ρ = [E(y<sub>i</sub>|z<sub>i</sub>=1) − E(y<sub>i</sub>|z<sub>i</sub>=0)] / [E(s<sub>i</sub>|z<sub>i</sub>=1) − E(s<sub>i</sub>|z<sub>i</sub>=0)]
                </div>
                <p style="text-align: center; margin-top: 0.5rem;">= 결과 평균의 차이 ÷ 처치 평균의 차이</p>
            </div>

            <h4>예시 1: 교육의 수익률</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;"></th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Q1–Q2 출생</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Q3–Q4 출생</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">차이</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">ln(주급)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">5.8916</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">5.9051</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.01349</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">교육연수</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">12.6881</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">12.8394</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.1514</td>
                </tr>
                <tr style="background: #ecfdf5;">
                    <td style="padding: 0.5rem; border: 1px solid #ddd;" colspan="3"><strong>Wald 추정치</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>0.0891</strong> (0.021)</td>
                </tr>
            </table>

            <h4>예시 2: 베트남 징병 추첨 (Angrist 1990)</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>설정:</strong> 무작위 징병 추첨번호 → 징병 대상 → 군 복무 → 소득</p>
                <ul>
                    <li><strong>도구변수:</strong> 징병 대상 여부 (무작위, 이진)</li>
                    <li><strong>처치:</strong> 참전 여부</li>
                    <li>징병 대상자는 복무 확률이 15.9%p 높았음</li>
                    <li>Wald 추정치: 군 복무로 1981년 소득 약 $2,741 감소</li>
                </ul>
                <p><strong>타당성 검증:</strong> 1969년 소득(추첨 이전)에는 효과 없음 → 도구변수가 깨끗함.</p>
            </div>

            <h4>예시 3: 출산과 노동공급 (Angrist & Evans 1998)</h4>
            <p>자녀 2명 이상인 여성에서 셋째 출산에 대한 두 가지 도구변수:</p>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">결과</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">OLS</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">쌍둥이 IV (1단계: 0.625)</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">동성 IV (1단계: 0.067)</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">취업</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.167</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.083</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.135</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">근로 주수</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−8.05</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−3.83</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−6.23</td>
                </tr>
            </table>
            <p>다른 도구변수가 다른 추정치를 제공 → 이질적 효과를 예고 (Part 2에서 다룸).</p>

            <h3>4.1.3 집단 데이터와 2SLS</h3>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>핵심 통찰:</strong> 더미 도구변수의 2SLS = 집단 평균의 GLS = 모든 가능한 Wald 추정량의 효율적 선형 결합.</p>
            </div>

            <p>도구변수가 이산값 (j = 1, …, J)을 취할 때, 집단 평균 ȳ<sub>j</sub>와 p̂<sub>j</sub>를 정의한다. 집단 회귀:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                ȳ<sub>j</sub> = α + ρp̂<sub>j</sub> + ε̄<sub>j</sub>
            </div>
            <p>집단 크기 n<sub>j</sub>로 가중한 GLS = 집단 더미를 도구변수로 사용한 2SLS.</p>

            <h4>시각적 도구변수 (VIV)</h4>
            <p>VIV 도표는 도구변수 셀별로 평균 결과 vs. 처치 확률을 보여준다. 이 점들을 통과하는 직선의 기울기가 IV 추정치이다. IV 전략의 강력한 시각적 점검 도구.</p>
        </div>
    </section>

    <!-- 4.2 점근 추론 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4.2 2SLS의 점근적 추론</h2>
        <div class="section-content">

            <h3>표준오차</h3>
            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>주의:</strong> "수동 2SLS" (y를 ŝ에 OLS 회귀)는 <strong>잘못된 표준오차</strong>를 제공한다. 올바른 오차 분산은 구조적 잔차 ε<sub>i</sub>의 분산이지, 2단계 잔차 ε<sub>i</sub> + (s<sub>i</sub> − ŝ<sub>i</sub>)의 분산이 아니다.</p>
            </div>

            <h3>과대식별 검정</h3>
            <p>도구변수가 내생변수보다 많을 때(과대식별), 모든 도구변수가 같은 답을 주는지 검정할 수 있다.</p>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>과대식별 검정 통계량:</strong> H<sub>0</sub>: E[Z<sub>i</sub>ε<sub>i</sub>] = 0 하에서, 최소화된 2SLS 목적함수는 χ²(q−1) 분포를 따른다.</p>
                <p><strong>계산:</strong> 2SLS 잔차를 모든 도구변수와 공변량에 회귀한 R²에 N을 곱한 값.</p>
            </div>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>주의사항:</strong> 과대식별 검정의 실용적 가치는 제한적이다.</p>
                <ul>
                    <li>IV 추정치가 <em>부정확</em>하면, 검정력이 낮아 나쁜 도구변수도 기각하지 못함</li>
                    <li>IV 추정치가 <em>정확</em>하면, 기각은 도구변수 실패가 아닌 처치효과 이질성 때문일 수 있음</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- 4.3 Two-Sample IV -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4.3 2표본 IV와 분할표본 IV</h2>
        <div class="section-content">

            <h3>2표본 IV (TSIV)</h3>
            <p>IV는 <strong>표본 적률만으로</strong> 구성할 수 있다. 1단계와 축약형 데이터가 같은 데이터셋에서 올 필요가 없으며, 같은 모집단에서 추출되면 된다.</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>TSIV가 유용한 경우:</strong> 단일 데이터셋에 필요한 모든 변수가 없을 때. 예:</p>
                <ul>
                    <li>데이터셋 1 (SSA 기록): 소득 + 추첨번호 → 축약형</li>
                    <li>데이터셋 2 (군사 기록): 참전 여부 + 추첨번호 → 1단계</li>
                </ul>
            </div>

            <h3>분할표본 IV (SSIV)</h3>
            <p>Angrist & Krueger (1995)가 제안한 계산적으로 간단한 TSIV 추정량:</p>
            <ol>
                <li>데이터셋 2에서 1단계 추정: π̂ = (Z₂'Z₂)⁻¹Z₂'W₂</li>
                <li>교차 표본 적합값 구성: Ŵ₁₂ = Z₁π̂</li>
                <li>데이터셋 1에서 y₁을 Ŵ₁₂에 회귀</li>
            </ol>
            <p>SSIV는 과대식별 모형의 편의 감소에도 도움이 된다 (Part 3에서 논의).</p>
        </div>
    </section>

    <!-- 요약 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Part 1 요약</h2>
        <div class="section-content">
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">개념</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">핵심 포인트</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>IV 추정량</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">ρ = Cov(y, z) / Cov(s, z) = 축약형 ÷ 1단계</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>배제제약</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">z는 s를 <em>통해서만</em> y에 영향</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>2SLS</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">내생변수를 1단계 적합값으로 대체</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Wald 추정량</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">결과 평균 차이 ÷ 처치 평균 차이 (이진 z)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>집단 데이터 = 2SLS</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">더미 도구변수의 집단 평균 GLS = 2SLS</td>
                </tr>
            </table>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>IV 레시피:</strong></p>
                <ol>
                    <li>(a) 처치와 상관되고, (b) 오차항과 무상관인 도구변수 찾기</li>
                    <li>1단계 추정 — 약하면 걱정 (Part 3에서 상세 논의)</li>
                    <li>축약형 확인 — 도구변수의 인과효과로, 항상 비편향</li>
                    <li>IV = 축약형 ÷ 1단계 계산</li>
                </ol>
            </div>
        </div>
    </section>

    <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee; display: flex; justify-content: space-between;">
        <a href="/study/angrist-ch3-ko" style="color: #666;">← Chapter 3: 회귀분석의 이해</a>
        <a href="/study/angrist-ch4-part2-ko" style="color: #2563eb;">Part 2: LATE & 이질적 효과 →</a>
    </div>

    <div style="margin-top: 2rem; padding: 1rem; background: #f9fafb; border-radius: 8px; font-size: 0.8rem; color: #6b7280;">
        <em>이 노트는 LLM (Claude)의 도움을 받아 작성되었습니다.</em>
    </div>
</div>
