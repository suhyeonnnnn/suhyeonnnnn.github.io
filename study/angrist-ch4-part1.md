---
layout: minimal_base
title: "Angrist Ch.4-1 - IV Basics, Wald & 2SLS"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Chapter 4 Part 1: IV Basics, Wald & 2SLS</h2>
            <a href="/study/angrist-ch4-part1-ko" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">한국어</a>
        </div>
        <div class="section-content">
            <p><em>Angrist & Pischke, Mostly Harmless Econometrics — Sections 4.1–4.3</em></p>
        </div>
    </section>

    <!-- Core Message -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Core Message</h2>
        <div class="section-content">
            <blockquote style="border-left: 4px solid #2563eb; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                <strong>Instrumental Variables (IV)</strong> solves omitted variables bias by using a variable (the instrument) that affects the outcome <em>only through</em> its effect on the treatment. The IV estimand is the ratio of the <strong>reduced form</strong> (instrument → outcome) to the <strong>first stage</strong> (instrument → treatment).
            </blockquote>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Key questions this part answers:</strong></p>
                <ol>
                    <li>What assumptions make IV valid? → Exclusion restriction + first stage</li>
                    <li>How does 2SLS work? → Replace endogenous variable with first-stage fitted values</li>
                    <li>What is the Wald estimator? → Simplest IV with a binary instrument</li>
                    <li>How are grouped data and 2SLS related? → 2SLS with dummies = GLS on group means</li>
                </ol>
            </div>
        </div>
    </section>

    <!-- 4.1 IV and Causality -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4.1 IV and Causality</h2>
        <div class="section-content">

            <h3>The Problem IV Solves</h3>
            <p>Suppose the "long regression" (with all necessary controls) is:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                y<sub>i</sub> = α + ρs<sub>i</sub> + A<sub>i</sub>'γ + v<sub>i</sub>
            </div>
            <p>where A<sub>i</sub> ("ability") makes schooling s<sub>i</sub> uncorrelated with v<sub>i</sub>. If A<sub>i</sub> is <strong>unobserved</strong>, OLS on the "short regression" y<sub>i</sub> = α + ρ̃s<sub>i</sub> + ε<sub>i</sub> is biased. IV fixes this without observing A<sub>i</sub>.</p>

            <h3>The IV Setup (Constant Effects)</h3>
            <p>An instrument z<sub>i</sub> must satisfy two conditions:</p>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Condition</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Formal Statement</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Meaning</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Relevance</strong> (First stage)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">Cov(s<sub>i</sub>, z<sub>i</sub>) ≠ 0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">The instrument actually affects the treatment</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Exclusion restriction</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">Cov(ε<sub>i</sub>, z<sub>i</sub>) = 0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">The instrument affects the outcome <em>only through</em> the treatment</td>
                </tr>
            </table>

            <h3>The IV Estimand</h3>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.2rem;">
                    ρ = Cov(y<sub>i</sub>, z<sub>i</sub>) / Cov(s<sub>i</sub>, z<sub>i</sub>) = <span style="color: #059669;">Reduced form</span> / <span style="color: #2563eb;">First stage</span>
                </div>
            </div>
            <p>The causal effect is the ratio of two regression coefficients:</p>
            <ul>
                <li><strong style="color: #059669;">Reduced form</strong>: regression of y<sub>i</sub> on z<sub>i</sub> (how the instrument affects the outcome)</li>
                <li><strong style="color: #2563eb;">First stage</strong>: regression of s<sub>i</sub> on z<sub>i</sub> (how the instrument affects the treatment)</li>
            </ul>

            <h3>Example: Quarter of Birth (Angrist & Krueger 1991)</h3>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Logic:</strong> School start-age rules + compulsory schooling laws → children born in early quarters get slightly <em>less</em> schooling.</p>
                <ul>
                    <li><strong>Treatment:</strong> years of education (s<sub>i</sub>)</li>
                    <li><strong>Instrument:</strong> quarter of birth (z<sub>i</sub>)</li>
                    <li><strong>Outcome:</strong> log weekly wages (y<sub>i</sub>)</li>
                </ul>
                <p><strong>Why valid?</strong> Date of birth is essentially random and plausibly affects earnings only through schooling.</p>
            </div>

            <h4>The Two Equations</h4>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                <strong>First stage:</strong> s<sub>i</sub> = X<sub>i</sub>'π<sub>10</sub> + π<sub>11</sub>z<sub>i</sub> + η<sub>1i</sub><br><br>
                <strong>Reduced form:</strong> y<sub>i</sub> = X<sub>i</sub>'π<sub>20</sub> + π<sub>21</sub>z<sub>i</sub> + η<sub>2i</sub>
            </div>
            <p>The IV estimand is ρ = π<sub>21</sub> / π<sub>11</sub>, also called the <strong>Indirect Least Squares (ILS)</strong> estimator.</p>

            <h3>4.1.1 Two-Stage Least Squares (2SLS)</h3>

            <p>2SLS operationalizes IV as a two-step procedure:</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Stage 1:</strong> Regress the endogenous variable on instruments and covariates to get fitted values.</p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; margin: 0.5rem 0;">
                    ŝ<sub>i</sub> = X<sub>i</sub>'π̂<sub>10</sub> + π̂<sub>11</sub>z<sub>i</sub>
                </div>
                <p><strong>Stage 2:</strong> Regress the outcome on fitted values and covariates.</p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; margin: 0.5rem 0;">
                    y<sub>i</sub> = δ'X<sub>i</sub> + ρŝ<sub>i</sub> + [ε<sub>i</sub> + (s<sub>i</sub> − ŝ<sub>i</sub>)]
                </div>
            </div>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Why does it work?</strong></p>
                <ul>
                    <li>ŝ<sub>i</sub> retains <em>only</em> the variation in schooling driven by the instrument</li>
                    <li>This quasi-experimental variation is uncorrelated with the error term</li>
                    <li>With a single instrument, 2SLS = ILS (reduced form ÷ first stage)</li>
                </ul>
            </div>

            <h4>Multiple Instruments</h4>
            <p>With three quarter-of-birth dummies (z<sub>1i</sub>, z<sub>2i</sub>, z<sub>3i</sub>), the first stage becomes:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                s<sub>i</sub> = X<sub>i</sub>'π<sub>10</sub> + π<sub>11</sub>z<sub>1i</sub> + π<sub>12</sub>z<sub>2i</sub> + π<sub>13</sub>z<sub>3i</sub> + η<sub>1i</sub>
            </div>
            <p>2SLS optimally combines multiple instruments into a single fitted value. The exclusion restriction requires that <em>all</em> instruments are uncorrelated with the structural error.</p>

            <h4>Results: Returns to Schooling</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Specification</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">OLS</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">2SLS</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Instruments</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">No controls</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.075</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.103 (0.024)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">QOB=1 dummy</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">YOB + SOB dummies</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.072</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.108 (0.019)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">3 QOB dummies</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+ QOB×YOB interactions</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.072</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.089 (0.016)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">30 instruments</td>
                </tr>
            </table>
            <p>2SLS estimates are slightly <em>larger</em> than OLS, suggesting OVB does not drive the schooling-earnings relationship in this case.</p>

            <h3>4.1.2 The Wald Estimator</h3>

            <p>The simplest IV setup: a <strong>single binary instrument</strong>, no covariates.</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>The Wald formula:</strong></p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.2rem; margin: 0.5rem 0;">
                    ρ = [E(y<sub>i</sub>|z<sub>i</sub>=1) − E(y<sub>i</sub>|z<sub>i</sub>=0)] / [E(s<sub>i</sub>|z<sub>i</sub>=1) − E(s<sub>i</sub>|z<sub>i</sub>=0)]
                </div>
                <p style="text-align: center; margin-top: 0.5rem;">= Difference in outcome means ÷ Difference in treatment means</p>
            </div>

            <h4>Example 1: Returns to Schooling</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;"></th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Born Q1–Q2</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Born Q3–Q4</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Difference</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">ln(weekly wage)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">5.8916</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">5.9051</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.01349</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Years of education</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">12.6881</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">12.8394</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.1514</td>
                </tr>
                <tr style="background: #ecfdf5;">
                    <td style="padding: 0.5rem; border: 1px solid #ddd;" colspan="3"><strong>Wald estimate</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>0.0891</strong> (0.021)</td>
                </tr>
            </table>

            <h4>Example 2: Vietnam Draft Lottery (Angrist 1990)</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Setup:</strong> Random draft lottery numbers → draft eligibility → military service → earnings</p>
                <ul>
                    <li><strong>Instrument:</strong> draft-eligibility (random, binary)</li>
                    <li><strong>Treatment:</strong> veteran status</li>
                    <li>Draft-eligible men were 15.9 pp more likely to serve</li>
                    <li>Wald estimate: service reduced 1981 earnings by ~$2,741</li>
                </ul>
                <p><strong>Validity check:</strong> No effect on 1969 earnings (pre-lottery) → instrument is clean.</p>
            </div>

            <h4>Example 3: Fertility and Labor Supply (Angrist & Evans 1998)</h4>
            <p>Two instruments for having a third child among mothers with ≥2 children:</p>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Outcome</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">OLS</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Twins IV (1st stage: 0.625)</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Same-sex IV (1st stage: 0.067)</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Employment</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.167</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.083</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.135</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Weeks worked</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−8.05</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−3.83</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−6.23</td>
                </tr>
            </table>
            <p>Different instruments yield different estimates → foreshadows heterogeneous effects (Part 2).</p>

            <h3>4.1.3 Grouped Data and 2SLS</h3>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Key insight:</strong> 2SLS with dummy instruments = GLS on group means = Efficient linear combination of all possible Wald estimators.</p>
            </div>

            <p>When the instrument takes on discrete values (j = 1, …, J), define group means ȳ<sub>j</sub> and p̂<sub>j</sub>. The grouped regression:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                ȳ<sub>j</sub> = α + ρp̂<sub>j</sub> + ε̄<sub>j</sub>
            </div>
            <p>GLS (weighted by group size n<sub>j</sub>) on this equation equals 2SLS using a full set of group dummies as instruments.</p>

            <h4>Visual Instrumental Variables (VIV)</h4>
            <p>A VIV plot displays the grouped-data relationship: average outcome vs. probability of treatment, across instrument cells. The slope of the line through these points is the IV estimate. This provides a powerful visual check on the IV strategy.</p>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Draft lottery VIV (Angrist 1990):</strong> Plotting average earnings residuals vs. probability of service across 5-number RSN cells gives an IV estimate of about −$2,400, consistent with the Wald estimate.</p>
            </div>
        </div>
    </section>

    <!-- 4.2 Asymptotic 2SLS Inference -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4.2 Asymptotic 2SLS Inference</h2>
        <div class="section-content">

            <h3>4.2.1 Standard Errors</h3>
            <p>The 2SLS standard errors differ from manual two-step OLS standard errors. The error variance should use the structural residual ε<sub>i</sub>, not the second-stage residual ε<sub>i</sub> + (s<sub>i</sub> − ŝ<sub>i</sub>). Always use canned 2SLS routines to get correct standard errors.</p>

            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Warning:</strong> Running "manual 2SLS" (regressing y on ŝ by OLS) gives <strong>wrong standard errors</strong>. The OLS residual variance includes the first-stage estimation error, overstating the true residual variance.</p>
            </div>

            <h3>4.2.2 Over-Identification Tests</h3>
            <p>When you have more instruments than endogenous variables (over-identification), you can test whether all instruments give the same answer.</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Over-ID test statistic:</strong> Under H<sub>0</sub>: E[Z<sub>i</sub>ε<sub>i</sub>] = 0, the minimized 2SLS minimand follows a χ²(q−1) distribution, where q is the number of instruments.</p>
                <p><strong>Computation:</strong> N × R² from regressing 2SLS residuals on all instruments and covariates.</p>
            </div>

            <p>With dummy instruments, the over-ID test is equivalent to a chi-square goodness-of-fit test for the VIV plot: does a straight line fit the group means well?</p>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Caveat:</strong> Over-ID tests have limited practical value.</p>
                <ul>
                    <li>When IV estimates are <em>imprecise</em>, the test has low power (can't reject even if instruments are bad)</li>
                    <li>When IV estimates are <em>precise</em>, rejection may reflect treatment effect heterogeneity, not invalid instruments</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- 4.3 Two-Sample IV -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4.3 Two-Sample IV and Split-Sample IV</h2>
        <div class="section-content">

            <h3>Two-Sample IV (TSIV)</h3>
            <p>IV can be constructed from <strong>sample moments alone</strong>. The first-stage and reduced-form data need not come from the same dataset, as long as both are drawn from the same population.</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>When is TSIV useful?</strong> When no single dataset contains all needed variables. For example:</p>
                <ul>
                    <li>Data set 1 (SSA records): earnings + draft lottery numbers → reduced form</li>
                    <li>Data set 2 (military records): veteran status + lottery numbers → first stage</li>
                </ul>
            </div>

            <h3>Split-Sample IV (SSIV)</h3>
            <p>Angrist & Krueger (1995) proposed a computationally simple TSIV estimator:</p>
            <ol>
                <li>Estimate the first stage in data set 2: get π̂ from (Z₂'Z₂)⁻¹Z₂'W₂</li>
                <li>Construct cross-sample fitted values: Ŵ₁₂ = Z₁π̂</li>
                <li>Regress y₁ on Ŵ₁₂ in data set 1</li>
            </ol>
            <p>SSIV can also help reduce bias in over-identified models (discussed in Part 3).</p>
        </div>
    </section>

    <!-- Summary -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Part 1 Summary</h2>
        <div class="section-content">
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Concept</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Key Point</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>IV Estimand</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">ρ = Cov(y, z) / Cov(s, z) = Reduced form ÷ First stage</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Exclusion Restriction</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">z affects y <em>only through</em> its effect on s</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>2SLS</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Replace endogenous variable with first-stage fitted values</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Wald Estimator</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Difference in outcome means ÷ Difference in treatment means (binary z)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Grouped Data = 2SLS</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">GLS on group means with dummy instruments equals 2SLS</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Over-ID Test</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Tests if all instruments produce the same estimate; limited practical value</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>TSIV / SSIV</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">First stage and reduced form can come from different datasets</td>
                </tr>
            </table>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>The IV recipe:</strong></p>
                <ol>
                    <li>Find an instrument that is (a) correlated with the treatment, and (b) uncorrelated with the error</li>
                    <li>Estimate the first stage — if it's weak, worry (more in Part 3)</li>
                    <li>Look at the reduced form — this is the causal effect of the instrument, always unbiased</li>
                    <li>Compute IV = reduced form ÷ first stage</li>
                </ol>
            </div>
        </div>
    </section>

    <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee; display: flex; justify-content: space-between;">
        <a href="/study/angrist-ch3" style="color: #666;">← Chapter 3: Making Regression Make Sense</a>
        <a href="/study/angrist-ch4-part2" style="color: #2563eb;">Part 2: LATE & Heterogeneous Effects →</a>
    </div>

    <div style="margin-top: 2rem; padding: 1rem; background: #f9fafb; border-radius: 8px; font-size: 0.8rem; color: #6b7280;">
        <em>This note was written with the assistance of LLM (Claude).</em>
    </div>
</div>
