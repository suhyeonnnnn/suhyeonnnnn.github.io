---
layout: minimal_base
title: "Angrist Ch.7 - Quantile Regression"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Chapter 7: Quantile Regression</h2>
            <a href="/study/angrist-ch7-quantile-regression-ko" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">한국어</a>
        </div>
        <div class="section-content">
            <p><em>Angrist & Pischke, Mostly Harmless Econometrics — Chapter 7</em></p>
            <p style="color: #6b7280; font-style: italic;">"Here's a prayer for you... Protect me from knowing what I don't need to know." — Douglas Adams</p>
        </div>
    </section>

    <!-- Core Message -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Core Message</h2>
        <div class="section-content">
            <blockquote style="border-left: 4px solid #2563eb; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                <strong>95% of applied econometrics is concerned with averages.</strong> But many variables have continuous distributions that can change in ways not revealed by averages — they can spread out or compress. <strong>Quantile regression</strong> lets us model entire distributions, not just means.
            </blockquote>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Key insight:</strong> Just as OLS fits a linear model to the conditional mean, quantile regression fits a linear model to conditional quantiles — allowing us to see whether treatment affects different parts of the distribution differently.</p>
            </div>
        </div>
    </section>

    <!-- 7.1 Quantile Regression Model -->
    <section class="section fade-in-delay">
        <h2 class="section-title">7.1 The Quantile Regression Model</h2>
        <div class="section-content">

            <h3>Conditional Quantile Function (CQF)</h3>
            <p>The starting point is the <strong>conditional quantile function</strong>:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: 'Times New Roman', serif; text-align: center; font-size: 1.1rem;">
                Q<sub>τ</sub>(y<sub>i</sub> | X<sub>i</sub>) = F<sub>Y</sub><sup>-1</sup>(τ | X<sub>i</sub>)
            </div>

            <table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc;">
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb; text-align: left;">τ value</th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb; text-align: left;">Meaning</th>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">τ = 0.10</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">Lower decile</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">τ = 0.50</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">Median</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">τ = 0.90</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">Upper decile</td>
                </tr>
            </table>

            <h3>CEF vs CQF</h3>
            <table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc;">
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;"></th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">CEF (OLS)</th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">CQF (Quantile Reg)</th>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;"><strong>Solves</strong></td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">min E[(y - m(X))²]</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">min E[ρ<sub>τ</sub>(y - q(X))]</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;"><strong>Loss function</strong></td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">Squared error</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">Check function ρ<sub>τ</sub></td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;"><strong>Estimates</strong></td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">Conditional mean</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">Conditional quantile</td>
                </tr>
            </table>

            <h3>The Check Function</h3>
            <p>The check function weights positive and negative residuals <strong>asymmetrically</strong>:</p>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: monospace;">
                ρ<sub>τ</sub>(u) = u · (τ - 1(u ≤ 0))<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= τ·u &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if u > 0<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= (τ-1)·u &nbsp;if u ≤ 0
            </div>

            <table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc;">
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">τ</th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">Weight on positive</th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">Weight on negative</th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">Result</th>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">0.5</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">0.5</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">0.5</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">Median (LAD)</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">0.9</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">0.9</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">0.1</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">Upper quantile</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">0.1</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">0.1</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">0.9</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">Lower quantile</td>
                </tr>
            </table>

        </div>
    </section>

    <!-- Location Shift vs Heteroskedasticity -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Location Shift vs Heteroskedasticity</h2>
        <div class="section-content">

            <h3>Case 1: Location Shift (Homoskedastic)</h3>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Model:</strong> y<sub>i</sub> ~ N(X<sub>i</sub>'β, σ²)</p>
                <p><strong>CQF:</strong> Q<sub>τ</sub>(y<sub>i</sub> | X<sub>i</sub>) = X<sub>i</sub>'β + σ·Φ<sup>-1</sup>(τ)</p>
                <p><strong>Key feature:</strong> Slope β is <em>identical</em> across all quantiles. Only the intercept changes with τ.</p>
            </div>

            <h3>Case 2: Heteroskedasticity (Location-Scale Model)</h3>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Model:</strong> y<sub>i</sub> ~ N(X<sub>i</sub>'β, (X<sub>i</sub>'γ)²)</p>
                <p><strong>CQF:</strong> Q<sub>τ</sub>(y<sub>i</sub> | X<sub>i</sub>) = X<sub>i</sub>'[β + γ·Φ<sup>-1</sup>(τ)]</p>
                <p><strong>Key feature:</strong> Slope <em>varies with τ</em>. Upper quantiles have larger coefficients → inequality increases with X.</p>
            </div>

        </div>
    </section>

    <!-- Empirical Example: Returns to Schooling -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Empirical Example: Returns to Schooling (Table 7.1.1)</h2>
        <div class="section-content">

            <p><strong>Data:</strong> 1980, 1990, 2000 U.S. Census. White/Black men aged 40-49. Controls: race, quadratic in potential experience.</p>

            <table style="width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.9rem;">
                <tr style="background: #1e40af; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">Census</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">0.10</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">0.25</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">0.50</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">0.75</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">0.90</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">OLS</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;"><strong>1980</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.074</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.074</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.068</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.070</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.079</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.072</td>
                </tr>
                <tr style="background: #f8fafc;">
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;"><strong>1990</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.112</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.110</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.106</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.111</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.137</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.114</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;"><strong>2000</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.092</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.105</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.111</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.120</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb; background: #fef3c7;"><strong>.157</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">.114</td>
                </tr>
            </table>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>1980:</strong> Coefficients similar across quantiles (~0.07) → <strong>Location shift</strong></p>
                <p><strong>2000:</strong> Upper decile (15.7%) >> Lower decile (9.2%) → <strong>Fanning out</strong></p>
                <p><strong>Interpretation:</strong> "Among the educated, the rich get even richer" — education increases both mean wages and inequality.</p>
            </div>

        </div>
    </section>

    <!-- Censored Quantile Regression -->
    <section class="section fade-in-delay">
        <h2 class="section-title">7.1.1 Censored Quantile Regression</h2>
        <div class="section-content">

            <p><strong>Problem:</strong> Some data is hidden (e.g., CPS top-coding, duration censoring).</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Key insight:</strong> Censoring from above doesn't affect quantiles <em>below</em> the censoring point.</p>
                <p>Example: If top 10% is censored → τ ≤ 0.90 estimates are unaffected.</p>
            </div>

            <p><strong>Powell (1986) solution:</strong></p>
            <ul>
                <li>Model: Q<sub>τ</sub>(y | X) = min(c, X'β<sub>τ</sub>)</li>
                <li>Only use observations where X'β < c</li>
            </ul>

            <p><strong>Buchinsky (1994) iterative algorithm:</strong></p>
            <ol>
                <li>Estimate β̂<sub>τ</sub> ignoring censoring</li>
                <li>Find cells with X'β̂<sub>τ</sub> < c</li>
                <li>Re-estimate using only those cells</li>
                <li>Repeat until convergence</li>
            </ol>

        </div>
    </section>

    <!-- Tricky Points -->
    <section class="section fade-in-delay">
        <h2 class="section-title">7.1.3 Tricky Points</h2>
        <div class="section-content">

            <h3>Tricky Point 1: Individual vs Distributional Effects</h3>
            <div style="background: #fef2f2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>"Training raised the lower decile"</strong> ≠ <strong>"Poor people became richer"</strong></p>
                <p>Quantile regression tells us about the <em>distribution's shape</em>, not about <em>specific individuals</em>. Unless we assume <strong>rank preservation</strong> (treatment doesn't change ranks), we can't interpret effects as individual-level.</p>
            </div>

            <h3>Tricky Point 2: Conditional ≠ Marginal Quantiles</h3>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>For means:</strong> E[y | X] = X'β ⟹ E[y] = E[X]'β ✓</p>
                <p><strong>For quantiles:</strong> Q<sub>τ</sub>(y | X) = X'β<sub>τ</sub> ⟹ Q<sub>τ</sub>(y) ≠ E[X]'β<sub>τ</sub> ✗</p>
                <p>Quantiles are nonlinear operators. Extracting marginal quantiles requires integrating over the entire distribution of X (Machado & Mata, 2005).</p>
            </div>

        </div>
    </section>

    <!-- 7.2 Quantile Treatment Effects -->
    <section class="section fade-in-delay">
        <h2 class="section-title">7.2 Quantile Treatment Effects (QTE)</h2>
        <div class="section-content">

            <h3>The Problem: Selection Bias</h3>
            <p>Just like OLS, quantile regression suffers from <strong>omitted variable bias</strong> when treatment is endogenous.</p>

            <table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f8fafc;">
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;"></th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">Exogenous d</th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">Endogenous d</th>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;"><strong>Mean</strong></td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">OLS</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">2SLS</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;"><strong>Quantile</strong></td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">QR</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;"><strong>QTE</strong></td>
                </tr>
            </table>

            <h3>QTE: Extending LATE to Quantiles</h3>
            <p>Abadie, Angrist, and Imbens (2002) extend the LATE framework to quantiles:</p>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: monospace;">
                Q<sub>τ</sub>(y | X, d, complier) = α<sub>τ</sub>·d + X'β<sub>τ</sub>
            </div>

            <p>α<sub>τ</sub> = effect on τ-quantile <strong>for compliers</strong></p>

            <h3>The Abadie Kappa</h3>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: monospace;">
                κ<sub>i</sub> = 1 - d<sub>i</sub>(1-z<sub>i</sub>)/(1-p(X<sub>i</sub>)) - (1-d<sub>i</sub>)z<sub>i</sub>/p(X<sub>i</sub>)
            </div>

            <p>Properties: E[κ | complier] = 1, E[κ | non-complier] = 0</p>

            <p><strong>QTE Estimator:</strong></p>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0; font-family: monospace;">
                (α<sub>τ</sub>, β<sub>τ</sub>) = arg min E[κ<sub>i</sub> · ρ<sub>τ</sub>(y<sub>i</sub> - α·d<sub>i</sub> - X<sub>i</sub>'b)]
            </div>

        </div>
    </section>

    <!-- QTE Implementation -->
    <section class="section fade-in-delay">
        <h2 class="section-title">QTE Implementation Steps</h2>
        <div class="section-content">

            <ol>
                <li><strong>Step 1:</strong> Probit z ~ y, X in d=1 subsample → save Ê[z | y, d=1, X]</li>
                <li><strong>Step 2:</strong> Probit z ~ y, X in d=0 subsample → save Ê[z | y, d=0, X]</li>
                <li><strong>Step 3:</strong> Probit z ~ X in full sample → save P̂(z=1 | X)</li>
                <li><strong>Step 4:</strong> Compute Ê[κ | y, d, X] using formula; trim to [0, 1]</li>
                <li><strong>Step 5:</strong> Run κ-weighted quantile regression</li>
                <li><strong>Step 6:</strong> Bootstrap entire procedure for standard errors</li>
            </ol>

        </div>
    </section>

    <!-- JTPA Example -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Empirical Example: JTPA Training (Table 7.2.1)</h2>
        <div class="section-content">

            <p><strong>Setting:</strong> Job Training Partnership Act (1980s US). z = randomized training offer, d = actual participation (~60%), y = 30-month earnings.</p>

            <h3>Panel A: OLS & Quantile Regression (Selection bias present)</h3>
            <table style="width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.9rem;">
                <tr style="background: #1e40af; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;"></th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">OLS</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">τ=0.15</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">τ=0.25</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">τ=0.50</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">τ=0.75</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">τ=0.85</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;"><strong>Training</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">3,754</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb; background: #fef2f2;">1,187</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">2,510</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">4,420</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">4,678</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">4,806</td>
                </tr>
                <tr style="background: #f8fafc;">
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;"><strong>% Impact</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">21%</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb; background: #fef2f2;"><strong>136%</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">75%</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">35%</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">17%</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">13%</td>
                </tr>
            </table>

            <h3>Panel B: 2SLS & QTE (Selection bias removed)</h3>
            <table style="width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.9rem;">
                <tr style="background: #1e40af; color: white;">
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;"></th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">2SLS</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">τ=0.15</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">τ=0.25</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">τ=0.50</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">τ=0.75</th>
                    <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">τ=0.85</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;"><strong>Training</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">1,593</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb; background: #ecfdf5;"><strong>121</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">702</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">1,544</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">3,131</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">3,378</td>
                </tr>
                <tr style="background: #f8fafc;">
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;"><strong>% Impact</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">9%</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb; background: #ecfdf5;"><strong>5%</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">12%</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">10%</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">11%</td>
                    <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">9%</td>
                </tr>
            </table>

            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Key finding:</strong> QR shows huge effect at τ=0.15 ($1,187, 136%). But QTE shows nearly zero ($121, 5%)!</p>
                <p><strong>Interpretation:</strong> Low-income trainees are more motivated → positive selection bias inflates QR estimates at lower quantiles. JTPA actually only worked at upper quantiles.</p>
            </div>

        </div>
    </section>

    <!-- Key Questions -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Three Key Questions</h2>
        <div class="section-content">

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <h4 style="margin-top: 0; color: #1e40af;">Q1. Quantile Regression vs OLS</h4>
                <p><strong>Q:</strong> How does QR differ from OLS, and when should you use it?</p>
                <p><strong>A:</strong> OLS estimates conditional means; QR estimates conditional quantiles. Use QR when: (1) analyzing inequality, (2) detecting heterogeneous effects, (3) distinguishing location shift vs fanning out, (4) robustness to outliers.</p>
            </div>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <h4 style="margin-top: 0; color: #1e40af;">Q2. Location Shift vs Fanning Out</h4>
                <p><strong>Q:</strong> What does it mean when quantile coefficients differ across τ?</p>
                <p><strong>A:</strong> Identical coefficients → location shift (distribution shifts uniformly). Increasing coefficients → fanning out (inequality increases with X). 2000 Census: upper decile return (15.7%) >> lower decile (9.2%) → education increases inequality.</p>
            </div>

            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <h4 style="margin-top: 0; color: #1e40af;">Q3. Why QTE?</h4>
                <p><strong>Q:</strong> Why might QR estimates be biased, and how does QTE fix this?</p>
                <p><strong>A:</strong> QR suffers from selection bias when treatment is endogenous. QTE applies IV logic: uses Abadie kappa to weight observations by probability of being a complier. JTPA example: QR lower quantile effect dropped from $1,187 to $121 (90% reduction) after correcting for selection.</p>
            </div>

        </div>
    </section>

    <!-- Summary Comparison -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Summary: OLS vs QR vs 2SLS vs QTE</h2>
        <div class="section-content">

            <table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #1e40af; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">Method</th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">Estimand</th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">Selection bias</th>
                    <th style="padding: 0.75rem; border: 1px solid #e5e7eb;">Distribution</th>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">OLS</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">E[y|X,d]</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">Present</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">Mean only</td>
                </tr>
                <tr style="background: #f8fafc;">
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">2SLS</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">E[y|X,d] for compliers</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">Removed</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">Mean only</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">QR</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">Q<sub>τ</sub>(y|X,d)</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">Present</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">Full distribution</td>
                </tr>
                <tr style="background: #ecfdf5;">
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;"><strong>QTE</strong></td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;">Q<sub>τ</sub>(y|X,d) for compliers</td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;"><strong>Removed</strong></td>
                    <td style="padding: 0.75rem; border: 1px solid #e5e7eb;"><strong>Full distribution</strong></td>
                </tr>
            </table>

        </div>
    </section>

</div>
