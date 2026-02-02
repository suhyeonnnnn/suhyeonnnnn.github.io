---
layout: minimal_base
title: "Angrist Ch.4-3 - IV Details"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Chapter 4 Part 3: IV Details</h2>
            <a href="/study/angrist-ch4-part3-ko" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">한국어</a>
        </div>
        <div class="section-content">
            <p><em>Angrist & Pischke, Mostly Harmless Econometrics — Section 4.6</em></p>
        </div>
    </section>

    <!-- Core Message -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Core Message</h2>
        <div class="section-content">
            <blockquote style="border-left: 4px solid #2563eb; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                This section covers practical pitfalls of IV: common mistakes in manual 2SLS, the difficulty of identifying peer effects, the relationship between 2SLS and nonlinear models (bivariate Probit), and the <strong>finite-sample bias</strong> of 2SLS when instruments are many or weak.
            </blockquote>
        </div>
    </section>

    <!-- 4.6.1 2SLS Mistakes -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4.6.1 Common 2SLS Mistakes</h2>
        <div class="section-content">

            <h3>Mistake 1: Covariate Ambivalence</h3>
            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>The mistake:</strong> Including different covariates in the first and second stages.</p>
            </div>
            <p>Griliches & Mason (1972) included age in the second stage but not in the first stage. This is wrong because the first-stage residual (s<sub>i</sub> − ŝ<sub>i</sub>) is only guaranteed to be uncorrelated with variables <em>included</em> in the first stage.</p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Rule:</strong> Always include the same exogenous covariates in both stages. If a covariate is good enough for the second stage, it's good enough for the first.</p>
            </div>

            <h3>Mistake 2: Forbidden Regressions</h3>
            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>The mistake:</strong> Using <em>nonlinear</em> first-stage fitted values (e.g., Probit) as plug-in replacements in the second stage.</p>
            </div>

            <p>Suppose d<sub>i</sub> is a binary endogenous variable. You might think: "Since d<sub>i</sub> is 0/1, use Probit for the first stage instead of OLS."</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Why it's wrong:</strong> Only OLS residuals are guaranteed to be uncorrelated with fitted values and covariates (by the normal equations). Probit residuals lack this property unless the Probit model is correctly specified — which we cannot verify.</p>
            </div>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Correct alternatives:</strong></p>
                <ul>
                    <li><strong>Standard 2SLS:</strong> Use a linear first stage (always consistent regardless of first-stage functional form)</li>
                    <li><strong>Nonlinear fits as instruments:</strong> Use d̂<sup>probit</sup> as an <em>instrument</em> (not a plug-in) in standard 2SLS. This can improve efficiency if the Probit model is a good approximation</li>
                </ul>
                <p><strong>Caveat:</strong> Using nonlinear fits as instruments implicitly uses the nonlinearity as identifying information. If the instruments Zi appear in the causal equation, the model should be unidentified, but the nonlinear first stage creates "back-door" identification through functional form — which is questionable.</p>
            </div>

            <h3>Mistake 3: Forbidden Nonlinear Second Stage</h3>
            <p>With a quadratic model y<sub>i</sub> = δ'X<sub>i</sub> + ρ₁s<sub>i</sub> + ρ₂s<sub>i</sub>² + ε<sub>i</sub>, do <strong>not</strong> plug in ŝ and ŝ² from a single first stage. Instead, treat both s<sub>i</sub> and s<sub>i</sub>² as separate endogenous variables, each with its own first-stage equation, and use proper 2SLS.</p>
        </div>
    </section>

    <!-- 4.6.2 Peer Effects -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4.6.2 Peer Effects</h2>
        <div class="section-content">

            <h3>Type 1: Effect of Group Average of One Variable on Individual Outcome of Another</h3>
            <p>Example: Does average schooling in a state (S̄<sub>jt</sub>) affect individual wages? (Acemoglu & Angrist 2000)</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                Y<sub>ijt</sub> = α<sub>j</sub> + λ<sub>t</sub> + ρs<sub>i</sub> + ψS̄<sub>jt</sub> + u<sub>jt</sub> + ε<sub>ijt</sub>
            </div>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Problem:</strong> If OLS and 2SLS (using state dummies) give different estimates of ρ, then ψ̂ ≠ 0 <em>mechanically</em>, even without true externalities.</p>
                <ul>
                    <li>If 2SLS > OLS (e.g., measurement error correction): spurious <em>positive</em> externality</li>
                    <li>If 2SLS < OLS (e.g., ability bias removed): spurious <em>negative</em> externality</li>
                </ul>
                <p>→ OLS of equation like this is very hard to interpret for peer effects.</p>
            </div>

            <h3>Type 2: Effect of Group Average on Same Individual Variable</h3>
            <p>"Does the average graduation rate of my classmates affect whether I graduate?"</p>

            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Regression of s<sub>ij</sub> on S̄<sub>j</sub> always has coefficient = 1.</strong> This is because S̄<sub>j</sub> is literally the fitted value from regressing s<sub>ij</sub> on school dummies. This regression is <strong>tautological</strong> and tells us nothing about causality.</p>
            </div>

            <p>Even using leave-one-out means S̄<sub>(−i)j</sub> is problematic because school-level common shocks (e.g., a good principal) create spurious correlation between individual and peer outcomes.</p>

            <h4>Better Approaches</h4>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p>Use <strong>ex ante peer characteristics</strong> that predate the outcome:</p>
                <ul>
                    <li><strong>Ammermueller & Pischke (2006):</strong> Books in peers' homes → student test scores (books are a pre-determined home characteristic)</li>
                    <li><strong>Angrist & Lang (2004):</strong> Number of bused-in low-achievers → resident students' test scores (determined by students <em>outside</em> the sample)</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- 4.6.3 LDV Reprise -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4.6.3 Limited Dependent Variables Reprise</h2>
        <div class="section-content">

            <h3>The Case for 2SLS over Bivariate Probit</h3>
            <p>When the dependent variable is binary (e.g., employment), should we use bivariate Probit instead of 2SLS?</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Arguments for sticking with 2SLS:</strong></p>
                <ul>
                    <li>2SLS captures LATE regardless of whether the dependent variable is binary, non-negative, or continuous</li>
                    <li>2SLS requires no distributional assumptions</li>
                    <li>2SLS estimates the causal effect <em>directly</em> — no need to compute marginal effects from latent-index coefficients</li>
                    <li>Bivariate Probit can estimate ATE (not just LATE), but only under <strong>joint normality</strong> — a strong assumption</li>
                </ul>
            </div>

            <h4>Bivariate Probit Setup</h4>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                <strong>First stage:</strong> d<sub>i</sub> = 1[X<sub>i</sub>'δ₀ + δ₁z<sub>i</sub> > v<sub>i</sub>]<br>
                <strong>Second stage:</strong> y<sub>i</sub> = 1[X<sub>i</sub>'β₀ + β₁d<sub>i</sub> > ε<sub>i</sub>]<br><br>
                Endogeneity arises from Corr(v<sub>i</sub>, ε<sub>i</sub>) ≠ 0.<br>
                Identified by assuming z<sub>i</sub> ⊥ (v<sub>i</sub>, ε<sub>i</sub>) and <strong>joint normality</strong>.
            </div>

            <h4>Empirical Comparison: Effect of Third Child on Female Employment</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.9rem;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Specification</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">2SLS</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Abadie</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Biprobit MFX</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Biprobit ATE</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">No covariates</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.138</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.138</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.138</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.139</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Some covariates</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.132</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.132</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.135</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.135</td>
                </tr>
                <tr style="background: #fee2e2;">
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+ linear age term</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.120</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.121</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>−0.171</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>−0.171</strong></td>
                </tr>
            </table>
            <p>Results are nearly identical without strong functional form assumptions. But when a linear age term replaces a dummy, bivariate Probit estimates jump to −0.171 while 2SLS and Abadie remain stable. This reflects extrapolation into sparse cells — exactly the fragility that nonlinear models introduce.</p>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Bottom line:</strong> 2SLS is robust to functional form. Bivariate Probit can give you ATE instead of LATE, but at the cost of strong distributional assumptions that may not hold. In practice, the two usually agree unless the Probit model is extrapolating.</p>
            </div>
        </div>
    </section>

    <!-- 4.6.4 Bias of 2SLS -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4.6.4 The Bias of 2SLS</h2>
        <div class="section-content">

            <h3>OLS Is Unbiased, 2SLS Is Not</h3>
            <p>OLS is unbiased (centered on the population coefficient in any sample size). 2SLS is only <strong>consistent</strong> — it converges to the right answer in large samples, but can be systematically off in finite samples.</p>

            <h3>The Bias Formula</h3>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    E[β̂<sub>2SLS</sub> − β] ≈ (β̂<sub>OLS bias</sub>) × 1/(F + 1)
                </div>
                <p style="text-align: center; margin-top: 0.5rem;">where F is the first-stage F-statistic on excluded instruments.</p>
            </div>

            <h4>Key Implications</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Scenario</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">2SLS Bias</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">F → ∞ (strong instruments)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Bias → 0 ✓</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">F → 0 (no first stage)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Bias → OLS bias (worst case)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">More instruments (higher q)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">F falls → Bias increases</td>
                </tr>
            </table>

            <h4>Source of Bias</h4>
            <p>The bias arises because the first stage is <em>estimated</em>, not known. Fitted values ŝ<sub>i</sub> = Zπ̂ contain sampling error (Pzη) that is correlated with the second-stage error ε. When instruments are weak, this sampling correlation dominates, pulling 2SLS toward OLS.</p>

            <h3>LIML: A Bias-Reducing Alternative</h3>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>LIML (Limited Information Maximum Likelihood)</strong> is approximately <strong>median-unbiased</strong> even with over-identification, while having the same large-sample distribution as 2SLS.</p>
                <ul>
                    <li>LIML is essentially a bias-corrected linear combination of OLS and 2SLS</li>
                    <li>Available in Stata and SAS</li>
                    <li>Monte Carlo evidence (Flores-Lagunes 2007) supports LIML across a wide range of scenarios</li>
                </ul>
            </div>

            <h4>Monte Carlo Evidence</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Setup (true β=1)</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">OLS Median</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">2SLS Median</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">LIML Median</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">q=2 (1 useful + 1 useless)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">~1.79</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">1.07</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">~1.0</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">q=20 (1 useful + 19 useless)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">~1.79</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">1.53</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">~1.0</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">q=20 (all useless)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">~1.79</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">~1.79</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">widely dispersed</td>
                </tr>
            </table>
            <p>LIML stays centered on β=1 even with many weak instruments, while 2SLS is pulled toward OLS. With truly irrelevant instruments, LIML's wide distribution correctly reflects the lack of information.</p>

            <h3>Practical Recommendations</h3>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <ol>
                    <li><strong>Report the first stage.</strong> Check sign, magnitude, and plausibility.</li>
                    <li><strong>Report the F-statistic</strong> on excluded instruments. Rule of thumb: F > 10 is safe (Stock, Wright & Yogo 2002), though not an absolute theorem.</li>
                    <li><strong>Report just-identified estimates</strong> using your single best instrument. Just-identified IV is median-unbiased and immune to the many-instruments problem.</li>
                    <li><strong>Compare 2SLS and LIML.</strong> If they agree, be reassured. If they disagree, worry — and look for stronger instruments.</li>
                    <li><strong>Look at the reduced form.</strong> The reduced-form regression (y on z) is OLS and therefore unbiased. If you can't see the causal relation in the reduced form, it's probably not there.</li>
                </ol>
            </div>

            <h4>Application: Angrist & Krueger (1991) Revisited</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.9rem;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Instruments</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">q</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">F-stat</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">2SLS</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">LIML</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">3 QOB dummies</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">3</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">32.3</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.105 (0.020)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.106 (0.020)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">QOB×YOB interactions</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">30</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">4.9</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.089 (0.016)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.093 (0.018)</td>
                </tr>
                <tr style="background: #fef3c7;">
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+ QOB×SOB interactions</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">180</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">2.6</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.093 (0.009)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.091 (0.011)</td>
                </tr>
            </table>
            <p>With 3 instruments and F=32, 2SLS and LIML agree closely. With 180 instruments and F=2.6, the F-statistic is low but LIML still agrees with 2SLS, suggesting the bias may not be fatal here despite the mechanical rule of thumb.</p>
        </div>
    </section>

    <!-- Summary -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Part 3 Summary</h2>
        <div class="section-content">
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Topic</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Key Lesson</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Covariate ambivalence</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Same covariates in both stages; otherwise residuals are correlated with fitted values</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Forbidden regression</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Never plug nonlinear fitted values into a second stage; use them as instruments instead</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Peer effects (Type 1)</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">OLS estimates of externalities are confounded by OLS-vs-IV differences in private returns</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Peer effects (Type 2)</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Regressing individual outcome on group mean of same outcome is tautological; use ex ante peer characteristics</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>2SLS vs. Bivariate Probit</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">2SLS is robust; Biprobit needs normality and is sensitive to covariates</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>2SLS bias</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Bias ≈ OLS bias / (F+1); many weak instruments → bias toward OLS</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>LIML</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Median-unbiased alternative to 2SLS; use for robustness checks</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>F > 10 rule</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Rule of thumb for instrument strength; not an absolute theorem</td>
                </tr>
            </table>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>The five-point IV checklist:</strong></p>
                <ol>
                    <li>Report and inspect the first stage</li>
                    <li>Report the F-statistic (aim for > 10)</li>
                    <li>Report just-identified estimates with your best instrument</li>
                    <li>Compare 2SLS and LIML</li>
                    <li>Check the reduced form — if the causal effect isn't visible there, it's probably not real</li>
                </ol>
            </div>
        </div>
    </section>

    <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee; display: flex; justify-content: space-between;">
        <a href="/study/angrist-ch4-part2" style="color: #666;">← Part 2: LATE & Heterogeneous Effects</a>
        <a href="/study" style="color: #2563eb;">Back to Study Notes →</a>
    </div>

    <div style="margin-top: 2rem; padding: 1rem; background: #f9fafb; border-radius: 8px; font-size: 0.8rem; color: #6b7280;">
        <em>This note was written with the assistance of LLM (Claude).</em>
    </div>
</div>
