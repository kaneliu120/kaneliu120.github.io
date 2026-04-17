---
layout: default
title: AI Industry Replacement Analysis
---

<section class="hero">
  <p class="eyebrow">GitHub Pages</p>
  <h1>AI Industry Replacement Analysis</h1>
  <p class="lede">Published article bodies from Kane's completed LinkedIn industry series. This site only contains the long-form article text.</p>
  <div class="action-row">
    <a class="button-link" href="{{ '/profile/' | relative_url }}">GitHub README</a>
    <a class="button-link secondary" href="https://github.com/kaneliu120">GitHub Profile</a>
  </div>
</section>

<section class="profile-intro">
  <div class="profile-copy">
    <p class="eyebrow">From GitHub Profile</p>
    <h2>Building <a href="https://opendata.best">opendata.best</a> — the unified API for government data.</h2>
    <p class="lede small">865 live data products across 42 countries. 445M+ indexed records.</p>
    <p>Copied directly from <a href="https://github.com/kaneliu120">kaneliu120</a>'s GitHub profile README to strengthen the connection between the site and the profile.</p>
  </div>
  <div class="profile-badges">
    <a href="https://opendata.best"><img src="https://img.shields.io/badge/opendata.best-865_APIs-blue?style=flat-square" alt="opendata.best 865 APIs"></a>
    <a href="https://apify.com/lentic_clockss"><img src="https://img.shields.io/badge/Apify_Store-43_Actors-green?style=flat-square" alt="Apify Store 43 Actors"></a>
    <a href="https://opendata.best/catalog"><img src="https://img.shields.io/badge/Countries-42-orange?style=flat-square" alt="Countries 42"></a>
    <a href="https://www.linkedin.com/in/boliu2024/"><img src="https://img.shields.io/badge/LinkedIn-Bo_Liu-0A66C2?style=flat-square&logo=linkedin" alt="LinkedIn Bo Liu"></a>
  </div>
</section>

<section class="post-list">
  {% assign posts_sorted = site.posts | sort: "date" | reverse %}
  {% for post in posts_sorted %}
  <article class="post-row">
    <div class="post-meta">{{ post.date | date: "%B %-d, %Y" }}</div>
    <div class="post-copy">
      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      {% if post.subtitle %}
      <p>{{ post.subtitle }}</p>
      {% endif %}
    </div>
  </article>
  {% endfor %}
</section>
