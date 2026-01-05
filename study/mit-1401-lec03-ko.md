---
layout: minimal_base
title: "MIT 14.01 Lec 3: 예산제약과 제약 하 선택"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Lecture 3: 예산제약과 제약 하 선택</h2>
            <a href="/study/mit-1401-lec03" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">English</a>
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
                "지난 시간에는 돈을 원하는 만큼 가질 수 있게 했습니다. 오늘은 나쁜 소식입니다. 오늘 예산제약을 부과합니다."
            </blockquote>
            <p>소비자 최적화는 <strong>무차별곡선이 예산제약에 접하는 곳</strong>에서 발생. 이 점에서 MRS = MRT.</p>
        </div>
    </section>

    <!-- Roadmap -->
    <section class="section fade-in-delay">
        <h2 class="section-title">소비자 이론 진행 상황</h2>
        <div class="section-content">
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <table style="width:100%; border-collapse: collapse;">
                    <tr style="border-bottom: 1px solid #e5e7eb;">
                        <td style="padding: 0.5rem; font-weight: 600;">Step 1 (Lec 2)</td>
                        <td style="padding: 0.5rem;">선호 → 효용함수 → 무차별곡선</td>
                        <td style="padding: 0.5rem; color: #10b981;">✓ 완료</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #e5e7eb;">
                        <td style="padding: 0.5rem; font-weight: 600;">Step 2 (Lec 3)</td>
                        <td style="padding: 0.5rem;">예산제약 → 제약 하 선택</td>
                        <td style="padding: 0.5rem; color: #2563eb;">← 오늘</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; font-weight: 600;">Step 3 (Lec 4)</td>
                        <td style="padding: 0.5rem;">수요곡선 도출</td>
                        <td style="padding: 0.5rem; color: #9ca3af;">다음</td>
                    </tr>
                </table>
            </div>
        </div>
    </section>

    <!-- 1. Budget Constraint -->
    <section class="section fade-in-delay">
        <h2 class="section-title">1. 예산제약</h2>
        <div class="section-content">
            
            <h4>핵심 가정: 저축이나 차입 없음</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p style="font-family: monospace; font-size: 1.1rem; text-align: center;">
                    예산 = 소득
                </p>
                <p>소득을 <strong>모두</strong> 소비재에 지출. 저축 없음, 차입 없음.</p>
                <p><em>"슬프게도, 이것은 미국인들에게 나쁜 근사가 아닙니다. 평균적인 미국인은 가용 저축이 $1,000 미만입니다."</em></p>
            </div>

            <h4>예산제약 방정식</h4>
            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p style="font-family: monospace; font-size: 1.1rem; text-align: center;">
                    Y = P<sub>C</sub> × C + P<sub>S</sub> × S
                </p>
            </div>
            
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.5rem; font-weight: 600; width: 20%;">Y</td>
                    <td style="padding: 0.5rem;">당신의 소득 (주어진 값)</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.5rem; font-weight: 600;">P<sub>C</sub> × C</td>
                    <td style="padding: 0.5rem;">쿠키 총 지출 = (쿠키 개당 가격) × (쿠키 개수)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; font-weight: 600;">P<sub>S</sub> × S</td>
                    <td style="padding: 0.5rem;">피자 총 지출 = (피자 조각당 가격) × (피자 조각 수)</td>
                </tr>
            </table>

            <h4>수치 예시</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">파라미터</th>
                    <th style="padding: 0.75rem; text-align: left;">값</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">소득 (Y)</td>
                    <td style="padding: 0.75rem;">$24</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">쿠키 가격 (P<sub>C</sub>)</td>
                    <td style="padding: 0.75rem;">$2</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">피자 가격 (P<sub>S</sub>)</td>
                    <td style="padding: 0.75rem;">$4</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">X절편 (쿠키만)</td>
                    <td style="padding: 0.75rem;">Y/P<sub>C</sub> = 24/2 = 12개</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">Y절편 (피자만)</td>
                    <td style="padding: 0.75rem;">Y/P<sub>S</sub> = 24/4 = 6조각</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem;">기울기</td>
                    <td style="padding: 0.75rem;">−P<sub>C</sub>/P<sub>S</sub> = −2/4 = −1/2</td>
                </tr>
            </table>

            <h4>기회집합 (Opportunity Set)</h4>
            <div style="background: #f0fdf4; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>정의:</strong> 예산제약 <strong>아래</strong> 영역은 모든 구매 가능한 조합을 나타냄.</p>
                <p><strong>Q:</strong> "모든 소득을 쓴다고 가정하면, 왜 선 아래 영역을 보나요?"</p>
                <p><strong>A:</strong> 항상 선 위에 <em>있을</em> 것임. 하지만 기회집합이 중요한 이유는 축소되면 선택지가 줄어듦 → 더 나빠짐.</p>
            </div>
        </div>
    </section>

    <!-- 2. Marginal Rate of Transformation -->
    <section class="section fade-in-delay">
        <h2 class="section-title">2. 한계전환율 (MRT)</h2>
        <div class="section-content">
            
            <h4>정의</h4>
            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p style="font-family: monospace; font-size: 1.1rem; text-align: center;">
                    MRT = −P<sub>C</sub>/P<sub>S</sub> = 예산제약의 기울기
                </p>
            </div>
            
            <p><strong>시장을 통해</strong> 한 재화를 다른 재화로 <strong>전환</strong>할 수 있는 비율.</p>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"이 수업은 연금술에 관한 것이 아닙니다. 쿠키를 피자로 바꾸는 법을 가르치지 않습니다."</em></p>
                <p style="margin-top: 0.5rem;">하지만 가격과 소득이 주어지면, <strong>기회비용</strong>은:</p>
                <ul>
                    <li>쿠키 1개 구매 = 피자 1/2조각을 <strong>못</strong> 사는 것</li>
                    <li>피자 1조각 구매 = 쿠키 2개를 <strong>못</strong> 사는 것</li>
                </ul>
            </div>

            <h4>MRS vs MRT: 핵심 구분</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">개념</th>
                    <th style="padding: 0.75rem; text-align: left;">공식</th>
                    <th style="padding: 0.75rem; text-align: left;">의미</th>
                    <th style="padding: 0.75rem; text-align: left;">결정 요인</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">MRS</td>
                    <td style="padding: 0.75rem;">−MU<sub>C</sub>/MU<sub>S</sub></td>
                    <td style="padding: 0.75rem;">교환<strong>하려는</strong> 비율</td>
                    <td style="padding: 0.75rem;">당신의 선호 (내적)</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; font-weight: 600;">MRT</td>
                    <td style="padding: 0.75rem;">−P<sub>C</sub>/P<sub>S</sub></td>
                    <td style="padding: 0.75rem;">교환<strong>할 수 있는</strong> 비율</td>
                    <td style="padding: 0.75rem;">시장 가격 (외적)</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- 3. Weight Watchers Example -->
    <section class="section fade-in-delay">
        <h2 class="section-title">3. 실제 적용: 웨이트 워처스</h2>
        <div class="section-content">
            
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>다이어트가 실패하는 이유:</strong> "이것 먹고, 저것 먹지 마"라고 하면 안 됨.</p>
                <p><strong>웨이트 워처스가 성공하는 이유:</strong> <strong>예산제약</strong>을 설정하고 최적화하게 함!</p>
            </div>

            <h4>작동 방식</h4>
            <ul>
                <li><strong>포인트 (가격처럼):</strong> 각 음식에 체중 증가 가능성에 따라 포인트 부여</li>
                <li><strong>예산 (소득처럼):</strong> 목표 체중에 따라 일일 포인트 예산 받음</li>
                <li><strong>선택 (최적화):</strong> 포인트를 어떻게 쓸지 스스로 결정</li>
            </ul>

            <h4>맥도날드 점심 예시 (30포인트 예산)</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;" colspan="2">옵션 A: 클래식 콤보</th>
                    <th style="padding: 0.75rem; text-align: left;" colspan="2">옵션 B: 가벼운 선택</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">빅맥</td>
                    <td style="padding: 0.75rem; text-align: center;">14 pts</td>
                    <td style="padding: 0.75rem;">10피스 너겟</td>
                    <td style="padding: 0.75rem; text-align: center;">12 pts</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">감자튀김</td>
                    <td style="padding: 0.75rem; text-align: center;">10 pts</td>
                    <td style="padding: 0.75rem;">사과 슬라이스</td>
                    <td style="padding: 0.75rem; text-align: center;">1 pt</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">콜라</td>
                    <td style="padding: 0.75rem; text-align: center;">6 pts</td>
                    <td style="padding: 0.75rem;">다이어트 콜라</td>
                    <td style="padding: 0.75rem; text-align: center;">0 pts</td>
                </tr>
                <tr style="background: #fef3c7;">
                    <td style="padding: 0.75rem; font-weight: 600;">총합</td>
                    <td style="padding: 0.75rem; text-align: center; font-weight: 600;">30 pts (오늘 끝!)</td>
                    <td style="padding: 0.75rem; font-weight: 600;">총합</td>
                    <td style="padding: 0.75rem; text-align: center; font-weight: 600;">13 pts (17 남음!)</td>
                </tr>
            </table>

            <p><em>"소비자가 임의의 규칙을 따르는 게 아니라 제약 안에서 마음을 따르게 합니다. 이것이 제약 하 최적화입니다."</em></p>
        </div>
    </section>

    <!-- 4. Changes in Budget Constraint -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4. 예산제약의 변화</h2>
        <div class="section-content">
            
            <h4>예산제약이 변하는 두 가지 방법</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">변화</th>
                    <th style="padding: 0.75rem; text-align: left;">효과</th>
                    <th style="padding: 0.75rem; text-align: left;">기울기</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">가격 변화</td>
                    <td style="padding: 0.75rem;">예산선이 <strong>회전(pivot)</strong></td>
                    <td style="padding: 0.75rem;">변화함</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem;">소득 변화</td>
                    <td style="padding: 0.75rem;">예산선이 <strong>평행이동</strong></td>
                    <td style="padding: 0.75rem;">불변</td>
                </tr>
            </table>

            <!-- Case 1: Price Change -->
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0; border-left: 4px solid #ef4444;">
                <p style="font-weight: 600; color: #dc2626;">Case 1: 가격 변화 (피자 $4 → $6)</p>
                <ul>
                    <li>X절편 (쿠키): 12에서 <strong>불변</strong></li>
                    <li>Y절편 (피자): 6에서 4로 <strong>감소</strong></li>
                    <li>새 기울기: −2/6 = <strong>−1/3</strong> (기존 −1/2)</li>
                    <li>기회집합 축소 → 더 나빠짐</li>
                </ul>
                <p><em>"소득은 변하지 않았습니다. 여전히 24달러가 있습니다. 하지만 더 나빠졌습니다. 소득은 살 수 있는 것의 표현일 뿐이니까요."</em></p>
            </div>

            <!-- Case 2: Income Change -->
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0; border-left: 4px solid #f59e0b;">
                <p style="font-weight: 600; color: #d97706;">Case 2: 소득 변화 ($24 → $20)</p>
                <ul>
                    <li>기울기: −1/2에서 <strong>불변</strong> (가격이 안 변했으므로)</li>
                    <li>양쪽 절편 모두 감소</li>
                    <li>기회집합 축소 → 더 나빠짐</li>
                </ul>
            </div>

            <h4>인플레이션은?</h4>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <ul>
                    <li><strong>균일 인플레이션</strong> (모든 가격이 같은 %로 상승): 소득 감소처럼 보임 (평행이동)</li>
                    <li><strong>차별적 인플레이션</strong> (가격이 다른 %로 상승): 가격 변화처럼 보임 (회전)</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- 5. Constrained Choice -->
    <section class="section fade-in-delay">
        <h2 class="section-title">5. 제약 하 선택: 최적점 찾기</h2>
        <div class="section-content">
            
            <h4>핵심 문제</h4>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <ul>
                    <li><strong>Lecture 2:</strong> 많을수록 좋다 (가능한 높은 IC에 도달)</li>
                    <li><strong>Lecture 3:</strong> 예산 이상으로 소비할 수 없음</li>
                </ul>
                <p><strong>해결:</strong> 예산제약에 <strong>닿는</strong> <strong>가장 높은 무차별곡선</strong>을 선택.</p>
            </div>

            <h4>수학적 조건: MRS = MRT</h4>
            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p>접점에서 기울기가 같음:</p>
                <p style="font-family: monospace; font-size: 1.1rem; text-align: center;">
                    MRS = MRT
                </p>
                <p style="font-family: monospace; font-size: 1.1rem; text-align: center;">
                    −MU<sub>C</sub>/MU<sub>S</sub> = −P<sub>C</sub>/P<sub>S</sub>
                </p>
                <p style="text-align: center;">또는 동치로:</p>
                <p style="font-family: monospace; font-size: 1.1rem; text-align: center;">
                    <strong>MU<sub>C</sub>/MU<sub>S</sub> = P<sub>C</sub>/P<sub>S</sub></strong>
                </p>
            </div>

            <h4>"가성비" 해석</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p>최적화 조건을 재정리:</p>
                <p style="font-family: monospace; font-size: 1.1rem; text-align: center;">
                    MU<sub>C</sub>/P<sub>C</sub> = MU<sub>S</sub>/P<sub>S</sub>
                </p>
                <ul>
                    <li><strong>Bang</strong> = MU (다음 단위로부터의 행복)</li>
                    <li><strong>Buck</strong> = P (다음 단위의 비용)</li>
                    <li><strong>Bang per Buck</strong> = MU/P (달러당 행복)</li>
                </ul>
                <p><strong>규칙:</strong> 모든 재화의 달러당 행복이 같아질 때까지 소비.</p>
            </div>

            <h4>점들의 그래픽 비교</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">점</th>
                    <th style="padding: 0.75rem; text-align: left;">위치</th>
                    <th style="padding: 0.75rem; text-align: left;">효용 (U = √(S×C))</th>
                    <th style="padding: 0.75rem; text-align: left;">왜 최적이 아닌가?</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">A</td>
                    <td style="padding: 0.75rem;">예산선 위</td>
                    <td style="padding: 0.75rem;">√10 ≈ 3.16</td>
                    <td style="padding: 0.75rem;">D보다 낮은 IC</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600; color: #10b981;">D</td>
                    <td style="padding: 0.75rem;">예산선에 접함</td>
                    <td style="padding: 0.75rem; font-weight: 600;">√18 ≈ 4.24</td>
                    <td style="padding: 0.75rem; color: #10b981;"><strong>최적!</strong></td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem;">E</td>
                    <td style="padding: 0.75rem;">예산선 밖</td>
                    <td style="padding: 0.75rem;">√32 ≈ 5.66</td>
                    <td style="padding: 0.75rem;">살 수 없음</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- 6. Mathematical Example -->
    <section class="section fade-in-delay">
        <h2 class="section-title">6. 왜 A점이 최적이 아닌가: 수학적 증명</h2>
        <div class="section-content">
            
            <h4>설정</h4>
            <ul>
                <li>U = √(S × C), A점: S = 5, C = 2</li>
                <li>P<sub>C</sub> = $2, P<sub>S</sub> = $4</li>
            </ul>

            <h4>Step 1: A점에서 MRS 계산</h4>
            <div style="background: #f5f5f5; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p style="font-family: monospace;">
                    MU<sub>C</sub> = 0.5 × 5 / √10 = 2.5 / √10<br>
                    MU<sub>S</sub> = 0.5 × 2 / √10 = 1 / √10<br><br>
                    MRS = −MU<sub>C</sub>/MU<sub>S</sub> = −2.5/1 = <strong>−2.5</strong>
                </p>
            </div>

            <h4>Step 2: MRT 계산</h4>
            <div style="background: #f5f5f5; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p style="font-family: monospace;">
                    MRT = −P<sub>C</sub>/P<sub>S</sub> = −2/4 = <strong>−0.5</strong>
                </p>
            </div>

            <h4>Step 3: 불균형 해석</h4>
            <div style="background: #fef2f2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <table style="width:100%; border-collapse: collapse;">
                    <tr style="border-bottom: 1px solid #e5e7eb;">
                        <td style="padding: 0.75rem;"><strong>MRS = −2.5</strong></td>
                        <td style="padding: 0.75rem;">쿠키 1개에 피자 2.5개 포기 <strong>의향</strong> 있음</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.75rem;"><strong>MRT = −0.5</strong></td>
                        <td style="padding: 0.75rem;">시장은 쿠키 1개에 피자 0.5개만 <strong>요구</strong></td>
                    </tr>
                </table>
                <p style="margin-top: 1rem;"><strong>결론:</strong> 쿠키를 높이 평가하지만 시장에서는 싸다! 좋은 거래 → 쿠키를 더 사라!</p>
            </div>

            <h4>일반 규칙</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">조건</th>
                    <th style="padding: 0.75rem; text-align: left;">행동</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">|MRS| > |MRT|</td>
                    <td style="padding: 0.75rem;">x축 재화(쿠키)를 더 사라</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem;">|MRS| < |MRT|</td>
                    <td style="padding: 0.75rem;">y축 재화(피자)를 더 사라</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- 7. SNAP Application -->
    <section class="section fade-in-delay">
        <h2 class="section-title">7. 정책 적용: SNAP vs 현금 이전</h2>
        <div class="section-content">
            
            <h4>SNAP이란?</h4>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>SNAP</strong> = Supplemental Nutrition Assistance Program (구 "푸드 스탬프")</p>
                <ul>
                    <li>가난한 사람들에게 <strong>식품에만 사용</strong>할 수 있는 직불카드 제공</li>
                    <li>자격: 빈곤선 이하 또는 근처 (~연간 $14,000)</li>
                </ul>
                <p><strong>질문:</strong> 왜 그냥 현금을 안 주나?</p>
            </div>

            <h4>두 유형의 사람</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">사람</th>
                    <th style="padding: 0.75rem; text-align: left;">선호</th>
                    <th style="padding: 0.75rem; text-align: left;">원래 선택 (소득 $5,000)</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">X</td>
                    <td style="padding: 0.75rem;">주거 좋아함, 많이 안 먹음</td>
                    <td style="padding: 0.75rem;">주거 $4,800, 음식 $200</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; font-weight: 600;">Y</td>
                    <td style="padding: 0.75rem;">음식 좋아함, 최소한의 주거</td>
                    <td style="padding: 0.75rem;">주거 $100, 음식 $4,900</td>
                </tr>
            </table>

            <h4>$500 SNAP (음식만) 효과</h4>
            <div style="background: #f0fdf4; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Y:</strong> 현금과 차이 없음! 이미 음식에 $4,900 지출 중.</p>
                <p><em>"돈은 대체 가능합니다. 음식 지출 중 $500을 SNAP으로 재분류하면 됩니다."</em></p>
            </div>

            <div style="background: #fef2f2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>X:</strong> 행동을 강제로 바꿔야 함!</p>
                <ul>
                    <li>현금이면 원했던 것: 주거 $5,200, 음식 $300</li>
                    <li>SNAP으로 받는 것: 주거 $5,000, 음식 $500</li>
                </ul>
                <p><strong>낮은 무차별곡선 → 더 나빠짐!</strong></p>
            </div>

            <h4>왜 정책 입안자들은 SNAP을 쓰나?</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"'주거'라는 단어를 지우고 '코카인'을 넣어보세요."</em></p>
                <p>정책 입안자들의 걱정: "가난한 사람들이 음식 대신 마약에 현금을 쓰면?"</p>
            </div>

            <h4>실증적 증거 (J-PAL 실험)</h4>
            <ul>
                <li><strong>실증:</strong> SNAP은 행동을 바꿈 — SNAP $1 → 현금보다 음식 $0.15 더 소비</li>
                <li><strong>규범:</strong> 현금 수령자들은 교육, 사업, 건강에 투자 — "나쁜" 것에 거의 안 씀</li>
                <li><strong>우간다:</strong> 현금 $150 → 18개월 후 수입 2배</li>
            </ul>
        </div>
    </section>

    <!-- Key Takeaways -->
    <section class="section fade-in-delay">
        <h2 class="section-title">핵심 요약</h2>
        <div class="section-content">
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: center; width: 5%;">#</th>
                    <th style="padding: 0.75rem; text-align: left; width: 25%;">개념</th>
                    <th style="padding: 0.75rem; text-align: left;">핵심 포인트</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">1</td>
                    <td style="padding: 0.75rem; font-weight: 600;">예산제약</td>
                    <td style="padding: 0.75rem;">Y = P<sub>C</sub>×C + P<sub>S</sub>×S; 기울기 = −P<sub>C</sub>/P<sub>S</sub></td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">2</td>
                    <td style="padding: 0.75rem; font-weight: 600;">MRT</td>
                    <td style="padding: 0.75rem;">시장이 허용하는 교환 비율; 예산선 기울기</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">3</td>
                    <td style="padding: 0.75rem; font-weight: 600;">최적화</td>
                    <td style="padding: 0.75rem;">MRS = MRT (IC와 예산선의 접점)</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">4</td>
                    <td style="padding: 0.75rem; font-weight: 600;">가성비 법칙</td>
                    <td style="padding: 0.75rem;">MU<sub>C</sub>/P<sub>C</sub> = MU<sub>S</sub>/P<sub>S</sub></td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">5</td>
                    <td style="padding: 0.75rem; font-weight: 600;">가격 변화</td>
                    <td style="padding: 0.75rem;">예산선이 회전; 기울기 변화</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; text-align: center;">6</td>
                    <td style="padding: 0.75rem; font-weight: 600;">현물 vs 현금</td>
                    <td style="padding: 0.75rem;">현물은 선택을 제약; 복지 감소 가능</td>
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
                    <td style="padding: 0.75rem;">예산제약 (Budget Constraint)</td>
                    <td style="padding: 0.75rem;">소득과 가격에 의해 부과되는 소비 묶음의 한계</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">기회집합 (Opportunity Set)</td>
                    <td style="padding: 0.75rem;">모든 구매 가능한 소비 묶음 (예산선 위/아래 영역)</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">MRT</td>
                    <td style="padding: 0.75rem;">한계전환율; 시장이 허용하는 재화 교환 비율</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">제약 하 최적화</td>
                    <td style="padding: 0.75rem;">예산제약 하에서 효용 극대화</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">접점 조건 (Tangency)</td>
                    <td style="padding: 0.75rem;">MRS = MRT; IC가 예산선에 닿는 최적점</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">대체가능성 (Fungibility)</td>
                    <td style="padding: 0.75rem;">돈은 재분류 가능; 출처와 관계없이 $1은 $1</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem;">현물급여 (In-Kind Benefits)</td>
                    <td style="padding: 0.75rem;">현금 대신 특정 재화/서비스로 주는 급여 (예: SNAP)</td>
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
