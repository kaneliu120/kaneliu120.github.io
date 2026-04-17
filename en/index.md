---
layout: default
title: English Industry Library
permalink: /en/
---

<section class="hero">
  <p class="eyebrow">English First Drafts</p>
  <h1>English AI Industry Library</h1>
  <p class="lede">English rewrites built from the Chinese source analysis folder. These pages are generated from local English drafts and published here in batches.</p>
  <p class="lede small">Currently published {{ site.en_docs | size }} English industry research pages.</p>
</section>

<section class="language-panel">
  <div class="language-copy">
    <p class="eyebrow">Scope</p>
    <h2>English counterparts to the Chinese source library.</h2>
    <p>This section mirrors the Chinese industry library with English rewrites based on the same source notes. The writing is structural and publication-oriented rather than line-by-line translation.</p>
  </div>
</section>

<section class="post-list">
  {% assign docs_sorted = site.en_docs | sort: "order_key" %}
  {% for doc in docs_sorted %}
  <article class="post-row">
    <div class="post-meta">{{ doc.source_code }}</div>
    <div class="post-copy">
      <h2><a href="{{ doc.url | relative_url }}">{{ doc.title }}</a></h2>
      {% if doc.source_file %}
      <p>{{ doc.source_file }}</p>
      {% endif %}
    </div>
  </article>
  {% endfor %}
</section>
