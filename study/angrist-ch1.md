---
layout: minimal_base
title: "Angrist Ch.1 - Questions about Questions"
---

<div class="content">
    <section class="section fade-in">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="section-title">Chapter 1: Questions about Questions</h2>
            <a href="/study/angrist-ch1-ko" style="background: #e5e7eb; color: #374151; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; text-decoration: none;">한국어</a>
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
                "Good econometrics cannot save a shaky research agenda, but the promiscuous use of fancy econometric techniques sometimes brings down a good one."
            </blockquote>
            <p>Every empirical research project should begin with four Frequently Asked Questions (FAQs).</p>
        </div>
    </section>

    <!-- FAQ 1 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">FAQ 1: What is the causal relationship of interest?</h2>
        <div class="section-content">
            <p>The most interesting research in social science is about <strong>cause and effect</strong>.</p>
            
            <h4>Why Causal Relationships?</h4>
            <ul>
                <li>Useful for making predictions about <strong>counterfactual</strong> worlds</li>
                <li>Helps predict consequences of policy changes</li>
                <li>Can be derived from economic models</li>
            </ul>

            <h4>Example: Causal Effect of Education</h4>
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Question:</strong> What is the causal effect of schooling on wages?</p>
                <p><strong>Definition:</strong> The increment to wages an individual would receive with more schooling</p>
                <p><strong>Finding:</strong> Causal effect of college degree ≈ <strong>40% higher wages</strong> on average</p>
                <p><strong>Applications:</strong> Predicting effects of changing college costs, strengthening attendance laws</p>
            </div>

            <h4>Units of Analysis</h4>
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #f5f5f5;">
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Unit</th>
                    <th style="padding: 0.5rem; border: 1px solid #ddd;">Research Example</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Individuals</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Education → Wages (Labor Economics)</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Firms</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">R&D Investment → Productivity</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Countries</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Colonial Institutions → Economic Growth (Acemoglu et al., 2001)</td>
                </tr>
            </table>
        </div>
    </section>

    <!-- FAQ 2 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">FAQ 2: What is the ideal experiment?</h2>
        <div class="section-content">
            <p>Contemplate the <strong>ideal experiment</strong> that could capture the causal effect of interest.</p>

            <h4>Why Think About Ideal Experiments?</h4>
            <ul>
                <li>Helps pick fruitful research topics</li>
                <li>Formulates causal questions precisely</li>
                <li>Highlights forces to manipulate and factors to hold constant</li>
            </ul>

            <blockquote style="border-left: 4px solid #dc2626; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                "If you can't devise an experiment that answers your question in a world where anything goes, then the odds of generating useful results with a modest budget and non-experimental survey data seem pretty slim."
            </blockquote>

            <h4>Examples</h4>
            <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Schooling & Wages:</strong> Offer potential dropouts a reward for finishing school → Angrist & Lavy (2007) actually ran this</p>
                <p><strong>Political Institutions:</strong> Randomly assign different government structures to former colonies on Independence Day → Hypothetical</p>
            </div>

            <h4>🚫 FUQ'd: Fundamentally Unidentified Questions</h4>
            <p>Questions that <strong>cannot be answered by any experiment</strong> are FUQ'd.</p>
            
            <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Example: Effect of school start age on 1st grade test scores</strong></p>
                <table style="width:100%; border-collapse: collapse; margin: 0.5rem 0;">
                    <tr style="background: #fecaca;">
                        <th style="padding: 0.5rem; border: 1px solid #ddd;">Comparison</th>
                        <th style="padding: 0.5rem; border: 1px solid #ddd;">Problem</th>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">Same grade</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">Late starters are older → <strong>Maturation effect</strong></td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">Same age</td>
                        <td style="padding: 0.5rem; border: 1px solid #ddd;">Early starters spent more time in school → <strong>Time-in-school effect</strong></td>
                    </tr>
                </table>
                <p style="margin-top: 0.5rem;"><strong>Fundamental issue:</strong> Start age = Current age − Time in school (deterministic link)</p>
                <p><strong>Solution:</strong> Study adult outcomes (earnings, highest grade completed) instead</p>
            </div>

            <h4>What's NOT FUQ'd: Causal Effects of Race/Gender</h4>
            <p>Race and gender seem hard to manipulate, but labor market discrimination research focuses on <strong>perceived</strong> race/gender.</p>
            <ul>
                <li>Shakespeare's Rosalind disguised as Ganymede</li>
                <li>Philip Roth's novel - Black professor passing as white</li>
                <li><strong>Audit studies:</strong> Experiments with fake resumes (Bertrand & Mullainathan, 2004)</li>
            </ul>
        </div>
    </section>

    <!-- FAQ 3 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">FAQ 3: What is the identification strategy?</h2>
        <div class="section-content">
            <p><strong>Identification Strategy:</strong> The manner in which a researcher uses observational data to approximate a real experiment.</p>
            
            <h4>Natural Experiments</h4>
            <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <p><strong>Example: Angrist & Krueger (1991)</strong></p>
                <ul>
                    <li>Used interaction between compulsory attendance laws and season of birth</li>
                    <li>Season of birth affects how much students are constrained by dropout laws</li>
                    <li>→ Estimates effect of finishing high school on wages</li>
                </ul>
            </div>

            <h4>Haavelmo (1944)'s Insight</h4>
            <blockquote style="border-left: 4px solid #10b981; padding-left: 1rem; margin: 1rem 0; color: #374151;">
                "A design of experiments is an essential appendix to any quantitative theory. Experiments may be grouped into two classes:<br>
                (1) Experiments we should like to make to verify certain hypotheses<br>
                (2) The stream of experiments that Nature is steadily turning out, which we merely watch as passive observers"
            </blockquote>
        </div>
    </section>

    <!-- FAQ 4 -->
    <section class="section fade-in-delay">
        <h2 class="section-title">FAQ 4: What is the mode of statistical inference?</h2>
        <div class="section-content">
            <p><strong>Mode of Statistical Inference</strong> (Rubin, 1991)</p>
            
            <h4>What to Specify</h4>
            <ul>
                <li>The <strong>population</strong> to be studied</li>
                <li>The <strong>sample</strong> to be used</li>
                <li><strong>Assumptions</strong> made when constructing standard errors</li>
            </ul>

            <h4>Practical Issues</h4>
            <ul>
                <li>Especially important with clustered or grouped data</li>
                <li>Ultimate success of even well-conceived projects turns on inference details</li>
            </ul>

            <div style="background: #f5f5f5; padding: 1rem; border-radius: 8px; margin: 1rem 0; text-align: center;">
                <p><strong>Econometrics Haiku</strong> (Keisuke Hirano)</p>
                <p style="font-style: italic; font-family: 'Times New Roman', serif;">
                    T-stat looks too good.<br>
                    Use robust standard errors—<br>
                    significance gone.
                </p>
            </div>
        </div>
    </section>

    <!-- Summary -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Chapter 1 Summary</h2>
        <div class="section-content">
            <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
                <tr style="background: #2563eb; color: white;">
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">FAQ</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Question</th>
                    <th style="padding: 0.75rem; border: 1px solid #ddd;">Key Point</th>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; text-align: center;">1</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Causal relationship?</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Predicting changes in counterfactual worlds</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; text-align: center;">2</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Ideal experiment?</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Must conceptualize, even if hypothetical</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; text-align: center;">3</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Identification strategy?</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Approximate experiments with natural variation</td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem; border: 1px solid #ddd; text-align: center;">4</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Mode of inference?</td>
                    <td style="padding: 0.5rem; border: 1px solid #ddd;">Population, sample, standard error assumptions</td>
                </tr>
            </table>
        </div>
    </section>

    <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee; display: flex; justify-content: space-between;">
        <a href="/study" style="color: #666;">← Back to Study Notes</a>
        <a href="/study/angrist-ch2" style="color: #2563eb;">Chapter 2: The Experimental Ideal →</a>
    </div>

    <div style="margin-top: 2rem; padding: 1rem; background: #f9fafb; border-radius: 8px; font-size: 0.8rem; color: #6b7280;">
        <em>This note was written with the assistance of LLM (Claude).</em>
    </div>
</div>
