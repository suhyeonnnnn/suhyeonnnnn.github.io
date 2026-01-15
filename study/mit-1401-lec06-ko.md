---
layout: minimal_base
title: "MIT 14.01 Lec 6: 비용"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Lecture 6: 비용 (Costs)</h2>
            <a href="/study/mit-1401-lec06" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">English</a>
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
                "오늘은 생산자 이론의 핵심 구성요소인 단기 비용곡선에 대해 이야기하겠습니다. 기업이 이윤을 극대화하는 방법은 비용을 최소화하는 것, 즉 최소 비용으로 가능한 효율적으로 재화를 생산하는 것입니다."
            </blockquote>
            <p>이 강의는 생산함수를 비용함수로 변환하고, 한계비용과 평균비용의 핵심 개념을 소개하며, 기업이 단기와 장기에서 어떻게 비용을 최소화하는지 보여줍니다. 또한 회계 비용과 경제적(기회) 비용의 중요한 차이를 탐구합니다.</p>
        </div>
    </section>

    <!-- 1. From Production to Costs -->
    <section class="section fade-in-delay">
        <h2 class="section-title">1. 생산함수에서 비용함수로</h2>
        <div class="section-content">
            
            <h4>1.1 왜 비용에 관심을 갖는가?</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"기업이 이윤을 극대화하는 방법은 비용을 최소화하는 것입니다. 최소 비용으로 가능한 효율적으로 재화를 생산하는 것이죠."</em></p>
            </div>

            <h4>1.2 비용함수</h4>
            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p><strong>정의:</strong> <strong>비용함수</strong> C(q)는 수량 q를 생산하는 데 드는 총비용을 알려줍니다.</p>
                <p style="font-family: monospace; text-align: center; margin-top: 0.5rem; font-size: 1.2rem;">
                    C(q) = r·K̄ + w·L(q)
                </p>
                <p style="text-align: center; color: #6b7280; font-size: 0.9rem;">
                    여기서 r = 자본의 임대율, w = 임금, K̄ = 고정 자본, L(q) = q에 필요한 노동
                </p>
            </div>

            <h4>1.3 비용함수 유도: 예제</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>주어진 조건:</strong></p>
                <ul>
                    <li>생산함수: q = √(L × K)</li>
                    <li>임금: w = 5</li>
                    <li>임대율: r = 10</li>
                    <li>고정 자본: K̄ = 1</li>
                </ul>
                
                <p style="margin-top: 1rem;"><strong>단계 1:</strong> 생산함수를 L에 대해 풀기</p>
                <p style="font-family: monospace; margin-left: 1rem;">q = √(L × K̄) → q² = L × K̄ → L = q²/K̄</p>
                
                <p style="margin-top: 0.5rem;"><strong>단계 2:</strong> 비용함수에 대입</p>
                <p style="font-family: monospace; margin-left: 1rem;">C(q) = r·K̄ + w·L = 10(1) + 5(q²/1) = 10 + 5q²</p>
                
                <div style="background: #dcfce7; padding: 0.75rem; border-radius: 4px; margin-top: 1rem;">
                    <p style="text-align: center; font-weight: 600;">최종 비용함수: C(q) = 10 + 5q²</p>
                </div>
            </div>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"w와 r이 어디서 오는지는 몇 강의 후에 가르쳐 드릴게요. 이 수업에서는 양파 껍질 벗기듯이 미스터리를 천천히 밝혀갑니다. 지금은 그냥 주어진 것으로 받아들이세요."</em></p>
            </div>
        </div>
    </section>

    <!-- 2. Types of Costs -->
    <section class="section fade-in-delay">
        <h2 class="section-title">2. 비용의 유형</h2>
        <div class="section-content">
            
            <h4>2.1 핵심 정의</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">비용 유형</th>
                    <th style="padding: 0.75rem; text-align: left;">정의</th>
                    <th style="padding: 0.75rem; text-align: left;">예제에서</th>
                    <th style="padding: 0.75rem; text-align: left;">공식</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">고정비용 (FC)</td>
                    <td style="padding: 0.75rem;">단기에 변하지 않는 비용</td>
                    <td style="padding: 0.75rem; font-family: monospace;">10</td>
                    <td style="padding: 0.75rem; font-family: monospace;">r·K̄</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">가변비용 (VC)</td>
                    <td style="padding: 0.75rem;">단기에 변할 수 있는 비용</td>
                    <td style="padding: 0.75rem; font-family: monospace;">5q²</td>
                    <td style="padding: 0.75rem; font-family: monospace;">w·L(q)</td>
                </tr>
                <tr style="background: #f0fdf4;">
                    <td style="padding: 0.75rem; font-weight: 600;">총비용 (TC)</td>
                    <td style="padding: 0.75rem;">고정비용과 가변비용의 합</td>
                    <td style="padding: 0.75rem; font-family: monospace;">10 + 5q²</td>
                    <td style="padding: 0.75rem; font-family: monospace;">FC + VC</td>
                </tr>
            </table>

            <h4>2.2 한계비용: 핵심 개념</h4>
            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p><strong>한계비용 (MC):</strong> <em>한 단위 더</em> 생산하는 데 드는 비용</p>
                <p style="font-family: monospace; text-align: center; margin-top: 0.5rem; font-size: 1.3rem;">
                    MC = dC/dq = dVC/dq
                </p>
                <p style="text-align: center; color: #6b7280; font-size: 0.9rem;">
                    (단기에서 dTC/dq = dVC/dq, 고정비용은 변하지 않으므로)
                </p>
            </div>

            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>우리 예제에서:</strong></p>
                <p style="font-family: monospace; margin-left: 1rem;">MC = d(10 + 5q²)/dq = <strong>10q</strong></p>
            </div>

            <h4>2.3 평균비용</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">평균비용 유형</th>
                    <th style="padding: 0.75rem; text-align: left;">공식</th>
                    <th style="padding: 0.75rem; text-align: left;">예제에서</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">평균고정비용 (AFC)</td>
                    <td style="padding: 0.75rem; font-family: monospace;">FC/q</td>
                    <td style="padding: 0.75rem; font-family: monospace;">10/q</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">평균가변비용 (AVC)</td>
                    <td style="padding: 0.75rem; font-family: monospace;">VC/q</td>
                    <td style="padding: 0.75rem; font-family: monospace;">5q</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; font-weight: 600;">평균(총)비용 (AC)</td>
                    <td style="padding: 0.75rem; font-family: monospace;">TC/q = AFC + AVC</td>
                    <td style="padding: 0.75rem; font-family: monospace;">10/q + 5q</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- 3. Cost Curves Graph -->
    <section class="section fade-in-delay">
        <h2 class="section-title">3. 비용곡선: 그래프 분석</h2>
        <div class="section-content">
            
            <div style="text-align: center; margin: 1.5rem 0;">
                <img src="/assets/images/fig6-1-cost-curves.png" alt="Figure 6-1: 비용곡선" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <p style="color: #6b7280; font-size: 0.9rem; margin-top: 0.5rem;"><strong>Figure 6-1:</strong> C(q) = 10 + 5q²의 비용곡선. MC, AC, AVC, AFC를 보여줍니다.</p>
            </div>

            <h4>3.1 곡선 모양 이해하기</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">곡선</th>
                    <th style="padding: 0.75rem; text-align: left;">모양</th>
                    <th style="padding: 0.75rem; text-align: left;">이유</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">MC = 10q</td>
                    <td style="padding: 0.75rem;">우상향 (선형)</td>
                    <td style="padding: 0.75rem;">추가 단위마다 비용 증가 (노동의 수확체감)</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">AFC = 10/q</td>
                    <td style="padding: 0.75rem;">항상 하락 (쌍곡선)</td>
                    <td style="padding: 0.75rem;">고정비용이 더 많은 단위에 분산</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">AVC = 5q</td>
                    <td style="padding: 0.75rem;">항상 상승 (선형)</td>
                    <td style="padding: 0.75rem;">노동의 한계생산물 체감</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; font-weight: 600;">AC = 10/q + 5q</td>
                    <td style="padding: 0.75rem;">U자형 (먼저 하락, 후에 상승)</td>
                    <td style="padding: 0.75rem;">처음엔 AFC가 끌어내리고, 후에 AVC가 끌어올림</td>
                </tr>
            </table>

            <h4>3.2 평균비용이 U자형인 이유</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"평균비용은 먼저 하락했다가 상승합니다. 왜 그럴까요? 처음에는 갚아야 할 큰 고정비용이 있기 때문이에요. 하지만 시간이 지나면 가변비용에 비해 고정비용이 작아집니다."</em></p>
            </div>

            <h4>3.3 핵심 관계: MC가 AC의 최솟값에서 교차</h4>
            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p><strong>핵심 규칙:</strong> 한계비용은 평균비용의 최솟값에서 평균비용과 교차합니다.</p>
            </div>

            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>직관:</strong></p>
                <ul>
                    <li>MC < AC: 한 단위 더 생산하면 평균이 내려감 → AC 하락</li>
                    <li>MC > AC: 한 단위 더 생산하면 평균이 올라감 → AC 상승</li>
                    <li>MC = AC: 평균이 상승도 하락도 안 함 → 최솟값!</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- 4. MC and MPL Relationship -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4. 한계비용과 한계생산물의 관계</h2>
        <div class="section-content">
            
            <h4>4.1 관계 유도</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>시작:</strong> C = r·K̄ + w·L</p>
                <p style="margin-top: 0.5rem;"><strong>q에 대해 미분:</strong></p>
                <p style="font-family: monospace; margin-left: 1rem;">MC = dC/dq = w · (dL/dq)</p>
                <p style="margin-top: 0.5rem;"><strong>그런데:</strong> MP<sub>L</sub> = dq/dL 이므로, dL/dq = 1/MP<sub>L</sub></p>
            </div>

            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p style="font-family: monospace; text-align: center; font-size: 1.3rem;">
                    MC = w / MP<sub>L</sub>
                </p>
            </div>

            <h4>4.2 해석</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"다음 단위 재화를 생산하는 한계비용은 노동자에게 얼마를 지불하느냐가 높을수록 높고, 각 노동자가 얼마나 생산적이냐가 높을수록 낮습니다."</em></p>
            </div>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">만약...</th>
                    <th style="padding: 0.75rem; text-align: left;">그러면 MC...</th>
                    <th style="padding: 0.75rem; text-align: left;">직관</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">w ↑ (임금 상승)</td>
                    <td style="padding: 0.75rem; color: #dc2626; font-weight: 600;">MC ↑</td>
                    <td style="padding: 0.75rem;">노동이 비싸짐 → 단위당 비용 증가</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem;">MP<sub>L</sub> ↑ (생산성 상승)</td>
                    <td style="padding: 0.75rem; color: #16a34a; font-weight: 600;">MC ↓</td>
                    <td style="padding: 0.75rem;">각 노동자가 더 많이 생산 → 단위당 노동자 수 감소</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem;">MP<sub>L</sub> ↓ (수확체감)</td>
                    <td style="padding: 0.75rem; color: #dc2626; font-weight: 600;">MC ↑</td>
                    <td style="padding: 0.75rem;">이것이 MC 곡선이 우상향하는 이유!</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- 5. Sunk Costs -->
    <section class="section fade-in-delay">
        <h2 class="section-title">5. 매몰비용: 중요한 구분</h2>
        <div class="section-content">
            
            <h4>5.1 고정비용 vs 매몰비용</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"지난 강의에서 장기에는 모든 투입물이 가변적이라고 했죠. 그걸 이미 철회할게요. 장기에도 가변적이지 않은 비용이 있어요. 그걸 매몰비용이라고 합니다."</em></p>
            </div>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;">비용 유형</th>
                    <th style="padding: 0.75rem; text-align: left;">정의</th>
                    <th style="padding: 0.75rem; text-align: left;">회수 가능?</th>
                    <th style="padding: 0.75rem; text-align: left;">예시</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">고정비용</td>
                    <td style="padding: 0.75rem;">단기 고정, 장기 가변</td>
                    <td style="padding: 0.75rem; color: #16a34a; font-weight: 600;">예 (팔 수 있음)</td>
                    <td style="padding: 0.75rem;">기계, 건물</td>
                </tr>
                <tr style="background: #fef2f2;">
                    <td style="padding: 0.75rem; font-weight: 600;">매몰비용</td>
                    <td style="padding: 0.75rem;">장기에도 절대 회수 불가</td>
                    <td style="padding: 0.75rem; color: #dc2626; font-weight: 600;">아니오 (영원히 사라짐)</td>
                    <td style="padding: 0.75rem;">의대 학비, 광고</td>
                </tr>
            </table>

            <h4>5.2 매몰비용 오류</h4>
            <div style="background: #fef2f2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p style="font-size: 1.1rem; font-weight: 600; text-align: center; color: #dc2626;">
                    "매몰비용은 일단 지불하면 의사결정과 무관합니다."
                </p>
                <p style="text-align: center; margin-top: 0.5rem;"><em>"경제학자들이 말하듯이, 매몰비용은 매몰된 거예요. 상관없어요. 무관해요."</em></p>
            </div>

            <h4>5.3 저니 콘서트 예시</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Gruber의 이야기:</strong></p>
                <ul>
                    <li>저니 콘서트 티켓을 장당 $125에 구매 (총 $250)</li>
                    <li>셋리스트를 보고 좋아하는 노래가 3곡뿐임을 깨달음</li>
                    <li>StubHub에서 티켓을 팔기로 결정</li>
                </ul>
                
                <p style="margin-top: 1rem;"><strong>질문:</strong> 지불한 $250이 StubHub에서 설정할 가격에 어떻게 영향을 미쳐야 할까요?</p>
                
                <div style="background: #dcfce7; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                    <p style="font-weight: 600;">답: 영향을 미치면 안 됩니다! 매몰비용이니까요.</p>
                    <p><em>"이미 지불했어요. 무관해요. 끝났어요. 이미 250을 냈어요. 사라졌어요. 슬플 수 있지만, 사라진 거예요."</em></p>
                </div>
            </div>

            <h4>5.4 가격을 결정해야 하는 것은?</h4>
            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>가는 것의 기회비용!</strong></p>
                <ul>
                    <li>정말 가고 싶지 않다면 → $0에도 팔 의향</li>
                    <li>$50 내고 갈 의향이 있다면 → 최소 가격 $50</li>
                    <li>누군가 당신의 가치보다 더 주면 → 팔기</li>
                    <li>누군가 당신의 가치보다 덜 주면 → 티켓 갖고 가기</li>
                </ul>
            </div>

            <h4>5.5 학생 Q&A: "하지만 매몰비용을 회수하고 싶어요!"</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>학생:</strong> "매몰비용을 회수하려고 생각할 것 같아요."</p>
                <p><strong>Gruber:</strong> <em>"네, 그럴 거예요. 사람들이 그렇게 생각하니까요. 하지만 틀렸어요."</em></p>
                <p style="margin-top: 0.5rem;"><em>"이렇게 생각해 보세요. 온라인에서 장당 $500에 팔 수 있다고 해요. 내가 $250 냈으니까 $250에만 팔아야 할까요? 아니요, $500에 파세요. 그러니까 $250 낸 건 무관해요."</em></p>
            </div>
        </div>
    </section>

    <!-- 6. Long-Run vs Short-Run Costs -->
    <section class="section fade-in-delay">
        <h2 class="section-title">6. 장기 vs 단기 비용</h2>
        <div class="section-content">
            
            <h4>6.1 핵심 직관</h4>
            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p style="font-size: 1.1rem; font-weight: 600; text-align: center;">
                    장기 비용 ≤ 단기 비용 (항상!)
                </p>
            </div>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"장기 비용은 항상 단기 비용의 하한입니다. 장기의 생산 비용은 항상 단기의 생산 비용과 같거나 낮아요."</em></p>
                <p style="margin-top: 0.5rem;"><strong>왜?</strong> <em>"조작할 수 있는 변수가 많을수록 더 최적화할 수 있어요."</em></p>
            </div>

            <h4>6.2 SRAC 곡선의 포락선으로서의 LRAC</h4>
            
            <div style="text-align: center; margin: 1.5rem 0;">
                <img src="/assets/images/fig6-2-lrac-envelope.png" alt="Figure 6-2: SRAC의 포락선으로서의 LRAC" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <p style="color: #6b7280; font-size: 0.9rem; margin-top: 0.5rem;"><strong>Figure 6-2:</strong> 단기 평균비용 곡선들의 포락선으로서의 장기 평균비용(LRAC).</p>
            </div>

            <h4>6.3 실제 사례: 테슬라</h4>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>테슬라 배터리 공장 이야기:</strong></p>
                
                <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                    <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                        <th style="padding: 0.75rem; text-align: left;">연도</th>
                        <th style="padding: 0.75rem; text-align: left;">상황</th>
                        <th style="padding: 0.75rem; text-align: left;">공장 규모</th>
                    </tr>
                    <tr style="border-bottom: 1px solid #e5e7eb;">
                        <td style="padding: 0.75rem;">2013</td>
                        <td style="padding: 0.75rem;">테슬라 설립, 머스크는 2017년까지 20,000대 판매 예상</td>
                        <td style="padding: 0.75rem;">작은 공장 건설 (SRAC¹)</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #e5e7eb;">
                        <td style="padding: 0.75rem;">2017</td>
                        <td style="padding: 0.75rem;">200,000명 대기자 명단! 수요 = q₃, q₁이 아님</td>
                        <td style="padding: 0.75rem; color: #dc2626;">잘못된 공장 규모!</td>
                    </tr>
                    <tr style="background: #f0fdf4;">
                        <td style="padding: 0.75rem;">2017 이후</td>
                        <td style="padding: 0.75rem;">세계 최대 배터리 공장 건설 (네바다)</td>
                        <td style="padding: 0.75rem; color: #16a34a;">SRAC³로 재최적화</td>
                    </tr>
                </table>
            </div>
        </div>
    </section>

    <!-- 7. Cost Minimization in the Long Run -->
    <section class="section fade-in-delay">
        <h2 class="section-title">7. 장기의 비용 최소화</h2>
        <div class="section-content">
            
            <h4>7.1 등비용선</h4>
            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p><strong>등비용선:</strong> 같은 총비용이 드는 L과 K의 모든 조합.</p>
                <p style="font-family: monospace; text-align: center; margin-top: 0.5rem; font-size: 1.2rem;">
                    C = w·L + r·K
                </p>
                <p style="text-align: center; color: #6b7280;">정리하면: K = C/r - (w/r)·L</p>
            </div>

            <div style="text-align: center; margin: 1.5rem 0;">
                <img src="/assets/images/fig6-3-isocost-lines.png" alt="Figure 6-3: 등비용선" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <p style="color: #6b7280; font-size: 0.9rem; margin-top: 0.5rem;"><strong>Figure 6-3:</strong> w=$5, r=$10일 때 등비용선.</p>
            </div>

            <h4>7.2 비용 최소화 조건</h4>
            <div style="text-align: center; margin: 1.5rem 0;">
                <img src="/assets/images/fig6-4-cost-minimization.png" alt="Figure 6-4: 비용 최소화" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <p style="color: #6b7280; font-size: 0.9rem; margin-top: 0.5rem;"><strong>Figure 6-4:</strong> 접점에서 비용 최소화.</p>
            </div>

            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p><strong>최적에서:</strong></p>
                <p style="font-family: monospace; text-align: center; font-size: 1.2rem;">
                    MRTS = -MP<sub>L</sub>/MP<sub>K</sub> = -w/r
                </p>
            </div>

            <h4>7.3 생산자 이론이 소비자 이론보다 어려운 이유</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"이래서 생산자 이론이 더 어려워요. 올바른 등비용선을 안 알려줬거든요. 소비자 이론에서는 예산 제약을 줬어요. 여기선 등비용선을 안 줘요."</em></p>
                
                <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                    <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                        <th style="padding: 0.75rem; text-align: left;">소비자 이론</th>
                        <th style="padding: 0.75rem; text-align: left;">생산자 이론</th>
                    </tr>
                    <tr style="border-bottom: 1px solid #e5e7eb;">
                        <td style="padding: 0.75rem;">예산이 고정 (주어진 소득)</td>
                        <td style="padding: 0.75rem;">예산이 선택 (얼마나 클지)</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.75rem;">접점에서 끝!</td>
                        <td style="padding: 0.75rem;">q를 먼저 선택해야!</td>
                    </tr>
                </table>
            </div>
        </div>
    </section>

    <!-- 8. Long-Run Expansion Path -->
    <section class="section fade-in-delay">
        <h2 class="section-title">8. 장기 확장경로</h2>
        <div class="section-content">
            
            <h4>8.1 정의</h4>
            <div style="background: #eff6ff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                <p><strong>장기 확장경로:</strong> 모든 가능한 산출량 수준 q에 대한 비용 최소화 L과 K 조합의 집합.</p>
            </div>

            <h4>8.2 선형 확장경로</h4>
            
            <div style="text-align: center; margin: 1.5rem 0;">
                <img src="/assets/images/fig6-5a-expansion-path-linear.png" alt="Figure 6-5a: 선형 확장경로" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <p style="color: #6b7280; font-size: 0.9rem; margin-top: 0.5rem;"><strong>Figure 6-5a:</strong> q = √(L×K)의 선형 확장경로. 항상 K = L/2 사용.</p>
            </div>

            <h4>8.3 비선형 확장경로</h4>

            <div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; margin: 1.5rem 0;">
                <div style="text-align: center; flex: 1; min-width: 300px;">
                    <img src="/assets/images/fig6-5b-expansion-path-capital.png" alt="Figure 6-5b" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                    <p style="color: #6b7280; font-size: 0.85rem; margin-top: 0.5rem;"><strong>Figure 6-5b:</strong> 자본이 덜 생산적 (맥도날드)</p>
                </div>
                <div style="text-align: center; flex: 1; min-width: 300px;">
                    <img src="/assets/images/fig6-5c-expansion-path-labor.png" alt="Figure 6-5c" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                    <p style="color: #6b7280; font-size: 0.85rem; margin-top: 0.5rem;"><strong>Figure 6-5c:</strong> 노동이 덜 생산적 (중장비 공장)</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 9. Accounting vs Economic Costs -->
    <section class="section fade-in-delay">
        <h2 class="section-title">9. 비용 측정: 회계 vs 경제학</h2>
        <div class="section-content">
            
            <h4>9.1 핵심 차이</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"여기서 경제학이 회계학보다 더 멋지다는 걸 알려드릴게요. 회계는 현금 흐름 비용만 고려해요. 경제학은 더 적절하게 기회비용도 고려해요."</em></p>
            </div>

            <h4>9.2 웹 디자인 스타트업 예시</h4>
            <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>시나리오:</strong> 당신(MIT 졸업생)이 졸업 후 웹 디자인 회사를 시작.</p>
                <ul>
                    <li>풀타임으로 일함 (자신에게 급여 없음)</li>
                    <li>프로그래머 1명을 연 $40,000에 고용</li>
                    <li>여분의 컴퓨터(수명 1년 남음)를 프로그래머에게 줌</li>
                    <li>1년 후, 매출 = $60,000</li>
                </ul>
            </div>

            <h4>9.3 두 가지 관점</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc; border-bottom: 2px solid #e5e7eb;">
                    <th style="padding: 0.75rem; text-align: left;"></th>
                    <th style="padding: 0.75rem; text-align: left;">회계사 엄마 👩‍💼</th>
                    <th style="padding: 0.75rem; text-align: left;">경제학자 아빠 👨‍🏫</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">매출</td>
                    <td style="padding: 0.75rem;">$60,000</td>
                    <td style="padding: 0.75rem;">$60,000</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">프로그래머 급여</td>
                    <td style="padding: 0.75rem;">-$40,000</td>
                    <td style="padding: 0.75rem;">-$40,000</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">당신의 포기한 급여</td>
                    <td style="padding: 0.75rem; color: #6b7280;">$0</td>
                    <td style="padding: 0.75rem; color: #dc2626;">-$100,000</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">컴퓨터 (팔 수 있었음)</td>
                    <td style="padding: 0.75rem; color: #6b7280;">$0</td>
                    <td style="padding: 0.75rem; color: #dc2626;">-$1,000</td>
                </tr>
                <tr style="border-top: 2px solid #e5e7eb;">
                    <td style="padding: 0.75rem; font-weight: 600;">이익</td>
                    <td style="padding: 0.75rem; color: #16a34a; font-weight: 600;">+$20,000 😊</td>
                    <td style="padding: 0.75rem; color: #dc2626; font-weight: 600;">-$81,000 😱</td>
                </tr>
            </table>

            <div style="background: #fef2f2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"기회비용은 진짜 비용이에요. 그래서 경제학을 '우울한 과학'이라고 부르는 거예요. 아무것도 공짜가 아니라는 걸 지적하거든요."</em></p>
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
                    <th style="padding: 0.75rem; width: 25%;">개념</th>
                    <th style="padding: 0.75rem;">핵심 포인트</th>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">1</td>
                    <td style="padding: 0.75rem; font-weight: 600;">비용함수</td>
                    <td style="padding: 0.75rem;">C(q) = FC + VC; 생산함수에서 유도</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">2</td>
                    <td style="padding: 0.75rem; font-weight: 600;">한계비용</td>
                    <td style="padding: 0.75rem;">MC = dC/dq = w/MP<sub>L</sub>; 수확체감으로 상승</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">3</td>
                    <td style="padding: 0.75rem; font-weight: 600;">평균비용</td>
                    <td style="padding: 0.75rem;">U자형; MC가 AC의 최솟값에서 교차</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">4</td>
                    <td style="padding: 0.75rem; font-weight: 600;">매몰비용</td>
                    <td style="padding: 0.75rem;">지불 후 의사결정과 무관</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">5</td>
                    <td style="padding: 0.75rem; font-weight: 600;">LRAC ≤ SRAC</td>
                    <td style="padding: 0.75rem;">변수가 많을수록 더 최적화 가능</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">6</td>
                    <td style="padding: 0.75rem; font-weight: 600;">비용 최소화</td>
                    <td style="padding: 0.75rem;">MRTS = w/r (접선 조건)</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 0.75rem; text-align: center;">7</td>
                    <td style="padding: 0.75rem; font-weight: 600;">확장경로</td>
                    <td style="padding: 0.75rem;">모든 산출량에 대한 비용 최소화 L,K 조합</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; text-align: center;">8</td>
                    <td style="padding: 0.75rem; font-weight: 600;">기회비용</td>
                    <td style="padding: 0.75rem;">경제적 비용 = 회계 비용 + 포기한 대안</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- What's Next -->
    <section class="section fade-in-delay">
        <h2 class="section-title">다음 내용은?</h2>
        <div class="section-content">
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><em>"다음 강의에서 q를 선택하게 해주는 추가 단계를 소개할 거예요."</em></p>
                <p style="margin-top: 0.5rem;"><strong>다음:</strong> 기업이 <em>얼마나</em> 생산할지 결정하는 방법 → 공급곡선 유도</p>
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
