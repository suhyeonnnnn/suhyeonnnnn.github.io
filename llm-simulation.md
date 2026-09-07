---
layout: minimal_base
title: "Predicting Spatial Choice Without Historical Data"
---

<div class="content">
    <!-- Back Button -->
    <div style="margin-bottom: 2rem;">
        <a href="research.html" style="color: var(--text-secondary); text-decoration: none; font-weight: 500;">
            ← Back to Research
        </a>
    </div>

    <!-- Paper Header -->
    <section class="section fade-in">
        <div class="research-header">
            <h1 class="research-title">Predicting Spatial Choice Without Historical Data: A Theory-Guided LLM Simulation Framework</h1>
            <div class="research-meta">
                <div class="authors"><strong>Lee, S.</strong>, Y. Yu, & D. Shin</div>
                <div class="venue">In preparation for <em>Journal of Management Information Systems</em></div>
                <div class="status"><span class="status-badge work-in-progress">Working Paper</span></div>
            </div>
        </div>
    </section>

    <!-- Abstract -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Overview</h2>
        <div class="section-content">
            <p>
                Predicting how people will use a space that does not yet exist is a cold-start problem: there is no
                usage history to learn from, and stated preferences collected through surveys often diverge from what
                people actually do. This paper asks whether a language model can stand in for the data a new market
                does not have, provided its reasoning is constrained by behavioral theory rather than by history.
            </p>
            <p>
                We develop the Person-Environment-Situation (P.E.S.) framework, which structures LLM reasoning around
                Lewin's field theory, and validate it against real facility usage records with the later period held out.
                The result is not that a language model imitates people, but that theory can substitute for the
                observational data a novel setting lacks.
            </p>
        </div>
    </section>

    <!-- Research Motivation -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Motivation</h2>
        <div class="section-content">
            <div class="motivation-card">
                <h4>The cold-start problem in facility design</h4>
                <p>
                    Design decisions for new buildings carry long-term economic and social consequences, yet the
                    behavior they aim to accommodate cannot be observed in advance. Existing approaches fall short in
                    predictable ways:
                </p>
                <ul>
                    <li>Surveys capture stated preferences that diverge from actual usage</li>
                    <li>Observational studies require an existing facility to observe</li>
                    <li>Space Syntax and layout planning models capture spatial logic but not behavioral complexity</li>
                    <li>Supervised prediction models require the very usage history that does not yet exist</li>
                </ul>
            </div>

            <div class="motivation-card">
                <h4>Why theory rather than history</h4>
                <p>
                    If a model cannot learn from past behavior in this setting, its predictions must be constrained by
                    something else. We use behavioral theory as that constraint, which also makes the reasoning behind
                    each prediction inspectable rather than opaque.
                </p>
            </div>
        </div>
    </section>

    <!-- Framework -->
    <section class="section fade-in-delay">
        <h2 class="section-title">The P.E.S. Framework</h2>
        <div class="section-content">
            <p>
                Kurt Lewin's field theory holds that behavior is a function of the person and the environment,
                B = f(P, E). The framework operationalizes this for language model reasoning by separating three
                inputs that are specified independently for each simulated decision.
            </p>

            <div class="framework-card">
                <h4>Person</h4>
                <ul>
                    <li>Demographic attributes and household composition</li>
                    <li>Preferences, goals, and current intentions</li>
                    <li>Constraints that shape what options are available to this person</li>
                </ul>
            </div>

            <div class="framework-card">
                <h4>Environment</h4>
                <ul>
                    <li>Physical layout and accessibility of the facility</li>
                    <li>Available amenities and what each affords</li>
                    <li>Ambient conditions and the presence of others</li>
                </ul>
            </div>

            <div class="framework-card">
                <h4>Situation</h4>
                <ul>
                    <li>Time of day, day of week, and season</li>
                    <li>Purpose of the visit and competing obligations</li>
                    <li>Social context in which the choice is made</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- Validation -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Validation</h2>
        <div class="section-content">
            <div class="method-card">
                <h4>Data</h4>
                <ul>
                    <li>Real facility usage records from residential complexes, spanning 18 months</li>
                    <li>The later period is held out entirely, so the model never sees the behavior it predicts</li>
                    <li>Predictions are compared against observed usage distributions rather than point outcomes</li>
                </ul>
            </div>

            <div class="method-card">
                <h4>Comparison</h4>
                <ul>
                    <li>Supervised learning baselines trained on historical usage</li>
                    <li>Existing LLM-based simulation tools</li>
                    <li>Distributional agreement measured by Jensen-Shannon Divergence</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- Related output -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Related Output</h2>
        <div class="section-content">
            <div class="method-card">
                <h4>PlaceSim (CIKM 2025)</h4>
                <p>
                    An earlier version of this framework was released as PlaceSim, a web-based platform that lets
                    architects, planners, and facility managers run these simulations without writing code. It was
                    published in the Proceedings of the ACM International Conference on Information and Knowledge
                    Management.
                    <a href="placesim.html">Read more</a> &middot;
                    <a href="https://doi.org/10.1145/3746252.3761461" target="_blank">doi:10.1145/3746252.3761461</a>
                </p>
            </div>
        </div>
    </section>

    <!-- Technical Specifications -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Keywords</h2>
        <div class="section-content">
            <div class="tech-specs">
                <div class="tech-stack">
                    <span class="tech-tag featured">LLM-based Behavioral Simulation</span>
                    <span class="tech-tag featured">Cold-Start Prediction</span>
                    <span class="tech-tag featured">Discrete Choice</span>
                    <span class="tech-tag">Environmental Psychology</span>
                    <span class="tech-tag">Facility Design</span>
                    <span class="tech-tag">Spatial Analytics</span>
                </div>
            </div>
        </div>
    </section>
</div>

<style>
.framework-card, .future-card {
    background: var(--bg-card);
    padding: 1.5rem;
    border-radius: var(--border-radius);
    margin-bottom: 1.5rem;
    box-shadow: var(--shadow-light);
    border-left: 4px solid #8b5cf6;
}

.framework-card h4, .future-card h4 {
    color: var(--text-primary);
    margin-bottom: 1rem;
    font-size: 1.1rem;
}

.status-badge.work-in-progress {
    background: rgba(245, 158, 11, 0.1);
    color: rgb(180, 83, 9);
    border: 1px solid rgba(245, 158, 11, 0.3);
}

.metric-value.neutral {
    color: var(--text-secondary);
}
</style>
