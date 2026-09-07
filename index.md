---
layout: home
title: Home
---

<div class="about-content">
    <div class="profile-card fade-in">
        <div class="profile-img">
            👨‍💻
        </div>
        <h3>{{ site.author.name }}</h3>
        <p>{{ site.author.degree }}</p>
        <p>{{ site.author.university }}</p>
        <p class="location">📍 {{ site.author.location }}</p>
        <div class="social-links">
            <a href="mailto:{{ site.author.email }}" aria-label="Email">
                <i class="fas fa-envelope"></i>
            </a>
            <a href="https://github.com/{{ site.author.github }}" target="_blank" aria-label="GitHub">
                <i class="fab fa-github"></i>
            </a>
        </div>
    </div>
    <div class="about-text fade-in">
        <p>
            Welcome! I'm a <span class="highlight">Ph.D. student at KAIST</span> in Management Engineering,
            advised by Prof. Donghyuk Shin. I study <span class="highlight">AI-mediated markets</span>:
            what changes when AI systems come to sit between people and the choices they make.
        </p>
        <p>
            I look at this shift from three sides. For <span class="highlight">consumers</span>, I ask whether
            marketing still works once an agent does the searching and buying. For
            <span class="highlight">platforms</span>, I ask whether rules and features still govern as intended
            once AI generates and filters content. For <span class="highlight">AI providers</span>, I ask how these
            systems should be built to work with people in the first place.
        </p>
        <p>
            My work combines causal inference on large-scale platform data, controlled experiments with
            LLM agents, and theory-guided behavioral simulation. Before starting my Ph.D., I was a visiting
            student at <span class="highlight">Carnegie Mellon University</span> in the AI Intensive Program.
        </p>
        <div class="quick-stats">
            <div class="stat-item">
                <span class="stat-number">3</span>
                <span class="stat-label">Publications</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">5</span>
                <span class="stat-label">Working Papers</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">8</span>
                <span class="stat-label">Conference Presentations</span>
            </div>
        </div>
    </div>
</div>
