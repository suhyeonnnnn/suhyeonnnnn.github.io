---
layout: minimal_base
title: "Angrist Ch.4-2 - LATE & Heterogeneous Effects"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Chapter 4 Part 2: LATE & Heterogeneous Effects</h2>
            <a href="/study/angrist-ch4-part2-ko" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">한국어</a>
        </div>
        <div class="section-content">
            <p><em>Angrist & Pischke, Mostly Harmless Econometrics — Sections 4.4–4.5</em></p>
        </div>
    </section>

    <!-- Core Message -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Core Message</h2>
        <div class="section-content">
            <blockquote style="border-left: 4px solid #2563eb; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                When treatment effects are <strong>heterogeneous</strong> (different people benefit differently), IV estimates the <strong>Local Average Treatment Effect (LATE)</strong> — the causal effect specifically for <em>compliers</em>, the subpopulation whose treatment status is changed by the instrument.
            </blockquote>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Key questions this part answers:</strong></p>
                <ol>
                    <li>What does IV estimate with heterogeneous effects? → LATE (effect on compliers)</li>
                    <li>Who are compliers? → People whose treatment changes with the instrument</li>
                    <li>How does LATE relate to ATE and ATT? → Generally different, unless special cases apply</li>
                    <li>How does 2SLS generalize? → Weighted average of covariate-specific LATEs</li>
                </ol>
            </div>
        </div>
    </section>

    <!-- 4.4 IV with Heterogeneous Potential Outcomes -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4.4 IV with Heterogeneous Potential Outcomes</h2>
        <div class="section-content">

            <h3>Why Heterogeneity Matters</h3>
            <p>Constant effects (y<sub>1i</sub> − y<sub>0i</sub> = ρ for all i) is unrealistic. Different people benefit differently from treatment. This raises two concerns:</p>
            <ul>
                <li><strong>Internal validity:</strong> What exactly is IV estimating?</li>
                <li><strong>External validity:</strong> Do the results generalize to other populations?</li>
            </ul>

            <h3>Setup: Generalized Potential Outcomes</h3>
            <p>Define potential outcomes indexed by <em>both</em> treatment and instrument:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                y<sub>i</sub>(d, z) = potential outcome for person i with treatment d and instrument z<br><br>
                d<sub>1i</sub> = treatment status if z<sub>i</sub> = 1<br>
                d<sub>0i</sub> = treatment status if z<sub>i</sub> = 0
            </div>

            <h3>4.4.1 The LATE Theorem (Imbens & Angrist, 1994)</h3>

            <h4>Four Assumptions</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Assumption</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Formal Statement</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Intuition</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>A1: Independence</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">{y<sub>i</sub>(d,z), d<sub>1i</sub>, d<sub>0i</sub>} ⊥ z<sub>i</sub></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Instrument is as good as randomly assigned</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>A2: Exclusion</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">y<sub>i</sub>(d, 0) = y<sub>i</sub>(d, 1) for d = 0, 1</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Instrument affects outcome <em>only through</em> treatment</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>A3: First stage</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">E[d<sub>1i</sub> − d<sub>0i</sub>] ≠ 0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Instrument affects treatment on average</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>A4: Monotonicity</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; font-family: 'Times New Roman', serif;">d<sub>1i</sub> ≥ d<sub>0i</sub> for all i (or vice versa)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">No one is pushed <em>away</em> from treatment by the instrument</td>
                </tr>
            </table>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>The LATE Theorem:</strong></p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem; margin: 0.5rem 0;">
                    [E(y<sub>i</sub>|z<sub>i</sub>=1) − E(y<sub>i</sub>|z<sub>i</sub>=0)] / [E(d<sub>i</sub>|z<sub>i</sub>=1) − E(d<sub>i</sub>|z<sub>i</sub>=0)]
                </div>
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem; margin: 0.5rem 0;">
                    = E[y<sub>1i</sub> − y<sub>0i</sub> | d<sub>1i</sub> > d<sub>0i</sub>]
                </div>
                <p style="text-align: center;">The IV estimand = <strong>average causal effect for compliers</strong></p>
            </div>

            <h4>Proof Sketch</h4>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Numerator (reduced form):</strong></p>
                <p style="font-family: 'Times New Roman', serif; padding-left: 1rem;">
                    E[y<sub>i</sub>|z=1] − E[y<sub>i</sub>|z=0] = E[(y<sub>1i</sub>−y<sub>0i</sub>)(d<sub>1i</sub>−d<sub>0i</sub>)]
                </p>
                <p>By monotonicity, (d<sub>1i</sub>−d<sub>0i</sub>) is 0 or 1, so this equals:</p>
                <p style="font-family: 'Times New Roman', serif; padding-left: 1rem;">
                    = E[y<sub>1i</sub>−y<sub>0i</sub> | d<sub>1i</sub>>d<sub>0i</sub>] × P[d<sub>1i</sub>>d<sub>0i</sub>]
                </p>
                <p><strong>Denominator (first stage):</strong> E[d<sub>1i</sub>−d<sub>0i</sub>] = P[d<sub>1i</sub>>d<sub>0i</sub>]</p>
                <p>Dividing cancels the compliance probability, leaving LATE.</p>
            </div>

            <h4>Why Monotonicity?</h4>
            <p>Without monotonicity, some people are "defiers" (d<sub>1i</sub> < d<sub>0i</sub>). The reduced form becomes:</p>
            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                E[(y<sub>1i</sub>−y<sub>0i</sub>)|compliers]·P[compliers] − E[(y<sub>1i</sub>−y<sub>0i</sub>)|defiers]·P[defiers]
            </div>
            <p>Positive effects could be canceled by defiers, making the reduced form misleading. Monotonicity rules out this possibility.</p>

            <h3>4.4.2 The Compliant Subpopulation</h3>

            <p>The instrument partitions the population into three groups:</p>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Group</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Definition</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Draft Lottery Example</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Compliers</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">d<sub>1i</sub> = 1, d<sub>0i</sub> = 0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Served <em>because</em> of draft eligibility</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Always-takers</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">d<sub>1i</sub> = d<sub>0i</sub> = 1</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Volunteered regardless</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Never-takers</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">d<sub>1i</sub> = d<sub>0i</sub> = 0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Exempted / deferred regardless</td>
                </tr>
            </table>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>LATE ≠ ATE ≠ ATT in general:</strong></p>
                <ul>
                    <li><strong>ATT</strong> (effect on the treated) = weighted average of effects on always-takers and compliers</li>
                    <li><strong>ATE</strong> (average treatment effect) = weighted average of effects on all three groups</li>
                    <li><strong>LATE</strong> = effect on compliers only</li>
                </ul>
            </div>

            <h4>Special Cases: LATE = ATT or LATE = Effect on Non-treated</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Scenario</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Example</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Why</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">No always-takers: E[d|z=0]=0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">JTPA training experiment</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Treated = compliers only → LATE = ATT</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">No never-takers: d<sub>1i</sub>=1 for all i</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Twins instrument, Minneapolis DV experiment</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Non-treated = compliers only → LATE = E[y₁−y₀|d=0]</td>
                </tr>
            </table>

            <h3>4.4.3 IV in Randomized Trials (Bloom 1984)</h3>

            <p>In a randomized trial with <strong>one-sided non-compliance</strong> (some offered treatment decline, but no control subject gets treatment), the IV estimand is the <strong>effect of treatment on the treated</strong>.</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Bloom's Result:</strong> If E[d<sub>i</sub>|z<sub>i</sub>=0] = 0 (no always-takers), then:</p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    ITT / Compliance rate = E[y<sub>1i</sub>−y<sub>0i</sub> | d<sub>i</sub>=1] = ATT
                </div>
            </div>

            <h4>Example: JTPA Training Experiment</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;"></th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">By Training Status (OLS)</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">By Assignment (ITT)</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">IV Estimate (ATT)</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Men</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">$3,970</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">$1,117</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">$1,825</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Women</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">$2,133</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">$1,243</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">$1,942</td>
                </tr>
            </table>
            <p>OLS (by actual training) overstates the effect due to selection. ITT understates it because only 60% complied. IV = ITT ÷ 0.6 gives the causal effect on compliers = ATT.</p>

            <h3>4.4.4 Counting and Characterizing Compliers</h3>

            <h4>Size of Complier Group</h4>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                P[d<sub>1i</sub> > d<sub>0i</sub>] = E[d<sub>i</sub>|z<sub>i</sub>=1] − E[d<sub>i</sub>|z<sub>i</sub>=0] = <strong>First stage</strong>
            </div>

            <h4>Proportion of Treated Who Are Compliers</h4>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                P[d<sub>1i</sub>>d<sub>0i</sub> | d<sub>i</sub>=1] = P[z<sub>i</sub>=1] × (First stage) / P[d<sub>i</sub>=1]
            </div>

            <h4>Complier Characteristics</h4>
            <p>Although individual compliers can't be identified, the <em>distribution</em> of characteristics can be described:</p>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Complier-characteristics ratio:</strong> For a binary characteristic x<sub>1i</sub>,</p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; margin: 0.5rem 0;">
                    P[x<sub>1i</sub>=1 | complier] / P[x<sub>1i</sub>=1] = (First stage for x<sub>1i</sub>=1 subgroup) / (Overall first stage)
                </div>
                <p>If this ratio > 1, compliers are disproportionately likely to have characteristic x₁.</p>
            </div>

            <h4>Example: Complier Characteristics for Twins vs. Same-Sex Instruments</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Characteristic</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Sample Mean</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Twins Ratio</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Same-Sex Ratio</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Age ≥ 30 at first birth</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.003</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">1.39</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">1.00</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">College graduate</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.132</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">1.14</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.70</td>
                </tr>
            </table>
            <p>Twins compliers are older and more educated; same-sex compliers are less educated. This helps explain why twins IV gives smaller labor supply effects (labor supply consequences of childbearing decline with education).</p>
        </div>
    </section>

    <!-- 4.5 Generalizing LATE -->
    <section class="section fade-in-delay">
        <h2 class="section-title">4.5 Generalizing LATE</h2>
        <div class="section-content">

            <h3>4.5.1 Multiple Instruments</h3>
            <p>With two instruments z<sub>1i</sub> and z<sub>2i</sub>, each having its own complier group, 2SLS produces:</p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                ρ<sub>2SLS</sub> = λ·ρ<sub>1</sub> + (1−λ)·ρ<sub>2</sub>
            </div>
            <p>where ρ<sub>j</sub> is the LATE using instrument j alone, and λ depends on the relative strength of each instrument in the first stage. Instruments with a stronger first stage get more weight.</p>

            <h3>4.5.2 Covariates in the Heterogeneous-Effects Model</h3>

            <p>When the instrument is only valid <em>conditional on covariates</em> X<sub>i</sub> (e.g., draft eligibility conditional on year of birth):</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Conditional independence:</strong> {y<sub>1i</sub>, y<sub>0i</sub>, d<sub>1i</sub>, d<sub>0i</sub>} ⊥ z<sub>i</sub> | X<sub>i</sub></p>
            </div>

            <h4>Saturate and Weight Theorem (Angrist & Imbens 1995)</h4>
            <p>With a fully saturated first stage (separate effect of z for each value of X) and saturated covariates in the second stage, 2SLS estimates:</p>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                ρ<sub>2SLS</sub> = E[ω(X<sub>i</sub>) · LATE(X<sub>i</sub>)]
            </div>
            <p>A weighted average of covariate-specific LATEs, with weights proportional to the variance of first-stage fitted values at each X value. Covariate values where the instrument creates more variation in treatment get more weight.</p>

            <h4>Abadie's Kappa Weighting (Abadie 2003)</h4>
            <p>2SLS approximates the causal response function for <em>compliers</em>: E[y<sub>i</sub> | d<sub>i</sub>, X<sub>i</sub>, complier]. The kappa-weighting function:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                κ<sub>i</sub> = 1 − d<sub>i</sub>(1−z<sub>i</sub>) / (1−P(z<sub>i</sub>=1|X<sub>i</sub>)) − (1−d<sub>i</sub>)z<sub>i</sub> / P(z<sub>i</sub>=1|X<sub>i</sub>)
            </div>
            <p>"finds" compliers by down-weighting always-takers (d=1, z=0) and never-takers (d=0, z=1). With a linear model for P(z=1|X), Abadie's estimator equals 2SLS.</p>

            <h3>4.5.3 Average Causal Response with Variable Treatment Intensity</h3>

            <p>When treatment is multi-valued (e.g., years of schooling s ∈ {0, 1, …, S}), the Wald estimand becomes:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>ACR Theorem (Angrist & Imbens 1995):</strong></p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; font-size: 1.05rem; margin: 0.5rem 0;">
                    IV estimand = Σ<sub>s</sub> ω<sub>s</sub> · E[Y<sub>s</sub> − Y<sub>s−1</sub> | s<sub>1i</sub> ≥ s > s<sub>0i</sub>]
                </div>
                <p style="margin-top: 0.5rem;">A weighted average of unit causal effects along the causal response function, with weights:</p>
                <div style="text-align: center; font-family: 'Times New Roman', serif; margin: 0.5rem 0;">
                    ω<sub>s</sub> = P[s<sub>1i</sub> ≥ s > s<sub>0i</sub>] / Σ<sub>j</sub> P[s<sub>1i</sub> ≥ j > s<sub>0i</sub>]
                </div>
            </div>

            <p><strong>Key insight:</strong> The weight at each point s is proportional to the shift in the CDF of treatment at that point, which can be estimated from data:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                P[s<sub>1i</sub> ≥ s > s<sub>0i</sub>] = P[s<sub>i</sub> < s | z=0] − P[s<sub>i</sub> < s | z=1]
            </div>

            <h4>Application: Compulsory Schooling Laws</h4>
            <p>Acemoglu & Angrist (2000) show that child labor and compulsory attendance laws shift the schooling distribution mainly in grades 8–12, with no effect on post-secondary schooling. Therefore, IV estimates using these instruments capture returns to schooling in the <strong>high-school range</strong>, not the college range.</p>

            <h4>Continuous Treatment: Average Derivative</h4>
            <p>When treatment is continuous (e.g., price), the IV estimand is a weighted average derivative:</p>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                IV = ∫ q'(t) · ω(t) dt
            </div>
            <p>Example: Angrist, Graddy & Imbens (2000) estimate the demand for fish at Fulton Fish Market using weather instruments. Stormy weather drives up prices, and IV recovers the demand elasticity averaged over the range of storm-induced price shifts.</p>
        </div>
    </section>

    <!-- Applied Case Study: Angrist & Evans (1998) -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Applied: Angrist & Evans (1998) — Fertility & Labor Supply</h2>
        <div class="section-content">
            <p><strong>Research question:</strong> Does having a third child causally reduce female labor supply?</p>

            <h3>The Identification Problem</h3>
            <p>Simple OLS comparison of mothers with 2 vs. 3+ children confounds causation with selection: women who have more children may have inherently stronger family-orientation preferences, leading to both more children <em>and</em> less labor supply.</p>

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <strong style="color: #92400e;">Core problem:</strong> Fertility is endogenous — unobservable preferences drive both the number of children and labor supply decisions simultaneously.
            </div>

            <h3>Two Instruments for a Third Child</h3>
            <p>Among mothers with ≥2 children, Angrist & Evans use two sources of exogenous variation:</p>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;"></th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Twins at second birth</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Same-sex (first two children)</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Logic</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Twins mechanically create ≥3 children</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Parents prefer mixed-sex sibship → more likely to try for a third</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>First stage</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.625 (very strong)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.067 (modest)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Validity</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Twin births are essentially random</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Child sex composition is random</td>
                </tr>
            </table>

            <h3>Results</h3>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Outcome</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">OLS</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Twins IV</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Same-sex IV</th>
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

            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <strong style="color: #92400e;">Key observation:</strong> |OLS| > |Same-sex IV| > |Twins IV|. Same treatment, same outcome, but different estimates. Why?
            </div>

            <h3>Why Estimates Differ: Different Compliers</h3>
            <p>Each instrument identifies effects for a <strong>different complier subpopulation</strong>:</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Twins compliers</strong> = mothers who would <em>not</em> have had a third child without twins</p>
                <ul>
                    <li>Older, more educated, established careers</li>
                    <li>Planned for 2 children → forced into 3 by twins</li>
                    <li>→ Labor supply impact is <strong>smaller</strong> (career attachment buffers the shock)</li>
                </ul>
            </div>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Same-sex compliers</strong> = mothers who had a third child due to sex-mix preference</p>
                <ul>
                    <li>Younger, less educated, early career stage</li>
                    <li>Strong family composition preferences</li>
                    <li>→ Labor supply impact is <strong>larger</strong> (less career attachment, higher opportunity cost)</li>
                </ul>
            </div>

            <h3>Mapping to ATE / ATT / ITT / LATE</h3>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Estimand</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Definition</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">In This Study</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong style="color: #dc2626;">ATE</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">E[Y(1)−Y(0)] for entire population</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Effect of 3rd child on <em>all</em> mothers with 2 children — not directly observed</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong style="color: #059669;">ATT</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">E[Y(1)−Y(0) | D=1] for treated</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Effect on mothers who <em>actually</em> had a 3rd child — OLS (−0.167) tries but is biased by selection</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong style="color: #d97706;">ITT</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">E[Y|Z=1]−E[Y|Z=0] by assignment</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Effect of being assigned twins/same-sex — reduced form, always unbiased</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong style="color: #7c3aed;">LATE</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">E[Y(1)−Y(0) | compliers]</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Twins: −0.083 | Same-sex: −0.135 — different compliers give different LATEs</td>
                </tr>
            </table>

            <h3>Mathematical Relationships</h3>
            <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif;">
                <p><strong>ATE</strong> = E[Y₁−Y₀|C]·π<sub>C</sub> + E[Y₁−Y₀|AT]·π<sub>AT</sub> + E[Y₁−Y₀|NT]·π<sub>NT</sub></p>
                <p><strong>ATT</strong> = E[Y₁−Y₀|C]·π<sub>C</sub>/(π<sub>C</sub>+π<sub>AT</sub>) + E[Y₁−Y₀|AT]·π<sub>AT</sub>/(π<sub>C</sub>+π<sub>AT</sub>)</p>
                <p><strong>ITT</strong> = LATE × π<sub>C</sub>  (always unbiased, |ITT| ≤ |LATE|)</p>
                <p><strong>LATE</strong> = E[Y₁−Y₀ | Compliers] = ITT / First stage</p>
            </div>

            <h4>Size Relationships</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Relationship</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Condition</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">|ITT| &lt; |LATE|</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Always (compliance rate &lt; 1)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">ATT ≥ ATE (typically)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">High-benefit individuals self-select into treatment</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">LATE = ATT</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">No always-takers (Bloom 1984)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">LATE₁ ≠ LATE₂</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Different IVs → different compliers (Angrist & Evans)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">LATE = ATE</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Homogeneous treatment effects (constant effect)</td>
                </tr>
            </table>

            <h4>Method → Estimand Mapping</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Method</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Estimates</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Generalizability</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">RCT (full compliance)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong style="color: #dc2626;">ATE</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Broad</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">RCT (non-compliance) + IV</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong style="color: #7c3aed;">LATE</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Compliers only</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">DID / Matching / PSM</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong style="color: #059669;">ATT</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Groups similar to treated</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">RDD</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong style="color: #7c3aed;">LATE at cutoff</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Near cutoff only</td>
                </tr>
            </table>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Key lessons from Angrist & Evans:</strong></p>
                <ol>
                    <li><strong>LATE ≠ ATE ≠ ATT.</strong> OLS (−0.167), Twins IV (−0.083), Same-sex IV (−0.135) all give different numbers for the same research question.</li>
                    <li><strong>Different instruments → different compliers → different LATEs.</strong> The choice of instrument determines <em>whose</em> effect you estimate.</li>
                    <li><strong>Complier characteristics explain the gap.</strong> The difference is systematic, not random — it traces back to demographics of each complier group.</li>
                    <li><strong>Policy implications change.</strong> −8% vs. −17% employment effects lead to completely different childcare policy conclusions.</li>
                </ol>
            </div>
        </div>
    </section>

    <!-- Summary -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Part 2 Summary</h2>
        <div class="section-content">
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Concept</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Key Point</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>LATE</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">IV = E[y₁−y₀ | compliers], not ATE or ATT in general</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Four Assumptions</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Independence, Exclusion, First stage, Monotonicity</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Monotonicity</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">No defiers; all affected people are pushed in the same direction</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Complier size</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">= First stage; characteristics via first-stage ratio across subgroups</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Bloom's Result</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">One-sided non-compliance → LATE = ATT (e.g., JTPA)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Multiple instruments</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">2SLS = weighted average of instrument-specific LATEs</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Covariates</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">2SLS = weighted average of covariate-specific LATEs</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>ACR Theorem</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Multi-valued treatment → weighted average of unit causal effects along the response function</td>
                </tr>
            </table>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Practical takeaway:</strong> Different instruments estimate effects for different subpopulations. Understanding <em>who</em> the compliers are is crucial for interpreting what your IV estimate means and whether it generalizes.</p>
            </div>
        </div>
    </section>

    <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee; display: flex; justify-content: space-between;">
        <a href="/study/angrist-ch4-part1" style="color: #666;">← Part 1: IV Basics, Wald & 2SLS</a>
        <a href="/study/angrist-ch4-part3" style="color: #2563eb;">Part 3: IV Details →</a>
    </div>

    <div style="margin-top: 2rem; padding: 1rem; background: #f9fafb; border-radius: 8px; font-size: 0.8rem; color: #6b7280;">
        <em>This note was written with the assistance of LLM (Claude).</em>
    </div>
</div>
