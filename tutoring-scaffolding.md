---
layout: minimal_base
title: "LLM Pedagogical Behavior in AI Tutoring Interactions"
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
            <h1 class="research-title">LLM Pedagogical Behavior in AI Tutoring Interactions</h1>
            <div class="research-meta">
                <div class="authors"><strong>Lee, S.</strong>, J. Baek, J. Park, & D. Shin</div>
                <div class="venue">Findings of the Association for Computational Linguistics: EMNLP, 2026</div>
                <div class="date"><a href="https://arxiv.org/abs/2608.22993" target="_blank">arXiv:2608.22993</a></div>
                <div class="status"><span class="status-badge forthcoming">Forthcoming</span></div>
            </div>
        </div>
    </section>

    <!-- Abstract -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Abstract</h2>
        <div class="section-content">
            <p>
                Students increasingly use LLMs as tutors for coursework and problem solving. Little is known about the
                level of assistance LLMs provide when students use them as tutors in authentic learning interactions.
                This matters because tutoring responses can differ substantially in how directly they help students
                complete a task. We operationalize this dimension as scaffolding level and develop a five-level scale,
                validated against human annotations, that characterizes responses according to the degree of direct
                assistance they provide.
            </p>
            <p>
                We apply the scale to 14,637 LLM responses from 203 students in a university AI course. Responses are
                overwhelmingly concentrated at high levels of assistance, with more than 95% classified as either
                Explaining or Solving. Scaffolding level is systematically associated with students' subsequent
                conversational behavior, but provides little additional predictive information about performance on
                three subsequent exams beyond prior achievement and dialogue behavior. These findings provide an
                empirical baseline for LLM assistance in tutoring interactions and a measurement framework for
                evaluating how alternative tutoring designs change that assistance.
            </p>
        </div>
    </section>

    <!-- What We Do -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Approach</h2>
        <div class="section-content">
            <div class="method-card">
                <h4>A scale for how much help a response gives</h4>
                <ul>
                    <li>Five levels ordered by how directly a response completes the task for the student</li>
                    <li>Validated against human annotations rather than assumed</li>
                    <li>Applied at the level of individual tutoring responses, not whole sessions</li>
                </ul>
            </div>

            <div class="method-card">
                <h4>Authentic classroom data</h4>
                <ul>
                    <li>14,637 LLM responses drawn from real coursework interactions</li>
                    <li>203 students in a university AI course</li>
                    <li>Three subsequent exams available as downstream outcomes</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- Findings -->
    <section class="section fade-in-delay">
        <h2 class="section-title">What We Find</h2>
        <div class="section-content">
            <div class="findings-grid">
                <div class="finding-card">
                    <div class="finding-icon">📈</div>
                    <h4>Assistance runs high</h4>
                    <p>Over 95% of responses fall into the two most direct levels, Explaining or Solving.</p>
                </div>

                <div class="finding-card">
                    <div class="finding-icon">💬</div>
                    <h4>It shapes the dialogue</h4>
                    <p>Scaffolding level is systematically associated with what students do next in the conversation.</p>
                </div>

                <div class="finding-card">
                    <div class="finding-icon">📝</div>
                    <h4>But not exam scores</h4>
                    <p>Beyond prior achievement and dialogue behavior, it adds little in predicting later exam performance.</p>
                </div>

                <div class="finding-card">
                    <div class="finding-icon">📏</div>
                    <h4>A baseline to build on</h4>
                    <p>The scale gives a way to evaluate whether alternative tutoring designs actually change assistance.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Keywords -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Keywords</h2>
        <div class="section-content">
            <div class="tech-specs">
                <div class="tech-stack">
                    <span class="tech-tag featured">AI Tutoring</span>
                    <span class="tech-tag featured">Scaffolding</span>
                    <span class="tech-tag featured">Human-AI Interaction</span>
                    <span class="tech-tag">LLM Measurement</span>
                    <span class="tech-tag">Learning Analytics</span>
                </div>
            </div>
        </div>
    </section>
</div>

<style>
.status-badge.forthcoming {
    background: rgba(34, 197, 94, 0.1);
    color: rgb(21, 128, 61);
    border: 1px solid rgba(34, 197, 94, 0.3);
}
</style>
