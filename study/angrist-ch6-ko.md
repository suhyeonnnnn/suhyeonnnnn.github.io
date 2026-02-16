---
layout: minimal_base
title: "Angrist Ch.6 - 회귀단절 설계"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Chapter 6: 회귀단절 설계 (RDD)</h2>
            <a href="/study/angrist-ch6" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">English</a>
        </div>
        <div class="section-content">
            <p><em>Angrist & Pischke, Mostly Harmless Econometrics — Chapter 6</em></p>
            <p style="color: #6b7280; font-style: italic;">"규칙이 많을수록, 규칙이 작을수록, 규칙이 자의적일수록, 더 좋다." — Douglas Adams</p>
        </div>
    </section>

    <!-- 핵심 메시지 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">핵심 메시지</h2>
        <div class="section-content">
            <blockquote style="border-left: 4px solid #2563eb; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                <strong>회귀단절(RD)</strong>은 처치를 결정하는 규칙에 대한 정확한 지식을 활용한다. 규칙 기반 세계에서 일부 규칙은 <em>자의적</em>이므로 좋은 자연실험을 제공한다. 핵심 통찰: 처치가 알려진 기준점에서 켜지고/꺼지면, 기준점 바로 위와 바로 아래의 단위들은 본질적으로 비교 가능하다 — 국지적 무작위 실험과 같다.
            </blockquote>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>RD의 두 가지 유형:</strong></p>
                <ul>
                    <li><strong>Sharp RD:</strong> 처치가 실행변수의 <em>결정적</em> 함수 — 기준점을 넘으면 처치가 완전히 켜지고/꺼짐</li>
                    <li><strong>Fuzzy RD:</strong> 기준점을 넘으면 처치 <em>확률</em>이 변함 — IV 설정으로 연결</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- 6.1 Sharp RD -->
    <section class="section fade-in-delay">
        <h2 class="section-title">6.1 Sharp RD</h2>
        <div class="section-content">

            <h3>설정</h3>
            <p>Sharp RD는 처치 상태가 공변량 x<sub>i</sub>("실행변수" 또는 "강제변수")의 <strong>결정적이고 불연속적인</strong> 함수일 때 사용:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center; font-size: 1.1rem;">
                d<sub>i</sub> = 1(x<sub>i</sub> ≥ x<sub>0</sub>) = 
                <span style="display: inline-block; text-align: left; vertical-align: middle;">
                    { 1 if x<sub>i</sub> ≥ x<sub>0</sub><br>
                    { 0 if x<sub>i</sub> < x<sub>0</sub>
                </span>
            </div>

            <p>여기서 x<sub>0</sub>은 알려진 <strong>임계값</strong> 또는 <strong>기준점</strong>.</p>

            <ul>
                <li><strong>결정적:</strong> x<sub>i</sub>를 알면 d<sub>i</sub>를 알 수 있음</li>
                <li><strong>불연속적:</strong> x<sub>i</sub>가 x<sub>0</sub>에 아무리 가까워져도 x<sub>i</sub> = x<sub>0</sub>이 될 때까지 처치는 변하지 않음</li>
            </ul>

            <h3>동기 부여 예시: 국가 장학금</h3>
            <p>최초의 RD 연구(Thistlethwaite & Campbell, 1960)의 질문: National Merit Scholarship Award를 받은 학생들이 장학금 <em>때문에</em> 대학 졸업률이 높은가?</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <ul>
                    <li><strong>실행변수 (x<sub>i</sub>):</strong> PSAT 점수</li>
                    <li><strong>기준점 (x<sub>0</sub>):</strong> 장학금 수여 임계값</li>
                    <li><strong>처치 (d<sub>i</sub>):</strong> 장학금 수령</li>
                    <li><strong>결과 (y<sub>i</sub>):</strong> 대학 졸업</li>
                </ul>
                <p style="margin-top: 0.5rem;"><strong>RD 접근법:</strong> 임계값 <em>바로 위</em>와 <em>바로 아래</em> PSAT 점수를 가진 학생들을 비교. 임계값에서 대학 졸업의 점프는 처치효과의 증거.</p>
            </div>

            <h3>핵심 특징: 중첩 없음</h3>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>매칭/회귀와의 중요한 차이:</strong></p>
                <p>RD에서는 처치군과 통제군 모두를 관측하는 x<sub>i</sub> 값이 <em>없다</em>. 중첩에 기반한 매칭 전략과 달리, <strong>RD 타당성은 외삽</strong>에 달려 있다 — 조건부 평균 함수가 기준점을 통해 매끄럽다는 가정.</p>
                <p style="margin-top: 0.5rem;">→ 이것이 RD에서 3장처럼 함수 형태에 대해 불가지론적일 수 없는 이유.</p>
            </div>

            <h3>Sharp RD 모형</h3>
            <p>잠재적 결과가 선형, 상수효과 모형을 따른다고 가정:</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                E[y<sub>0i</sub> | x<sub>i</sub>] = α + βx<sub>i</sub><br>
                y<sub>1i</sub> = y<sub>0i</sub> + ρ
            </div>

            <p>이로부터 회귀식:</p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center; font-size: 1.1rem;">
                y<sub>i</sub> = α + βx<sub>i</sub> + ρd<sub>i</sub> + ε<sub>i</sub>
            </div>

            <p>여기서 ρ가 관심 인과효과.</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>3장 회귀와의 핵심 차이:</strong></p>
                <p>여기서 d<sub>i</sub>는 x<sub>i</sub>와 상관되어 있을 뿐 아니라 — x<sub>i</sub>의 <em>결정적 함수</em>이다. RD는 다음을 구별하여 인과효과를 포착:</p>
                <ul>
                    <li><strong>불연속적</strong> 함수: 1(x<sub>i</sub> ≥ x<sub>0</sub>)</li>
                    <li><strong>매끄러운</strong> 함수: x<sub>i</sub></li>
                </ul>
            </div>

            <h3>시각적 직관</h3>
            <div style="background: #f9f9f9; padding: 1.5rem; border-radius: 8px; margin: 1rem 0; text-align: center;">
                <pre style="font-family: monospace; font-size: 0.85rem; text-align: left; display: inline-block;">
패널 A: 선형 E[y₀|x]           패널 B: 비선형 E[y₀|x]

  y│                               y│
   │        ●●●●                    │           ●●●●
   │       ●                        │         ●●
   │      ● ← 점프 (ρ)              │       ●● ← 점프 (ρ)
   │     ●                          │     ●●
   │   ●●                           │   ●●
   │ ●●                             │ ●●
   └──────────────── x              └──────────────── x
          x₀                               x₀

패널 C: 비선형성을 불연속으로 오인

  y│
   │               ●●●●
   │           ●●●●
   │        ●●●    ← 급격한 곡선, 처치 아님!
   │     ●●●
   │   ●●
   │ ●●
   └──────────────── x
          x₀
                </pre>
            </div>

            <h3>다항식 통제</h3>
            <p>E[y<sub>0i</sub> | x<sub>i</sub>] = f(x<sub>i</sub>)가 비선형이면? f(x<sub>i</sub>)를 p차 다항식으로 모형화:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                y<sub>i</sub> = α + β<sub>1</sub>x<sub>i</sub> + β<sub>2</sub>x<sub>i</sub>² + ... + β<sub>p</sub>x<sub>i</sub><sup>p</sup> + ρd<sub>i</sub> + ε<sub>i</sub>
            </div>

            <p>f(x<sub>i</sub>)가 x<sub>0</sub>에서 <strong>연속</strong>인 한, 불연속적 점프 ρ를 여전히 식별 가능.</p>

            <h3>양쪽에 다른 기울기 허용</h3>
            <p>더 유연한 모형은 E[y<sub>0i</sub>|x<sub>i</sub>]와 E[y<sub>1i</sub>|x<sub>i</sub>]에 다른 추세 함수 허용. x̃<sub>i</sub> ≡ x<sub>i</sub> − x<sub>0</sub> 정의 (기준점에 중심화):</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                y<sub>i</sub> = α + β<sub>01</sub>x̃<sub>i</sub> + β<sub>02</sub>x̃<sub>i</sub>² + ... + β<sub>0p</sub>x̃<sub>i</sub><sup>p</sup><br>
                &nbsp;&nbsp;&nbsp;&nbsp;+ ρd<sub>i</sub> + δ<sub>1</sub>d<sub>i</sub>x̃<sub>i</sub> + δ<sub>2</sub>d<sub>i</sub>x̃<sub>i</sub>² + ... + δ<sub>p</sub>d<sub>i</sub>x̃<sub>i</sub><sup>p</sup> + ε<sub>i</sub>
            </div>

            <ul>
                <li>ρ = x<sub>i</sub> = x<sub>0</sub>에서의 처치효과</li>
                <li>교호작용 (d<sub>i</sub>x̃<sub>i</sub>, d<sub>i</sub>x̃<sub>i</sub>², ...)이 기준점 위/아래에서 다른 기울기 허용</li>
                <li>x<sub>0</sub>에 중심화하면 ρ가 여전히 기준점에서의 효과 포착</li>
            </ul>

            <h3>비모수적 RD</h3>
            <p>함수 형태 의존성을 완전히 피하려면 기준점 주변의 <strong>좁은 창</strong>에 집중:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                lim<sub>ε→0</sub> { E[y<sub>i</sub> | x<sub>0</sub> < x<sub>i</sub> < x<sub>0</sub>+ε] − E[y<sub>i</sub> | x<sub>0</sub>−ε < x<sub>i</sub> < x<sub>0</sub>] } = E[y<sub>1i</sub> − y<sub>0i</sub> | x<sub>i</sub> = x<sub>0</sub>]
            </div>

            <p>x<sub>0</sub> 좌우의 작은 이웃에서 평균을 비교하면 f(x<sub>i</sub>)를 올바르게 설정하지 않아도 되는 추정치 제공.</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>실용적 접근법:</strong></p>
                <ul>
                    <li><strong>국소 선형 회귀:</strong> x<sub>0</sub> 근처에 더 많은 가중치를 주는 가중 최소제곱 (Hahn, Todd, van der Klaauw, 2001)</li>
                    <li><strong>단절 표본:</strong> 대역폭 h에 대해 [x<sub>0</sub>−h, x<sub>0</sub>+h] 내 관측치로 제한 (Angrist & Lavy, 1999)</li>
                </ul>
            </div>

            <h3>Sharp RD 강건성 검정</h3>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">검정</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">확인할 것</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>대역폭 민감도</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">x<sub>0</sub> 주변 창을 좁혀도 추정치가 안정적이어야 (필요한 다항식 항 감소)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>처치 전 공변량</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">처치 전에 결정된 공변량에서 점프 없어야 (균형 검정)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>실행변수 밀도</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">x<sub>0</sub> 주변에 뭉침/조작 없어야 (McCrary, 2008 검정)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>위약 기준점</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">정책 변화가 없는 다른 x<sub>i</sub> 값에서 점프 없어야</td>
                </tr>
            </table>

            <h3>예시: Lee (2008) — 현직자 이점</h3>
            <p><strong>질문:</strong> 선거에서 이기면 다음 선거에서 정당에 이점이 있는가(현직 효과)?</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <ul>
                    <li><strong>실행변수 (x<sub>i</sub>):</strong> t선거에서 민주당 득표 마진</li>
                    <li><strong>기준점 (x<sub>0</sub>):</strong> 0 (50% 득표율)</li>
                    <li><strong>처치 (d<sub>i</sub>):</strong> 민주당이 t선거 승리 (현직 정당)</li>
                    <li><strong>결과 (y<sub>i</sub>):</strong> t+1선거에서 민주당 승리 확률</li>
                </ul>
            </div>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>핵심 통찰:</strong> d<sub>i</sub> = 1(득표 마진 ≥ 0)이 x<sub>i</sub>의 결정적 함수이므로, x<sub>i</sub> 외의 <em>교란변수가 없다</em>. 이것이 RD 설정의 특징적 장점.</p>
            </div>

            <p><strong>결과:</strong></p>
            <ul>
                <li>승리 확률은 과거 득표율의 증가 함수 (놀랍지 않음)</li>
                <li>0% 마진에서 <strong>~40 퍼센트 포인트의 극적인 점프</strong></li>
                <li>간신히 이기는 것(vs. 간신히 지는 것)이 다음 선거 승리 확률을 40pp 높임</li>
            </ul>

            <p><strong>타당성 검정:</strong> Lee는 지난 선거 <em>전</em> 민주당 승리를 검토. 현재 기준점에서 점프가 없어야 함 — 실제로 없어서 설계에 대한 확신 증가.</p>

            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>조작 우려:</strong> 정당이 기준점 근처에서 득표율을 조작할 수 있는가?</p>
                <p>2000년 플로리다 재검표는 이것이 접전에서 실제 우려임을 시사. McCrary (2008)는 x<sub>0</sub> 주변 x<sub>i</sub> 밀도를 검토하여 조작에 대한 공식 검정 제안.</p>
            </div>
        </div>
    </section>

    <!-- 6.2 Fuzzy RD -->
    <section class="section fade-in-delay">
        <h2 class="section-title">6.2 Fuzzy RD는 IV이다</h2>
        <div class="section-content">

            <h3>처치가 결정적이지 않을 때</h3>
            <p>많은 상황에서 기준점을 넘는 것이 처치를 <em>완벽하게</em> 결정하지 않음 — 처치 <em>확률</em>만 바꿈. 이것이 <strong>fuzzy RD</strong>.</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                P[d<sub>i</sub> = 1 | x<sub>i</sub>] = 
                <span style="display: inline-block; text-align: left; vertical-align: middle;">
                    { g<sub>1</sub>(x<sub>i</sub>) if x<sub>i</sub> ≥ x<sub>0</sub><br>
                    { g<sub>0</sub>(x<sub>i</sub>) if x<sub>i</sub> < x<sub>0</sub>
                </span>
                &nbsp;&nbsp;where g<sub>1</sub>(x<sub>0</sub>) ≠ g<sub>0</sub>(x<sub>0</sub>)
            </div>

            <p>함수 g<sub>0</sub>과 g<sub>1</sub>은 x<sub>0</sub>에서 <strong>다르기만</strong> 하면 됨(그리고 차이가 클수록 좋음!).</p>

            <h3>Fuzzy RD = IV</h3>
            <p>t<sub>i</sub> = 1(x<sub>i</sub> ≥ x<sub>0</sub>)를 임계값 통과 더미로 정의. 불연속 t<sub>i</sub>가 처치 d<sub>i</sub>의 <strong>도구변수</strong>가 됨.</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>2SLS 설정:</strong></p>
                <p><strong>1단계:</strong></p>
                <div style="font-family: 'Times New Roman', serif; margin: 0.5rem 0; padding-left: 1rem;">
                    d<sub>i</sub> = π<sub>0</sub> + π<sub>1</sub>x<sub>i</sub> + π<sub>2</sub>x<sub>i</sub>² + ... + π<sub>p</sub>x<sub>i</sub><sup>p</sup> + <strong>γt<sub>i</sub></strong> + η<sub>1i</sub>
                </div>
                <p>여기서 γ는 1단계 효과 (기준점에서 처치 확률의 점프).</p>
                
                <p style="margin-top: 0.5rem;"><strong>2단계:</strong></p>
                <div style="font-family: 'Times New Roman', serif; margin: 0.5rem 0; padding-left: 1rem;">
                    y<sub>i</sub> = α + β<sub>1</sub>x<sub>i</sub> + β<sub>2</sub>x<sub>i</sub>² + ... + β<sub>p</sub>x<sub>i</sub><sup>p</sup> + <strong>ρd<sub>i</sub></strong> + ε<sub>i</sub>
                </div>
            </div>

            <h3>축약형</h3>
            <p>1단계를 2단계에 대입:</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                y<sub>i</sub> = α' + β'<sub>1</sub>x<sub>i</sub> + β'<sub>2</sub>x<sub>i</sub>² + ... + β'<sub>p</sub>x<sub>i</sub><sup>p</sup> + <strong>(ργ)t<sub>i</sub></strong> + η<sub>2i</sub>
            </div>

            <p>t<sub>i</sub>의 축약형 계수는 ργ (인과효과 × 1단계).</p>

            <h3>비모수적 Fuzzy RD: Wald 추정량</h3>
            <p>x<sub>0</sub> 주변의 작은 이웃에서 fuzzy RD는 단순한 Wald/IV 추정량이 됨:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center; font-size: 1.05rem;">
                ρ = lim<sub>ε→0</sub> 
                <span style="display: inline-block; border-top: 1px solid black; padding-top: 0.3rem;">
                    E[y<sub>i</sub> | x<sub>0</sub> < x<sub>i</sub> < x<sub>0</sub>+ε] − E[y<sub>i</sub> | x<sub>0</sub>−ε < x<sub>i</sub> < x<sub>0</sub>]
                </span>
                <br>
                <span style="display: inline-block; border-bottom: 1px solid black; padding-bottom: 0.3rem;">
                    E[d<sub>i</sub> | x<sub>0</sub> < x<sub>i</sub> < x<sub>0</sub>+ε] − E[d<sub>i</sub> | x<sub>0</sub>−ε < x<sub>i</sub> < x<sub>0</sub>]
                </span>
                = <span style="display: inline-block; border-top: 1px solid black; padding-top: 0.3rem;">축약형 점프</span>
                <br>
                <span style="display: inline-block; border-bottom: 1px solid black; padding-bottom: 0.3rem;">1단계 점프</span>
            </div>

            <h3>LATE 해석</h3>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Fuzzy RD는 국소 평균 처치효과(LATE)를 추정:</strong></p>
                <p>효과는 <strong>순응자</strong>에 대한 것 — x<sub>i</sub>가 x<sub>0</sub> 바로 아래에서 바로 위로 이동할 때 처치 상태가 바뀌는 개인들.</p>
                <p style="margin-top: 0.5rem;"><strong>이중 국소성:</strong></p>
                <ol>
                    <li>LATE는 순응자만을 위한 것 (모든 IV와 마찬가지)</li>
                    <li>효과는 x<sub>i</sub> = x<sub>0</sub>에서 추정됨 (기준점에 국소적)</li>
                </ol>
            </div>

            <h3>예시: Angrist & Lavy (1999) — 학급 규모 효과</h3>
            <p><strong>질문:</strong> 더 작은 학급이 학생 시험 점수를 향상시키는가? (테네시 STAR 실험과 같은 질문)</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>설정:</strong> 이스라엘 학교는 최대 학급 규모가 40명 ("마이모니데스 규칙").</p>
                <ul>
                    <li>≤40명 학년 → 1개 학급 (최대 40명)</li>
                    <li>41명 학년 → 2개 학급 (~20명씩)</li>
                    <li>81명 학년 → 3개 학급 (~27명씩)</li>
                </ul>
                <p style="margin-top: 0.5rem;"><strong>마이모니데스 규칙 공식:</strong></p>
                <div style="font-family: 'Times New Roman', serif; text-align: center; margin: 0.5rem 0;">
                    m<sub>sc</sub> = e<sub>s</sub> / (int[(e<sub>s</sub>−1)/40] + 1)
                </div>
                <p>여기서 e<sub>s</sub> = 등록인원, m<sub>sc</sub> = 예측 학급 규모.</p>
            </div>

            <h4>왜 Fuzzy인가?</h4>
            <p>마이모니데스 규칙이 학급 규모를 <em>완벽하게</em> 예측하지 못함 — 일부 학교는 40명 미만에서도 학급을 분할. 이것이 fuzzy 설계를 만듦.</p>

            <h4>RD 설정</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">RD 요소</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">이 연구에서</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">실행변수 (x<sub>i</sub>)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">학년 등록인원 (e<sub>s</sub>)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">기준점 (x<sub>0</sub>)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">40, 80, 120, ...</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">처치 (d<sub>i</sub>)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">실제 학급 규모 (n<sub>sc</sub>)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">도구변수 (t<sub>i</sub>)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">마이모니데스 규칙에서 예측된 학급 규모 (m<sub>sc</sub>)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">결과 (y<sub>i</sub>)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">시험 점수</td>
                </tr>
            </table>

            <h4>시각적: 톱니 패턴</h4>
            <div style="background: #f9f9f9; padding: 1.5rem; border-radius: 8px; margin: 1rem 0; text-align: center;">
                <pre style="font-family: monospace; font-size: 0.85rem; text-align: left; display: inline-block;">
학급 규모
    │
 40 │     ●●●●●                ●●●●●
    │    ●     \              ●     \
 30 │   ●       \            ●       \
    │  ●         \          ●         \
 20 │ ●           ●●●●●●●●●●           ●●●●
    │              ↑                    ↑
    └───────────────────────────────────────── 등록인원
              40  41          80  81

    --- = 마이모니데스 규칙 (예측)
    ●●● = 실제 학급 규모 (fuzzy)
                </pre>
            </div>

            <h4>결과: 5학년 수학 점수</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.9rem;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;"></th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;" colspan="3">OLS</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;" colspan="2">2SLS (전체)</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;" colspan="2">2SLS (±5)</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Wald (±3)</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>학급 규모</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+.322</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+.076</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+.019</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>−.230</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>−.261</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−.185</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−.443</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−.270</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(표준오차)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(.039)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(.036)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(.044)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(.092)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(.113)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(.151)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(.236)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(.281)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">통제변수</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">없음</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">%취약</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+등록</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">선형</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">2차</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">선형</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">2차</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">더미</td>
                </tr>
            </table>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>핵심 발견:</strong></p>
                <ul>
                    <li><strong>OLS:</strong> 양의 관계 (큰 학급 → 높은 점수) — 선택에 기인할 가능성 (좋은 학교가 큰 학급)</li>
                    <li><strong>OLS + 통제:</strong> 효과가 0 방향으로 축소</li>
                    <li><strong>2SLS:</strong> 강한 음의 효과 (−0.23 ~ −0.26) — 작은 학급이 점수 향상</li>
                    <li><strong>단절 표본:</strong> 덜 정밀하지만 비슷한 크기 (~−0.27)</li>
                </ul>
                <p style="margin-top: 0.5rem;"><strong>해석:</strong> 7명 학급 규모 감소(테네시 STAR와 같이)가 수학 점수를 ~1.75점 올림, 효과 크기 ≈ 0.18σ. 테네시 STAR 결과와 유사!</p>
            </div>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>정밀도 vs. 강건성 상충:</strong></p>
                <p>단절 표본을 줄이면 추정치가 덜 정밀해지지만(큰 표준오차) 함수 형태 가정에 대해 더 강건해짐. 추정치가 설정에 걸쳐 안정적(~−0.25)인 것이 안심됨.</p>
            </div>
        </div>
    </section>

    <!-- 요약 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Chapter 6 요약</h2>
        <div class="section-content">
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">개념</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">핵심 포인트</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>RD 핵심 아이디어</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">자의적 규칙이 자연실험 생성 — 실행변수의 기준점이 처치 결정</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Sharp RD</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">d<sub>i</sub> = 1(x<sub>i</sub> ≥ x<sub>0</sub>) 결정적; 관측변수에 의한 선택 이야기</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Fuzzy RD</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">P(d<sub>i</sub>=1)가 x<sub>0</sub>에서 점프; t<sub>i</sub>=1(x<sub>i</sub>≥x<sub>0</sub>)가 d<sub>i</sub>의 도구가 되는 IV 설정</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>식별</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">불연속적 점프(처치)와 매끄러운 추세(실행변수) 구별</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>함수 형태</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">E[y<sub>0</sub>|x] 모형화 필요 — 다항식 사용, 다른 기울기 허용, 또는 좁은 대역폭 집중</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>타당성 검정</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">처치 전 공변량 균형, 조작 없음(밀도 검정), 위약 기준점, 대역폭 민감도</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>LATE</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">RD 추정치는 x<sub>0</sub>에 국소적; fuzzy RD는 기준점 순응자의 LATE</td>
                </tr>
            </table>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>RD 실용적 체크리스트:</strong></p>
                <ol>
                    <li>✓ 처치 배정 규칙이 알려진 기준점에 기반하는지 확인</li>
                    <li>✓ 설계가 sharp인지 fuzzy인지 확인</li>
                    <li>✓ 결과 vs. 실행변수 그래프 — 가시적 점프 찾기</li>
                    <li>✓ 실행변수의 매끄러운 함수 통제(다항식)</li>
                    <li>✓ 기준점 양쪽에 다른 기울기 허용</li>
                    <li>✓ 기준점에서 처치 전 공변량 균형 검정</li>
                    <li>✓ 조작 검정(실행변수 밀도)</li>
                    <li>✓ 대역폭 변화 — 추정치가 안정적이어야</li>
                    <li>✓ Fuzzy RD의 경우: 1단계 강도 확인</li>
                </ol>
            </div>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Sharp vs. Fuzzy 요약:</strong></p>
                <table style="width:100%; border-collapse: collapse; margin: 0.5rem 0;">
                    <tr style="background: #e5e7eb;">
                        <th style="padding: 0.5rem; border: 1px solid #ddd;"></th>
                        <th style="padding: 0.5rem; border: 1px solid #ddd;">Sharp RD</th>
                        <th style="padding: 0.5rem; border: 1px solid #ddd;">Fuzzy RD</th>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">기준점에서 처치</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">확실히 0→1로 전환</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">확률이 증가</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">추정</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">다항식 통제와 OLS</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">2SLS (IV)</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">추정량</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">x<sub>0</sub>에서의 ATE</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">x<sub>0</sub> 순응자의 LATE</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">예시</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">Lee (2008) — 선거 승리</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">Angrist & Lavy (1999) — 학급 규모</td>
                    </tr>
                </table>
            </div>
        </div>
    </section>

    <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee; display: flex; justify-content: space-between;">
        <a href="/study/angrist-ch5-ko" style="color: #666;">← Ch 5: 고정효과 & DD</a>
        <a href="/study" style="color: #2563eb;">학습 노트로 →</a>
    </div>

    <div style="margin-top: 2rem; padding: 1rem; background: #f9fafb; border-radius: 8px; font-size: 0.8rem; color: #6b7280;">
        <em>이 노트는 LLM (Claude)의 도움을 받아 작성되었습니다.</em>
    </div>
</div>
