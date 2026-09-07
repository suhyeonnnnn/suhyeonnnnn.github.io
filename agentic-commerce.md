---
layout: minimal_base
title: "When the Buyer Is a Machine: The Diagnosticity-Exploration Tradeoff in Agentic Commerce"
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
            <h1 class="research-title">When the Buyer Is a Machine: The Diagnosticity-Exploration Tradeoff in Agentic Commerce</h1>
            <div class="research-meta">
                <div class="authors"><strong>Lee, S.</strong>, D. Shin, & S. P. Han</div>
                <div class="venue">Accepted at ICIS 2026 (Lisbon) and INFORMS CIST 2026 (San Francisco)</div>
                <div class="date">In preparation for <em>Information Systems Research</em></div>
                <div class="status"><span class="status-badge work-in-progress">Working Paper</span></div>
            </div>
        </div>
    </section>

    <!-- Overview -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Overview</h2>
        <div class="section-content">
            <p>
                Consumers are beginning to hand purchase decisions to AI agents that search, compare, and choose on
                their behalf. Marketing was built around human decision-making, so the question is whether it still
                works once the buyer is a machine. We find that it does, but not in the way it works on people.
            </p>
            <p>
                The cues that move an agent are not the cues that move a person. Agents follow aggregated social proof
                and largely ignore the scarcity and urgency appeals that drive human buyers. We argue the reason is
                architectural rather than psychological: an effective cue shortens the agent's search rather than
                persuading it.
            </p>
        </div>
    </section>

    <!-- Design -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Experimental Design</h2>
        <div class="section-content">
            <div class="method-card">
                <h4>Sandboxed shopping environment</h4>
                <ul>
                    <li>A replica of a live e-commerce interface, built so that every page element can be controlled</li>
                    <li>Fictional brands with matched attributes, so brand familiarity cannot drive choice</li>
                    <li>Price, rating, and display position randomized; marketing cues manipulated alone</li>
                    <li>Roughly 23,000 agent purchases collected across several commercial models</li>
                </ul>
            </div>

            <div class="method-card">
                <h4>Categories</h4>
                <ul>
                    <li>Four product categories spanning durables and replenishables</li>
                    <li>Eight candidate products per choice set</li>
                    <li>Model version, temperature, and seed fixed for reproducibility</li>
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
                    <div class="finding-icon">🔍</div>
                    <h4>Agents barely compare</h4>
                    <p>With eight candidates on screen, agents typically open one or two before deciding.</p>
                </div>

                <div class="finding-card">
                    <div class="finding-icon">📊</div>
                    <h4>Cues are not equal</h4>
                    <p>Aggregated social proof such as a best-seller badge moves choice sharply, while scarcity and urgency do not.</p>
                </div>

                <div class="finding-card">
                    <div class="finding-icon">🔒</div>
                    <h4>Forcing search barely helps</h4>
                    <p>Requiring the agent to open every candidate leaves most of the badge effect intact.</p>
                </div>

                <div class="finding-card">
                    <div class="finding-icon">🧭</div>
                    <h4>A different reference point</h4>
                    <p>People weigh alternatives against each other; agents judge each candidate against the request itself.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Interpretation -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Interpretation</h2>
        <div class="section-content">
            <div class="motivation-card">
                <h4>Why aggregated signals dominate</h4>
                <p>
                    When each candidate is judged on its own against a stated request rather than against rival
                    options, only cues that already carry ranking information inside them remain evaluable. A
                    best-seller badge encodes what other buyers chose; a countdown timer does not. The gap is
                    structural, which is why influence survives delegation but changes shape: it shifts from the
                    buyer's emotions to the agent's search.
                </p>
            </div>
        </div>
    </section>

    <!-- Implications -->
    <section class="section fade-in-delay">
        <h2 class="section-title">Implications</h2>
        <div class="section-content">
            <div class="applications-grid">
                <div class="application-card">
                    <h4>Sellers</h4>
                    <p>Cue portfolios tuned for human shoppers lose much of their effect once agents mediate purchases.</p>
                </div>

                <div class="application-card">
                    <h4>Platforms</h4>
                    <p>Ranking and badge systems carry more weight than intended when agents rely on them as the main evaluable signal.</p>
                </div>

                <div class="application-card">
                    <h4>Agent designers</h4>
                    <p>Shallow search is not only a cost decision; it determines which signals can influence the outcome at all.</p>
                </div>

                <div class="application-card">
                    <h4>Policy</h4>
                    <p>Consumer protection built around persuasion of people may not reach the mechanism that operates here.</p>
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
                    <span class="tech-tag featured">AI Agents</span>
                    <span class="tech-tag featured">Agentic Commerce</span>
                    <span class="tech-tag featured">Algorithmic Delegation</span>
                    <span class="tech-tag">Marketing Cues</span>
                    <span class="tech-tag">Consumer Search</span>
                    <span class="tech-tag">Discrete Choice</span>
                </div>
            </div>
        </div>
    </section>
</div>

<style>
.status-badge.work-in-progress {
    background: rgba(245, 158, 11, 0.1);
    color: rgb(180, 83, 9);
    border: 1px solid rgba(245, 158, 11, 0.3);
}
</style>
