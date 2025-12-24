---
layout: minimal_base
title: "Angrist Ch.2 - The Experimental Ideal"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Chapter 2: The Experimental Ideal</h2>
            <a href="/study/angrist-ch2" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">English</a>
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
                가장 신뢰할 수 있고 영향력 있는 연구 설계는 <strong>무작위 배정(random assignment)</strong>을 사용한다.
            </blockquote>
        </div>
    </section>

    <!-- 2.1 Selection Problem -->
    <section class="section fade-in-delay">
        <h2 class="section-title">2.1 선택 편의 문제 (The Selection Problem)</h2>
        <div class="section-content">
            
            <h4>동기 예시: 병원이 사람들을 더 건강하게 만드는가?</h4>
            <p>NHIS(National Health Interview Survey) 데이터로 입원 경험에 따른 건강 상태 비교:</p>
            
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">그룹</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">표본 크기</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">평균 건강 상태</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">표준오차</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">입원 경험 있음</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">7,774</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">2.79</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.014</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">입원 경험 없음</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">90,049</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">2.07</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.003</td>
                </tr>
            </table>
            <p><strong>차이:</strong> 0.71 (t-통계량 = 58.9) → 표면적으로 병원에 가면 더 아파 보임!</p>
            
            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>왜 이런 결과가?</strong> 병원에 가는 사람들은 애초에 더 아픈 사람들이다.</p>
            </div>

            <h4>잠재적 결과 프레임워크 (Potential Outcomes Framework)</h4>
            <p><strong>Rubin Causal Model</strong>의 핵심 개념 (Rubin, 1974, 1977; Holland, 1986)</p>
            
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>표기법:</strong></p>
                <ul>
                    <li>D<sub>i</sub> ∈ {0, 1}: 처치 여부 (예: 병원 방문)</li>
                    <li>Y<sub>i</sub>: 관측된 결과</li>
                    <li>Y<sub>1i</sub>: 처치를 받았을 때의 잠재적 결과</li>
                    <li>Y<sub>0i</sub>: 처치를 받지 않았을 때의 잠재적 결과</li>
                </ul>
                <p><strong>개인 i의 인과효과:</strong> Y<sub>1i</sub> − Y<sub>0i</sub></p>
            </div>

            <p><strong>관측된 결과:</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                Y<sub>i</sub> = Y<sub>0i</sub> + (Y<sub>1i</sub> − Y<sub>0i</sub>) · D<sub>i</sub>
            </div>

            <h4>선택 편의의 공식적 분해</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p style="text-align: center; font-family: 'Times New Roman', serif;">
                    <span style="border-bottom: 2px solid #000;">E[Y<sub>i</sub>|D<sub>i</sub>=1] − E[Y<sub>i</sub>|D<sub>i</sub>=0]</span><br>
                    <small>관측된 평균 차이</small>
                </p>
                <p style="text-align: center; font-size: 1.5rem;">=</p>
                <p style="text-align: center; font-family: 'Times New Roman', serif;">
                    <span style="color: #2563eb; border-bottom: 2px solid #2563eb;">E[Y<sub>1i</sub> − Y<sub>0i</sub> | D<sub>i</sub>=1]</span> + 
                    <span style="color: #dc2626; border-bottom: 2px solid #dc2626;">E[Y<sub>0i</sub>|D<sub>i</sub>=1] − E[Y<sub>0i</sub>|D<sub>i</sub>=0]</span>
                </p>
                <p style="text-align: center;">
                    <span style="color: #2563eb;">■ ATT (처치받은 집단의 평균 처치효과)</span><br>
                    <span style="color: #dc2626;">■ Selection Bias (선택 편의)</span>
                </p>
            </div>

            <h4>선택 편의란?</h4>
            <ul>
                <li>처치를 받은 집단과 받지 않은 집단 간 <strong>Y<sub>0i</sub>의 차이</strong></li>
                <li>병원 예시: 아픈 사람이 치료를 받으러 감 → 선택 편의는 <strong>음수</strong></li>
                <li>양의 처치효과를 완전히 가릴 수 있음</li>
            </ul>
        </div>
    </section>

    <!-- 2.2 Random Assignment -->
    <section class="section fade-in-delay">
        <h2 class="section-title">2.2 무작위 배정이 선택 편의를 해결하는 방법</h2>
        <div class="section-content">
            
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>핵심 원리:</strong> 무작위 배정은 D<sub>i</sub>를 잠재적 결과와 <strong>독립(independent)</strong>으로 만든다.</p>
            </div>

            <h4>수학적 유도</h4>
            <p>무작위 배정 하에서:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                <p>E[Y<sub>i</sub>|D<sub>i</sub>=1] − E[Y<sub>i</sub>|D<sub>i</sub>=0]</p>
                <p>= E[Y<sub>1i</sub>|D<sub>i</sub>=1] − E[Y<sub>0i</sub>|D<sub>i</sub>=0]</p>
                <p>= E[Y<sub>1i</sub>|D<sub>i</sub>=1] − E[Y<sub>0i</sub>|D<sub>i</sub>=1] <span style="color: #666;">(독립성에 의해)</span></p>
                <p>= E[Y<sub>1i</sub> − Y<sub>0i</sub>|D<sub>i</sub>=1]</p>
                <p>= <strong>E[Y<sub>1i</sub> − Y<sub>0i</sub>]</strong> <span style="color: #2563eb;">(= ATE, 평균 처치효과)</span></p>
            </div>
            <p>→ <strong>선택 편의가 사라지고, 평균 처치효과(ATE)를 직접 추정 가능!</strong></p>

            <h4>실증 사례: 비실험 vs 무작위 실험</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">연구 분야</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">비실험적 비교</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">무작위 실험 결과</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">호르몬 대체 요법 (HRT)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Nurses Health Study: HRT 사용자가 더 건강</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Women's Health Initiative: 효과 거의 없음, 심각한 부작용 발견</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">직업 훈련 프로그램</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">참가자가 비참가자보다 소득 낮음</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">대부분 양의 효과 (Lalonde, 1986)</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- 2.3 Tennessee STAR -->
    <section class="section fade-in-delay">
        <h2 class="section-title">2.3 Tennessee STAR 실험</h2>
        <div class="section-content">
            
            <h4>실험 개요</h4>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <ul>
                    <li><strong>목적:</strong> 학급 규모가 학생 성취도에 미치는 영향 추정</li>
                    <li><strong>시기:</strong> 1985/86년 시작, 4년간 진행 (유치원 → 3학년)</li>
                    <li><strong>규모:</strong> 약 11,600명, 비용 약 $12 million</li>
                    <li><strong>처치 집단:</strong>
                        <ol>
                            <li>소규모 학급 (13-17명)</li>
                            <li>일반 학급 (22-25명) + 파트타임 보조교사</li>
                            <li>일반 학급 + 풀타임 보조교사</li>
                        </ol>
                    </li>
                </ul>
            </div>

            <h4>무작위 배정 검증 (Balance Check)</h4>
            <p>무작위 배정이 성공했는지 확인하기 위해 사전 특성을 비교:</p>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.9rem;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">변수</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">소규모</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">일반</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">일반/보조</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">P-value</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">무료 급식</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">.47</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">.48</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">.50</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">.09</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">백인/아시아인</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">.68</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">.67</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">.66</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">.26</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">1985년 나이</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">5.44</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">5.43</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">5.42</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">.32</td>
                </tr>
                <tr style="background: #ecfdf5;">
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">유치원 학급 규모</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">15.10</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">22.40</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">22.80</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">.00</td>
                </tr>
                <tr style="background: #ecfdf5;">
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">유치원 백분위 점수</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">54.70</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">48.90</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">50.00</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">.00</td>
                </tr>
            </table>
            <p>✅ 학생 특성(무료 급식, 인종, 나이)은 집단 간 균형 → <strong>무작위 배정 성공</strong></p>

            <h4>주요 결과</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">변수</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">(1)</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">(2)</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">(3)</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">(4)</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>소규모 학급</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">4.82 (2.19)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">5.37 (1.26)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">5.36 (1.21)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">5.37 (1.19)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">일반/보조 학급</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">.12 (2.23)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">.29 (1.13)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">.53 (1.09)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">.31 (1.07)</td>
                </tr>
                <tr style="background: #f5f5f5;">
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">학교 고정효과</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">No</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Yes</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Yes</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Yes</td>
                </tr>
                <tr style="background: #f5f5f5;">
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">학생 특성 통제</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">No</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">No</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Yes</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Yes</td>
                </tr>
            </table>
            
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>핵심 결과:</strong></p>
                <ul>
                    <li><strong>소규모 학급 효과:</strong> 약 5-6 백분위 점수 상승</li>
                    <li><strong>효과 크기:</strong> 약 0.2 표준편차 (σ)</li>
                    <li>일반/보조 학급 효과: 작고 통계적으로 유의하지 않음</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- 2.4 Regression Analysis -->
    <section class="section fade-in-delay">
        <h2 class="section-title">2.4 실험 데이터의 회귀분석</h2>
        <div class="section-content">
            
            <h4>상수 처치효과 모형</h4>
            <p>처치효과가 모든 개인에게 동일하다고 가정 (Y<sub>1i</sub> − Y<sub>0i</sub> = ρ):</p>
            
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                Y<sub>i</sub> = <span style="color: #2563eb;">α</span> + <span style="color: #dc2626;">ρ</span> D<sub>i</sub> + <span style="color: #059669;">η<sub>i</sub></span>
            </div>
            <p style="text-align: center;">
                <span style="color: #2563eb;">α = E(Y<sub>0i</sub>)</span> &nbsp;&nbsp;
                <span style="color: #dc2626;">ρ = 처치효과</span> &nbsp;&nbsp;
                <span style="color: #059669;">η<sub>i</sub> = Y<sub>0i</sub> − E(Y<sub>0i</sub>)</span>
            </p>

            <h4>선택 편의의 회귀적 표현</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p style="font-family: 'Times New Roman', serif;">
                    E[Y<sub>i</sub>|D<sub>i</sub>=1] − E[Y<sub>i</sub>|D<sub>i</sub>=0] = <span style="color: #dc2626;">ρ</span> + <span style="color: #7c3aed;">[E[η<sub>i</sub>|D<sub>i</sub>=1] − E[η<sub>i</sub>|D<sub>i</sub>=0]]</span>
                </p>
                <p>
                    <span style="color: #dc2626;">■ ρ: 처치효과</span><br>
                    <span style="color: #7c3aed;">■ 선택 편의: 오차항 η<sub>i</sub>와 설명변수 D<sub>i</sub> 간의 상관관계</span>
                </p>
            </div>
            <p><strong>무작위 배정 시:</strong> 선택 편의 = 0 → 회귀계수가 인과효과를 추정</p>

            <h4>공변량(Covariates)의 역할</h4>
            <p><strong>긴 회귀모형:</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif;">
                Y<sub>i</sub> = α + ρD<sub>i</sub> + X<sub>i</sub>'γ + η<sub>i</sub>
            </div>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">역할</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">설명</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">STAR 예시</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>1. 조건부 무작위 배정 통제</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">특정 변수 내에서만 무작위 배정된 경우 해당 변수 통제 필요</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">학교 내에서만 무작위 배정 → 학교 고정효과 포함</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>2. 추정 정밀도 향상</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">X<sub>i</sub>가 D<sub>i</sub>와 상관없더라도 Y<sub>i</sub>의 분산을 설명하면 표준오차 감소</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">인종, 나이, 무료급식 통제 → 표준오차 감소 (1.26 → 1.21)</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- Quasi-Experiment -->
    <section class="section fade-in-delay">
        <h2 class="section-title">준실험적 접근: Angrist & Lavy (1999)</h2>
        <div class="section-content">
            <p>무작위 실험이 불가능할 때, <strong>자연실험(Natural Experiment)</strong>을 활용</p>
            
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>배경:</strong> 이스라엘 학급 규모 상한 = 40명 (Maimonides' Rule)</p>
                <ul>
                    <li>5학년 코호트 40명 → 학급 규모 40명</li>
                    <li>5학년 코호트 41명 → 학급이 둘로 분리 → 학급 규모 약 20명</li>
                </ul>
            </div>

            <h4>핵심 가정</h4>
            <p>40명 vs 41명 코호트의 학생들은 능력, 가정환경 등에서 유사 → <strong>"무작위 배정과 같은(as good as randomly assigned)"</strong> 상황</p>

            <h4>결과 비교</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">분석 방법</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">결과</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">단순 비교 (Naive)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">작은 학급 학생들의 점수가 더 <strong style="color: #dc2626;">낮음</strong> (선택 편의)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">준실험적 분석 (RDD)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">학급 규모와 성취도 간 <strong style="color: #2563eb;">강한 양의 관계</strong></td>
                </tr>
            </table>
        </div>
    </section>

    <!-- 요약 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Chapter 2 요약</h2>
        <div class="section-content">
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">개념</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">설명</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>잠재적 결과</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Y<sub>1i</sub>, Y<sub>0i</sub>: 처치 여부에 따른 가상의 결과</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>인과효과</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Y<sub>1i</sub> − Y<sub>0i</sub>: 개인의 처치효과</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>선택 편의</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">처치/비처치 집단 간 기저 특성 차이</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>무작위 배정</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">D<sub>i</sub>와 잠재적 결과를 독립으로 만들어 선택 편의 제거</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>자연실험</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">외생적 변이를 활용하여 무작위 실험을 근사</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- 참고문헌 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">참고문헌</h2>
        <div class="section-content">
            <ul style="font-size: 0.9rem;">
                <li>Krueger, A. B. (1999). Experimental estimates of education production functions. <em>QJE</em>.</li>
                <li>Angrist, J. D., & Lavy, V. (1999). Using Maimonides' rule to estimate the effect of class size. <em>QJE</em>.</li>
                <li>Rubin, D. B. (1974). Estimating causal effects of treatments. <em>Journal of Educational Psychology</em>.</li>
                <li>Holland, P. W. (1986). Statistics and causal inference. <em>JASA</em>.</li>
                <li>Lalonde, R. J. (1986). Evaluating the econometric evaluations of training programs. <em>AER</em>.</li>
            </ul>
        </div>
    </section>

    <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee; display: flex; justify-content: space-between;">
        <a href="/study/angrist-ch1-ko" style="color: #666;">← Chapter 1</a>
        <a href="/study" style="color: #2563eb;">Back to Study Notes →</a>
    </div>

    <div style="margin-top: 2rem; padding: 1rem; background: #f9fafb; border-radius: 8px; font-size: 0.8rem; color: #6b7280;">
        <em>이 노트는 LLM(Claude)을 활용하여 작성되었습니다.</em>
    </div>
</div>
