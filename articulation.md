---
layout: minimal_base
title: "How You Ask Shapes What You Get: A Theory-Seeded Measurement of Articulation in Advice-Seeking LLM Conversations"
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
            <h1 class="research-title">How You Ask Shapes What You Get: A Theory-Seeded Measurement of Articulation in Advice-Seeking LLM Conversations</h1>
            <div class="research-meta">
                <div class="authors">Baek, J., <strong>S. Lee</strong>, & D. Shin</div>
                <div class="venue">Findings of the Association for Computational Linguistics: EMNLP, 2026</div>
                <div class="date"><a href="https://arxiv.org/abs/2608.29591" target="_blank">arXiv:2608.29591</a></div>
                <div class="status"><span class="status-badge forthcoming">Forthcoming</span></div>
            </div>
        </div>
    </section>

    <!-- Abstract -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Abstract</h2>
        <div class="section-content">
            <p>
                Users articulate the same advice-seeking request in different ways: some specify detailed constraints,
                others gesture at a vague need. Prior work treats this variation as noise to be averaged away; we
                instead treat it as a stable, measurable structure in the input distribution.
            </p>
            <p>
                We ask whether articulation, meaning how people ask, forms latent dimensions separable from topic,
                meaning what they ask about, and whether it is associated with how language models respond. We extract
                interpretable features from 16,447 advice-seeking prompts pooled from public chat corpora (WildChat,
                LMSYS, and ShareChat) and recover a small set of latent articulation factors that replicate across
                train/test splits and across corpora.
            </p>
        </div>
    </section>

    <!-- Why it matters -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Why This Question</h2>
        <div class="section-content">
            <div class="motivation-card">
                <h4>Variation in how people ask is usually discarded</h4>
                <p>
                    Existing work treats prompt variation either as noise to be removed, as in the paraphrase
                    robustness literature, or as a problem of model behavior. Both framings sit downstream of a more
                    basic question that has not been answered for naturalistic chat: does articulation variation in the
                    wild form a stable structure separable from topic?
                </p>
            </div>

            <div class="motivation-card">
                <h4>The answer determines what an evaluation can see</h4>
                <p>
                    If articulation collapses onto topic, then varying prompts across topics already covers it and
                    nothing is missed. If it is a separate dimension, evaluations that sample only across topics leave
                    a systematic part of real usage unexamined.
                </p>
            </div>
        </div>
    </section>

    <!-- Approach -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Approach</h2>
        <div class="section-content">
            <div class="method-card">
                <h4>Data</h4>
                <ul>
                    <li>16,447 advice-seeking prompts pooled from WildChat, LMSYS, and ShareChat</li>
                    <li>Real user conversations rather than constructed prompt sets</li>
                </ul>
            </div>

            <div class="method-card">
                <h4>Measurement</h4>
                <ul>
                    <li>Interpretable features rather than opaque embeddings, so the factors can be read</li>
                    <li>Latent articulation factors recovered and checked for replication across splits and corpora</li>
                    <li>Separability from topic tested directly rather than assumed</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- Keywords -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Keywords</h2>
        <div class="section-content">
            <div class="tech-specs">
                <div class="tech-stack">
                    <span class="tech-tag featured">Human-AI Interaction</span>
                    <span class="tech-tag featured">Prompt Articulation</span>
                    <span class="tech-tag featured">LLM Measurement</span>
                    <span class="tech-tag">Advice Seeking</span>
                    <span class="tech-tag">Chat Corpora</span>
                    <span class="tech-tag">Latent Factor Models</span>
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
