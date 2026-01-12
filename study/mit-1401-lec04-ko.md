---
layout: minimal_base
title: "MIT 14.01 Lec 4: 수요곡선과 소득/대체효과"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Lecture 4: 수요곡선과 소득/대체효과</h2>
            <a href="/study/mit-1401-lec04" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">English</a>
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
                "지난 두 강의에서 그 기초를 쌓았고, 오늘은 수요곡선이 실제로 어디서 나오는지 보여드리겠습니다."
            </blockquote>
            <p>수요곡선은 <strong>다양한 가격에서 최적 소비</strong>를 찾아 도출한다. 가격이 바뀌면 두 가지 효과가 동시에 발생: <strong>대체효과</strong>와 <strong>소득효과</strong>.</p>
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
                        <td style="padding: 0.5rem; color: #10b981;">✓ 완료</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; font-weight: 600;">Step 3 (Lec 4)</td>
                        <td style="padding: 0.5rem;">수요곡선 도출</td>
                        <td style="padding: 0.5rem; color: #2563eb;">← 오늘</td>
                    </tr>
                </table>
            </div>
        </div>
    </section>

    <!-- 1. Deriving a Demand Curve -->
    <section class="section fade-in-delay">
        <h2 class="section-title">1. 수요곡선 도출하기</h2>
        <div class="section-content">
            
            <h4>정의</h4>
            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p><strong>수요곡선:</strong> 재화의 가격과 소비자가 원하는 수량 사이의 관계</p>
            </div>

            <h4>설정 (복습)</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.5rem; font-weight: 600;">효용함수</td>
                    <td style="padding: 0.5rem;">U = √(S × C)</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.5rem; font-weight: 600;">예산제약</td>
                    <td style="padding: 0.5rem;">Y = P<sub>S</sub> × S + P<sub>C</sub> × C</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.5rem; font-weight: 600;">소득 (Y)</td>
                    <td style="padding: 0.5rem;">$24</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.5rem; font-weight: 600;">피자 가격 (P<sub>S</sub>)</td>
                    <td style="padding: 0.5rem;">$4</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; font-weight: 600;">쿠키 가격 (P<sub>C</sub>)</td>
                    <td style="padding: 0.5rem;">$2 (초기값)</td>
                </tr>
            </table>

            <h4>Step 1: 최적 소비 구하기</h4>
            <div style="background: #f5f5f5; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p><strong>최적화 조건:</strong> MRS = MRT</p>
                <p style="font-family: monospace;">
                    -S/C = -P<sub>C</sub>/P<sub>S</sub> = -2/4 = -1/2<br>
                    → S = C/2 ... (식 1)
                </p>
                <p><strong>예산제약:</strong></p>
                <p style="font-family: monospace;">
                    24 = 4S + 2C<br>
                    (1) 대입: 24 = 4(C/2) + 2C = 4C<br>
                    → C* = 6, S* = 3
                </p>
            </div>

            <h4>Step 2: 쿠키 가격 변화시키기</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">P<sub>C</sub></th>
                    <th style="padding: 0.75rem; text-align: left;">MRT</th>
                    <th style="padding: 0.75rem; text-align: left;">최적화</th>
                    <th style="padding: 0.75rem; text-align: left;">결과</th>
                    <th style="padding: 0.75rem; text-align: left;">점</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">$4/3</td>
                    <td style="padding: 0.75rem;">-1/3</td>
                    <td style="padding: 0.75rem;">S = C/3</td>
                    <td style="padding: 0.75rem;">C=9, S=3</td>
                    <td style="padding: 0.75rem;">C</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">$2</td>
                    <td style="padding: 0.75rem;">-1/2</td>
                    <td style="padding: 0.75rem;">S = C/2</td>
                    <td style="padding: 0.75rem;">C=6, S=3</td>
                    <td style="padding: 0.75rem;">A</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem;">$3</td>
                    <td style="padding: 0.75rem;">-3/4</td>
                    <td style="padding: 0.75rem;">S = 3C/4</td>
                    <td style="padding: 0.75rem;">C=4, S=3</td>
                    <td style="padding: 0.75rem;">B</td>
                </tr>
            </table>

            <h4>Step 3: 수요곡선 그리기</h4>
            <div style="text-align: center; margin: 1.5rem 0;">
                <img src="/assets/images/mit1401-fig4-1.png" alt="Figure 4-1: 수요곡선 도출" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <p style="color: #6b7280; font-size: 0.9rem; margin-top: 0.5rem;">Figure 4-1: 효용 극대화로부터 수요곡선 도출</p>
            </div>

            <div style="background: #f0fdf4; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>핵심:</strong> 수요곡선은 다양한 가격에서 효용을 최적화하고 각 가격에서 원하는 수량을 찾아 도출된다.</p>
            </div>

            <h4>학생 질문: "왜 피자 수량이 안 변하죠?"</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"좋은 관찰입니다! 쿠키 가격이 변해도 피자 수량이 안 변하는 건 일반적인 법칙이 아닙니다. 이 특정 효용함수의 특성이에요."</em></p>
                <p>이를 <strong>flat cross-price consumption curve</strong>라고 부른다 — 계산을 간단하게 만드는 이 효용함수의 특별한 성질.</p>
            </div>
        </div>
    </section>

    <!-- 2. Elasticity of Demand -->
    <section class="section fade-in-delay">
        <h2 class="section-title">2. 수요의 탄력성</h2>
        <div class="section-content">
            
            <h4>정의</h4>
            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p style="font-family: monospace; font-size: 1.1rem; text-align: center;">
                    ε = (ΔQ/Q) / (ΔP/P) ≈ (dQ/dP) × (P/Q)
                </p>
                <p style="text-align: center;">"수요가 가격 변화에 얼마나 반응하는가?"</p>
            </div>

            <h4>극단적 케이스</h4>
            <div style="display: flex; gap: 1rem; margin: 1.5rem 0; flex-wrap: wrap;">
                <div style="flex: 1; min-width: 280px; text-align: center;">
                    <img src="/assets/images/mit1401-fig4-2.png" alt="Figure 4-2: 완전 비탄력적 수요" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                    <p style="color: #6b7280; font-size: 0.85rem; margin-top: 0.5rem;">Figure 4-2: 완전 비탄력적 (ε = 0)</p>
                </div>
                <div style="flex: 1; min-width: 280px; text-align: center;">
                    <img src="/assets/images/mit1401-fig4-3.png" alt="Figure 4-3: 완전 탄력적 수요" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                    <p style="color: #6b7280; font-size: 0.85rem; margin-top: 0.5rem;">Figure 4-3: 완전 탄력적 (ε = -∞)</p>
                </div>
            </div>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">유형</th>
                    <th style="padding: 0.75rem; text-align: left;">ε 값</th>
                    <th style="padding: 0.75rem; text-align: left;">곡선 모양</th>
                    <th style="padding: 0.75rem; text-align: left;">대체재</th>
                    <th style="padding: 0.75rem; text-align: left;">예시</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">완전 비탄력적</td>
                    <td style="padding: 0.75rem;">ε = 0</td>
                    <td style="padding: 0.75rem;">수직</td>
                    <td style="padding: 0.75rem;">없음</td>
                    <td style="padding: 0.75rem;">인슐린</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">비탄력적</td>
                    <td style="padding: 0.75rem;">-1 < ε < 0</td>
                    <td style="padding: 0.75rem;">가파름</td>
                    <td style="padding: 0.75rem;">적음</td>
                    <td style="padding: 0.75rem;">가솔린, 물</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">탄력적</td>
                    <td style="padding: 0.75rem;">ε < -1</td>
                    <td style="padding: 0.75rem;">완만함</td>
                    <td style="padding: 0.75rem;">많음</td>
                    <td style="padding: 0.75rem;">사치품</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem;">완전 탄력적</td>
                    <td style="padding: 0.75rem;">ε = -∞</td>
                    <td style="padding: 0.75rem;">수평</td>
                    <td style="padding: 0.75rem;">무한</td>
                    <td style="padding: 0.75rem;">맥도날드 vs 버거킹</td>
                </tr>
            </table>

            <h4>핵심 원리: 대체가능성 = 탄력성</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"탄력성을 구분하는 핵심 특성은 대체가능성입니다. 대체재가 없는 재화는 비탄력적이에요. 대체재가 많은 재화는 매우 탄력적입니다."</em></p>
            </div>

            <h4>강의실 대화</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>학생:</strong> "가솔린이요?"</p>
                <p><strong>Gruber:</strong> "가솔린은 어느 정도 비탄력적이죠. 출근은 해야 하니까요. 하지만 버스도 있고, 자전거도 있고, 걸을 수도 있고, 새 차를 살 수도 있죠. 그래서 완전 비탄력적은 아니에요."</p>
                <p style="margin-top: 1rem;"><strong>학생:</strong> "인슐린이요?"</p>
                <p><strong>Gruber:</strong> "인슐린이 우리가 쓰는 전형적인 예시입니다. 대체재가 없어요. 당뇨병 위기 상황에서 '$1 더 비싸? 그냥 죽을래'라고 안 합니다."</p>
            </div>
        </div>
    </section>

    <!-- 3. Income and Demand: Engel Curves -->
    <section class="section fade-in-delay">
        <h2 class="section-title">3. 소득과 수요: 엥겔곡선</h2>
        <div class="section-content">
            
            <h4>소득이 변하면?</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">소득 (Y)</th>
                    <th style="padding: 0.75rem; text-align: left;">쿠키 (C*)</th>
                    <th style="padding: 0.75rem; text-align: left;">피자 (S*)</th>
                    <th style="padding: 0.75rem; text-align: left;">점</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">$16</td>
                    <td style="padding: 0.75rem;">4</td>
                    <td style="padding: 0.75rem;">2</td>
                    <td style="padding: 0.75rem;">C</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">$24</td>
                    <td style="padding: 0.75rem;">6</td>
                    <td style="padding: 0.75rem;">3</td>
                    <td style="padding: 0.75rem;">A</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem;">$32</td>
                    <td style="padding: 0.75rem;">8</td>
                    <td style="padding: 0.75rem;">4</td>
                    <td style="padding: 0.75rem;">B</td>
                </tr>
            </table>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>핵심:</strong> 가격비 불변 → MRS = MRT 조건 불변</p>
                <p>예산선이 <strong>평행이동</strong> (회전 아님)</p>
            </div>

            <h4>엥겔곡선 (Engel Curve)</h4>
            <div style="text-align: center; margin: 1.5rem 0;">
                <img src="/assets/images/mit1401-fig4-4.png" alt="Figure 4-4: 엥겔곡선 생성" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <p style="color: #6b7280; font-size: 0.9rem; margin-top: 0.5rem;">Figure 4-4: 엥겔곡선 생성</p>
            </div>

            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p><strong>정의:</strong> 소득과 수요량 사이의 관계</p>
                <p style="font-family: monospace; font-size: 1.1rem; text-align: center; margin-top: 0.5rem;">
                    γ = (ΔQ/Q) / (ΔY/Y) ≈ (dQ/dY) × (Y/Q)
                </p>
                <p style="text-align: center;"><strong>소득탄력성</strong></p>
            </div>

            <h4>감마(γ) vs 엡실론(ε)</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"감마가 엡실론보다 훨씬 더 흥미롭습니다. 엡실론은 0에서 마이너스 무한대 사이의 어떤 음수예요. 감마는 훨씬 더 넓은 범위를 가질 수 있어요."</em></p>
            </div>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">탄력성</th>
                    <th style="padding: 0.75rem; text-align: left;">범위</th>
                    <th style="padding: 0.75rem; text-align: left;">제약</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">ε (가격)</td>
                    <td style="padding: 0.75rem;">0 ~ -∞</td>
                    <td style="padding: 0.75rem;">항상 ≤ 0</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem;">γ (소득)</td>
                    <td style="padding: 0.75rem;">-∞ ~ +∞</td>
                    <td style="padding: 0.75rem;">제약 없음</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- 4. Classification of Goods -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4. 소득탄력성에 따른 재화 분류</h2>
        <div class="section-content">
            
            <h4>전체 분류</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">유형</th>
                    <th style="padding: 0.75rem; text-align: left;">γ 값</th>
                    <th style="padding: 0.75rem; text-align: left;">의미</th>
                    <th style="padding: 0.75rem; text-align: left;">예시</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">열등재</td>
                    <td style="padding: 0.75rem;">γ < 0</td>
                    <td style="padding: 0.75rem;">소득↑ → 수요↓</td>
                    <td style="padding: 0.75rem;">라면</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">필수재</td>
                    <td style="padding: 0.75rem;">0 < γ < 1</td>
                    <td style="padding: 0.75rem;">소득↑ → 예산 비중↓</td>
                    <td style="padding: 0.75rem;">집세, 기본 식료품</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; font-weight: 600;">사치재</td>
                    <td style="padding: 0.75rem;">γ > 1</td>
                    <td style="padding: 0.75rem;">소득↑ → 예산 비중↑</td>
                    <td style="padding: 0.75rem;">외식, 명품시계</td>
                </tr>
            </table>

            <h4>라면: 궁극의 열등재</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"라면이 그 예시입니다. 라면이 궁극의 열등재예요. 아무도 라면을 먹고 싶어서 안 먹어요. 요즘 고급 라면 식당들이 있긴 한데, 거기 가면 안 돼요."</em></p>
                <p><em>"사람들은 라면이 싸서 먹어요. 부자가 되면 라면 소비가 줄어요."</em></p>
            </div>

            <h4>필수재 vs 열등재: 핵심 구분</h4>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <table style="width:100%; border-collapse: collapse;">
                    <tr style="border-bottom: 1px solid #e5e7eb;">
                        <td style="padding: 0.75rem; font-weight: 600;">열등재</td>
                        <td style="padding: 0.75rem;">소득↑ → <strong>절대량 감소</strong></td>
                    </tr>
                    <tr>
                        <td style="padding: 0.75rem; font-weight: 600;">필수재</td>
                        <td style="padding: 0.75rem;">소득↑ → 증가하지만 <strong>소득보다 느리게</strong></td>
                    </tr>
                </table>
                <p style="margin-top: 1rem;"><em>"집세가 완벽한 예시예요. 부자들은 가난한 사람들보다 좋은 아파트를 가지고 있어요. 하지만 부자들이 아파트에 쓰는 예산 비중은 가난한 사람들보다 낮아요."</em></p>
            </div>
        </div>
    </section>

    <!-- 5. Mechanics of Price Change -->
    <section class="section fade-in-delay">
        <h2 class="section-title">5. 가격 변화의 메커니즘</h2>
        <div class="section-content">
            
            <h4>왜 이게 중요한가</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"가격이 변하면 두 가지가 동시에 일어납니다. 인식하지 못할 수도 있지만, 실제로 가격이 변하면 두 가지가 일어나요."</em></p>
            </div>

            <h4>두 가지 동시 효과</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">효과</th>
                    <th style="padding: 0.75rem; text-align: left;">정의</th>
                    <th style="padding: 0.75rem; text-align: left;">메커니즘</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">대체효과</td>
                    <td style="padding: 0.75rem;">상대적으로 비싸진 재화에서 이탈</td>
                    <td style="padding: 0.75rem;">상대가격 변화</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; font-weight: 600;">소득효과</td>
                    <td style="padding: 0.75rem;">실질적으로 부자/가난해짐</td>
                    <td style="padding: 0.75rem;">실질 구매력 변화</td>
                </tr>
            </table>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"가격이 변하면 두 가지가 일어나요. 재화들이 차별적으로 매력적이 되고, 부자가 되거나 가난해져요. 두 가지 모두 가격 변화에 대한 반응을 이끌어내요."</em></p>
            </div>
        </div>
    </section>

    <!-- 6. Decomposing Price Changes -->
    <section class="section fade-in-delay">
        <h2 class="section-title">6. 소득효과와 대체효과 분해하기</h2>
        <div class="section-content">
            
            <h4>예시 설정</h4>
            <ul>
                <li><strong>출발점 (A):</strong> C = 6, S = 3 (BC1 위)</li>
                <li><strong>가격 변화:</strong> P<sub>C</sub>: $2 → $3</li>
                <li><strong>도착점 (C):</strong> C = 4, S = 3 (BC2 위)</li>
            </ul>

            <h4>대체효과 측정 방법</h4>
            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p><strong>정의:</strong> 효용을 일정하게 유지하면서 수량 변화</p>
                <p style="font-family: monospace; text-align: center;">ΔQ|<sub>Ū</sub></p>
            </div>

            <p><strong>그래픽 방법:</strong> 두 가지 특성을 가진 <strong>가상의 예산선 BC'</strong> 그리기:</p>
            <ol>
                <li>새 예산선과 <strong>평행</strong> (새 가격비 -3/4 반영)</li>
                <li>원래 무차별곡선에 <strong>접함</strong> (효용 일정 유지)</li>
            </ol>

            <div style="text-align: center; margin: 1.5rem 0;">
                <img src="/assets/images/mit1401-fig4-5.png" alt="Figure 4-5: 정상재의 소득/대체효과" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <p style="color: #6b7280; font-size: 0.9rem; margin-top: 0.5rem;">Figure 4-5: 정상재의 소득효과와 대체효과</p>
            </div>

            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0; border-left: 4px solid #2563eb;">
                <p><em>"일정한 효용에서 수량 변화를 보여주는 거예요. 효용을 어떻게 일정하게 유지하죠? 같은 무차별곡선에 머무르는 거예요."</em></p>
            </div>

            <h4>결과</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">이동</th>
                    <th style="padding: 0.75rem; text-align: left;">효과</th>
                    <th style="padding: 0.75rem; text-align: left;">쿠키</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">A → B</td>
                    <td style="padding: 0.75rem;">대체효과</td>
                    <td style="padding: 0.75rem;">6 → 4.89</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">B → C</td>
                    <td style="padding: 0.75rem;">소득효과</td>
                    <td style="padding: 0.75rem;">4.89 → 4</td>
                </tr>
                <tr style="background: #f0fdf4;">
                    <td style="padding: 0.75rem; font-weight: 600;">A → C</td>
                    <td style="padding: 0.75rem; font-weight: 600;">총 효과</td>
                    <td style="padding: 0.75rem; font-weight: 600;">6 → 4</td>
                </tr>
            </table>

            <h4>대체효과는 항상 음수(-)</h4>
            <div style="background: #fef2f2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>수학적 증명:</strong></p>
                <ol>
                    <li>접점에서: MU<sub>C</sub>/MU<sub>S</sub> = P<sub>C</sub>/P<sub>S</sub></li>
                    <li>P<sub>C</sub>/P<sub>S</sub>가 올라감 (쿠키가 더 비싸짐)</li>
                    <li>등식 유지하려면 MU<sub>C</sub>/MU<sub>S</sub>도 올라가야</li>
                    <li>MU<sub>C</sub>를 올리려면 → 쿠키를 줄여야 (한계효용 체감!)</li>
                    <li>MU<sub>S</sub>를 내리려면 → 피자를 늘려야</li>
                </ol>
                <p><strong>결론:</strong> 가격↑ → 대체효과는 항상 음수</p>
            </div>

            <h4>소득효과의 부호는 재화 유형에 따라 다름</h4>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>왜 "실질적으로 가난해지는가"?</strong></p>
                <p><em>"소득 자체는 안 떨어졌지만, 자원은 떨어졌어요. 그 소득으로 살 수 있는 게 줄었어요. 실질적으로 가난해진 거예요."</em></p>
                <p style="margin-top: 1rem;"><strong>학생:</strong> "기회집합이 수축됐네요."</p>
                <p><strong>Gruber:</strong> "맞아요. 기회집합이 수축됐어요."</p>
            </div>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">재화 유형</th>
                    <th style="padding: 0.75rem; text-align: left;">소득↓ 시</th>
                    <th style="padding: 0.75rem; text-align: left;">소득효과</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">정상재</td>
                    <td style="padding: 0.75rem;">수요↓</td>
                    <td style="padding: 0.75rem;">음수 (대체효과와 같은 방향)</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem;">열등재</td>
                    <td style="padding: 0.75rem;">수요↑</td>
                    <td style="padding: 0.75rem;">양수 (대체효과와 반대 방향)</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- 7. Inferior Good Example -->
    <section class="section fade-in-delay">
        <h2 class="section-title">7. 열등재 예시: 스테이크 vs 감자</h2>
        <div class="section-content">
            
            <h4>설정</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"Figure 4.6은 더 이상 피자와 쿠키가 아니에요. 이제 스테이크와 감자예요. 피자와 쿠키는 둘 다 정상재니까요."</em></p>
                <p><em>"감자가 전형적인 열등재예요. 가난한 사람들, 특히 옛날에는 감자를 먹어야 했어요. 키우기 싸고 매우 든든하거든요."</em></p>
            </div>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.5rem; font-weight: 600;">소득</td>
                    <td style="padding: 0.5rem;">$25</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.5rem; font-weight: 600;">스테이크 가격</td>
                    <td style="padding: 0.5rem;">$5</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; font-weight: 600;">감자 가격</td>
                    <td style="padding: 0.5rem;">$1 → $3</td>
                </tr>
            </table>

            <div style="text-align: center; margin: 1.5rem 0;">
                <img src="/assets/images/mit1401-fig4-6.png" alt="Figure 4-6: 열등재의 소득/대체효과" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <p style="color: #6b7280; font-size: 0.9rem; margin-top: 0.5rem;">Figure 4-6: 열등재(감자)의 소득효과와 대체효과</p>
            </div>

            <h4>분해</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">효과</th>
                    <th style="padding: 0.75rem; text-align: left;">감자</th>
                    <th style="padding: 0.75rem; text-align: left;">설명</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">대체효과 (A→B)</td>
                    <td style="padding: 0.75rem;">7.5 → 4 ↓</td>
                    <td style="padding: 0.75rem;">가격↑ → 덜 원함 (항상!)</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">소득효과 (B→C)</td>
                    <td style="padding: 0.75rem;">4 → 5 ↑</td>
                    <td style="padding: 0.75rem;">가난해짐 + 열등재 → 더 원함!</td>
                </tr>
                <tr style="background: #fef3c7;">
                    <td style="padding: 0.75rem; font-weight: 600;">순효과</td>
                    <td style="padding: 0.75rem; font-weight: 600;">7.5 → 5 ↓</td>
                    <td style="padding: 0.75rem;">두 효과가 서로 상쇄</td>
                </tr>
            </table>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"소득효과는 반대 방향으로 가요. 감자가 열등재니까요. 다시 말해, 이제 너무 가난해져서, 감자가 너무 비싸져서, 스테이크 살 돈이 없어요. 그래서 감자를 더 먹어야 해요. 아이러니하죠?"</em></p>
            </div>
        </div>
    </section>

    <!-- 8. Giffen Goods -->
    <section class="section fade-in-delay">
        <h2 class="section-title">8. 기펜재 (Giffen Good)</h2>
        <div class="section-content">
            
            <h4>정의</h4>
            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p><strong>기펜재:</strong> 소득효과가 대체효과를 압도해서 <strong>수요곡선이 우상향</strong>하는 열등재</p>
                <p style="text-align: center; font-weight: 600; margin-top: 0.5rem;">가격↑ → 수요↑ (수요법칙 위반!)</p>
            </div>

            <h4>존재하는가?</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"Giffen이라는 이름이 좋아요. Griffin(그리핀)과 발음이 비슷하거든요. 그리핀은 상상의 동물이에요. 기펜재도 대부분 상상이에요. 훌륭한 이론적 개념이지만 실제로는 존재하지 않아요."</em></p>
            </div>

            <h4>아일랜드 감자 기근 이야기</h4>
            <div style="background: #fef2f2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>주장:</strong> 감자 역병 때 감자 가격이 올랐는데 1인당 감자 소비가 올랐다. 그러니까 감자는 기펜재다!</p>
                <p style="margin-top: 1rem;"><strong>Gruber의 반박:</strong></p>
                <p><em>"사람들이 놓친 게 뭐냐면요. 감자 역병이 또 뭘 했냐는 거예요. 돈 있는 사람들은 전부 아일랜드를 떠났어요! 남은 사람들은 극빈층뿐이었어요."</em></p>
                <p><em>"그래서 데이터를 보면 1인당 감자가 올랐어요. 기펜재네! 하지만 놓친 게 뭐냐면 '인당'이 달라졌다는 거예요. 각 사람이 더 먹은 게 아니에요. 감자 안 먹던 사람들이 떠난 거예요."</em></p>
            </div>

            <h4>기펜재 vs 베블런재</h4>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>학생:</strong> "베블런재요?"</p>
                <p><strong>Gruber:</strong> "베블런재는 완전히 다른 개념이에요. 사회적 지위를 신경 쓰기 때문에 가격이 오르면 더 원한다는 개념이에요. 하지만 그건 행동경제학적인 거예요. 표준 경제학 효과가 아니에요."</p>
            </div>
        </div>
    </section>

    <!-- 9. Summary Chart -->
    <section class="section fade-in-delay">
        <h2 class="section-title">9. 종합 정리표</h2>
        <div class="section-content">
            
            <h4>정상재</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">가격 변화</th>
                    <th style="padding: 0.75rem; text-align: left;">대체효과</th>
                    <th style="padding: 0.75rem; text-align: left;">소득효과</th>
                    <th style="padding: 0.75rem; text-align: left;">순효과</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">↑</td>
                    <td style="padding: 0.75rem;">−</td>
                    <td style="padding: 0.75rem;">−</td>
                    <td style="padding: 0.75rem; font-weight: 600; color: #dc2626;">− (명확)</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem;">↓</td>
                    <td style="padding: 0.75rem;">+</td>
                    <td style="padding: 0.75rem;">+</td>
                    <td style="padding: 0.75rem; font-weight: 600; color: #16a34a;">+ (명확)</td>
                </tr>
            </table>

            <h4>열등재</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">가격 변화</th>
                    <th style="padding: 0.75rem; text-align: left;">대체효과</th>
                    <th style="padding: 0.75rem; text-align: left;">소득효과</th>
                    <th style="padding: 0.75rem; text-align: left;">순효과</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">↑</td>
                    <td style="padding: 0.75rem;">−</td>
                    <td style="padding: 0.75rem; color: #dc2626; font-weight: 600;">+</td>
                    <td style="padding: 0.75rem; font-weight: 600; color: #d97706;">? (불명확)</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem;">↓</td>
                    <td style="padding: 0.75rem;">+</td>
                    <td style="padding: 0.75rem; color: #dc2626; font-weight: 600;">−</td>
                    <td style="padding: 0.75rem; font-weight: 600; color: #d97706;">? (불명확)</td>
                </tr>
            </table>

            <h4>왜 이게 중요한가</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"6강 정도 후에 말씀드릴 거예요. 얼마나 열심히 일할지, 얼마나 저축할지 결정할 때, 소득효과와 대체효과가 서로 반대로 작용하기 시작할 거예요."</em></p>
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
                    <th style="padding: 0.75rem; text-align: left; width: 25%;">개념</th>
                    <th style="padding: 0.75rem; text-align: left;">핵심 포인트</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">1</td>
                    <td style="padding: 0.75rem; font-weight: 600;">수요곡선 도출</td>
                    <td style="padding: 0.75rem;">다양한 가격에서 최적 수량 계산</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">2</td>
                    <td style="padding: 0.75rem; font-weight: 600;">탄력성</td>
                    <td style="padding: 0.75rem;">대체재 많음 = 탄력적</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">3</td>
                    <td style="padding: 0.75rem; font-weight: 600;">엥겔곡선</td>
                    <td style="padding: 0.75rem;">소득-수요 관계; γ로 재화 분류</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">4</td>
                    <td style="padding: 0.75rem; font-weight: 600;">대체효과</td>
                    <td style="padding: 0.75rem;">항상 가격 변화와 반대 부호</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">5</td>
                    <td style="padding: 0.75rem; font-weight: 600;">소득효과</td>
                    <td style="padding: 0.75rem;">정상재면 같은 방향; 열등재면 반대</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; text-align: center;">6</td>
                    <td style="padding: 0.75rem; font-weight: 600;">기펜재</td>
                    <td style="padding: 0.75rem;">이론적으로만 존재; 실제로는 없음</td>
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
                    <td style="padding: 0.75rem;">수요곡선</td>
                    <td style="padding: 0.75rem;">가격과 수요량 사이의 관계</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">가격탄력성 (ε)</td>
                    <td style="padding: 0.75rem;">가격 변화에 대한 수요의 반응성</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">엥겔곡선</td>
                    <td style="padding: 0.75rem;">소득과 수요량 사이의 관계</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">소득탄력성 (γ)</td>
                    <td style="padding: 0.75rem;">소득 변화에 대한 수요의 반응성</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">정상재</td>
                    <td style="padding: 0.75rem;">γ > 0; 소득 증가시 수요 증가</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">열등재</td>
                    <td style="padding: 0.75rem;">γ < 0; 소득 증가시 수요 감소</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">대체효과</td>
                    <td style="padding: 0.75rem;">상대가격 변화에 따른 수요 변화 (효용 일정)</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">소득효과</td>
                    <td style="padding: 0.75rem;">실질 구매력 변화에 따른 수요 변화</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem;">기펜재</td>
                    <td style="padding: 0.75rem;">소득효과 > 대체효과인 열등재</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- Footer -->
    <section class="section fade-in-delay">
        <div class="section-content" style="text-align: center; color: #6b7280; font-size: 0.9rem;">
            <p><em>Last updated: 2025-01-10</em></p>
            <p><a href="/study/mit-1401-overview-ko">← 코스 개요로 돌아가기</a></p>
        </div>
    </section>
</div>
