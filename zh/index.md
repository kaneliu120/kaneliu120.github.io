---
layout: default
title: 中文行业库
permalink: /zh/
---

<section class="hero">
  <p class="eyebrow">Chinese First</p>
  <h1>AI 人工替代中文行业库</h1>
  <p class="lede">基于“AI的人工替代全景分析”源文件夹整理。这里先发布中文版本，英文版本后续按同一结构扩展。</p>
  <p class="lede small">当前已发布 {{ site.zh_docs | size }} 篇中文行业研究页。</p>
</section>

<section class="language-panel">
  <div class="language-copy">
    <p class="eyebrow">Scope</p>
    <h2>排除已做 LinkedIn 终版的行业。</h2>
    <p>本页收录的是尚未进入 LinkedIn 终版流程的中文行业评估文档，直接按源文档发布，保留原始研究结构、表格和岗位评估内容。</p>
  </div>
</section>

<section class="post-list">
  {% assign docs_sorted = site.zh_docs | sort: "order_key" %}
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
