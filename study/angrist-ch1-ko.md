---
layout: minimal_base
title: "Angrist Ch.1 - Questions about Questions"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Chapter 1: Questions about Questions</h2>
            <a href="/study/angrist-ch1" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">English</a>
        </div>
        <div class="section-content">
            <p><em>Angrist & Pischke, Mostly Harmless Econometrics</em></p>
        </div>
    </section>

    <!-- 핵심 메시지 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">핵심 메시지</h2>
        <div class="section-content">
            <blockquote style="border-left: 4px solid #2563eb; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                "좋은 계량경제학은 흔들리는 연구 아젠다를 구할 수 없지만, 화려한 기법의 남용은 좋은 아젠다마저 무너뜨릴 수 있다."
            </blockquote>
            <p>모든 실증 연구는 네 가지 핵심 질문(FAQs)에서 시작해야 한다.</p>
        </div>
    </section>

    <!-- FAQ 1 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">FAQ 1: 관심 있는 인과관계는 무엇인가?</h2>
        <div class="section-content">
            <p>사회과학에서 가장 흥미로운 연구는 <strong>인과관계(cause and effect)</strong>에 관한 것이다.</p>
            
            <h4>왜 인과관계인가?</h4>
            <ul>
                <li>인과관계는 <strong>반사실적(counterfactual)</strong> 세계에서 무슨 일이 일어날지 예측 가능</li>
                <li>정책 변화의 결과를 예측하는 데 유용</li>
                <li>경제 모델에서 이론적으로 도출 가능</li>
            </ul>

            <h4>예시: 교육의 인과효과</h4>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>질문:</strong> 교육이 임금에 미치는 인과효과는 무엇인가?</p>
                <p><strong>정의:</strong> 개인이 더 많은 교육을 받았을 때 얻게 되는 임금의 증가분</p>
                <p><strong>연구 결과:</strong> 대학 학위의 인과효과 ≈ 평균 <strong>40% 더 높은 임금</strong></p>
                <p><strong>활용:</strong> 대학 등록금 변화, 의무교육법 강화의 결과 예측</p>
            </div>

            <h4>분석 단위의 다양성</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">분석 단위</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">연구 예시</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">개인</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">교육 → 임금 (노동경제학)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">기업</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">R&D 투자 → 생산성</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">국가</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">식민지 제도 → 경제성장 (Acemoglu et al., 2001)</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- FAQ 2 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">FAQ 2: 이상적인 실험은 무엇인가?</h2>
        <div class="section-content">
            <p>인과효과를 포착하기 위해 <strong>가상의 이상적 실험(ideal experiment)</strong>을 구상해보라.</p>

            <h4>이상적 실험을 구상하는 이유</h4>
            <ul>
                <li>유용한 연구 주제 선택에 도움</li>
                <li>인과적 질문을 정확하게 공식화</li>
                <li>조작하고 싶은 변수와 통제하고 싶은 요인을 명확히 함</li>
            </ul>

            <blockquote style="border-left: 4px solid #dc2626; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                "아무 제약 없는 세상에서도 실험을 설계할 수 없다면, 제한된 예산과 비실험적 데이터로 유용한 결과를 얻을 가능성은 희박하다."
            </blockquote>

            <h4>예시</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>교육과 임금:</strong> 잠재적 중퇴자에게 졸업 보상을 제공하고 결과 연구 → Angrist & Lavy (2007) 실제 수행</p>
                <p><strong>정치 제도:</strong> 독립 기념일에 무작위로 다른 정부 구조 배정 → 가설적 실험</p>
            </div>

            <h4>🚫 FUQ'd: Fundamentally Unidentified Questions</h4>
            <p><strong>어떤 실험으로도 답할 수 없는 질문</strong>을 FUQ'd라고 부른다.</p>
            
            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>예시: 학교 입학 연령이 1학년 시험 성적에 미치는 영향</strong></p>
                <table style="width:100%; border-collapse: collapse; margin: 0.5rem 0;">
                    <tr style="background: #fecaca;">
                        <th style="padding: 0.5rem; border: 1px solid #ddd;">비교 방식</th>
                        <th style="padding: 0.5rem; border: 1px solid #ddd;">문제점</th>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">같은 학년에서 비교</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">늦게 입학한 학생이 더 나이가 많음 → <strong>성숙 효과</strong></td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">같은 나이에서 비교</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">일찍 입학한 학생이 학교에 더 오래 다님 → <strong>재학 기간 효과</strong></td>
                    </tr>
                </table>
                <p style="margin-top: 0.5rem;"><strong>근본적 문제:</strong> 입학 연령 = 현재 나이 - 재학 기간 (결정론적 관계)</p>
                <p><strong>해결책:</strong> 성인이 된 후의 결과(소득, 최종학력)는 연구 가능</p>
            </div>

            <h4>FUQ'd가 아닌 것: 인종/성별의 인과효과</h4>
            <p>인종이나 성별은 조작이 어려워 보이지만, 노동시장 차별 연구에서는 <strong>"인식된" 인종/성별</strong>의 효과를 연구할 수 있다.</p>
            <ul>
                <li>Shakespeare의 Rosalind가 Ganymede로 변장</li>
                <li>Philip Roth의 소설 - 흑인 교수가 백인으로 통과</li>
                <li><strong>Audit studies:</strong> 가짜 이력서를 사용한 실험 (Bertrand & Mullainathan, 2004)</li>
            </ul>
        </div>
    </section>

    <!-- FAQ 3 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">FAQ 3: 식별 전략은 무엇인가?</h2>
        <div class="section-content">
            <p><strong>식별 전략(Identification Strategy)</strong>: 관측 데이터를 사용하여 실제 실험을 근사하는 방법</p>
            
            <h4>자연실험 (Natural Experiment)</h4>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>예시: Angrist & Krueger (1991)</strong></p>
                <ul>
                    <li>의무교육법과 출생 계절의 상호작용 활용</li>
                    <li>출생 계절이 생일에 중퇴할 수 있는 정도에 영향</li>
                    <li>→ 고등학교 졸업이 임금에 미치는 효과 추정</li>
                </ul>
            </div>

            <h4>Haavelmo (1944)의 통찰</h4>
            <blockquote style="border-left: 4px solid #10b981; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                "실험 설계는 모든 정량적 이론의 필수 부록이다. 실험은 두 가지로 구분된다:<br>
                (1) 특정 가설을 검증하기 위해 우리가 하고 싶은 실험<br>
                (2) 자연이 스스로 수행하고 우리가 수동적으로 관찰하는 실험"
            </blockquote>
        </div>
    </section>

    <!-- FAQ 4 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">FAQ 4: 통계적 추론 방식은 무엇인가?</h2>
        <div class="section-content">
            <p><strong>Mode of Statistical Inference</strong> (Rubin, 1991)</p>
            
            <h4>명시해야 할 사항</h4>
            <ul>
                <li>연구 대상 <strong>모집단</strong></li>
                <li>사용할 <strong>표본</strong></li>
                <li>표준오차 계산 시의 <strong>가정</strong></li>
            </ul>

            <h4>실제적 문제</h4>
            <ul>
                <li>군집화(clustered) 또는 그룹화된 데이터에서 특히 중요</li>
                <li>잘 설계된 프로젝트도 추론의 세부사항에서 성패가 갈림</li>
            </ul>

            <div style="background: #f5f5f5; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center;">
                <p><strong>계량경제학 하이쿠</strong> (Keisuke Hirano)</p>
                <p style="font-style: italic; font-family: 'Times New Roman', serif;">
                    T-stat looks too good.<br>
                    Use robust standard errors—<br>
                    significance gone.
                </p>
            </div>
        </div>
    </section>

    <!-- 요약 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Chapter 1 요약</h2>
        <div class="section-content">
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">FAQ</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">질문</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">핵심</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; text-align: center;">1</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">인과관계는?</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">반사실적 세계에서의 변화 예측</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; text-align: center;">2</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">이상적 실험은?</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">가설적이더라도 구상 필요</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; text-align: center;">3</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">식별 전략은?</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">자연실험으로 실험 근사</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; text-align: center;">4</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">추론 방식은?</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">모집단, 표본, 표준오차 가정</td>
                </tr>
            </table>
        </div>
    </section>

    <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee; display: flex; justify-content: space-between;">
        <a href="/study" style="color: #666;">← Back to Study Notes</a>
        <a href="/study/angrist-ch2-ko" style="color: #2563eb;">Chapter 2 →</a>
    </div>

    <div style="margin-top: 2rem; padding: 1rem; background: #f9fafb; border-radius: 8px; font-size: 0.8rem; color: #6b7280;">
        <em>이 노트는 LLM(Claude)을 활용하여 작성되었습니다.</em>
    </div>
</div>
