---
layout: minimal_base
title: "MIT 14.01 Lec 7: 경쟁 I"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Lecture 7: 경쟁 I (Competition I)</h2>
            <a href="/study/mit-1401-lec07" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">English</a>
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
                "생산자 이론에서는 예산 제약이 주어지지 않습니다. 얼마나 생산할지 선택할 수 있어요. 이를 위해 모델에 세 번째 요소인 시장 구조를 추가할 겁니다."
            </blockquote>
            <p>이 강의는 기업이 얼마나 생산할지 결정하는 빠진 조각인 <strong>시장 구조</strong>를 소개합니다. <strong>완전경쟁</strong>에 집중하여 이윤 극대화 조건 <strong>P = MC</strong>를 유도하고, 기업 공급곡선이 시장 공급곡선으로 어떻게 합쳐지는지 보여줍니다.</p>
        </div>
    </section>

    <!-- 1. Market Structure Overview -->
    <section class="section fade-in-delay">
        <h2 class="section-title">1. 시장 구조: 빠진 조각</h2>
        <div class="section-content">
            
            <h4>1.1 생산자 이론의 공백</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"생산자 이론이 소비자 이론보다 어려운 한 가지 이유는 예산 제약이 주어지지 않기 때문입니다. 얼마를 가질지 선택할 수 있어요. 얼마나 생산할지 선택할 수 있습니다."</em></p>
            </div>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">소비자 이론</th>
                    <th style="padding: 0.75rem; text-align: left;">생산자 이론</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">예산 주어짐 (소득)</td>
                    <td style="padding: 0.75rem;">예산 제약 없음!</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">2개 방정식, 2개 미지수</td>
                    <td style="padding: 0.75rem;">3번째 요소 필요</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem;">제약 하에 효용 극대화</td>
                    <td style="padding: 0.75rem;"><em>얼마나</em> 생산할지 선택해야</td>
                </tr>
            </table>

            <h4>1.2 세 가지 시장 구조</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">구조</th>
                    <th style="padding: 0.75rem; text-align: left;">기업 수</th>
                    <th style="padding: 0.75rem; text-align: left;">예시</th>
                    <th style="padding: 0.75rem; text-align: left;">다루는 시기</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb; background: #f0fdf4;">
                    <td style="padding: 0.75rem; font-weight: 600;">완전경쟁</td>
                    <td style="padding: 0.75rem;">다수 (무한)</td>
                    <td style="padding: 0.75rem;">원자재, eBay</td>
                    <td style="padding: 0.75rem;">지금 (Lec 7-8)</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">독점</td>
                    <td style="padding: 0.75rem;">1개</td>
                    <td style="padding: 0.75rem;">공익사업, 특허</td>
                    <td style="padding: 0.75rem;">중간고사 후</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; font-weight: 600;">과점</td>
                    <td style="padding: 0.75rem;">소수</td>
                    <td style="padding: 0.75rem;">자동차 산업</td>
                    <td style="padding: 0.75rem;">중간고사 후</td>
                </tr>
            </table>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"과점이 실제로 대부분의 시장이 보이는 방식입니다. 경쟁하는 기업이 있지만, 너무 많지는 않아요. 자동차 산업을 생각해 보세요. 자동차 회사가 하나 이상 있지만, 1,000개는 없잖아요."</em></p>
            </div>
        </div>
    </section>

    <!-- 2. Perfect Competition -->
    <section class="section fade-in-delay">
        <h2 class="section-title">2. 완전경쟁: 정의와 가정</h2>
        <div class="section-content">
            
            <h4>2.1 핵심 정의</h4>
            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p><strong>가격수용자(Price-Takers):</strong> 완전경쟁 시장에서 모든 기업은 <strong>가격수용자</strong>입니다. 어떤 개별 기업의 행동도 시장 가격에 영향을 미칠 수 없습니다.</p>
            </div>

            <h4>2.2 언제 성립하는가? 완전탄력적 기업 수요</h4>
            
            <div style="text-align: center; margin: 1.5rem 0;">
                <img src="/assets/images/fig7-1-perfectly-elastic-demand.png" alt="Figure 7-1: 완전탄력적 수요" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <p style="color: #6b7280; font-size: 0.9rem; margin-top: 0.5rem;"><strong>Figure 7-1:</strong> 완전경쟁에서 각 기업은 완전탄력적 수요에 직면. 주의: x축은 <strong>소문자 q</strong> (기업), 대문자 Q (시장)가 아님.</p>
            </div>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"이건 시장 수요가 완전탄력적이라는 말이 아닙니다. 특정 기업에 대한 수요가 매우 탄력적이라는 거예요. 에펠탑 조각상에 대한 수요 전체가 완전탄력적이라는 게 아니라, 판매자들 사이에서 기업별 수요가 완전탄력적이라는 거죠."</em></p>
            </div>

            <h4>2.3 세 가지 핵심 가정</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">#</th>
                    <th style="padding: 0.75rem; text-align: left;">가정</th>
                    <th style="padding: 0.75rem; text-align: left;">의미</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">1</td>
                    <td style="padding: 0.75rem;">동일한 제품</td>
                    <td style="padding: 0.75rem;">모든 기업이 정확히 같은 것을 판매</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">2</td>
                    <td style="padding: 0.75rem;">완전한 가격 정보</td>
                    <td style="padding: 0.75rem;">모든 소비자가 모든 기업의 가격을 앎</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; font-weight: 600;">3</td>
                    <td style="padding: 0.75rem;">거래비용 없음</td>
                    <td style="padding: 0.75rem;">어떤 기업에서든 쉽게 쇼핑 가능</td>
                </tr>
            </table>

            <h4>2.4 에펠탑 열쇠고리 예시</h4>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"에펠탑을 생각해 보세요. 말 그대로 수백 명의 사람들이 담요를 펴고 똑같은 에펠탑 열쇠고리를 팔고 있어요. 사람들이 얼마를 받는지 쉽게 볼 수 있죠. 서로 바로 옆에 있으니까요. 거래비용이 거의 없어요. 같은 열쇠고리라는 걸 알 수 있고요."</em></p>
                <p style="margin-top: 0.5rem;"><strong>결과:</strong> 한 학생이 확인한 결과, 에펠탑 바로 근처의 모든 판매자들이 동일한 가격을 받았습니다! 하지만 멀리 가면 가격이 달랐어요 (다른 위치 = 더 이상 동일하지 않음).</p>
            </div>
        </div>
    </section>

    <!-- 3. Profit Maximization -->
    <section class="section fade-in-delay">
        <h2 class="section-title">3. 완전경쟁에서의 이윤 극대화</h2>
        <div class="section-content">
            
            <h4>3.1 기업의 목표</h4>
            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p style="font-family: monospace; text-align: center; font-size: 1.2rem;">
                    max π(q) = R(q) - C(q)
                </p>
                <p style="text-align: center; color: #6b7280;">여기서 R(q) = 수입, C(q) = 비용</p>
            </div>

            <h4>3.2 1차 조건</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>미분하고 0으로 설정:</strong></p>
                <p style="font-family: monospace; margin-left: 1rem;">dπ/dq = dR/dq - dC/dq = 0</p>
                <p style="font-family: monospace; margin-left: 1rem; margin-top: 0.5rem;"><strong>MR = MC</strong></p>
            </div>

            <div style="background: #dcfce7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p style="font-size: 1.1rem; font-weight: 600; text-align: center;">
                    일반 규칙: 한계수입 = 한계비용
                </p>
            </div>

            <h4>3.3 완전경쟁에서: MR = P</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"경쟁 시장에서 한계수입이 뭔지 알아요. 다음 단위를 팔면 뭘 얻나요? 시장 가격 p를 얻죠. 그건 주어진 거예요. 한계수입은 항상 p입니다."</em></p>
            </div>

            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p style="font-size: 1.3rem; font-weight: 600; text-align: center; color: #2563eb;">
                    P = MC
                </p>
                <p style="text-align: center; color: #6b7280;">완전경쟁에서의 이윤 극대화 규칙</p>
            </div>
        </div>
    </section>

    <!-- 4. Worked Example -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4. 예제: 최적 생산량과 이윤 찾기</h2>
        <div class="section-content">
            
            <h4>4.1 설정</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <ul>
                    <li>비용함수: <strong>C(q) = 10 + 5q²</strong></li>
                    <li>시장 가격: <strong>p = 30</strong></li>
                    <li>한계비용: <strong>MC = dC/dq = 10q</strong></li>
                </ul>
            </div>

            <h4>4.2 최적 생산량 찾기</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>P = MC 설정:</strong></p>
                <p style="font-family: monospace; margin-left: 1rem;">30 = 10q</p>
                <p style="font-family: monospace; margin-left: 1rem;"><strong>q* = 3</strong></p>
            </div>

            <div style="text-align: center; margin: 1.5rem 0;">
                <img src="/assets/images/fig7-2-profit-maximization.png" alt="Figure 7-2: 이윤 극대화" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <p style="color: #6b7280; font-size: 0.9rem; margin-top: 0.5rem;"><strong>Figure 7-2:</strong> 왼쪽: 수입(R)과 비용(C) 곡선. 오른쪽: q = 3에서 최대를 보여주는 이윤 곡선.</p>
            </div>

            <h4>4.3 언덕 오르기 직관</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"구름 속에 있는 산을 오르고 있다고 생각해 보세요. 산 정상에 가려고 하는데, 한 발짝 앞밖에 볼 수 없어요. 앞으로 한 발 내딛고 올라가면, 산 위로 가고 있는 거예요. 앞으로 한 발 내딛고 내려가면, 산 아래로 가는 거죠."</em></p>
            </div>

            <h4>4.4 이윤 계산</h4>
            <div style="text-align: center; margin: 1.5rem 0;">
                <img src="/assets/images/fig7-3-cost-curves-profit.png" alt="Figure 7-3: 이윤 직사각형" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <p style="color: #6b7280; font-size: 0.9rem; margin-top: 0.5rem;"><strong>Figure 7-3:</strong> 이윤 = (P - ATC) × q = 파란색 직사각형.</p>
            </div>

            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>단계 1: q = 3에서 평균비용 찾기</strong></p>
                <p style="font-family: monospace; margin-left: 1rem;">AC = C(q)/q = (10 + 5q²)/q = 10/q + 5q</p>
                <p style="font-family: monospace; margin-left: 1rem;">AC(3) = 10/3 + 5(3) = 3.33 + 15 = <strong>18.33</strong></p>
                
                <p style="margin-top: 1rem;"><strong>단계 2: 단위당 이윤 계산</strong></p>
                <p style="font-family: monospace; margin-left: 1rem;">단위당 이윤 = P - AC = 30 - 18.33 = <strong>11.67</strong></p>
                
                <p style="margin-top: 1rem;"><strong>단계 3: 총이윤 계산</strong></p>
                <p style="font-family: monospace; margin-left: 1rem;">π = (P - AC) × q = 11.67 × 3 ≈ <strong>35</strong></p>
            </div>

            <div style="background: #dcfce7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p style="text-align: center;"><strong>이윤 = (가격 - 평균비용) × 수량</strong></p>
                <p style="text-align: center; color: #6b7280;">이것이 Figure 7-3의 파란색 직사각형 면적</p>
            </div>
        </div>
    </section>

    <!-- 5. Effect of a Tax -->
    <section class="section fade-in-delay">
        <h2 class="section-title">5. 스트레스 테스트: 세금이 부과되면?</h2>
        <div class="section-content">
            
            <h4>5.1 단위당 $10 세금 추가</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>질문:</strong> 기업이 판매 단위당 $10를 지불해야 하면 어떻게 될까요?</p>
                <p style="margin-top: 0.5rem;"><strong>새 비용함수:</strong></p>
                <p style="font-family: monospace; margin-left: 1rem;">C(q) = 10 + 5q² + 10q</p>
                <p style="color: #dc2626; margin-top: 0.5rem;"><em>주의: 20 + 5q²가 아닙니다. 세금은 단위당이지, 고정액이 아니에요!</em></p>
            </div>

            <h4>5.2 새로운 최적 생산량</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>새 MC:</strong> d(10 + 5q² + 10q)/dq = 10q + 10</p>
                <p style="margin-top: 0.5rem;"><strong>P = MC 설정:</strong></p>
                <p style="font-family: monospace; margin-left: 1rem;">30 = 10q + 10</p>
                <p style="font-family: monospace; margin-left: 1rem;"><strong>q* = 2</strong> (3에서 감소)</p>
            </div>

            <div style="text-align: center; margin: 1.5rem 0;">
                <img src="/assets/images/fig7-4-cost-curves-tax.png" alt="Figure 7-4: 세금의 효과" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <p style="color: #6b7280; font-size: 0.9rem; margin-top: 0.5rem;"><strong>Figure 7-4:</strong> 세금으로 MC가 위로 이동. 이윤 직사각형이 너비(적은 단위)와 높이(단위당 낮은 이윤) 모두 줄어듦.</p>
            </div>

            <h4>5.3 이윤에 대한 두 가지 효과</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">효과</th>
                    <th style="padding: 0.75rem; text-align: left;">세금 전</th>
                    <th style="padding: 0.75rem; text-align: left;">세금 후</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">수량 (너비)</td>
                    <td style="padding: 0.75rem;">3</td>
                    <td style="padding: 0.75rem; color: #dc2626;">2 ↓</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">단위당 이윤 (높이)</td>
                    <td style="padding: 0.75rem;">11.67</td>
                    <td style="padding: 0.75rem; color: #dc2626;">더 낮음 ↓</td>
                </tr>
                <tr style="background: #fef2f2;">
                    <td style="padding: 0.75rem; font-weight: 600;">총이윤</td>
                    <td style="padding: 0.75rem;">~35</td>
                    <td style="padding: 0.75rem; color: #dc2626; font-weight: 600;">훨씬 작음</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- 6. The Shutdown Rule -->
    <section class="section fade-in-delay">
        <h2 class="section-title">6. 폐업 규칙: 언제 생산을 중단할까</h2>
        <div class="section-content">
            
            <h4>6.1 핵심 통찰: 손실 ≠ 폐업</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"단기에서 손실이 반드시 폐업의 이유는 아닙니다. 돈을 잃으면서도 사업을 계속하고 싶을 수 있어요."</em></p>
            </div>

            <h4>6.2 예시: 가격이 $10으로 하락</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>C(q) = 10 + 5q²이고 p = 10일 때:</strong></p>
                <ul>
                    <li>MC = 10q, 그래서 p = MC에서: q* = 1</li>
                    <li>수입 = 10 × 1 = 10</li>
                    <li>비용 = 10 + 5(1)² = 15</li>
                    <li>이윤 = 10 - 15 = <strong>-5 (손실!)</strong></li>
                </ul>
            </div>

            <h4>6.3 폐업해야 할까?</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>q = 1 생산하면:</strong> 이윤 = -5</p>
                <p><strong>q = 0 생산하면:</strong> 이윤 = -10 (고정비용은 여전히 지불!)</p>
                <p style="margin-top: 0.5rem; color: #16a34a; font-weight: 600;">폐업하고 10을 잃는 것보다 생산하고 5를 잃는 게 낫다!</p>
            </div>

            <h4>6.4 폐업 규칙</h4>
            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p style="font-family: monospace; text-align: center; font-size: 1.2rem;">
                    폐업 조건: P < AVC
                </p>
                <p style="text-align: center; color: #6b7280;">가격이 가변비용을 충당하는 한 계속 생산</p>
            </div>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"고정비용은 단기에서 매몰되어 있어요. 무관합니다. 이미 지불했어요. 그냥 다음 단위에 대해 물어보세요: 돈을 벌까?"</em></p>
            </div>

            <h4>6.5 우리 예제에서: 절대 폐업 안 함</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>C(q) = 10 + 5q²의 경우:</strong></p>
                <ul>
                    <li>VC = 5q²</li>
                    <li>AVC = 5q</li>
                    <li>최적에서 (MC = P): 10q = P → q = P/10</li>
                    <li>따라서 AVC = 5(P/10) = 0.5P</li>
                </ul>
                <p style="margin-top: 0.5rem; color: #16a34a; font-weight: 600;">AVC = 0.5P < P 항상 성립하므로, 이 비용함수로는 기업이 절대 폐업하지 않음.</p>
            </div>
        </div>
    </section>

    <!-- 7. Deriving the Supply Curve -->
    <section class="section fade-in-delay">
        <h2 class="section-title">7. 공급곡선 유도</h2>
        <div class="section-content">
            
            <h4>7.1 기업의 공급 결정</h4>
            <div style="text-align: center; margin: 1.5rem 0;">
                <img src="/assets/images/fig7-5-firm-supply-decision.png" alt="Figure 7-5: 기업 공급 결정" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <p style="color: #6b7280; font-size: 0.9rem; margin-top: 0.5rem;"><strong>Figure 7-5:</strong> 각 가격에서 기업은 P = MC인 곳에서 생산.</p>
            </div>

            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <ul>
                    <li>P = 10일 때: q = 1 생산</li>
                    <li>P = 20일 때: q = 2 생산</li>
                    <li>P = 30일 때: q = 3 생산</li>
                    <li>P = 40일 때: q = 4 생산</li>
                </ul>
            </div>

            <h4>7.2 핵심 통찰</h4>
            <div style="background: #dcfce7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p style="font-size: 1.1rem; font-weight: 600; text-align: center;">
                    공급곡선 = 한계비용 곡선
                </p>
            </div>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"수요곡선은 재화에 대한 한계 지불의사였어요. 공급곡선은 다음 재화를 생산하는 한계비용입니다."</em></p>
            </div>

            <h4>7.3 단기 기업 공급곡선</h4>
            <div style="text-align: center; margin: 1.5rem 0;">
                <img src="/assets/images/fig7-6-sr-firm-supply.png" alt="Figure 7-6: 단기 기업 공급" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <p style="color: #6b7280; font-size: 0.9rem; margin-top: 0.5rem;"><strong>Figure 7-6:</strong> 단기 기업 공급곡선 S = MC = 10q.</p>
            </div>

            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p><strong>기술적 정의:</strong></p>
                <p style="text-align: center;">단기 공급곡선 = <strong>폐업점 위의</strong> MC 곡선</p>
                <p style="text-align: center; color: #6b7280;">(최소 AVC 위)</p>
            </div>

            <h4>7.4 장기 vs 단기 공급</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;"></th>
                    <th style="padding: 0.75rem; text-align: left;">단기</th>
                    <th style="padding: 0.75rem; text-align: left;">장기</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">공급곡선</td>
                    <td style="padding: 0.75rem;">최소 AVC 위의 MC</td>
                    <td style="padding: 0.75rem;">MC (그냥)</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">폐업 규칙</td>
                    <td style="padding: 0.75rem;">P < AVC</td>
                    <td style="padding: 0.75rem;">π < 0</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; font-weight: 600;">이유</td>
                    <td style="padding: 0.75rem;">나중에 K를 재최적화 가능</td>
                    <td style="padding: 0.75rem;">이미 모든 것을 최적화함</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- 8. From Firm to Market Supply -->
    <section class="section fade-in-delay">
        <h2 class="section-title">8. 기업 공급에서 시장 공급으로</h2>
        <div class="section-content">
            
            <div style="text-align: center; margin: 1.5rem 0;">
                <img src="/assets/images/fig7-7-sr-market-supply.png" alt="Figure 7-7: 시장 공급" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <p style="color: #6b7280; font-size: 0.9rem; margin-top: 0.5rem;"><strong>Figure 7-7:</strong> 동일한 기업을 추가하면 시장 공급이 더 탄력적. S₁ = 1개 기업, S₂ = 2개 기업, S₃ = 3개 기업.</p>
            </div>

            <h4>8.1 기업 공급 합산</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>n개의 동일한 기업:</strong></p>
                <ul>
                    <li>각 기업: q = P/10</li>
                    <li>시장: Q = n × (P/10)</li>
                </ul>
            </div>

            <h4>8.2 핵심 통찰: 더 많은 기업 = 더 탄력적 공급</h4>
            <div style="background: #dcfce7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p style="font-size: 1.1rem; font-weight: 600; text-align: center;">
                    더 많은 동일한 기업 → 더 평평한 (더 탄력적인) 시장 공급곡선
                </p>
            </div>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"경쟁 시장에 무한히 많은 기업이 있고, 기업이 많을수록 공급곡선이 더 탄력적이라면, 공급곡선에 어떤 의미가 있는지 생각해 보세요..."</em></p>
                <p style="color: #6b7280; margin-top: 0.5rem;">(다음 강의에서 탐구합니다!)</p>
            </div>
        </div>
    </section>

    <!-- 9. Full Equilibrium Derivation -->
    <section class="section fade-in-delay">
        <h2 class="section-title">9. 모든 것을 종합: 완전 균형</h2>
        <div class="section-content">
            
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"이것이 MIT에서 배우는 아름다움이에요. 이걸 하는 입문 경제학 강의는 찾을 수 없을 거예요. Paul Samuelson이 이 수업을 가르치기 전에는 사람들이 그래프만 가르치고 끝냈어요. 수학을 원하세요? 수학을 드리죠."</em></p>
            </div>

            <h4>단계 A: 공급곡선 구하기</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>1. 생산함수로 시작:</strong> q = √(L × K)</p>
                <p><strong>2. 주어진 것:</strong> w = 5, r = 10, K̄ = 1</p>
                <p><strong>3. 비용함수 유도:</strong> C(q) = 10 + 5q²</p>
                <p><strong>4. MC 구하기:</strong> MC = 10q</p>
                <p><strong>5. 기업 공급 (P = MC):</strong> q = P/10</p>
            </div>

            <h4>단계 B: 시장 공급곡선 만들기</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>n = 6개 기업 가정</strong></p>
                <p style="font-family: monospace; margin-left: 1rem;">Q = 6 × (P/10) = 3P/5</p>
                <p style="margin-top: 0.5rem;"><strong>시장 공급:</strong> Q = (3/5)P</p>
            </div>

            <h4>단계 C: 수요곡선 구하기</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>소비자 이론에서:</strong> Q = 48 - P</p>
            </div>

            <h4>단계 D: 균형 찾기</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>공급 = 수요 설정:</strong></p>
                <p style="font-family: monospace; margin-left: 1rem;">(3/5)P = 48 - P</p>
                <p style="font-family: monospace; margin-left: 1rem;">(8/5)P = 48</p>
                <p style="font-family: monospace; margin-left: 1rem;"><strong>P* = 30</strong></p>
                <p style="font-family: monospace; margin-left: 1rem;"><strong>Q* = 18</strong></p>
            </div>

            <h4>단계 E: 개별 기업 행동 확인</h4>
            <div style="background: #dcfce7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <ul>
                    <li>시장 수량 Q* = 18</li>
                    <li>6개 동일 기업: 각각 q* = 18/6 = <strong>3</strong> 생산</li>
                    <li>확인: P = 30에서 기업은 MC = P 설정 → 10q = 30 → q = 3 ✓</li>
                </ul>
                <p style="margin-top: 0.5rem; font-weight: 600; text-align: center;">시장의 마법: 모두가 만족!</p>
            </div>
        </div>
    </section>

    <!-- Summary -->
    <section class="section fade-in-delay">
        <h2 class="section-title">핵심 요약</h2>
        <div class="section-content">
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; width: 5%;">#</th>
                    <th style="padding: 0.75rem; width: 30%;">개념</th>
                    <th style="padding: 0.75rem;">핵심 포인트</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">1</td>
                    <td style="padding: 0.75rem; font-weight: 600;">시장 구조</td>
                    <td style="padding: 0.75rem;">얼마나 생산할지 결정하는 "세 번째 요소"</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">2</td>
                    <td style="padding: 0.75rem; font-weight: 600;">완전경쟁</td>
                    <td style="padding: 0.75rem;">기업은 가격수용자; 완전탄력적 수요에 직면</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">3</td>
                    <td style="padding: 0.75rem; font-weight: 600;">이윤 극대화 규칙</td>
                    <td style="padding: 0.75rem;">MR = MC; 경쟁에서: P = MC</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">4</td>
                    <td style="padding: 0.75rem; font-weight: 600;">이윤 계산</td>
                    <td style="padding: 0.75rem;">π = (P - AC) × q = 이윤 직사각형</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">5</td>
                    <td style="padding: 0.75rem; font-weight: 600;">폐업 규칙</td>
                    <td style="padding: 0.75rem;">단기: P < AVC면 폐업; 장기: π < 0이면 폐업</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">6</td>
                    <td style="padding: 0.75rem; font-weight: 600;">공급곡선</td>
                    <td style="padding: 0.75rem;">= MC 곡선 (단기에서 폐업점 위)</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; text-align: center;">7</td>
                    <td style="padding: 0.75rem; font-weight: 600;">시장 공급</td>
                    <td style="padding: 0.75rem;">기업 공급의 합; 더 많은 기업 = 더 탄력적</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- What's Next -->
    <section class="section fade-in-delay">
        <h2 class="section-title">다음 내용은?</h2>
        <div class="section-content">
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>다음:</strong> 경쟁 II - 무한히 많은 기업이 있으면 어떻게 될까? 장기 균형과 진입/퇴출의 역할.</p>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <section class="section fade-in-delay">
        <div class="section-content" style="text-align: center; color: #6b7280; font-size: 0.9rem;">
            <p><a href="/study/mit-1401-overview-ko">← 코스 개요로 돌아가기</a></p>
        </div>
    </section>
</div>
