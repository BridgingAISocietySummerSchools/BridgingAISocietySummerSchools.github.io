---
title: "About Us"
subtitle: "Who We Are"
description: "Meet the team behind Bridging AI and Society"
permalink: /about/
---

## 👥 Who We Are

We are a team of two passionate educators dedicated to making AI and machine learning accessible across disciplines. Our mission is to bridge the gap between technical foundations and societal impact through collaborative, hands-on learning.

<style>
  .author-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
  }

  .author-profile {
    background-color: #fff;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s, box-shadow 0.2s;
  }

  .author-profile:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.2);
  }

  .author-avatar img {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 1rem;
  }

  .author-profile h3 {
    margin-bottom: 0.25rem;
    font-size: 1.25rem;
    color: #333;
  }

  .author-title {
    color: #666;
    font-style: italic;
    margin-bottom: 1.25rem;
  }

  .author-info {
    text-align: left;
    font-size: 0.95rem;
    line-height: 1.5;
    color: #444;
  }

  .author-info p {
    margin: 0.5rem 0;
  }

  .author-links {
    margin-top: 1.5rem;
  }

  .author-links p {
    margin: 0.25rem 0;
    font-size: 0.8rem;
    /* color: #007bff; */
  }

  .author-links a {
    text-decoration: none;
    font-weight: bold;
  }

  .author-links a:hover {
    text-decoration: underline;
  }
</style>

<div class="author-grid">
  <div class="author-profile">
    <div class="author-avatar">
      <img src="{{ '/assets/img/headshot-christoph.jpg' | relative_url }}" alt="Dr. Christoph Weisser">
    </div>

    <h3>Dr. Christoph Weisser</h3>
    <p class="author-title">Technical Lead Analytics & AI<br>BASF</p>

    <div class="author-info">
      <p><strong>Ph.D.</strong> in applied statistics</p>
      <p><strong>Research:</strong> applied statistics and data science, forecasting, agentic systems</p>
      <p>Passionate about teaching and business data science</p>
    </div>

    <div class="author-links">
      <!-- <p>
        <a href="#" class="email-link" data-user="christoph.weisser" data-domain="oxfordalumni.org">
          <i class="fas fa-envelope" style="margin-right: 0.4rem;"></i>
          <span class="email-text">[email protected]</span>
        </a>
      </p> -->
      <p>
        <a href="https://linkedin.com/in/christophweisser" target="_blank">
          <i class="fab fa-linkedin" style="margin-right: 0.4rem;"></i>
          Connect on LinkedIn
        </a>
      </p>
    </div>
  </div>

  <div class="author-profile">
    <div class="author-avatar">
      <img src="{{ '/assets/img/headshot-knut.jpg' | relative_url }}" alt="Dr. Knut Zoch">
    </div>

    <h3>Dr. Knut Zoch</h3>
    <p class="author-title">Physicist<br>Harvard University</p>

    <div class="author-info">
      <p><strong>Ph.D.</strong> in experimental particle physics</p>
      <p><strong>Research:</strong> big data analytics at CERN, machine learning for science</p>
      <p>Passionate about teaching and interdisciplinary science</p>
    </div>

    <div class="author-links">
      <!-- <p>
        <a href="#" class="email-link" data-user="knut.zoch" data-domain="cern.ch">
          <i class="fas fa-envelope" style="margin-right: 0.4rem;"></i>
          <span class="email-text">[email protected]</span>
        </a>
      </p> -->
      <p>
        <a href="https://linkedin.com/in/knutzk" target="_blank">
          <i class="fab fa-linkedin" style="margin-right: 0.4rem;"></i>
          Connect on LinkedIn
        </a>
      </p>
    </div>
  </div>
</div>

<div style="text-align: center; margin-top: 2rem; font-style: italic; color: #666;">
  We look forward to learning and exploring with you!
</div>

## 🎯 Our Mission

We believe that understanding AI and machine learning should not be limited to data scientists. By creating accessible, interdisciplinary educational experiences, we aim to:

- **Democratize AI education** across all academic disciplines
- **Foster critical thinking** about AI's role in society
- **Build bridges** between technical expertise and societal impact
- **Empower educators** with flexible, reusable teaching materials


<script>
  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('.email-link').forEach(link => {
      const user = link.dataset.user;
      const domain = link.dataset.domain;
      const email = `${user}@${domain}`;
      link.href = `mailto:${email}`;
      link.querySelector('.email-text').textContent = email;
    });
  });
</script>