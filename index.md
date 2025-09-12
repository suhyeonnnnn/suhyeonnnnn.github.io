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
            Welcome! I'm a <span class="highlight">M.S. student at KAIST</span> in Management Engineering, 
            advised by Prof. Donghyuk Shin. My research focuses on <span class="highlight">Digital Marketing, 
            Social Media, and User Behavior</span> using cutting-edge AI technologies.
        </p>
        <p>
            I'm particularly interested in applying <span class="highlight">Generative AI, LLMs, and Computer Vision</span> 
            to understand how digital platforms shape user behavior and marketing effectiveness. 
            Currently, I'm a visiting student at <span class="highlight">Carnegie Mellon University</span> 
            participating in the AI Intensive Program.
        </p>
        <p>
            My work bridges the gap between advanced AI methodologies and practical marketing insights, 
            aiming to create innovative solutions for understanding and predicting human behavior 
            in digital environments.
        </p>
        <div class="quick-stats">
            <div class="stat-item">
                <span class="stat-number">3+</span>
                <span class="stat-label">Publications</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">10+</span>
                <span class="stat-label">Conference Presentations</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">$4K+</span>
                <span class="stat-label">Awards & Prizes</span>
            </div>
        </div>
    </div>
</div>
