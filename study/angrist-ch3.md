---
layout: minimal_base
title: "Angrist Ch.3 - Making Regression Make Sense"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Chapter 3: Making Regression Make Sense</h2>
            <a href="/study/angrist-ch3-ko" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">한국어</a>
        </div>
        <div class="section-content">
            <p><em>Angrist & Pischke, Mostly Harmless Econometrics</em></p>
        </div>
    </section>

    <!-- Core Message -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Core Message</h2>
        <div class="section-content">
            <blockquote style="border-left: 4px solid #2563eb; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                Regression is useful because it provides the best linear approximation to the <strong>Conditional Expectation Function (CEF)</strong>. The question of <em>when</em> regression is causal depends on the <strong>Conditional Independence Assumption (CIA)</strong>.
            </blockquote>
        </div>
    </section>

    <!-- 3.1 Regression Fundamentals -->
    <section class="section fade-in-delay">
        <h2 class="section-title">3.1 Regression Fundamentals</h2>
        <div class="section-content">
            
            <h3>3.1.1 The Conditional Expectation Function (CEF)</h3>
            
            <p>The CEF is the expected value of Y<sub>i</sub> given X<sub>i</sub>:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                E[Y<sub>i</sub> | X<sub>i</sub>]
            </div>
            
            <p><strong>Example:</strong> The CEF of log wages given schooling shows that people with more education earn more on average (~10% per year).</p>

            <h4>The Law of Iterated Expectations</h4>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p>An unconditional expectation equals the expectation of the CEF:</p>
                <div style="text-align: center; font-family: 'Times New Roman', serif;">
                    E[Y<sub>i</sub>] = E{ E[Y<sub>i</sub> | X<sub>i</sub>] }
                </div>
            </div>

            <h4>Three Key Properties of the CEF</h4>
            
            <p><strong>Property 1: CEF Decomposition</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                Y<sub>i</sub> = E[Y<sub>i</sub> | X<sub>i</sub>] + ε<sub>i</sub>
            </div>
            <p>where:</p>
            <ul>
                <li>ε<sub>i</sub> is mean-independent of X<sub>i</sub>: E[ε<sub>i</sub> | X<sub>i</sub>] = 0</li>
                <li>ε<sub>i</sub> is uncorrelated with any function of X<sub>i</sub></li>
            </ul>
            <p>→ Any random variable can be decomposed into a part "explained by X" (the CEF) and an orthogonal residual.</p>

            <p><strong>Property 2: CEF Prediction</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                E[Y<sub>i</sub> | X<sub>i</sub>] = arg min<sub>m(X)</sub> E[(Y<sub>i</sub> − m(X<sub>i</sub>))²]
            </div>
            <p>→ The CEF is the <strong>Minimum Mean Squared Error (MMSE)</strong> predictor of Y given X.</p>

            <p><strong>Property 3: ANOVA Theorem</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                V(Y<sub>i</sub>) = V(E[Y<sub>i</sub> | X<sub>i</sub>]) + E[V(Y<sub>i</sub> | X<sub>i</sub>)]
            </div>
            <p>→ Total variance = Variance explained by X + Residual variance</p>

            <h3>3.1.2 Linear Regression and the CEF</h3>
            
            <p>The population regression coefficient is defined as:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif;">
                β = arg min<sub>b</sub> E[(Y<sub>i</sub> − X<sub>i</sub>'b)²]
            </div>
            
            <p>Solution:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif;">
                β = E[X<sub>i</sub>X<sub>i</sub>']<sup>−1</sup> E[X<sub>i</sub>Y<sub>i</sub>]
            </div>

            <h4>Regression Anatomy Formula</h4>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p>For the k-th regressor in a multivariate regression:</p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    β<sub>k</sub> = Cov(Y<sub>i</sub>, x̃<sub>ki</sub>) / V(x̃<sub>ki</sub>)
                </div>
                <p style="margin-top: 0.5rem;">where x̃<sub>ki</sub> is the residual from regressing x<sub>ki</sub> on all other covariates.</p>
            </div>
            <p><strong>Interpretation:</strong> Each coefficient in a multivariate regression is the bivariate slope after "partialling out" all other variables.</p>

            <h4>Three Justifications for Regression</h4>
            
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Theorem</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Statement</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">When it applies</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Linear CEF</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">If the CEF is linear, regression gives you the CEF</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Joint normality, saturated models</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Best Linear Predictor</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">X'β is the best linear predictor of Y (MMSE)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Always</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Regression-CEF</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">X'β provides the best linear approximation to E[Y|X]</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Always (even if CEF is nonlinear)</td>
                </tr>
            </table>
            
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Key insight:</strong> Even if the CEF is nonlinear, regression provides the best linear approximation to it. This is the most general justification for using regression.</p>
            </div>

            <h3>3.1.3 Asymptotic OLS Inference</h3>
            
            <p>The OLS estimator:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif;">
                β̂ = (Σ X<sub>i</sub>X<sub>i</sub>')<sup>−1</sup> Σ X<sub>i</sub>Y<sub>i</sub>
            </div>

            <h4>Key Asymptotic Results</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Result</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">What it says</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Law of Large Numbers</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Sample moments → Population moments</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Central Limit Theorem</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">√N(β̂ − β) → Normal distribution</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Slutsky's Theorem</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Can replace probability limits with constants</td>
                </tr>
            </table>

            <h4>Heteroskedasticity-Robust Standard Errors</h4>
            <p>The robust variance estimator:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif;">
                V(β̂) = E[X<sub>i</sub>X<sub>i</sub>']<sup>−1</sup> E[X<sub>i</sub>X<sub>i</sub>'e<sub>i</sub>²] E[X<sub>i</sub>X<sub>i</sub>']<sup>−1</sup>
            </div>
            
            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Why use robust SEs?</strong></p>
                <ul>
                    <li>If CEF is nonlinear, residuals vary with X → heteroskedasticity is natural</li>
                    <li>Default (homoskedastic) SEs assume E[e<sub>i</sub>² | X<sub>i</sub>] = σ² (constant)</li>
                    <li>Robust SEs are valid without this assumption</li>
                </ul>
            </div>

            <h3>3.1.4 Saturated Models</h3>
            
            <p><strong>Definition:</strong> A saturated model has a separate parameter for every possible value of X.</p>
            
            <p><strong>Example with two dummies (x<sub>1</sub> = college, x<sub>2</sub> = female):</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                Y<sub>i</sub> = α + β·x<sub>1i</sub> + γ·x<sub>2i</sub> + δ·(x<sub>1i</sub>·x<sub>2i</sub>) + ε<sub>i</sub>
            </div>
            
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Term</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Name</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Interpretation</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">β, γ</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Main effects</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Effect of each variable separately</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">δ</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Interaction term</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">How college effect differs by gender</td>
                </tr>
            </table>
            
            <p><strong>Key point:</strong> Saturated models fit the CEF perfectly because the CEF is linear in the dummy regressors.</p>
        </div>
    </section>

    <!-- 3.2 Regression and Causality -->
    <section class="section fade-in-delay">
        <h2 class="section-title">3.2 Regression and Causality</h2>
        <div class="section-content">
            
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Central Question:</strong> When does regression have a causal interpretation?</p>
                <p><strong>Answer:</strong> When the CEF it approximates is causal, which requires the <strong>Conditional Independence Assumption (CIA)</strong>.</p>
            </div>

            <h3>3.2.1 The Conditional Independence Assumption (CIA)</h3>
            
            <h4>Setup: Potential Outcomes</h4>
            <p>For schooling s, let Y<sub>si</sub> = f<sub>i</sub>(s) denote person i's potential earnings with s years of education.</p>
            
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>The CIA states:</strong></p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem; margin: 1rem 0;">
                    Y<sub>si</sub> ⊥ s<sub>i</sub> | X<sub>i</sub>
                </div>
                <p>"Potential outcomes are independent of actual schooling, conditional on X"</p>
            </div>

            <h4>What does CIA mean?</h4>
            <ul>
                <li><strong>Selection on observables:</strong> X<sub>i</sub> captures all reasons why schooling and potential outcomes are correlated</li>
                <li><strong>As good as random:</strong> Conditional on X, schooling is "as good as randomly assigned"</li>
            </ul>

            <h4>Implications of CIA</h4>
            <p>Given CIA, conditional comparisons are causal:</p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                E[Y<sub>i</sub> | X<sub>i</sub>, s<sub>i</sub> = s] − E[Y<sub>i</sub> | X<sub>i</sub>, s<sub>i</sub> = s−1] = E[f<sub>i</sub>(s) − f<sub>i</sub>(s−1) | X<sub>i</sub>]
            </div>
            <p>→ The difference in mean earnings between schooling levels has a causal interpretation!</p>

            <h4>From CIA to Regression</h4>
            <p>Assume a linear constant-effects model:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                f<sub>i</sub>(s) = α + ρs + η<sub>i</sub>
            </div>
            <p>where η<sub>i</sub> is the random part of potential earnings.</p>
            
            <p>Decompose η<sub>i</sub>:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                η<sub>i</sub> = X<sub>i</sub>'γ + v<sub>i</sub>
            </div>
            
            <p>The causal regression model becomes:</p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                Y<sub>i</sub> = α + ρs<sub>i</sub> + X<sub>i</sub>'γ + v<sub>i</sub>
            </div>
            <p>Given CIA, v<sub>i</sub> is uncorrelated with s<sub>i</sub> and X<sub>i</sub>, so <strong>ρ is the causal effect</strong>.</p>

            <h3>3.2.2 The Omitted Variables Bias (OVB) Formula</h3>
            
            <p>Consider a "long" regression with ability controls A<sub>i</sub>:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                Y<sub>i</sub> = α + ρs<sub>i</sub> + A<sub>i</sub>'γ + ε<sub>i</sub>
            </div>
            
            <p>And a "short" regression without A<sub>i</sub>:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                Y<sub>i</sub> = α̃ + ρ̃s<sub>i</sub> + ε̃<sub>i</sub>
            </div>

            <h4>The OVB Formula</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    ρ̃ = ρ + γ'δ<sub>As</sub>
                </div>
                <p style="margin-top: 1rem; text-align: center;">
                    <strong>Short = Long + (Effect of omitted) × (Regression of omitted on included)</strong>
                </p>
            </div>
            
            <p>where δ<sub>As</sub> is the coefficient from regressing A<sub>i</sub> on s<sub>i</sub>.</p>

            <h4>Application: Returns to Schooling</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Controls</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Schooling Coefficient</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">None</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.132</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Age dummies</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.131</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+ Family background</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.114</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+ AFQT score</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.087</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+ Occupation dummies</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.066</td>
                </tr>
            </table>
            <p><em>Source: NLSY data</em></p>
            
            <p>→ Coefficient decreases as we add controls that are positively correlated with both wages and schooling.</p>

            <h3>3.2.3 Bad Control</h3>
            
            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Bad controls</strong> are variables that are themselves <strong>outcomes</strong> of the treatment.</p>
                <p><strong>Good controls</strong> are variables determined <strong>before</strong> the treatment.</p>
            </div>

            <h4>Example: Controlling for Occupation</h4>
            <p>Should we control for occupation in a schooling regression?</p>
            
            <p><strong>Problem:</strong> College affects occupation choice!</p>
            <ul>
                <li>w<sub>i</sub> = 1 if white collar job</li>
                <li>College → more likely white collar</li>
            </ul>

            <p><strong>Comparing within occupation:</strong></p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                E[Y<sub>i</sub> | w<sub>i</sub>=1, c<sub>i</sub>=1] − E[Y<sub>i</sub> | w<sub>i</sub>=1, c<sub>i</sub>=0]<br><br>
                = E[Y<sub>1i</sub> − Y<sub>0i</sub> | w<sub>1i</sub>=1] + <span style="color: #dc2626;">{E[Y<sub>0i</sub> | w<sub>1i</sub>=1] − E[Y<sub>0i</sub> | w<sub>0i</sub>=1]}</span>
            </div>
            <p style="text-align: center;"><span style="color: #dc2626;">↑ Selection bias from composition change</span></p>

            <p><strong>Why is this bias?</strong></p>
            <ul>
                <li>College graduates who work white collar = typical graduates</li>
                <li>Non-graduates who work white collar = exceptional non-graduates</li>
                <li>→ Comparing different types of people!</li>
            </ul>

            <h4>Proxy Control Problem</h4>
            <p>What if we use a "late" ability measure (measured after schooling)?</p>
            
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                al<sub>i</sub> = π<sub>0</sub> + π<sub>1</sub>s<sub>i</sub> + π<sub>2</sub>a<sub>i</sub>
            </div>
            <p>If schooling increases measured ability (π<sub>1</sub> > 0), controlling for late ability biases the schooling coefficient <strong>downward</strong>.</p>

            <h4>Rule of Thumb</h4>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Timing matters!</strong></p>
                <ul>
                    <li>✅ Variables measured <strong>before</strong> treatment → Good controls</li>
                    <li>❌ Variables measured <strong>after</strong> treatment → Potentially bad controls</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- Summary -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Chapter 3 Summary</h2>
        <div class="section-content">
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Concept</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Key Point</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>CEF</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">E[Y|X] - the MMSE predictor of Y given X</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Regression</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Best linear approximation to the CEF</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Regression Anatomy</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">β<sub>k</sub> = bivariate slope after partialling out other Xs</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>CIA</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Y<sub>s</sub> ⊥ s | X - makes regression causal</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>OVB Formula</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Short = Long + (Omitted effect) × (Omitted on included)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Bad Control</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Don't control for outcomes of treatment</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- References -->
    <section class="section fade-in-delay">
        <h2 class="section-title">References</h2>
        <div class="section-content">
            <ul style="font-size: 0.9rem;">
                <li>Barnow, B., Cain, G., & Goldberger, A. (1981). Selection on observables. <em>Evaluation Studies Review Annual</em>.</li>
                <li>White, H. (1980). A heteroskedasticity-consistent covariance matrix estimator. <em>Econometrica</em>.</li>
                <li>Frisch, R., & Waugh, F. (1933). Partial time regressions as compared with individual trends. <em>Econometrica</em>.</li>
                <li>Angrist, J. (1998). Estimating the labor market impact of voluntary military service. <em>Econometrica</em>.</li>
            </ul>
        </div>
    </section>

    <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee; display: flex; justify-content: space-between;">
        <a href="/study/angrist-ch2" style="color: #666;">← Chapter 2: The Experimental Ideal</a>
        <a href="/study" style="color: #2563eb;">Back to Study Notes →</a>
    </div>

    <div style="margin-top: 2rem; padding: 1rem; background: #f9fafb; border-radius: 8px; font-size: 0.8rem; color: #6b7280;">
        <em>This note was written with the assistance of LLM (Claude).</em>
    </div>
</div>
