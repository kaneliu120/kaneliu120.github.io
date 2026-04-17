---
layout: default
title: AI Industry Replacement Analysis
---

<section class="hero">
  <p class="eyebrow">GitHub Pages</p>
  <h1>AI Industry Replacement Analysis</h1>
  <p class="lede">Published article bodies from Kane's completed LinkedIn industry series. This site only contains the long-form article text.</p>
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
