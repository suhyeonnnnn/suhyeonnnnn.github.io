---
layout: minimal_base
title: "Treatment Effects Guide - ATE, ATT, ITT, LATE"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Treatment Effects: ATE, ATT, ITT, LATE</h2>
            <a href="/study/treatment-effects-ko" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">한국어</a>
        </div>
        <div class="section-content">
            <p><em>Applied guide with Angrist & Evans (1998) case study — Companion to MHE Chapter 4</em></p>
        </div>
    </section>

    <!-- Core Message -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Core Message</h2>
        <div class="section-content">
            <blockquote style="border-left: 4px solid #2563eb; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                Not "what is the effect?" but <strong>"the effect for whom?"</strong> — The same treatment can yield different estimates (ATE, ATT, ITT, LATE) depending on the target population. Understanding which estimand your method identifies is essential for correct interpretation and policy design.
            </blockquote>
        </div>
    </section>

    <!-- Part 1: Definitions -->
    <section class="section fade-in-delay">
        <h2 class="section-title">1. Treatment Effect Estimands</h2>
        <div class="section-content">

            <!-- ATE -->
            <div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1.5rem 0;">
                <h3 style="margin-top: 0;"><span style="background: #dc2626; color: white; padding: 0.2rem 0.5rem; border-radius: 4px; font-family: monospace; font-size: 0.85rem;">ATE</span> Average Treatment Effect</h3>
                <p>The average causal effect across the <strong>entire population</strong>.</p>
                <div style="background: white; border: 1px solid #fecaca; padding: 1rem; border-radius: 6px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    ATE = E[Y<sub>i</sub>(1) − Y<sub>i</sub>(0)]
                </div>
                <ul>
                    <li>Compares: everyone treated vs. everyone untreated</li>
                    <li>Relevant when: considering <strong>universal policy</strong> (e.g., mandatory program for all)</li>
                    <li>Challenge: counterfactual is never observed → requires strong assumptions or perfect RCT</li>
                </ul>
            </div>

            <!-- ATT -->
            <div style="background: #ecfdf5; border-left: 4px solid #059669; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1.5rem 0;">
                <h3 style="margin-top: 0;"><span style="background: #059669; color: white; padding: 0.2rem 0.5rem; border-radius: 4px; font-family: monospace; font-size: 0.85rem;">ATT</span> Average Treatment Effect on the Treated</h3>
                <p>The average causal effect among those who <strong>actually received treatment</strong>.</p>
                <div style="background: white; border: 1px solid #a7f3d0; padding: 1rem; border-radius: 6px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    ATT = E[Y<sub>i</sub>(1) − Y<sub>i</sub>(0) | D<sub>i</sub> = 1]
                </div>
                <ul>
                    <li>Compares: treated group's actual outcome vs. what they would have experienced without treatment</li>
                    <li>Relevant when: evaluating a <strong>voluntary program</strong> for its participants</li>
                    <li>Typically ATT > ATE when high-benefit individuals self-select into treatment</li>
                </ul>
            </div>

            <div style="background: #fef3c7; border: 1px solid #fcd34d; padding: 1rem 1.5rem; border-radius: 6px; margin: 1.5rem 0; font-size: 0.95rem;">
                <strong style="color: #92400e;">ATE vs ATT:</strong> With heterogeneous effects and self-selection, these differ. If people with larger treatment benefits tend to participate, then <strong>ATT > ATE</strong>.
            </div>

            <!-- ITT -->
            <div style="background: #fffbeb; border-left: 4px solid #d97706; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1.5rem 0;">
                <h3 style="margin-top: 0;"><span style="background: #d97706; color: white; padding: 0.2rem 0.5rem; border-radius: 4px; font-family: monospace; font-size: 0.85rem;">ITT</span> Intent-to-Treat</h3>
                <p>The effect of being <strong>assigned</strong> to treatment, regardless of actual take-up.</p>
                <div style="background: white; border: 1px solid #fde68a; padding: 1rem; border-radius: 6px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    ITT = E[Y<sub>i</sub> | Z<sub>i</sub> = 1] − E[Y<sub>i</sub> | Z<sub>i</sub> = 0]
                </div>
                <ul>
                    <li>Z is assignment, D is actual treatment receipt</li>
                    <li><strong>Always unbiased</strong> — preserves randomization even with non-compliance</li>
                    <li>Reflects the <strong>realistic effect of offering</strong> a program (including non-participation)</li>
                    <li>|ITT| ≤ |LATE| because ITT = LATE × compliance rate</li>
                </ul>
            </div>

            <!-- LATE -->
            <div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1.5rem 0;">
                <h3 style="margin-top: 0;"><span style="background: #7c3aed; color: white; padding: 0.2rem 0.5rem; border-radius: 4px; font-family: monospace; font-size: 0.85rem;">LATE</span> Local Average Treatment Effect</h3>
                <p>The average causal effect for <strong>compliers</strong> — those whose treatment status is changed by the instrument.</p>
                <div style="background: white; border: 1px solid #c4b5fd; padding: 1rem; border-radius: 6px; margin: 1rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.1rem;">
                    LATE = Cov(Y, Z) / Cov(D, Z) = ITT / First Stage
                </div>
                <ul>
                    <li>Only for <strong>compliers</strong> — excludes always-takers and never-takers</li>
                    <li>Requires <strong>monotonicity</strong> assumption (no defiers)</li>
                    <li>Different instruments → different compliers → different LATEs</li>
                    <li>RDD estimates are also interpretable as LATE at the cutoff</li>
                </ul>
            </div>

            <!-- Summary Table -->
            <h3>Summary Comparison</h3>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Estimand</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Target Population</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Primary Context</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Method</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #dc2626; font-weight: 500;">ATE</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Entire population</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Universal policy effect</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">RCT (full compliance)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #059669; font-weight: 500;">ATT</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Treated group</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Voluntary program evaluation</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">DID, Matching/PSM</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #d97706; font-weight: 500;">ITT</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Assigned group</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">RCT with non-compliance</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Reduced form</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #7c3aed; font-weight: 500;">LATE</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Compliers</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">IV / RDD estimation</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">2SLS, Wald estimator</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- Part 2: Angrist & Evans -->
    <section class="section fade-in-delay">
        <h2 class="section-title">2. Case Study: Angrist & Evans (1998)</h2>
        <div class="section-content">
            <p><strong>Research question:</strong> Does having a third child causally reduce female labor supply?</p>

            <h3>The Identification Problem</h3>
            <p>Simple OLS comparison of mothers with 2 vs. 3+ children confounds causation with selection: women who have more children may have inherently stronger family-orientation preferences, leading to both more children <em>and</em> less labor supply.</p>

            <div style="background: #fef3c7; border: 1px solid #fcd34d; padding: 1rem 1.5rem; border-radius: 6px; margin: 1rem 0;">
                <strong style="color: #92400e;">Core problem:</strong> Fertility is endogenous — unobservable preferences drive both the number of children and labor supply decisions simultaneously.
            </div>

            <h3>Two Instruments for a Third Child</h3>
            <p>Among mothers with ≥2 children, Angrist & Evans use two sources of exogenous variation in the probability of having a third child:</p>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;"></th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Twins at second birth</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Same-sex (first two children)</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Logic</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Twins mechanically create ≥3 children</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Parents prefer a mixed-sex sibship → more likely to try for a third</td>
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

            <div style="background: #fef3c7; border: 1px solid #fcd34d; padding: 1rem 1.5rem; border-radius: 6px; margin: 1rem 0;">
                <strong style="color: #92400e;">Key observation:</strong> |OLS| > |Same-sex IV| > |Twins IV|. Same treatment, same outcome, but different estimates. Why?
            </div>

            <h3>Why Estimates Differ: Different Compliers</h3>
            <p>Each instrument identifies effects for a <strong>different complier subpopulation</strong>:</p>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #7c3aed; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Characteristic</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Sample Mean</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Twins Ratio</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Same-sex Ratio</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Age ≥ 30 at first birth</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.003</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>1.39</strong> (overrepresented)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">1.00 (average)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">College graduate</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">0.132</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>1.14</strong> (overrepresented)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>0.70</strong> (underrepresented)</td>
                </tr>
            </table>
            <p style="font-size: 0.9rem; color: #6b7280;"><em>Ratio > 1 means the characteristic is overrepresented among compliers relative to the population.</em></p>

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

            <h3>Mapping to Treatment Effect Concepts</h3>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Estimand</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Interpretation in This Study</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Value / Status</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #dc2626; font-weight: 500;">ATE</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Effect of 3rd child on <em>all</em> mothers with 2 children</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Not directly observed; somewhere between the two LATEs</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #059669; font-weight: 500;">ATT</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Effect on mothers who <em>actually</em> had a 3rd child</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">OLS (−0.167) tries to estimate this but is biased by selection</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #d97706; font-weight: 500;">ITT</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Effect of being "assigned" twins / same-sex</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Reduced form: e.g., twins RF on employment = −0.052</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #7c3aed; font-weight: 500;">LATE</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Effect for mothers pushed into 3rd child <em>by the instrument</em></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Twins: −0.083 | Same-sex: −0.135</td>
                </tr>
            </table>

            <h3>Lessons from This Study</h3>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <ol>
                    <li><strong>LATE ≠ ATE ≠ ATT.</strong> OLS (−0.167), Twins IV (−0.083), Same-sex IV (−0.135) all give different numbers for the same research question.</li>
                    <li><strong>Different instruments → different compliers → different LATEs.</strong> The choice of instrument determines <em>whose</em> effect you estimate.</li>
                    <li><strong>Complier characteristics explain the gap.</strong> The difference is systematic, not random — it traces back to the demographics of each complier group.</li>
                    <li><strong>Policy implications change.</strong> −8% vs. −17% employment effects lead to completely different childcare policy conclusions.</li>
                </ol>
            </div>
        </div>
    </section>

    <!-- Part 3: Mathematical Relationships -->
    <section class="section fade-in-delay">
        <h2 class="section-title">3. Mathematical Relationships</h2>
        <div class="section-content">

            <h3>Population Subgroups Under Monotonicity</h3>
            <p>The instrument partitions the population into three groups (assuming no defiers):</p>

            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Group</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Definition</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Share</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Compliers (C)</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">d<sub>1i</sub> = 1, d<sub>0i</sub> = 0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">π<sub>C</sub> = E[D|Z=1] − E[D|Z=0] = First stage</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Always-takers (AT)</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">d<sub>1i</sub> = d<sub>0i</sub> = 1</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">π<sub>AT</sub> = E[D|Z=0]</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;"><strong>Never-takers (NT)</strong></td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">d<sub>1i</sub> = d<sub>0i</sub> = 0</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">π<sub>NT</sub> = 1 − E[D|Z=1]</td>
                </tr>
            </table>

            <h3>Decomposition of Each Estimand</h3>

            <div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1.5rem 0;">
                <h4 style="margin-top: 0; color: #dc2626;">ATE: Weighted average across all groups</h4>
                <div style="background: white; border: 1px solid #fecaca; padding: 1rem; border-radius: 6px; margin: 0.5rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.05rem;">
                    ATE = E[Y₁−Y₀|C]·π<sub>C</sub> + E[Y₁−Y₀|AT]·π<sub>AT</sub> + E[Y₁−Y₀|NT]·π<sub>NT</sub>
                </div>
            </div>

            <div style="background: #ecfdf5; border-left: 4px solid #059669; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1.5rem 0;">
                <h4 style="margin-top: 0; color: #059669;">ATT: Compliers + Always-takers</h4>
                <div style="background: white; border: 1px solid #a7f3d0; padding: 1rem; border-radius: 6px; margin: 0.5rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.05rem;">
                    ATT = E[Y₁−Y₀|C] · π<sub>C</sub>/(π<sub>C</sub>+π<sub>AT</sub>) + E[Y₁−Y₀|AT] · π<sub>AT</sub>/(π<sub>C</sub>+π<sub>AT</sub>)
                </div>
                <p style="font-size: 0.9rem;">Treated = compliers + always-takers. Never-takers are excluded (they don't get treated).</p>
            </div>

            <div style="background: #fffbeb; border-left: 4px solid #d97706; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1.5rem 0;">
                <h4 style="margin-top: 0; color: #d97706;">ITT: LATE × Compliance rate</h4>
                <div style="background: white; border: 1px solid #fde68a; padding: 1rem; border-radius: 6px; margin: 0.5rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.05rem;">
                    ITT = LATE × (E[D|Z=1] − E[D|Z=0]) = LATE × π<sub>C</sub>
                </div>
                <p style="font-size: 0.9rem;">Always unbiased (OLS of Y on Z). Smaller than LATE in magnitude because compliance rate < 1.</p>
            </div>

            <div style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 1.5rem 0;">
                <h4 style="margin-top: 0; color: #7c3aed;">LATE: Compliers only</h4>
                <div style="background: white; border: 1px solid #c4b5fd; padding: 1rem; border-radius: 6px; margin: 0.5rem 0; text-align: center; font-family: 'Times New Roman', serif; font-size: 1.05rem;">
                    LATE = E[Y₁−Y₀ | Compliers] = ITT / First Stage
                </div>
                <p style="font-size: 0.9rem;">Excludes always-takers and never-takers entirely.</p>
            </div>

            <h3>Special Case: LATE = ATT (Bloom 1984)</h3>
            <div style="background: #f0fdf4; border: 1px solid #86efac; padding: 1.5rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>When there are no always-takers</strong> (one-sided non-compliance), i.e., E[D|Z=0] = 0:</p>
                <div style="background: white; border: 1px solid #86efac; padding: 1rem; border-radius: 6px; margin: 0.5rem 0; text-align: center; font-family: 'Times New Roman', serif;">
                    Always-takers = 0 → Treated = Compliers only → <strong>LATE = ATT</strong>
                </div>
                <p><strong>Example:</strong> JTPA training experiment — you can't access training without assignment, so everyone who trained was a complier. IV = ITT ÷ compliance rate = ATT.</p>
            </div>

            <h3>Size Relationships</h3>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Relationship</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Condition</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Example</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">|ITT| &lt; |LATE|</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Always (when compliance &lt; 1)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">ITT = LATE × compliance rate</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">ATT ≥ ATE (typically)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">High-benefit individuals self-select</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Voluntary job training, college</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">LATE = ATT</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">No always-takers</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">JTPA experiment (Bloom 1984)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">LATE₁ ≠ LATE₂</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Different IVs → different compliers</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Angrist & Evans: Twins ≠ Same-sex</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">LATE = ATE</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Homogeneous treatment effects</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Constant effect for everyone</td>
                </tr>
            </table>

            <h3>Methodology → Estimand Connection</h3>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Method</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Estimates</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Generalizability</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">RCT (full compliance)</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #dc2626; font-weight: 500;">ATE</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Broad</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">RCT (non-compliance) + IV</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #7c3aed; font-weight: 500;">LATE</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Compliers only</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">DID</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #059669; font-weight: 500;">ATT</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Groups similar to treated</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">RDD</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #7c3aed; font-weight: 500;">LATE at cutoff</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Near cutoff only</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Matching / PSM</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; color: #059669; font-weight: 500;">ATT</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Groups similar to treated</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- Takeaway -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Takeaway</h2>
        <div class="section-content">
            <div style="background: #ecfdf5; padding: 1.5rem; border-radius: 8px; margin: 1rem 0;">
                <p>When reading or writing empirical research, always ask:</p>
                <ol>
                    <li><strong>What estimand does this method identify?</strong> (ATE, ATT, or LATE?)</li>
                    <li><strong>Who are the compliers?</strong> (If IV/RDD — whose effect are we learning about?)</li>
                    <li><strong>Does the estimand match the policy question?</strong> (Universal program → ATE; voluntary → ATT; nudge → LATE)</li>
                    <li><strong>Are the compliers relevant for the intended policy?</strong> (Pilot enthusiasts ≠ general population)</li>
                </ol>
            </div>
        </div>
    </section>

    <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee; display: flex; justify-content: space-between;">
        <a href="/study/angrist-ch4-part2" style="color: #666;">← Ch.4 Part 2: LATE & Heterogeneous Effects</a>
        <a href="/study/angrist-ch4-part3" style="color: #2563eb;">Ch.4 Part 3: IV Details →</a>
    </div>

    <div style="margin-top: 2rem; padding: 1rem; background: #f9fafb; border-radius: 8px; font-size: 0.8rem; color: #6b7280;">
        <em>This note was written with the assistance of LLM (Claude).</em>
    </div>
</div>
