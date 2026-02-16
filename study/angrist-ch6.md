---
layout: minimal_base
title: "Angrist Ch.6 - Regression Discontinuity Designs"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Chapter 6: Regression Discontinuity Designs</h2>
            <a href="/study/angrist-ch6-ko" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">한국어</a>
        </div>
        <div class="section-content">
            <p><em>Angrist & Pischke, Mostly Harmless Econometrics — Chapter 6</em></p>
            <p style="color: #6b7280; font-style: italic;">"The more rules, the tinier the rules, the more arbitrary they are, the better." — Douglas Adams</p>
        </div>
    </section>

    <!-- Core Message -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Core Message</h2>
        <div class="section-content">
            <blockquote style="border-left: 4px solid #2563eb; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                <strong>Regression Discontinuity (RD)</strong> exploits precise knowledge of the rules determining treatment. In a rule-based world, some rules are <em>arbitrary</em> and therefore provide good natural experiments. The key insight: if treatment switches on/off at a known cutoff, units just above and just below the cutoff are essentially comparable — like a local randomized experiment.
            </blockquote>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Two flavors of RD:</strong></p>
                <ul>
                    <li><strong>Sharp RD:</strong> Treatment is a <em>deterministic</em> function of a running variable — crossing the cutoff switches treatment on/off completely</li>
                    <li><strong>Fuzzy RD:</strong> Crossing the cutoff changes the <em>probability</em> of treatment — leads to an IV setup</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- 6.1 Sharp RD -->
    <section class="section fade-in-delay">
        <h2 class="section-title">6.1 Sharp RD</h2>
        <div class="section-content">

            <h3>The Setup</h3>
            <p>Sharp RD is used when treatment status is a <strong>deterministic and discontinuous</strong> function of a covariate x<sub>i</sub> (the "running variable" or "forcing variable"):</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center; font-size: 1.1rem;">
                d<sub>i</sub> = 1(x<sub>i</sub> ≥ x<sub>0</sub>) = 
                <span style="display: inline-block; text-align: left; vertical-align: middle;">
                    { 1 if x<sub>i</sub> ≥ x<sub>0</sub><br>
                    { 0 if x<sub>i</sub> < x<sub>0</sub>
                </span>
            </div>

            <p>where x<sub>0</sub> is a known <strong>threshold</strong> or <strong>cutoff</strong>.</p>

            <ul>
                <li><strong>Deterministic:</strong> Once we know x<sub>i</sub>, we know d<sub>i</sub></li>
                <li><strong>Discontinuous:</strong> No matter how close x<sub>i</sub> gets to x<sub>0</sub>, treatment is unchanged until x<sub>i</sub> = x<sub>0</sub></li>
            </ul>

            <h3>Motivating Example: National Merit Scholarships</h3>
            <p>The first RD study (Thistlethwaite & Campbell, 1960) asked: Do students who win National Merit Scholarship Awards have higher college completion rates <em>because</em> of the award?</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <ul>
                    <li><strong>Running variable (x<sub>i</sub>):</strong> PSAT score</li>
                    <li><strong>Cutoff (x<sub>0</sub>):</strong> Award threshold</li>
                    <li><strong>Treatment (d<sub>i</sub>):</strong> Receiving the scholarship</li>
                    <li><strong>Outcome (y<sub>i</sub>):</strong> College completion</li>
                </ul>
                <p style="margin-top: 0.5rem;"><strong>RD approach:</strong> Compare students with PSAT scores <em>just above</em> and <em>just below</em> the threshold. Any jump in college completion at the threshold is evidence of a treatment effect.</p>
            </div>

            <h3>Key Feature: No Overlap</h3>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Important distinction from matching/regression:</strong></p>
                <p>In RD, there is <em>no value of x<sub>i</sub></em> where we observe both treatment and control units. Unlike matching strategies based on overlap, <strong>RD validity turns on extrapolation</strong> — our willingness to assume the conditional mean function is smooth through the cutoff.</p>
                <p style="margin-top: 0.5rem;">→ This is why we cannot be as agnostic about functional form in RD as in Chapter 3.</p>
            </div>

            <h3>The Sharp RD Model</h3>
            <p>Assume potential outcomes follow a linear, constant-effects model:</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                E[y<sub>0i</sub> | x<sub>i</sub>] = α + βx<sub>i</sub><br>
                y<sub>1i</sub> = y<sub>0i</sub> + ρ
            </div>

            <p>This leads to the regression:</p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center; font-size: 1.1rem;">
                y<sub>i</sub> = α + βx<sub>i</sub> + ρd<sub>i</sub> + ε<sub>i</sub>
            </div>

            <p>where ρ is the causal effect of interest.</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Key difference from Chapter 3 regression:</strong></p>
                <p>Here d<sub>i</sub> is not just correlated with x<sub>i</sub> — it's a <em>deterministic function</em> of x<sub>i</sub>. RD captures causal effects by distinguishing:</p>
                <ul>
                    <li>The <strong>discontinuous</strong> function: 1(x<sub>i</sub> ≥ x<sub>0</sub>)</li>
                    <li>The <strong>smooth</strong> function: x<sub>i</sub></li>
                </ul>
            </div>

            <h3>Visual Intuition</h3>
            <div style="background: #f9f9f9; padding: 1.5rem; border-radius: 8px; margin: 1rem 0; text-align: center;">
                <pre style="font-family: monospace; font-size: 0.85rem; text-align: left; display: inline-block;">
Panel A: Linear E[y₀|x]          Panel B: Nonlinear E[y₀|x]

  y│                               y│
   │        ●●●●                    │           ●●●●
   │       ●                        │         ●●
   │      ● ← Jump (ρ)              │       ●● ← Jump (ρ)
   │     ●                          │     ●●
   │   ●●                           │   ●●
   │ ●●                             │ ●●
   └──────────────── x              └──────────────── x
          x₀                               x₀

Panel C: Nonlinearity mistaken for discontinuity

  y│
   │               ●●●●
   │           ●●●●
   │        ●●●    ← Sharp curve, NOT treatment!
   │     ●●●
   │   ●●
   │ ●●
   └──────────────── x
          x₀
                </pre>
            </div>

            <h3>Polynomial Controls</h3>
            <p>What if E[y<sub>0i</sub> | x<sub>i</sub>] = f(x<sub>i</sub>) is nonlinear? Model f(x<sub>i</sub>) with a p<sup>th</sup>-order polynomial:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                y<sub>i</sub> = α + β<sub>1</sub>x<sub>i</sub> + β<sub>2</sub>x<sub>i</sub>² + ... + β<sub>p</sub>x<sub>i</sub><sup>p</sup> + ρd<sub>i</sub> + ε<sub>i</sub>
            </div>

            <p>As long as f(x<sub>i</sub>) is <strong>continuous</strong> at x<sub>0</sub>, we can still identify the discontinuous jump ρ.</p>

            <h3>Allowing Different Slopes on Each Side</h3>
            <p>A more flexible model allows different trend functions for E[y<sub>0i</sub>|x<sub>i</sub>] and E[y<sub>1i</sub>|x<sub>i</sub>]. Define x̃<sub>i</sub> ≡ x<sub>i</sub> − x<sub>0</sub> (centering at the cutoff):</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                y<sub>i</sub> = α + β<sub>01</sub>x̃<sub>i</sub> + β<sub>02</sub>x̃<sub>i</sub>² + ... + β<sub>0p</sub>x̃<sub>i</sub><sup>p</sup><br>
                &nbsp;&nbsp;&nbsp;&nbsp;+ ρd<sub>i</sub> + δ<sub>1</sub>d<sub>i</sub>x̃<sub>i</sub> + δ<sub>2</sub>d<sub>i</sub>x̃<sub>i</sub>² + ... + δ<sub>p</sub>d<sub>i</sub>x̃<sub>i</sub><sup>p</sup> + ε<sub>i</sub>
            </div>

            <ul>
                <li>ρ = treatment effect at x<sub>i</sub> = x<sub>0</sub></li>
                <li>Interactions (d<sub>i</sub>x̃<sub>i</sub>, d<sub>i</sub>x̃<sub>i</sub>², ...) allow different slopes above/below cutoff</li>
                <li>Centering at x<sub>0</sub> ensures ρ still captures the effect at the cutoff</li>
            </ul>

            <h3>Nonparametric RD</h3>
            <p>To avoid functional form dependence entirely, focus on a <strong>narrow window</strong> around the cutoff:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                lim<sub>ε→0</sub> { E[y<sub>i</sub> | x<sub>0</sub> < x<sub>i</sub> < x<sub>0</sub>+ε] − E[y<sub>i</sub> | x<sub>0</sub>−ε < x<sub>i</sub> < x<sub>0</sub>] } = E[y<sub>1i</sub> − y<sub>0i</sub> | x<sub>i</sub> = x<sub>0</sub>]
            </div>

            <p>Comparing averages in small neighborhoods left and right of x<sub>0</sub> provides an estimate that doesn't depend on correctly specifying f(x<sub>i</sub>).</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Practical approaches:</strong></p>
                <ul>
                    <li><strong>Local linear regression:</strong> Weighted least squares with more weight near x<sub>0</sub> (Hahn, Todd, van der Klaauw, 2001)</li>
                    <li><strong>Discontinuity sample:</strong> Restrict to observations within [x<sub>0</sub>−h, x<sub>0</sub>+h] for bandwidth h (Angrist & Lavy, 1999)</li>
                </ul>
            </div>

            <h3>Robustness Checks for Sharp RD</h3>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Check</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">What to Look For</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Bandwidth sensitivity</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Estimates should be stable as you narrow the window around x<sub>0</sub> (fewer polynomial terms needed)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Pre-treatment covariates</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">No jump in covariates determined before treatment (balance check)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Density of running variable</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">No bunching/manipulation around x<sub>0</sub> (McCrary, 2008 test)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Placebo cutoffs</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">No jumps at other values of x<sub>i</sub> where there is no policy change</td>
                </tr>
            </table>

            <h3>Example: Lee (2008) — Incumbency Advantage</h3>
            <p><strong>Question:</strong> Does winning an election give parties an advantage in the next election (incumbency effect)?</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <ul>
                    <li><strong>Running variable (x<sub>i</sub>):</strong> Democratic vote share margin in election t</li>
                    <li><strong>Cutoff (x<sub>0</sub>):</strong> 0 (50% vote share)</li>
                    <li><strong>Treatment (d<sub>i</sub>):</strong> Democrat won election t (incumbent party)</li>
                    <li><strong>Outcome (y<sub>i</sub>):</strong> Probability Democrat wins election t+1</li>
                </ul>
            </div>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Key insight:</strong> Because d<sub>i</sub> = 1(vote margin ≥ 0) is a deterministic function of x<sub>i</sub>, there are <em>no confounding variables other than x<sub>i</sub></em>. This is a signal feature of RD.</p>
            </div>

            <p><strong>Results:</strong></p>
            <ul>
                <li>Win probability is an increasing function of past vote share (unsurprising)</li>
                <li><strong>Dramatic jump of ~40 percentage points</strong> at the 0% margin</li>
                <li>Barely winning (vs. barely losing) increases next-election win probability by 40pp</li>
            </ul>

            <p><strong>Validity check:</strong> Lee examines Democratic victories <em>before</em> the last election. These should show no jump at the current cutoff — and they don't, increasing confidence in the design.</p>

            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Manipulation concern:</strong> Could parties manipulate vote shares near the cutoff?</p>
                <p>The 2000 Florida recount suggests this is a real concern in close elections. McCrary (2008) proposes formal tests for manipulation by examining the density of x<sub>i</sub> around x<sub>0</sub>.</p>
            </div>
        </div>
    </section>

    <!-- 6.2 Fuzzy RD -->
    <section class="section fade-in-delay">
        <h2 class="section-title">6.2 Fuzzy RD is IV</h2>
        <div class="section-content">

            <h3>When Treatment Isn't Deterministic</h3>
            <p>In many settings, crossing the cutoff doesn't <em>perfectly</em> determine treatment — it only changes the <em>probability</em> of treatment. This is <strong>fuzzy RD</strong>.</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                P[d<sub>i</sub> = 1 | x<sub>i</sub>] = 
                <span style="display: inline-block; text-align: left; vertical-align: middle;">
                    { g<sub>1</sub>(x<sub>i</sub>) if x<sub>i</sub> ≥ x<sub>0</sub><br>
                    { g<sub>0</sub>(x<sub>i</sub>) if x<sub>i</sub> < x<sub>0</sub>
                </span>
                &nbsp;&nbsp;where g<sub>1</sub>(x<sub>0</sub>) ≠ g<sub>0</sub>(x<sub>0</sub>)
            </div>

            <p>The functions g<sub>0</sub> and g<sub>1</sub> can be anything as long as they <strong>differ at x<sub>0</sub></strong> (and the more the better!).</p>

            <h3>Fuzzy RD = IV</h3>
            <p>Define t<sub>i</sub> = 1(x<sub>i</sub> ≥ x<sub>0</sub>) as a dummy for crossing the threshold. The discontinuity t<sub>i</sub> becomes an <strong>instrument</strong> for treatment d<sub>i</sub>.</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>2SLS Setup:</strong></p>
                <p><strong>First stage:</strong></p>
                <div style="font-family: 'Times New Roman', serif; margin: 0.5rem 0; padding-left: 1rem;">
                    d<sub>i</sub> = π<sub>0</sub> + π<sub>1</sub>x<sub>i</sub> + π<sub>2</sub>x<sub>i</sub>² + ... + π<sub>p</sub>x<sub>i</sub><sup>p</sup> + <strong>γt<sub>i</sub></strong> + η<sub>1i</sub>
                </div>
                <p>where γ is the first-stage effect (jump in treatment probability at cutoff).</p>
                
                <p style="margin-top: 0.5rem;"><strong>Second stage:</strong></p>
                <div style="font-family: 'Times New Roman', serif; margin: 0.5rem 0; padding-left: 1rem;">
                    y<sub>i</sub> = α + β<sub>1</sub>x<sub>i</sub> + β<sub>2</sub>x<sub>i</sub>² + ... + β<sub>p</sub>x<sub>i</sub><sup>p</sup> + <strong>ρd<sub>i</sub></strong> + ε<sub>i</sub>
                </div>
            </div>

            <h3>Reduced Form</h3>
            <p>Substituting the first stage into the second stage:</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center;">
                y<sub>i</sub> = α' + β'<sub>1</sub>x<sub>i</sub> + β'<sub>2</sub>x<sub>i</sub>² + ... + β'<sub>p</sub>x<sub>i</sub><sup>p</sup> + <strong>(ργ)t<sub>i</sub></strong> + η<sub>2i</sub>
            </div>

            <p>The reduced-form coefficient on t<sub>i</sub> equals ργ (causal effect × first stage).</p>

            <h3>Nonparametric Fuzzy RD: The Wald Estimator</h3>
            <p>In a small neighborhood around x<sub>0</sub>, fuzzy RD becomes a simple Wald/IV estimator:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center; font-size: 1.05rem;">
                ρ = lim<sub>ε→0</sub> 
                <span style="display: inline-block; border-top: 1px solid black; padding-top: 0.3rem;">
                    E[y<sub>i</sub> | x<sub>0</sub> < x<sub>i</sub> < x<sub>0</sub>+ε] − E[y<sub>i</sub> | x<sub>0</sub>−ε < x<sub>i</sub> < x<sub>0</sub>]
                </span>
                <br>
                <span style="display: inline-block; border-bottom: 1px solid black; padding-bottom: 0.3rem;">
                    E[d<sub>i</sub> | x<sub>0</sub> < x<sub>i</sub> < x<sub>0</sub>+ε] − E[d<sub>i</sub> | x<sub>0</sub>−ε < x<sub>i</sub> < x<sub>0</sub>]
                </span>
                = <span style="display: inline-block; border-top: 1px solid black; padding-top: 0.3rem;">Reduced form jump</span>
                <br>
                <span style="display: inline-block; border-bottom: 1px solid black; padding-bottom: 0.3rem;">First stage jump</span>
            </div>

            <h3>LATE Interpretation</h3>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Fuzzy RD estimates a Local Average Treatment Effect (LATE):</strong></p>
                <p>The effect is for <strong>compliers</strong> — individuals whose treatment status changes as x<sub>i</sub> moves from just below to just above x<sub>0</sub>.</p>
                <p style="margin-top: 0.5rem;"><strong>Double locality:</strong></p>
                <ol>
                    <li>LATE is for compliers only (as with any IV)</li>
                    <li>Effect is estimated at x<sub>i</sub> = x<sub>0</sub> (local to the cutoff)</li>
                </ol>
            </div>

            <h3>Example: Angrist & Lavy (1999) — Class Size Effects</h3>
            <p><strong>Question:</strong> Do smaller classes improve student test scores? (Same question as Tennessee STAR experiment)</p>

            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Setting:</strong> Israeli schools have a maximum class size of 40 ("Maimonides' Rule").</p>
                <ul>
                    <li>Grades with ≤40 students → 1 class (up to 40 students)</li>
                    <li>Grades with 41 students → 2 classes (~20 students each)</li>
                    <li>Grades with 81 students → 3 classes (~27 students each)</li>
                </ul>
                <p style="margin-top: 0.5rem;"><strong>Maimonides' Rule formula:</strong></p>
                <div style="font-family: 'Times New Roman', serif; text-align: center; margin: 0.5rem 0;">
                    m<sub>sc</sub> = e<sub>s</sub> / (int[(e<sub>s</sub>−1)/40] + 1)
                </div>
                <p>where e<sub>s</sub> = enrollment, m<sub>sc</sub> = predicted class size.</p>
            </div>

            <h4>Why Fuzzy?</h4>
            <p>Maimonides' Rule doesn't predict class size <em>perfectly</em> — some schools split classes at enrollments below 40. This creates a fuzzy design.</p>

            <h4>The RD Setup</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">RD Component</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">In This Study</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Running variable (x<sub>i</sub>)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Grade enrollment (e<sub>s</sub>)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Cutoffs (x<sub>0</sub>)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">40, 80, 120, ...</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Treatment (d<sub>i</sub>)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Actual class size (n<sub>sc</sub>)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Instrument (t<sub>i</sub>)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Predicted class size from Maimonides' Rule (m<sub>sc</sub>)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Outcome (y<sub>i</sub>)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Test scores</td>
                </tr>
            </table>

            <h4>Visual: The Sawtooth Pattern</h4>
            <div style="background: #f9f9f9; padding: 1.5rem; border-radius: 8px; margin: 1rem 0; text-align: center;">
                <pre style="font-family: monospace; font-size: 0.85rem; text-align: left; display: inline-block;">
Class size
    │
 40 │     ●●●●●                ●●●●●
    │    ●     \              ●     \
 30 │   ●       \            ●       \
    │  ●         \          ●         \
 20 │ ●           ●●●●●●●●●●           ●●●●
    │              ↑                    ↑
    └───────────────────────────────────────── Enrollment
              40  41          80  81

    --- = Maimonides' Rule (predicted)
    ●●● = Actual class size (fuzzy)
                </pre>
            </div>

            <h4>Results: 5th Grade Math Scores</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.9rem;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;"></th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;" colspan="3">OLS</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;" colspan="2">2SLS (Full)</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;" colspan="2">2SLS (±5)</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Wald (±3)</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Class size</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+.322</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+.076</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+.019</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>−.230</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>−.261</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−.185</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−.443</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">−.270</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(s.e.)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(.039)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(.036)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(.044)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(.092)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(.113)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(.151)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(.236)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">(.281)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Controls</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">None</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">%disadv</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">+enroll</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">linear</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">quadratic</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">linear</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">quadratic</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">dummies</td>
                </tr>
            </table>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Key findings:</strong></p>
                <ul>
                    <li><strong>OLS:</strong> Positive relationship (larger classes → higher scores) — likely due to selection (better schools have larger classes)</li>
                    <li><strong>OLS + controls:</strong> Effect shrinks toward zero</li>
                    <li><strong>2SLS:</strong> Strong negative effect (−0.23 to −0.26) — smaller classes improve scores</li>
                    <li><strong>Discontinuity samples:</strong> Less precise but similar magnitude (~−0.27)</li>
                </ul>
                <p style="margin-top: 0.5rem;"><strong>Interpretation:</strong> A 7-student reduction in class size (as in Tennessee STAR) raises Math scores by ~1.75 points, effect size ≈ 0.18σ. Similar to Tennessee STAR results!</p>
            </div>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Precision vs. Robustness tradeoff:</strong></p>
                <p>As we shrink the discontinuity sample, estimates become less precise (larger s.e.) but more robust to functional form assumptions. The fact that estimates remain stable (~−0.25) across specifications is reassuring.</p>
            </div>
        </div>
    </section>

    <!-- Summary -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Chapter 6 Summary</h2>
        <div class="section-content">
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Concept</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Key Point</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>RD Core Idea</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Arbitrary rules create natural experiments — treatment determined by cutoff in running variable</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Sharp RD</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">d<sub>i</sub> = 1(x<sub>i</sub> ≥ x<sub>0</sub>) deterministically; selection-on-observables story</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Fuzzy RD</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">P(d<sub>i</sub>=1) jumps at x<sub>0</sub>; IV setup where t<sub>i</sub>=1(x<sub>i</sub>≥x<sub>0</sub>) instruments for d<sub>i</sub></td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Identification</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Distinguish discontinuous jump (treatment) from smooth trend (running variable)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Functional Form</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Must model E[y<sub>0</sub>|x] — use polynomials, allow different slopes, or focus on narrow bandwidth</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Validity Checks</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Pre-treatment covariate balance, no manipulation (density test), placebo cutoffs, bandwidth sensitivity</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>LATE</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">RD estimates are local to x<sub>0</sub>; fuzzy RD is LATE for compliers at the cutoff</td>
                </tr>
            </table>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Practical Checklist for RD:</strong></p>
                <ol>
                    <li>✓ Verify treatment assignment rule is based on known cutoff</li>
                    <li>✓ Check whether design is sharp or fuzzy</li>
                    <li>✓ Plot outcome vs. running variable — look for visible jump</li>
                    <li>✓ Control for smooth function of running variable (polynomial)</li>
                    <li>✓ Allow different slopes on each side of cutoff</li>
                    <li>✓ Check balance of pre-treatment covariates at cutoff</li>
                    <li>✓ Test for manipulation (density of running variable)</li>
                    <li>✓ Vary bandwidth — estimates should be stable</li>
                    <li>✓ For fuzzy RD: check first-stage strength</li>
                </ol>
            </div>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Sharp vs. Fuzzy Summary:</strong></p>
                <table style="width:100%; border-collapse: collapse; margin: 0.5rem 0;">
                    <tr style="background: #e5e7eb;">
                        <th style="padding: 0.5rem; border: 1px solid #ddd;"></th>
                        <th style="padding: 0.5rem; border: 1px solid #ddd;">Sharp RD</th>
                        <th style="padding: 0.5rem; border: 1px solid #ddd;">Fuzzy RD</th>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">Treatment at cutoff</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">Switches 0→1 with certainty</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">Probability increases</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">Estimation</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">OLS with polynomial controls</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">2SLS (IV)</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">Estimand</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">ATE at x<sub>0</sub></td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">LATE for compliers at x<sub>0</sub></td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">Example</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">Lee (2008) — election win</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">Angrist & Lavy (1999) — class size</td>
                    </tr>
                </table>
            </div>
        </div>
    </section>

    <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee; display: flex; justify-content: space-between;">
        <a href="/study/angrist-ch5" style="color: #666;">← Ch 5: Fixed Effects & DD</a>
        <a href="/study" style="color: #2563eb;">Back to Study Notes →</a>
    </div>

    <div style="margin-top: 2rem; padding: 1rem; background: #f9fafb; border-radius: 8px; font-size: 0.8rem; color: #6b7280;">
        <em>This note was written with the assistance of LLM (Claude).</em>
    </div>
</div>
