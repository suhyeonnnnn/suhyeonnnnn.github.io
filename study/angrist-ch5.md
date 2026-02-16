---
layout: minimal_base
title: "Angrist Ch.5 - Fixed Effects, DD, and Panel Data"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Chapter 5: Fixed Effects, Differences-in-Differences, and Panel Data</h2>
            <a href="/study/angrist-ch5-ko" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">한국어</a>
        </div>
        <div class="section-content">
            <p><em>Angrist & Pischke, Mostly Harmless Econometrics — Chapter 5</em></p>
            <p style="color: #6b7280; font-style: italic;">"The first thing to realize about parallel universes... is that they are not parallel." — Douglas Adams</p>
        </div>
    </section>

    <!-- Core Message -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Core Message</h2>
        <div class="section-content">
            <blockquote style="border-left: 4px solid #2563eb; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                When important confounders are <strong>unobserved but fixed over time</strong>, we can eliminate them using panel data strategies: <strong>fixed effects</strong> (within-person variation) or <strong>differences-in-differences</strong> (parallel trends assumption). These methods "punt on comparisons in levels" while requiring counterfactual trends to be the same.
            </blockquote>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>The identification toolkit so far:</strong></p>
                <ul>
                    <li><strong>Chapter 3:</strong> Control for <em>observed</em> confounders (regression, matching)</li>
                    <li><strong>Chapter 4:</strong> Use instruments when confounders are <em>unobserved</em></li>
                    <li><strong>Chapter 5:</strong> Exploit <em>time/cohort dimension</em> when confounders are unobserved but fixed</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- 5.1 Individual Fixed Effects -->
    <section class="section fade-in-delay">
        <h2 class="section-title">5.1 Individual Fixed Effects</h2>
        <div class="section-content">

            <h3>Motivation: Union Wage Premium</h3>
            <p>Classic question in Labor Economics: Do workers whose wages are set by collective bargaining earn more <em>because</em> of this, or would they earn more anyway (perhaps because they are more experienced or skilled)?</p>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <strong style="color: #92400e;">The Problem:</strong> Unobserved worker ability A<sub>i</sub> affects both union status and wages. If more able workers are more likely to join unions, OLS overstates the union effect.
            </div>

            <h3>The Fixed Effects Setup</h3>
            <p>Let y<sub>it</sub> = log earnings of worker i at time t, and d<sub>it</sub> = union status. Assume:</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                <p><strong>Conditional independence:</strong></p>
                <p style="text-align: center;">E(y<sub>0it</sub> | A<sub>i</sub>, X<sub>it</sub>, t, d<sub>it</sub>) = E(y<sub>0it</sub> | A<sub>i</sub>, X<sub>it</sub>, t)</p>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">Union status is as good as randomly assigned <em>conditional on</em> unobserved ability A<sub>i</sub>, observed covariates X<sub>it</sub>, and time.</p>
            </div>

            <p><strong>Key assumption:</strong> The unobserved A<sub>i</sub> appears <strong>without a time subscript</strong> in a linear model:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                E(y<sub>0it</sub> | A<sub>i</sub>, X<sub>it</sub>, t) = α + λ<sub>t</sub> + A'<sub>i</sub>γ + X<sub>it</sub>β
            </div>

            <p>With constant, additive treatment effect ρ:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                E(y<sub>1it</sub> | A<sub>i</sub>, X<sub>it</sub>, t) = E(y<sub>0it</sub> | A<sub>i</sub>, X<sub>it</sub>, t) + ρ
            </div>

            <p>This implies the <strong>fixed effects model</strong>:</p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center; font-size: 1.1rem;">
                y<sub>it</sub> = α<sub>i</sub> + λ<sub>t</sub> + ρd<sub>it</sub> + X<sub>it</sub>β + ε<sub>it</sub>
            </div>
            <p>where α<sub>i</sub> ≡ α + A'<sub>i</sub>γ is the <strong>individual fixed effect</strong> (treated as a parameter to be estimated), and λ<sub>t</sub> is a <strong>year effect</strong> (coefficients on time dummies).</p>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <strong style="color: #92400e;">Note:</strong> These assumptions are <em>more restrictive</em> than those in Chapter 3. We need the linear, additive functional form to make progress on unobserved confounders using panel data without instruments.
            </div>

            <h3>Estimation Strategy 1: Deviations from Means</h3>
            <p>With panel data (repeated observations on individuals), we can eliminate α<sub>i</sub>. First, calculate individual averages:</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                ȳ<sub>i</sub> = α<sub>i</sub> + λ̄ + ρd̄<sub>i</sub> + X̄<sub>i</sub>β + ε̄<sub>i</sub>
            </div>

            <p>Subtracting from the original equation:</p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                (y<sub>it</sub> − ȳ<sub>i</sub>) = (λ<sub>t</sub> − λ̄) + ρ(d<sub>it</sub> − d̄<sub>i</sub>) + (X<sub>it</sub> − X̄<sub>i</sub>)β + (ε<sub>it</sub> − ε̄<sub>i</sub>)
            </div>

            <p><strong>The fixed effect α<sub>i</sub> is eliminated!</strong> This is called the <strong>"within estimator"</strong> or <strong>"analysis of covariance"</strong>.</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Why does this work algebraically?</strong></p>
                <p>By the regression anatomy formula (3.1.3), estimating with a full set of person dummies is the same as regressing on the residuals from a regression on those dummies. The residuals from regressing on person dummies are exactly deviations from person means.</p>
            </div>

            <h3>Estimation Strategy 2: First Differencing</h3>
            <p>An alternative to deviations from means:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                Δy<sub>it</sub> = Δλ<sub>t</sub> + ρΔd<sub>it</sub> + ΔX<sub>it</sub>β + Δε<sub>it</sub>
            </div>

            <p>where Δy<sub>it</sub> = y<sub>it</sub> − y<sub>it−1</sub>.</p>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Method</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Deviations from Means</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">First Differencing</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">With T = 2</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;" colspan="2" align="center">Algebraically identical</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">With T > 2</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">More efficient if ε<sub>it</sub> is homoskedastic & serially uncorrelated</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">May be more convenient; note Δε<sub>it</sub> is serially correlated</td>
                </tr>
            </table>

            <h3>Fixed Effects vs. Random Effects</h3>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Random effects</strong> assumes α<sub>i</sub> is <em>uncorrelated</em> with the regressors. Then α<sub>i</sub> becomes part of the residual (no OVB from ignoring it), but residuals for a given person are correlated across periods.</p>
                <p style="margin-top: 0.5rem;"><strong>The authors prefer:</strong> OLS with fixed effects + robust standard errors, rather than GLS under random effects. GLS requires stronger assumptions (linear CEF, homoskedasticity) and efficiency gains are typically modest.</p>
            </div>

            <h3>Example: Union Wage Effects (Freeman 1984)</h3>
            <p>Freeman uses four panel data sets to estimate union wage effects:</p>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Survey</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Cross-section</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Fixed Effects</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">May CPS, 1974-75</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.19</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.09</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">NLS Young Men, 1970-78</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.28</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.19</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Michigan PSID, 1970-79</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.23</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.14</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">QES, 1973-77</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.14</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.16</td>
                </tr>
            </table>

            <p><strong>Pattern:</strong> FE estimates (0.09–0.19) are generally smaller than cross-section estimates (0.14–0.28). This suggests <strong>positive selection bias</strong> in cross-section — more able workers join unions <em>and</em> earn more.</p>

            <h3>Caution 1: Measurement Error</h3>
            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>FE estimates are notoriously susceptible to attenuation bias:</strong></p>
                <ul>
                    <li>Economic variables like union status tend to be <strong>persistent</strong> (a union member this year is likely a union member next year)</li>
                    <li>Measurement error often <strong>changes year-to-year</strong> (union status may be misreported this year but not next)</li>
                    <li>→ While few workers are misclassified in any single year, observed year-to-year <em>changes</em> in union status may be mostly noise</li>
                    <li>→ More measurement error in Δd<sub>it</sub> than in d<sub>it</sub> → FE estimates biased toward zero</li>
                </ul>
            </div>

            <p><strong>Possible fixes:</strong></p>
            <ul>
                <li><strong>IV:</strong> Use cross-sibling reports as instruments (Ashenfelter & Krueger 1994)</li>
                <li><strong>External validation:</strong> Adjust estimates using measurement error rates from validation surveys (Card 1996)</li>
            </ul>

            <h3>Caution 2: Removing Good Variation (Twins Example)</h3>
            <p>Differencing/demeaning removes <em>both</em> good and bad variation. The transformation may kill OVB bathwater but also remove useful information.</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Twins and Returns to Schooling:</strong></p>
                <p>Ashenfelter & Krueger (1994) and Ashenfelter & Rouse (1998) estimate returns to schooling using twins, controlling for family fixed effects (common family/genetic background).</p>
                <p style="margin-top: 0.5rem;"><strong>Surprising result:</strong> Within-family estimates are <em>larger</em> than OLS!</p>
                <p style="margin-top: 0.5rem;"><strong>Bound & Solon (1999) critique:</strong></p>
                <ul>
                    <li>Even twins have small differences: first-borns typically have higher birth weight and higher IQ</li>
                    <li>While within-twin differences are small, so is the difference in their schooling</li>
                    <li>→ A small amount of unobserved ability differences could cause substantial bias</li>
                </ul>
            </div>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <strong style="color: #92400e;">Bottom line:</strong> Avoid overly strong claims when interpreting fixed-effects estimates. The exact nature of unobserved variables typically remains somewhat mysterious.
            </div>
        </div>
    </section>

    <!-- 5.2 Differences-in-Differences -->
    <section class="section fade-in-delay">
        <h2 class="section-title">5.2 Differences-in-Differences (DD)</h2>
        <div class="section-content">

            <h3>When Treatment Varies at Group Level</h3>
            <p>FE requires panel data with repeated observations on the <em>same individuals</em>. Often, however, treatment varies only at a more aggregate level (state, cohort). Examples:</p>
            <ul>
                <li>State policies on health care benefits for pregnant workers</li>
                <li>State minimum wages</li>
                <li>Court rulings on employment law</li>
            </ul>
            <p>The source of OVB must therefore be unobserved variables at the <strong>state and year level</strong>.</p>

            <h3>Classic Example: Card & Krueger (1994) — Minimum Wage</h3>
            <p>Classic question: In a competitive labor market, higher minimum wages should reduce employment (moving up a downward-sloping demand curve). Does this actually happen?</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Natural experiment:</strong></p>
                <ul>
                    <li><strong>April 1, 1992:</strong> New Jersey raised state minimum from $4.25 to $5.05</li>
                    <li><strong>Pennsylvania:</strong> Stayed at $4.25 (federal minimum)</li>
                    <li><strong>Data:</strong> Employment at fast food restaurants (Burger King, Wendy's, etc.) in NJ and eastern PA</li>
                    <li><strong>Timing:</strong> February 1992 (before) and November 1992 (after)</li>
                </ul>
            </div>

            <h3>The DD Model</h3>
            <p>Define potential outcomes:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                y<sub>1ist</sub> = employment if high minimum wage<br>
                y<sub>0ist</sub> = employment if low minimum wage
            </div>

            <p><strong>Key assumption — parallel trends in absence of treatment:</strong></p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center; font-size: 1.1rem;">
                E(y<sub>0ist</sub> | s, t) = γ<sub>s</sub> + λ<sub>t</sub>
            </div>

            <p>This says: in the absence of a minimum wage change, employment is determined by the sum of:</p>
            <ul>
                <li><strong>γ<sub>s</sub>:</strong> Time-invariant state effect (plays the role of α<sub>i</sub> in individual FE)</li>
                <li><strong>λ<sub>t</sub>:</strong> Year effect common across states</li>
            </ul>

            <p>With constant treatment effect δ:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                y<sub>ist</sub> = γ<sub>s</sub> + λ<sub>t</sub> + δd<sub>st</sub> + ε<sub>ist</sub>
            </div>
            <p>where d<sub>st</sub> is a dummy for high-minimum-wage state-periods and E(ε<sub>ist</sub> | s, t) = 0.</p>

            <h3>Deriving the DD Estimator</h3>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                <p><strong>Control state (PA):</strong></p>
                <p style="padding-left: 1rem;">E[y|PA, Nov] − E[y|PA, Feb] = λ<sub>Nov</sub> − λ<sub>Feb</sub></p>
                
                <p style="margin-top: 0.5rem;"><strong>Treatment state (NJ):</strong></p>
                <p style="padding-left: 1rem;">E[y|NJ, Nov] − E[y|NJ, Feb] = λ<sub>Nov</sub> − λ<sub>Feb</sub> + δ</p>
                
                <p style="margin-top: 0.5rem;"><strong>Difference-in-differences:</strong></p>
                <p style="padding-left: 1rem;">[E[y|NJ, Nov] − E[y|NJ, Feb]] − [E[y|PA, Nov] − E[y|PA, Feb]] = <strong>δ</strong></p>
            </div>

            <h3>Card & Krueger Results</h3>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">FTE Employment</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">PA (Control)</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">NJ (Treatment)</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">NJ − PA</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Before (Feb)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">23.33 (1.35)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">20.44 (0.51)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−2.89 (1.44)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">After (Nov)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">21.17 (0.94)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">21.03 (0.52)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.14 (1.07)</td>
                </tr>
                <tr style="background: #f0fdf4;">
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Change</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>−2.16</strong> (1.25)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>+0.59</strong> (0.54)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; background: #dcfce7;"><strong>+2.76</strong> (1.36)</td>
                </tr>
            </table>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Interpretation:</strong></p>
                <ul>
                    <li>PA employment fell by 2.16 workers per store</li>
                    <li>NJ employment rose by 0.59 workers per store</li>
                    <li><strong>DD = +2.76</strong> — opposite of standard prediction!</li>
                    <li>Higher minimum wage did not reduce employment; if anything, it slightly increased it</li>
                </ul>
            </div>

            <h3>Visual Representation</h3>
            <div style="background: #f9f9f9; padding: 1.5rem; border-radius: 8px; margin: 1rem 0; text-align: center;">
                <pre style="font-family: monospace; font-size: 0.85rem; text-align: left; display: inline-block;">
Employment
    │
    │                    ●───────● Treatment (observed)
    │                   ╱         
    │                  ╱  ← Treatment effect (δ)
    │                 ╱           
    │                ●─ ─ ─ ─ ─ ●  Counterfactual
    │               ╱               (parallel to control)
    │              ╱
    │  ●─────────●  Control (observed)
    │
    └────────────────────────────── Time
              Before      After

Key insight: We never observe the counterfactual.
The parallel trends assumption lets us use
the control group's change as a proxy.
                </pre>
            </div>

            <h3>Testing Parallel Trends</h3>
            <p>The identifying assumption can be investigated with <strong>multiple pre-treatment periods</strong>. Do treatment and control follow similar trends before treatment?</p>

            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Card & Krueger (2000) Follow-up:</strong></p>
                <p>Administrative payroll data for restaurants in NJ and PA for multiple years reveal:</p>
                <ul>
                    <li>Feb-Nov 1992: Slight PA decline, little NJ change (consistent with original survey)</li>
                    <li>But: Substantial year-to-year variation in other periods</li>
                    <li>Employment swings often differ substantially between states</li>
                    <li>PA employment fell relative to NJ over 1992-1995, mostly <em>before</em> the 1996 federal minimum increase</li>
                </ul>
                <p style="margin-top: 0.5rem;"><strong>Concern:</strong> PA may not provide a good measure of counterfactual NJ employment.</p>
            </div>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Better Example: Pischke (2007) — German School Term Length</strong></p>
                <ul>
                    <li>Until 1960s: German states (except Bavaria) started school in Spring</li>
                    <li>1966-67: Non-Bavarian states switched to Fall start</li>
                    <li>Transition required <strong>two short school years</strong> (24 weeks instead of 37)</li>
                    <li>Outcome: Grade repetition rates for 2nd graders</li>
                </ul>
                <p style="margin-top: 0.5rem;"><strong>Results:</strong></p>
                <ul>
                    <li>Bavaria (control): Flat repetition rates ~2.5% from 1966 onwards</li>
                    <li>Treatment states: Higher baseline (~4-4.5%), jump by ~1 percentage point for affected cohorts, then return to baseline</li>
                    <li>→ Strong visual evidence of parallel trends + transitory treatment effect</li>
                </ul>
            </div>

            <h3>5.2.1 Regression DD</h3>
            <p>DD can be estimated via regression. Let NJ<sub>s</sub> = dummy for NJ, d<sub>t</sub> = dummy for November:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center; font-size: 1.05rem;">
                y<sub>ist</sub> = α + γ·NJ<sub>s</sub> + λ·d<sub>t</sub> + <strong>δ·(NJ<sub>s</sub> × d<sub>t</sub>)</strong> + ε<sub>ist</sub>
            </div>

            <p><strong>Parameter interpretation:</strong></p>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Parameter</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Meaning</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">α</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">E[y | PA, Feb] = γ<sub>PA</sub> + λ<sub>Feb</sub></td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">γ</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">E[y | NJ, Feb] − E[y | PA, Feb] = γ<sub>NJ</sub> − γ<sub>PA</sub></td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">λ</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">E[y | PA, Nov] − E[y | PA, Feb] = λ<sub>Nov</sub> − λ<sub>Feb</sub></td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;"><strong>δ</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>DD estimate</strong> = {E[y|NJ,Nov] − E[y|NJ,Feb]} − {E[y|PA,Nov] − E[y|PA,Feb]}</td>
                </tr>
            </table>

            <p>This is a <strong>saturated model</strong>: 4 possible values of E(y|s,t), 4 parameters.</p>

            <h4>Advantages of Regression DD:</h4>

            <p><strong>1. Easy to add states/periods:</strong> Just include more dummies. The generalization includes a dummy for each state and period.</p>

            <p><strong>2. Variable treatment intensity:</strong> Instead of switched-on/off treatment, use continuous measures.</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Example: Card (1992) — Federal Minimum Wage</strong></p>
                <p>In 1990, federal minimum increased from $3.35 to $3.80. Impact varies by state (irrelevant in high-wage Connecticut, big deal in low-wage Mississippi).</p>
                <div style="font-family: 'Times New Roman', serif; text-align: center; margin: 0.5rem 0;">
                    y<sub>ist</sub> = γ<sub>s</sub> + λ<sub>t</sub> + δ·(fa<sub>s</sub> × d<sub>t</sub>) + ε<sub>ist</sub>
                </div>
                <p>where fa<sub>s</sub> = baseline fraction of teens earning below $3.80 in state s (treatment intensity).</p>
            </div>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Outcome</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Δ Mean Log Wage</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Δ Emp/Pop Ratio</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Fraction affected (fa<sub>s</sub>)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.15 (0.03)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.02 (0.03)</td>
                </tr>
            </table>
            <p>Wages rose more in states where minimum wage had more bite (0.15), but employment was largely unrelated to fraction affected (0.02 ≈ 0).</p>

            <p><strong>3. Easy to add covariates:</strong> Control for time-varying state characteristics X<sub>st</sub> (e.g., adult employment as proxy for state economic conditions).</p>

            <h3>Granger-Style Causality Tests: Leads and Lags</h3>
            <p>When the sample includes many years and treatment timing varies across states, we can test whether "causes happen before consequences":</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                y<sub>ist</sub> = γ<sub>s</sub> + λ<sub>t</sub> + Σ<sub>τ=0</sub><sup>m</sup> δ<sub>−τ</sub>d<sub>s,t−τ</sub> + Σ<sub>τ=1</sub><sup>q</sup> δ<sub>+τ</sub>d<sub>s,t+τ</sub> + X<sub>ist</sub>β + ε<sub>ist</sub>
            </div>

            <ul>
                <li><strong>Lags</strong> (δ<sub>−τ</sub>): Post-treatment effects — how do effects evolve over time?</li>
                <li><strong>Leads</strong> (δ<sub>+τ</sub>): Pre-treatment "effects" — should be zero if treatment is causal!</li>
            </ul>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Example: Autor (2003) — Employment Protection & Temp Workers</strong></p>
                <p>State court rulings allowing "unjust dismissal" lawsuits → Do firms use more temp workers?</p>
                <p style="margin-top: 0.5rem;"><strong>Estimated leads and lags pattern:</strong></p>
                <ul>
                    <li><strong>2 years before, 1 year before:</strong> No effect (leads ≈ 0) ✓</li>
                    <li><strong>Year of adoption:</strong> Small positive effect</li>
                    <li><strong>1-3 years after:</strong> Sharply increasing effects</li>
                    <li><strong>4+ years after:</strong> Effects flatten at permanently higher level</li>
                </ul>
                <p style="margin-top: 0.5rem;">This pattern is consistent with a causal interpretation: no anticipation, gradual adjustment.</p>
            </div>

            <h3>State-Specific Trends</h3>
            <p>Alternative robustness check: allow treatment and control to follow different <em>linear</em> trends:</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                y<sub>ist</sub> = γ<sub>0s</sub> + γ<sub>1s</sub>·t + λ<sub>t</sub> + δd<sub>st</sub> + X<sub>ist</sub>β + ε<sub>ist</sub>
            </div>

            <p>This allows limited heterogeneity in trends. It's heartening if results survive, discouraging otherwise.</p>

            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Example: Besley & Burgess (2004) — Labor Regulation in India</strong></p>
                <table style="width:100%; border-collapse: collapse; margin: 0.5rem 0; font-size: 0.9rem;">
                    <tr style="background: #f5f5f5;">
                        <th style="padding: 0.5rem; border: 1px solid #ddd;">Specification</th>
                        <th style="padding: 0.5rem; border: 1px solid #ddd;">Labor Regulation Effect</th>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">DD only</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.186 (0.064)</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">DD + state-level controls</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">−0.104 (0.039)</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>DD + state-specific trends</strong></td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>0.0002 (0.02)</strong></td>
                    </tr>
                </table>
                <p style="margin-top: 0.5rem;"><strong>Interpretation:</strong> Without trends, labor regulation appears to reduce output. With state trends, the effect disappears → regulation increased in states where output was <em>already declining</em>.</p>
            </div>

            <h3>Picking Controls: Composition Changes</h3>
            <p>DD sets up an implicit treatment-control comparison. A potential pitfall: <strong>composition changes</strong> as a result of treatment.</p>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Example: Welfare benefits and labor supply</strong></p>
                <p>If generous welfare states attract poor people with weak labor force attachment (program-induced migration), DD makes generous welfare look worse for labor supply than it really is.</p>
                <p style="margin-top: 0.5rem;"><strong>Fix:</strong> Use state of birth or previous residence (unchanged by treatment but correlated with current location). This can be implemented as an IV strategy.</p>
            </div>

            <h3>Triple Differences (DDD)</h3>
            <p>When treatment varies along three dimensions (state × time × age), use higher-order contrasts:</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                y<sub>iast</sub> = γ<sub>st</sub> + λ<sub>at</sub> + μ<sub>as</sub> + δd<sub>ast</sub> + X<sub>iast</sub>β + ε<sub>iast</sub>
            </div>

            <p>This controls for:</p>
            <ul>
                <li>γ<sub>st</sub>: State × time effects (common across age groups)</li>
                <li>λ<sub>at</sub>: Age × time effects (common across states)</li>
                <li>μ<sub>as</sub>: State × age effects (common across time)</li>
            </ul>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Example: Yelowitz (1995) — Medicaid Expansion</strong></p>
                <p>Medicaid eligibility was once tied to AFDC (cash welfare). In the 1980s, some states extended coverage to children in families ineligible for AFDC.</p>
                <p style="margin-top: 0.5rem;">Treatment varies by state, time, <em>and</em> child's age. DDD compares across all three dimensions, providing more convincing control than standard DD.</p>
            </div>
        </div>
    </section>

    <!-- 5.3 FE vs LDV -->
    <section class="section fade-in-delay">
        <h2 class="section-title">5.3 Fixed Effects versus Lagged Dependent Variables</h2>
        <div class="section-content">

            <h3>The Dilemma</h3>
            <p>FE and DD are based on <strong>time-invariant omitted variables</strong>. But for many questions, this assumption doesn't seem plausible.</p>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Example: Training Program Evaluation</strong></p>
                <p>People in government training programs have often suffered a recent setback (job loss). Many programs explicitly target such people.</p>
                <p style="margin-top: 0.5rem;"><strong>Ashenfelter (1978), Ashenfelter & Card (1985):</strong> Training participants exhibit a <strong>pre-program earnings dip</strong>.</p>
                <p style="margin-top: 0.5rem;">Past earnings is a <em>time-varying</em> confounder that cannot be subsumed in a time-invariant α<sub>i</sub>.</p>
            </div>

            <h3>Two Competing Models</h3>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;"></th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Fixed Effects</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Lagged Dependent Variable</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Selection based on</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Time-invariant unobservables (α<sub>i</sub>)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Past outcomes (y<sub>it−h</sub>)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>CIA</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif; font-size: 0.9rem;">E(y<sub>0it</sub>|α<sub>i</sub>, X<sub>it</sub>, d<sub>it</sub>) = E(y<sub>0it</sub>|α<sub>i</sub>, X<sub>it</sub>)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif; font-size: 0.9rem;">E(y<sub>0it</sub>|y<sub>it−h</sub>, X<sub>it</sub>, d<sub>it</sub>) = E(y<sub>0it</sub>|y<sub>it−h</sub>, X<sub>it</sub>)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Model</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif; font-size: 0.9rem;">y<sub>it</sub> = α<sub>i</sub> + λ<sub>t</sub> + ρd<sub>it</sub> + X<sub>it</sub>β + ε<sub>it</sub></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif; font-size: 0.9rem;">y<sub>it</sub> = θ + γy<sub>it−h</sub> + λ<sub>t</sub> + ρd<sub>it</sub> + X<sub>it</sub>β + ε<sub>it</sub></td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Appropriate when</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Permanent unobserved ability/preferences drive selection</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Recent setback/change drives selection (training programs)</td>
                </tr>
            </table>

            <h3>Can We Include Both?</h3>
            <p>Tempting to estimate a model with both α<sub>i</sub> and y<sub>it−1</sub>:</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                y<sub>it</sub> = α<sub>i</sub> + γy<sub>it−1</sub> + λ<sub>t</sub> + ρd<sub>it</sub> + X<sub>it</sub>β + ε<sub>it</sub>
            </div>

            <p>To remove α<sub>i</sub>, we difference:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                Δy<sub>it</sub> = γΔy<sub>it−1</sub> + Δλ<sub>t</sub> + ρΔd<sub>it</sub> + ΔX<sub>it</sub>β + Δε<sub>it</sub>
            </div>

            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Nickell (1981) Problem:</strong></p>
                <p>Δy<sub>it−1</sub> = y<sub>it−1</sub> − y<sub>it−2</sub> contains ε<sub>it−1</sub></p>
                <p>Δε<sub>it</sub> = ε<sub>it</sub> − ε<sub>it−1</sub> also contains ε<sub>it−1</sub></p>
                <p style="margin-top: 0.5rem;">→ <strong>Regressor correlated with error!</strong> OLS is inconsistent.</p>
            </div>

            <p><strong>Possible fix:</strong> Use y<sub>it−2</sub> as an instrument for Δy<sub>it−1</sub>. But this requires:</p>
            <ul>
                <li>At least 3 periods of data</li>
                <li>ε<sub>it</sub> to be serially uncorrelated (unlikely — earnings are highly persistent)</li>
            </ul>

            <h3>The Bracketing Property</h3>
            <p>The FE and LDV models are <strong>not nested</strong>. Only the combined model (which is hard to estimate) nests both. However, they have a useful <strong>bracketing property</strong>:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <table style="width:100%; border-collapse: collapse; margin: 0;">
                    <tr style="background: #059669; color: white;">
                        <th style="padding: 0.75rem; border: 1px solid #ddd;">If True Model Is...</th>
                        <th style="padding: 0.75rem; border: 1px solid #ddd;">But You Estimate...</th>
                        <th style="padding: 0.75rem; border: 1px solid #ddd;">Bias Direction</th>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">LDV (selection on y<sub>it−1</sub>)</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">FE (differencing)</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Upward</strong> — estimate too big</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">FE (selection on α<sub>i</sub>)</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">LDV (control for y<sub>it−1</sub>)</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Downward</strong> — estimate too small</td>
                    </tr>
                </table>
            </div>

            <p><strong>Implication:</strong> FE and LDV estimates <strong>bracket</strong> the true causal effect. You can think of them as providing bounds.</p>

            <h3>Appendix: Why Bracketing Works</h3>

            <details style="margin: 1rem 0; padding: 1rem; background: #f9f9f9; border-radius: 8px;">
                <summary style="cursor: pointer; font-weight: 600; color: #2563eb;">Click to expand: Mathematical derivation</summary>
                <div style="margin-top: 1rem;">
                    <p><strong>Case 1: LDV is correct, but you use FE</strong></p>
                    <p>True model (simplified, no covariates/time effects, d<sub>it−1</sub> = 0):</p>
                    <div style="font-family: 'Times New Roman', serif; padding: 0.5rem; background: white; border-radius: 4px; margin: 0.5rem 0;">
                        y<sub>it</sub> = α<sub>i</sub> + ρd<sub>it</sub> + ε<sub>it</sub>
                    </div>
                    <p>where ε<sub>it</sub> is serially uncorrelated and uncorrelated with α<sub>i</sub>, d<sub>it</sub>.</p>
                    
                    <p>You mistakenly control for y<sub>it−1</sub> = α<sub>i</sub> + ε<sub>it−1</sub>. The LDV estimator has probability limit:</p>
                    <div style="font-family: 'Times New Roman', serif; padding: 0.5rem; background: white; border-radius: 4px; margin: 0.5rem 0;">
                        Cov(y<sub>it</sub>, d̃<sub>it</sub>) / V(d̃<sub>it</sub>)
                    </div>
                    <p>where d̃<sub>it</sub> = d<sub>it</sub> − [regression of d<sub>it</sub> on y<sub>it−1</sub>].</p>
                    
                    <p>Substituting α<sub>i</sub> = y<sub>it−1</sub> − ε<sub>it−1</sub>:</p>
                    <div style="font-family: 'Times New Roman', serif; padding: 0.5rem; background: white; border-radius: 4px; margin: 0.5rem 0;">
                        y<sub>it</sub> = y<sub>it−1</sub> + ρd<sub>it</sub> + ε<sub>it</sub> − ε<sub>it−1</sub>
                    </div>
                    
                    <p>The LDV estimator picks up:</p>
                    <div style="font-family: 'Times New Roman', serif; padding: 0.5rem; background: white; border-radius: 4px; margin: 0.5rem 0;">
                        ρ + σ²<sub>ε</sub> / V(d̃<sub>it</sub>)
                    </div>
                    
                    <p>Since trainees have low y<sub>it−1</sub>, the correlation between d<sub>it</sub> and y<sub>it−1</sub> is negative (π < 0). The bias term is positive → <strong>LDV estimate is too small</strong>.</p>

                    <hr style="margin: 1rem 0;">

                    <p><strong>Case 2: FE is correct, but you use LDV</strong></p>
                    <p>True model:</p>
                    <div style="font-family: 'Times New Roman', serif; padding: 0.5rem; background: white; border-radius: 4px; margin: 0.5rem 0;">
                        y<sub>it</sub> = θ + γy<sub>it−1</sub> + ρd<sub>it</sub> + ε<sub>it</sub>
                    </div>
                    <p>where ε<sub>it</sub> is serially uncorrelated and 0 < γ < 1 (stationarity).</p>
                    
                    <p>You mistakenly difference (FE). Subtracting y<sub>it−1</sub>:</p>
                    <div style="font-family: 'Times New Roman', serif; padding: 0.5rem; background: white; border-radius: 4px; margin: 0.5rem 0;">
                        y<sub>it</sub> − y<sub>it−1</sub> = θ + (γ−1)y<sub>it−1</sub> + ρd<sub>it</sub> + ε<sub>it</sub>
                    </div>
                    
                    <p>The differenced estimator picks up:</p>
                    <div style="font-family: 'Times New Roman', serif; padding: 0.5rem; background: white; border-radius: 4px; margin: 0.5rem 0;">
                        ρ + (γ−1) × Cov(y<sub>it−1</sub>, d<sub>it</sub>) / V(d<sub>it</sub>)
                    </div>
                    
                    <p>Since γ < 1 (so γ−1 < 0) and trainees have low y<sub>it−1</sub> (negative correlation), the bias term is positive → <strong>FE estimate is too big</strong>.</p>
                </div>
            </details>

            <h3>Practical Advice</h3>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <ol>
                    <li><strong>Check robustness:</strong> Estimate both FE and LDV models. If they give similar results, you can be more confident.</li>
                    <li><strong>Interpret as bounds:</strong> If results differ, the truth likely lies between them (FE upper bound, LDV lower bound for positive effects).</li>
                    <li><strong>Think about selection:</strong> Is selection more plausibly based on permanent characteristics (FE) or recent history (LDV)?</li>
                </ol>
                <p style="margin-top: 0.5rem;"><strong>Example:</strong> Guryan (2004) uses this bracketing reasoning in studying the effects of court-ordered busing on Black high school graduation rates.</p>
            </div>
        </div>
    </section>

    <!-- Summary -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Chapter 5 Summary</h2>
        <div class="section-content">
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Concept</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Key Point</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Fixed Effects</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Eliminates time-invariant unobserved confounders using within-unit variation</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>FE Estimation</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Deviations from means or first-differencing (equivalent with T=2)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>FE Limitations</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Measurement error amplified; removes both good and bad variation</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>DD</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">FE for aggregate data: (ΔTreatment) − (ΔControl)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Parallel Trends</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Key DD assumption — treatment & control would follow same trend absent treatment</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Regression DD</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">State + time dummies + interaction; allows variable treatment intensity, covariates</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Testing DD</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Pre-trends, leads/lags (Granger), state-specific trends, triple differences</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>FE vs. LDV</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Different assumptions; not nested; estimates bracket true effect</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Bracketing</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">FE too big if LDV true; LDV too small if FE true → bounds on causal effect</td>
                </tr>
            </table>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Practical Checklist:</strong></p>
                <ol>
                    <li>✓ FE/DD exploit <strong>within-unit variation over time</strong> — gives up level comparisons</li>
                    <li>✓ Always <strong>test parallel trends</strong> with pre-treatment data when possible</li>
                    <li>✓ Check for <strong>measurement error</strong> effects (FE may be attenuated)</li>
                    <li>✓ Run <strong>leads/lags</strong> specification — leads should be zero</li>
                    <li>✓ Try <strong>state-specific trends</strong> as robustness check</li>
                    <li>✓ Consider <strong>both FE and LDV</strong> — they bracket the truth</li>
                    <li>✓ Watch for <strong>composition changes</strong> in treatment/control groups</li>
                </ol>
            </div>
        </div>
    </section>

    <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee; display: flex; justify-content: space-between;">
        <a href="/study/angrist-ch4-part3" style="color: #666;">← Ch 4-3: IV Details</a>
        <a href="/study/angrist-ch6" style="color: #9ca3af;">Ch 6: RDD →</a>
    </div>

    <div style="margin-top: 2rem; padding: 1rem; background: #f9fafb; border-radius: 8px; font-size: 0.8rem; color: #6b7280;">
        <em>This note was written with the assistance of LLM (Claude).</em>
    </div>
</div>
