---
layout: minimal_base
title: "Research"
---

<div class="content">
    <section class="section fade-in">
        <h2 class="section-title">Research Interests</h2>
        <div class="section-content">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 2rem;">
                <div style="background: rgba(0, 0, 0, 0.02); padding: 2rem; border-radius: 15px;">
                    <h3 style="color: var(--primary-color); margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;">
                        🎯 Substantive Areas
                    </h3>
                    <ul style="list-style: none; padding: 0;">
                        {% if site.research.substantive %}
                            {% for area in site.research.substantive %}
                                <li style="padding: 0.5rem 0; border-bottom: 1px solid rgba(0,0,0,0.05);">{{ area }}</li>
                            {% endfor %}
                        {% else %}
                            <li style="padding: 0.5rem 0; border-bottom: 1px solid rgba(0,0,0,0.05);">Digital Marketing</li>
                            <li style="padding: 0.5rem 0; border-bottom: 1px solid rgba(0,0,0,0.05);">Social Media</li>
                            <li style="padding: 0.5rem 0; border-bottom: 1px solid rgba(0,0,0,0.05);">User Behavior</li>
                            <li style="padding: 0.5rem 0;">AI Applications</li>
                        {% endif %}
                    </ul>
                </div>
                
                <div style="background: rgba(0, 0, 0, 0.02); padding: 2rem; border-radius: 15px;">
                    <h3 style="color: var(--primary-color); margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;">
                        🔧 Methodological Areas
                    </h3>
                    <ul style="list-style: none; padding: 0;">
                        {% if site.research.methodological %}
                            {% for method in site.research.methodological %}
                                <li style="padding: 0.5rem 0; border-bottom: 1px solid rgba(0,0,0,0.05);">{{ method }}</li>
                            {% endfor %}
                        {% else %}
                            <li style="padding: 0.5rem 0; border-bottom: 1px solid rgba(0,0,0,0.05);">Generative AI</li>
                            <li style="padding: 0.5rem 0; border-bottom: 1px solid rgba(0,0,0,0.05);">Large Language Models</li>
                            <li style="padding: 0.5rem 0; border-bottom: 1px solid rgba(0,0,0,0.05);">Computer Vision</li>
                            <li style="padding: 0.5rem 0;">Machine Learning</li>
                        {% endif %}
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <section class="section fade-in-delay">
        <h2 class="section-title">Publications</h2>
        <div class="section-content">
            <div class="news-item">
                <div class="news-date">2025</div>
                <div class="news-title">PlaceSim: An LLM-based Interactive Platform for Human Behavior Simulation</div>
                <div class="news-description">
                    <strong>CIKM 2025</strong> - Conference on Information and Knowledge Management, Seoul, Korea
                </div>
            </div>
            
            <div class="news-item">
                <div class="news-date">2025</div>
                <div class="news-title">Dynamics of Online WOM and Performance</div>
                <div class="news-description">
                    <strong>ISMS Marketing Science Conference</strong> - Presented research findings
                </div>
            </div>
        </div>
    </section>

    <section class="section fade-in-delay">
        <h2 class="section-title">Research Experience</h2>
        <div class="section-content">
            <div class="news-item">
                <div class="news-date">2024 - Present</div>
                <div class="news-title">Graduate Research Assistant</div>
                <div class="news-description">
                    KAIST, Management Engineering<br>
                    Advisor: Prof. Donghyuk Shin
                </div>
            </div>
            
            <div class="news-item">
                <div class="news-date">Dec 2024 - Jul 2025</div>
                <div class="news-title">Visiting Student Researcher</div>
                <div class="news-description">
                    Carnegie Mellon University<br>
                    AI Intensive Program, Pittsburgh, PA
                </div>
            </div>
        </div>
    </section>
</div>
