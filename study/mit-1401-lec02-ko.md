---
layout: minimal_base
title: "MIT 14.01 Lec 2: 선호와 효용함수"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Lecture 2: 선호와 효용함수</h2>
            <a href="/study/mit-1401-lec02" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">English</a>
        </div>
        <div class="section-content">
            <p><em>MIT 14.01 Principles of Microeconomics | Fall 2023 | Prof. Jonathan Gruber</em></p>
        </div>
    </section>

    <!-- Core Message -->
    <section class="section fade-in-delay">
        <h2 class="section-title">핵심 메시지</h2>
        <div class="section-content">
            <blockquote style="border-left: 4px solid #2563eb; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                "효용은 오직 서수적(ordinal) 의미로만 중요하다 — 선택지의 순위를 매기는 것."
            </blockquote>
            <p>소비자 수요는 세 단계로 도출: (1) 선호 공리 → (2) 효용함수 → (3) 예산제약. 이번 강의는 처음 두 단계를 다룸.</p>
        </div>
    </section>

    <!-- Roadmap -->
    <section class="section fade-in-delay">
        <h2 class="section-title">소비자 수요 도출 로드맵</h2>
        <div class="section-content">
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <ul>
                    <li><strong>Step 1:</strong> 소비자 선호의 공리 (오늘)</li>
                    <li><strong>Step 2:</strong> 공리를 효용함수로 변환 (오늘)</li>
                    <li><strong>Step 3:</strong> 예산제약 도입 → 수요 도출 (다음 강의)</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- 1. Assumptions on Preferences -->
    <section class="section fade-in-delay">
        <h2 class="section-title">1. 선호에 관한 세 가지 핵심 가정</h2>
        <div class="section-content">
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">가정</th>
                    <th style="padding: 0.75rem; text-align: left;">의미</th>
                    <th style="padding: 0.75rem; text-align: left;">함의</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">완비성 (Completeness)</td>
                    <td style="padding: 0.75rem;">두 선택지가 주어지면, 하나를 선호하거나, 다른 것을 선호하거나, 무차별</td>
                    <td style="padding: 0.75rem;">"모르겠어" 불가 — 소비자는 항상 의견이 있음</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">이행성 (Transitivity)</td>
                    <td style="padding: 0.75rem;">A ≻ B이고 B ≻ C이면, A ≻ C</td>
                    <td style="padding: 0.75rem;">표준적인 수학적 가정</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; font-weight: 600;">비포만성 (Non-satiation)</td>
                    <td style="padding: 0.75rem;">많을수록 좋다</td>
                    <td style="padding: 0.75rem;">무료로 제공하면 항상 받음</td>
                </tr>
            </table>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>비포만성에 대한 주의:</strong></p>
                <ul>
                    <li>10번째 단위가 9번째만큼 행복하게 한다는 뜻이 아님</li>
                    <li>단지 10번째 단위가 없는 것보다는 낫다는 것</li>
                    <li>"재화(goods)"에 적용 — 원하는 것 (눈 찔리기 같은 "비재화"가 아님)</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- 2. Indifference Curves -->
    <section class="section fade-in-delay">
        <h2 class="section-title">2. 무차별곡선</h2>
        <div class="section-content">
            <p><strong>정의:</strong> 소비자에게 동일한 만족(효용)을 주는 모든 재화 조합을 연결한 곡선.</p>

            <h4>예시: 피자와 쿠키</h4>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <ul>
                    <li><strong>선택 A:</strong> 피자 2조각, 쿠키 1개</li>
                    <li><strong>선택 B:</strong> 피자 1조각, 쿠키 2개</li>
                    <li><strong>선택 C:</strong> 피자 2조각, 쿠키 2개</li>
                </ul>
                <p>A와 B에 무차별하지만 C를 둘 다보다 선호 → A와 B는 같은 무차별곡선, C는 더 높은 곡선에 위치.</p>
            </div>

            <h4>무차별곡선의 네 가지 속성</h4>
            
            <!-- Property 1 -->
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0; border-left: 4px solid #2563eb;">
                <p style="font-weight: 600; color: #1e40af; margin-bottom: 0.5rem;">속성 1: 높은 IC가 선호됨</p>
                <p><strong>이유:</strong> 비포만성 (많을수록 좋다)</p>
                <p>IC₂가 IC₁보다 원점에서 멀리 있음 → 피자도 많고 쿠키도 많음 → IC₂가 선호됨.</p>
            </div>

            <!-- Property 2 -->
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0; border-left: 4px solid #2563eb;">
                <p style="font-weight: 600; color: #1e40af; margin-bottom: 0.5rem;">속성 2: IC는 우하향함</p>
                <p><strong>이유:</strong> 비포만성 (적은 것과 많은 것에 무차별할 수 없음)</p>
                <div style="background: #fef2f2; padding: 0.75rem; border-radius: 4px; margin: 0.5rem 0;">
                    <p><strong>귀류법 — 만약 IC가 우상향한다면:</strong></p>
                    <p>A점 (피자 1, 쿠키 1)과 B점 (피자 3, 쿠키 3)이 같은 IC 위에 있게 됨.</p>
                    <p>→ A와 B에 무차별하다는 뜻.</p>
                    <p>→ 하지만 B는 모든 것이 더 많다! 어떻게 무차별할 수 있나? <strong>모순!</strong></p>
                </div>
                <p>따라서 쿠키를 얻으면서 무차별하려면 피자를 포기해야 함 → IC는 우하향.</p>
            </div>

            <!-- Property 3 -->
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0; border-left: 4px solid #2563eb;">
                <p style="font-weight: 600; color: #1e40af; margin-bottom: 0.5rem;">속성 3: IC는 절대 교차하지 않음</p>
                <p><strong>이유:</strong> 이행성 + 비포만성</p>
                <div style="background: #fef2f2; padding: 0.75rem; border-radius: 4px; margin: 0.5rem 0;">
                    <p><strong>귀류법 — 만약 두 IC가 A점에서 교차한다면:</strong></p>
                    <ul>
                        <li>A와 B가 IC₁ 위 → A ~ B (무차별)</li>
                        <li>A와 C가 IC₂ 위 → A ~ C (무차별)</li>
                        <li>이행성에 의해: B ~ C</li>
                    </ul>
                    <p><strong>하지만!</strong> B가 C보다 피자가 많고 쿠키는 같다면 → 비포만성에 의해 B ≻ C.</p>
                    <p>B ~ C 이면서 B ≻ C? <strong>모순!</strong></p>
                </div>
                <p>따라서 무차별곡선은 절대 교차할 수 없음.</p>
            </div>

            <!-- Property 4 -->
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0; border-left: 4px solid #2563eb;">
                <p style="font-weight: 600; color: #1e40af; margin-bottom: 0.5rem;">속성 4: 각 점에는 하나의 IC만 지나감</p>
                <p><strong>이유:</strong> 완비성 (자신의 느낌을 알아야 함)</p>
                <div style="background: #fef2f2; padding: 0.75rem; border-radius: 4px; margin: 0.5rem 0;">
                    <p><strong>만약 두 IC가 A점을 지나간다면:</strong></p>
                    <ul>
                        <li>IC₁ 위: 묶음 A가 효용 수준 U₁을 줌</li>
                        <li>IC₂ 위: 묶음 A가 효용 수준 U₂을 줌</li>
                    </ul>
                    <p>같은 묶음, 두 가지 다른 효용 수준? → A에 대해 어떻게 느끼는지 모르는 것.</p>
                    <p>이는 <strong>완비성</strong>을 위반 — 항상 묶음들의 순위를 매길 수 있어야 함!</p>
                </div>
                <p>따라서 각 점을 정확히 하나의 IC만 지나감.</p>
            </div>

            <h4>요약 표</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">#</th>
                    <th style="padding: 0.75rem; text-align: left;">속성</th>
                    <th style="padding: 0.75rem; text-align: left;">핵심 직관</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">1</td>
                    <td style="padding: 0.75rem;">높은 IC가 선호됨</td>
                    <td style="padding: 0.75rem;">많을수록 좋다</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">2</td>
                    <td style="padding: 0.75rem;">우하향</td>
                    <td style="padding: 0.75rem;">한 재화를 얻으려면 다른 것을 포기해야 무차별 유지</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">3</td>
                    <td style="padding: 0.75rem;">교차하지 않음</td>
                    <td style="padding: 0.75rem;">교차하면 "B~A~C 그러나 B≻C" 모순 발생</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem;">4</td>
                    <td style="padding: 0.75rem;">점당 하나의 IC</td>
                    <td style="padding: 0.75rem;">각 묶음은 정확히 하나의 만족 수준을 가짐</td>
                </tr>
            </table>

            <h4>실제 예시: 직업 선택</h4>
            <div style="background: #f5f5f5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p>두 차원으로 직업을 선택하는 대학원생:</p>
                <ul>
                    <li><strong>X축:</strong> 날씨 품질</li>
                    <li><strong>Y축:</strong> 학교/직장 품질</li>
                </ul>
                <p><strong>선택지:</strong> Princeton (훌륭한 품질, 보통 날씨) vs. Santa Cruz (좋은 품질, 훌륭한 날씨)</p>
                <p><strong>결정:</strong> IMF (DC) 선택 — Princeton보다 좋은 날씨, Santa Cruz보다 좋은 직장</p>
                <p><em>참고: "정답"은 없음 — 선호는 개인적인 것.</em></p>
            </div>
        </div>
    </section>

    <!-- 3. Utility Functions -->
    <section class="section fade-in-delay">
        <h2 class="section-title">3. 효용함수</h2>
        <div class="section-content">
            <p><strong>정의:</strong> 선호를 수학적으로 표현하여 각 재화 묶음에 숫자를 부여하는 것.</p>
            <p>핵심 아이디어: <strong>무차별곡선을 수식으로 표현!</strong></p>

            <h4>예시: 제곱근 효용</h4>
            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p style="font-family: monospace; font-size: 1.1rem; text-align: center;">U = √(S × C)</p>
                <p style="text-align: center;">S = 피자 조각, C = 쿠키</p>
            </div>

            <p><strong>검증:</strong></p>
            <ul>
                <li>U(2, 1) = √2 ≈ 1.41</li>
                <li>U(1, 2) = √2 ≈ 1.41 → A와 B에 무차별 ✓</li>
                <li>U(2, 2) = 2 → C를 선호 ✓</li>
            </ul>

            <h4>왜 √ 형태를 쓰나?</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0; border-left: 4px solid #2563eb;">
                <p><strong>학생 질문:</strong> "U = S × C도 같은 순위를 줌. 왜 √를 쓰나요?"</p>
                <p><strong>답:</strong> 다른 형태는 다른 속성을 가짐:</p>
                <table style="width:100%; border-collapse: collapse; margin: 0.5rem 0;">
                    <tr style="border-bottom: 1px solid #e5e7eb;">
                        <td style="padding: 0.5rem; font-family: monospace;">U = S × C</td>
                        <td style="padding: 0.5rem;">한계효용이 일정</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #e5e7eb;">
                        <td style="padding: 0.5rem; font-family: monospace;">U = √(S × C)</td>
                        <td style="padding: 0.5rem;">한계효용이 <strong>체감</strong> ✓</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; font-family: monospace;">U = (S × C)²</td>
                        <td style="padding: 0.5rem;">한계효용이 체증</td>
                    </tr>
                </table>
                <p>세 가지 모두 같은 <strong>순위</strong>를 주지만, √는 현실을 반영: 10번째 조각은 1번째만큼 만족스럽지 않음.</p>
            </div>

            <h4>핵심 통찰: 서수적, 기수적이 아님</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>효용은 순위 매기기에만 의미 있고, 절대적 행복 측정이 아님.</strong></p>
                
                <table style="width:100%; border-collapse: collapse; margin: 0.5rem 0;">
                    <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                        <th style="padding: 0.5rem; text-align: left;"></th>
                        <th style="padding: 0.5rem; text-align: left;">기수적 (틀림)</th>
                        <th style="padding: 0.5rem; text-align: left;">서수적 (맞음)</th>
                    </tr>
                    <tr style="border-bottom: 1px solid #e5e7eb;">
                        <td style="padding: 0.5rem; font-weight: 600;">의미</td>
                        <td style="padding: 0.5rem;">숫자가 절대적 의미를 가짐</td>
                        <td style="padding: 0.5rem;">순서만 중요</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #e5e7eb;">
                        <td style="padding: 0.5rem; font-weight: 600;">예시</td>
                        <td style="padding: 0.5rem;">온도 (30°C = 2×15°C)</td>
                        <td style="padding: 0.5rem;">영화 순위 (1위 > 2위)</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; font-weight: 600;">효용</td>
                        <td style="padding: 0.5rem;">"U=6은 U=3보다 2배 행복" ❌</td>
                        <td style="padding: 0.5rem;">"U=6 > U=3이므로 선호" ✓</td>
                    </tr>
                </table>

                <p style="margin-top: 0.5rem;"><strong>핵심:</strong> U = S×C, U = √(S×C), U = ln(S×C) 모두 같은 순위 → 같은 선호에 대한 유효한 효용함수.</p>
            </div>

            <h4>같은 순위 확인</h4>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p>묶음 (2,3) vs (3,2) 비교:</p>
                <table style="width:100%; border-collapse: collapse; margin: 0.5rem 0;">
                    <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                        <th style="padding: 0.5rem;">효용함수</th>
                        <th style="padding: 0.5rem;">U(2,3)</th>
                        <th style="padding: 0.5rem;">U(3,2)</th>
                        <th style="padding: 0.5rem;">선호?</th>
                    </tr>
                    <tr style="border-bottom: 1px solid #e5e7eb;">
                        <td style="padding: 0.5rem; font-family: monospace;">S × C</td>
                        <td style="padding: 0.5rem;">6</td>
                        <td style="padding: 0.5rem;">6</td>
                        <td style="padding: 0.5rem;">무차별</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #e5e7eb;">
                        <td style="padding: 0.5rem; font-family: monospace;">√(S × C)</td>
                        <td style="padding: 0.5rem;">2.45</td>
                        <td style="padding: 0.5rem;">2.45</td>
                        <td style="padding: 0.5rem;">무차별</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; font-family: monospace;">(S × C)²</td>
                        <td style="padding: 0.5rem;">36</td>
                        <td style="padding: 0.5rem;">36</td>
                        <td style="padding: 0.5rem;">무차별</td>
                    </tr>
                </table>
                <p><strong>숫자는 다르지만 순위는 동일!</strong></p>
            </div>
        </div>
    </section>

    <!-- 4. Marginal Utility -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4. 한계효용과 체감하는 한계효용</h2>
        <div class="section-content">
            
            <h4>한계효용이란?</h4>
            <p><strong>정의:</strong> 재화를 <strong>한 단위 더</strong> 소비할 때 얻는 추가 효용.</p>
            
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>총효용 vs 한계효용:</strong></p>
                <ul>
                    <li><strong>U(3)</strong> = 3단위로부터의 총 만족</li>
                    <li><strong>MU(3)</strong> = 3번째 단위로부터의 추가 만족 = U(3) - U(2)</li>
                </ul>
            </div>

            <h4>수학적 유도</h4>
            <p>U = √(S × C)에서 편미분 사용:</p>
            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p style="font-family: monospace; text-align: center;">
                    MU<sub>C</sub> = ∂U/∂C = S / (2√(S×C))
                </p>
                <p style="font-family: monospace; text-align: center;">
                    MU<sub>S</sub> = ∂U/∂S = C / (2√(S×C))
                </p>
            </div>

            <h4>∂U/∂C가 무슨 뜻인가?</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0; border-left: 4px solid #10b981;">
                <p><strong>편미분</strong> = "다른 변수를 상수로 두고, U가 C에 따라 어떻게 변하는가?"</p>
                <ul>
                    <li>일반 미분 (d/dx): 변수 1개만</li>
                    <li>편미분 (∂/∂x): 여러 변수, 나머지는 상수 취급</li>
                </ul>
                <p>∂ 기호 (d 대신)는: <strong>S를 상수로 취급</strong>한 후 C에 대해 미분한다는 뜻.</p>
                <p style="margin-top: 0.5rem;"><strong>MU<sub>C</sub></strong> = "피자를 고정하고 쿠키를 하나 더 먹으면 얼마나 더 행복해지나?"</p>
            </div>

            <h4>단계별 계산</h4>
            <div style="background: #f5f5f5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p style="font-family: monospace;">
                    U = (S × C)<sup>1/2</sup><br><br>
                    S를 상수로 취급하고 C에 대해 미분:<br><br>
                    ∂U/∂C = (1/2) × S<sup>1/2</sup> × C<sup>-1/2</sup><br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= (1/2) × √S / √C<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= (1/2) × √(S/C)<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= S / (2√(S×C))
                </p>
            </div>

            <h4>체감하는 한계효용 ⭐</h4>
            <blockquote style="border-left: 4px solid #2563eb; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                "많을수록 좋지만, 다음 단위는 이전 것만큼 좋지는 않다."
            </blockquote>

            <div style="background: #f0fdf4; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>직관적 예시 — 배고픔:</strong></p>
<pre style="font-family: monospace; margin: 0.5rem 0; background: #fff; padding: 0.5rem; border-radius: 4px;">
하루 종일 못 먹었는데 피자가 왔다!

1번째 조각: "최고!!!"       → MU = 😍😍😍😍😍 (5)
2번째 조각: "여전히 좋아"   → MU = 😍😍😍😍 (4)
3번째 조각: "꽤 괜찮아"     → MU = 😍😍😍 (3)
4번째 조각: "배부르다"      → MU = 😍😍 (2)
5번째 조각: "더 못 먹겠어"  → MU = 😍 (1)
</pre>
                <p><strong>핵심:</strong> 총효용은 계속 증가 (5조각 > 4조각), 하지만 한계효용은 감소.</p>
            </div>

            <h4>수치 예시: 피자를 2조각으로 고정</h4>
            <p>MU<sub>C</sub> = S / (2√(S×C))이고 S = 2일 때:</p>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: center;">쿠키 (C)</th>
                    <th style="padding: 0.75rem; text-align: center;">√(S×C)</th>
                    <th style="padding: 0.75rem; text-align: center;">효용</th>
                    <th style="padding: 0.75rem; text-align: center;">MU<sub>C</sub></th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">1</td>
                    <td style="padding: 0.75rem; text-align: center;">√2 ≈ 1.41</td>
                    <td style="padding: 0.75rem; text-align: center;">1.41</td>
                    <td style="padding: 0.75rem; text-align: center;">0.71</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">2</td>
                    <td style="padding: 0.75rem; text-align: center;">√4 = 2.00</td>
                    <td style="padding: 0.75rem; text-align: center;">2.00</td>
                    <td style="padding: 0.75rem; text-align: center;">0.50</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">3</td>
                    <td style="padding: 0.75rem; text-align: center;">√6 ≈ 2.45</td>
                    <td style="padding: 0.75rem; text-align: center;">2.45</td>
                    <td style="padding: 0.75rem; text-align: center;">0.41</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; text-align: center;">4</td>
                    <td style="padding: 0.75rem; text-align: center;">√8 ≈ 2.83</td>
                    <td style="padding: 0.75rem; text-align: center;">2.83</td>
                    <td style="padding: 0.75rem; text-align: center;">0.35</td>
                </tr>
            </table>
            <p style="text-align: center; color: #6b7280;">쿠키가 증가하면 효용↑ 하지만 MU↓ → <strong>체감하는 한계효용</strong></p>

            <h4>중요한 구분</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">개념</th>
                    <th style="padding: 0.75rem; text-align: left;">수량↑ 시</th>
                    <th style="padding: 0.75rem; text-align: left;">이유</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">효용 (U)</td>
                    <td style="padding: 0.75rem;">증가 ↑</td>
                    <td style="padding: 0.75rem;">비포만성 (많을수록 좋다)</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; font-weight: 600;">한계효용 (MU)</td>
                    <td style="padding: 0.75rem;">감소 ↓</td>
                    <td style="padding: 0.75rem;">수확체감</td>
                </tr>
            </table>
            <p><strong>이 둘은 모순이 아님!</strong> 6번째 조각도 여전히 행복을 더함 (U↑), 단지 5번째만큼은 아님 (MU↓).</p>
        </div>
    </section>

    <!-- 5. Marginal Rate of Substitution -->
    <section class="section fade-in-delay">
        <h2 class="section-title">5. 한계대체율 (MRS)</h2>
        <div class="section-content">
            <h4>정의</h4>
            <p><strong>동일한 효용 수준을 유지</strong>하면서 한 재화를 다른 재화로 교환하려는 비율.</p>
            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p style="font-family: monospace; font-size: 1.1rem; text-align: center;">
                    MRS = ΔS/ΔC = −MU<sub>C</sub>/MU<sub>S</sub>
                </p>
                <p style="text-align: center;">= 무차별곡선의 기울기 = 한계효용의 비율</p>
            </div>

            <h4>유도: 왜 MRS = −MU<sub>C</sub>/MU<sub>S</sub>인가?</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0; border-left: 4px solid #2563eb;">
                <p><strong>핵심 아이디어:</strong> IC를 따라 이동하면 효용이 변하지 않음 (ΔU = 0)</p>
                
                <p style="margin-top: 1rem;"><strong>Step 1:</strong> 두 재화를 모두 바꿀 때 총 효용 변화:</p>
                <p style="font-family: monospace; padding-left: 1rem;">ΔU = (ΔS × MU<sub>S</sub>) + (ΔC × MU<sub>C</sub>)</p>
                <p style="padding-left: 1rem; font-size: 0.9rem; color: #666;">= (피자 변화 × 피자당 효용) + (쿠키 변화 × 쿠키당 효용)</p>
                
                <p style="margin-top: 1rem;"><strong>Step 2:</strong> IC 위에서는 효용이 변하지 않음:</p>
                <p style="font-family: monospace; padding-left: 1rem;">ΔU = 0</p>
                <p style="font-family: monospace; padding-left: 1rem;">∴ ΔS × MU<sub>S</sub> + ΔC × MU<sub>C</sub> = 0</p>
                
                <p style="margin-top: 1rem;"><strong>Step 3:</strong> ΔS/ΔC 구하기:</p>
                <p style="font-family: monospace; padding-left: 1rem;">ΔS × MU<sub>S</sub> = −ΔC × MU<sub>C</sub></p>
                <p style="font-family: monospace; padding-left: 1rem;">ΔS/ΔC = −MU<sub>C</sub>/MU<sub>S</sub></p>
                
                <p style="margin-top: 1rem;"><strong>결과:</strong></p>
                <p style="font-family: monospace; padding-left: 1rem; font-size: 1.1rem;"><strong>MRS = −MU<sub>C</sub>/MU<sub>S</sub></strong></p>
            </div>

            <h4>U = √(S × C)일 때:</h4>
            <div style="background: #faf5ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p style="font-family: monospace;">MRS = −MU<sub>C</sub>/MU<sub>S</sub> = −[S/(2√SC)] / [C/(2√SC)] = <strong>−S/C</strong></p>
            </div>

            <h4>예시: 무차별곡선 위의 세 점 (U = 2)</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: center;">점</th>
                    <th style="padding: 0.75rem; text-align: center;">피자 (S)</th>
                    <th style="padding: 0.75rem; text-align: center;">쿠키 (C)</th>
                    <th style="padding: 0.75rem; text-align: center;">MRS = −S/C</th>
                    <th style="padding: 0.75rem; text-align: left;">해석</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">A</td>
                    <td style="padding: 0.75rem; text-align: center;">4</td>
                    <td style="padding: 0.75rem; text-align: center;">1</td>
                    <td style="padding: 0.75rem; text-align: center;">−4</td>
                    <td style="padding: 0.75rem;">쿠키 1개에 피자 4개 포기 가능 (쿠키가 정말 필요!)</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">B</td>
                    <td style="padding: 0.75rem; text-align: center;">2</td>
                    <td style="padding: 0.75rem; text-align: center;">2</td>
                    <td style="padding: 0.75rem; text-align: center;">−1</td>
                    <td style="padding: 0.75rem;">무차별: 피자 1개 = 쿠키 1개</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; text-align: center;">C</td>
                    <td style="padding: 0.75rem; text-align: center;">1</td>
                    <td style="padding: 0.75rem; text-align: center;">4</td>
                    <td style="padding: 0.75rem; text-align: center;">−1/4</td>
                    <td style="padding: 0.75rem;">쿠키 1개에 피자 1/4만 포기 (피자가 정말 필요!)</td>
                </tr>
            </table>

            <h4>체감하는 MRS: 왜 IC가 볼록한가</h4>
            <div style="background: #f0fdf4; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>A → B → C로 이동하면:</strong></p>
                <ul>
                    <li>피자 감소 (4 → 2 → 1) → 피자가 더 귀해짐</li>
                    <li>쿠키 증가 (1 → 2 → 4) → 쿠키가 덜 귀해짐</li>
                    <li>|MRS| 감소 (4 → 1 → 0.25) → 쿠키를 위해 피자를 덜 포기하려 함</li>
                </ul>
                <p style="margin-top: 0.5rem;"><strong>이것이 무차별곡선이 원점에 대해 볼록한 이유!</strong></p>
            </div>

            <h4>체감하는 MU vs 체감하는 MRS</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">개념</th>
                    <th style="padding: 0.75rem; text-align: left;">의미</th>
                    <th style="padding: 0.75rem; text-align: left;">관계</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">체감하는 MU</td>
                    <td style="padding: 0.75rem;">같은 재화를 더 많이 → 추가 만족 감소</td>
                    <td style="padding: 0.75rem;">원인</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; font-weight: 600;">체감하는 MRS</td>
                    <td style="padding: 0.75rem;">한 재화가 많아지면 → 다른 재화로 교환 의향 감소</td>
                    <td style="padding: 0.75rem;">결과</td>
                </tr>
            </table>
            <p><strong>연결:</strong> C↑이면 MU<sub>C</sub>↓이고 MU<sub>S</sub>↑ → MRS = −MU<sub>C</sub>/MU<sub>S</sub> → |MRS|↓</p>
        </div>
    </section>

    <!-- 6. Concave IC -->
    <section class="section fade-in-delay">
        <h2 class="section-title">6. 왜 오목한 무차별곡선은 안 되나?</h2>
        <div class="section-content">
            <p>U = S² + C² = 65 (원점에 대해 오목) 고려</p>
            
            <div style="background: #fef2f2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>문제점:</strong></p>
                <ul>
                    <li>(피자 8, 쿠키 1): MRS = −1/8 → 피자를 쿠키로 거의 안 바꾸려 함</li>
                    <li>(피자 4, 쿠키 7): MRS = −7/4 → 쿠키 1개에 피자 거의 2개 포기</li>
                </ul>
                <p><strong>말이 안 됨!</strong> 왜 피자가 더 적을 때 피자를 더 많이 포기하나?</p>
            </div>

            <p><strong>결론:</strong> 수학적으로는 가능하지만, 오목한 IC는 일반적인 인간 선호를 대표하지 않음. 볼록한 IC (체감하는 MRS)를 표준으로 가정.</p>
        </div>
    </section>

    <!-- 7. Real-World Application -->
    <section class="section fade-in-delay">
        <h2 class="section-title">7. 실제 적용: 음료 사이즈</h2>
        <div class="section-content">
            <h4>체감하는 한계효용의 증거</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">회사</th>
                    <th style="padding: 0.75rem; text-align: center;">Small</th>
                    <th style="padding: 0.75rem; text-align: center;">Large</th>
                    <th style="padding: 0.75rem; text-align: center;">가격 차이</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">Starbucks (아이스 커피)</td>
                    <td style="padding: 0.75rem; text-align: center;">$4.55</td>
                    <td style="padding: 0.75rem; text-align: center;">$5.45</td>
                    <td style="padding: 0.75rem; text-align: center;">2배 양에 $0.90 추가</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem;">McDonald's (콜라)</td>
                    <td style="padding: 0.75rem; text-align: center;">$2.29</td>
                    <td style="padding: 0.75rem; text-align: center;">$2.99</td>
                    <td style="padding: 0.75rem; text-align: center;">2배 양에 $0.70 추가</td>
                </tr>
            </table>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>왜?</strong></p>
                <ul>
                    <li>첫 16 oz가 갈증의 대부분을 해결</li>
                    <li>추가 16 oz는 좋지만 그만큼 가치 있지는 않음</li>
                    <li>회사들은 소비자가 큰 사이즈에 비례적으로 더 내지 않을 것을 앎</li>
                    <li>McDonald's 원가: ~$0.03 (small) vs ~$0.04 (large)</li>
                </ul>
                <p><strong>비즈니스 함의:</strong> 회사들은 체감하는 MRS에 기반해 가격 책정 — 선호가 볼록하다고 믿는 증거!</p>
            </div>
        </div>
    </section>

    <!-- Key Takeaways -->
    <section class="section fade-in-delay">
        <h2 class="section-title">핵심 요약</h2>
        <div class="section-content">
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: center; width: 5%;">#</th>
                    <th style="padding: 0.75rem; text-align: left; width: 30%;">개념</th>
                    <th style="padding: 0.75rem; text-align: left;">핵심 포인트</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">1</td>
                    <td style="padding: 0.75rem; font-weight: 600;">세 가지 공리</td>
                    <td style="padding: 0.75rem;">완비성, 이행성, 비포만성</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">2</td>
                    <td style="padding: 0.75rem; font-weight: 600;">무차별곡선</td>
                    <td style="padding: 0.75rem;">우하향, 교차 안 함, 원점에 대해 볼록</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">3</td>
                    <td style="padding: 0.75rem; font-weight: 600;">효용함수</td>
                    <td style="padding: 0.75rem;">수학적 표현; 서수적, 기수적 아님</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">4</td>
                    <td style="padding: 0.75rem; font-weight: 600;">체감하는 MU</td>
                    <td style="padding: 0.75rem;">추가 단위마다 덜 만족</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; text-align: center;">5</td>
                    <td style="padding: 0.75rem; font-weight: 600;">MRS</td>
                    <td style="padding: 0.75rem;">IC 기울기 = −MU<sub>C</sub>/MU<sub>S</sub>; 곡선을 따라 체감</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- Key Terms -->
    <section class="section fade-in-delay">
        <h2 class="section-title">핵심 용어</h2>
        <div class="section-content">
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">용어</th>
                    <th style="padding: 0.75rem; text-align: left;">정의</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">완비성 (Completeness)</td>
                    <td style="padding: 0.75rem;">소비자는 항상 두 묶음의 순위를 매길 수 있음</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">이행성 (Transitivity)</td>
                    <td style="padding: 0.75rem;">A ≻ B이고 B ≻ C이면, A ≻ C</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">비포만성 (Non-satiation)</td>
                    <td style="padding: 0.75rem;">많을수록 좋다</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">무차별곡선 (Indifference Curve)</td>
                    <td style="padding: 0.75rem;">동일한 효용을 주는 묶음들의 궤적</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">효용함수 (Utility Function)</td>
                    <td style="padding: 0.75rem;">선호의 수학적 표현</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">한계효용 (MU)</td>
                    <td style="padding: 0.75rem;">한 단위 추가로부터의 추가 효용</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">체감하는 MU</td>
                    <td style="padding: 0.75rem;">수량이 증가하면 MU가 감소</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem;">한계대체율 (MRS)</td>
                    <td style="padding: 0.75rem;">IC 위에서 재화 간 교환 비율; IC의 기울기</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- Footer -->
    <section class="section fade-in-delay">
        <div class="section-content" style="text-align: center; color: #6b7280; font-size: 0.9rem;">
            <p><em>Last updated: 2025-01-05</em></p>
            <p><a href="/study/mit-1401-overview-ko">← 코스 개요로 돌아가기</a></p>
        </div>
    </section>
</div>
