---
layout: home
title: "Global Trade Networks: A Historical Journey"
date: 2024-03-26
author: s214588

---



This interactive visualization project explores the evolution of global trade networks using historical data from 1870 to 2014. Through a series of interconnected stories, we examine the global development, with a certain focus on the United States of America, and how they rose to economic power, as well as beginning to lose their edge.

Choose any story card below to begin your exploration, or follow them in sequence for a guided journey through the data.

<div class="story-grid">
    <a href="{{ site.baseurl }}/stories/data-quality" class="story-card">
        <img src="{{ site.baseurl }}/assets/images/data-quality-thumb.png" alt="Data Quality Analysis" class="story-thumbnail">
        <div class="story-content">
            <h3>Understanding the Data</h3>
            <p>Explore the quality and coverage of our historical trade dataset.</p>
        </div>
    </a>

    <a href="{{ site.baseurl }}/stories/trade-volumes" class="story-card">
        <img src="{{ site.baseurl }}/assets/images/trade-volumes-thumb.png" alt="Trade Volumes" class="story-thumbnail">
        <div class="story-content">
            <h3>Global Trade Volumes</h3>
            <p>The rise and fall of trade volumes through major historical events.</p>
        </div>
    </a>

    <a href="{{ site.baseurl }}/stories/network-analysis" class="story-card">
        <img src="{{ site.baseurl }}/assets/images/network-thumb.png" alt="Network Analysis" class="story-thumbnail">
        <div class="story-content">
            <h3>Trade Networks</h3>
            <p>Network analysis revealing key players and relationships.</p>
        </div>
    </a>
</div>

<!-- ## About This Project



## Project Overview

This project focuses on [brief description of your project's focus].

## Visualizations

{% for visualization in site.visualizations %}
  <div class="visualization-preview">
    <h2><a href="{{ visualization.url | relative_url }}">{{ visualization.title }}</a></h2>
    {% if visualization.description %}
      <p>{{ visualization.description }}</p>
    {% endif %}
  </div>
{% endfor %}

## About

## Repository

The source code for this project is available on [GitHub](https://github.com/Magdk01/SDAV_exam_project).  -->


<style>
.visualization-preview {
  margin: 2rem 0;
  padding: 1.5rem;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: transform 0.2s ease-in-out;
}

.visualization-preview:hover {
  transform: translateY(-2px);
}

.visualization-preview h2 {
  margin: 0 0 1rem 0;
  font-size: 1.8rem;
}

.visualization-preview h2 a {
  color: #333;
  text-decoration: none;
}

.visualization-preview h2 a:hover {
  color: #0366d6;
}

.visualization-description {
  color: #666;
  margin-bottom: 0.5rem;
}

.visualization-meta {
  color: #888;
  font-size: 0.9rem;
}
</style>