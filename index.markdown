---
layout: home
title: "Global Trade Networks: A Historical Journey"
date: 2024-03-26
author: s214588

---



In light of today's shifting geopolitical landscape and China's emergence as the world's largest export market, this interactive visualization project explores a crucial historical transition in global trade from 1870 to 2014. Through a series of interconnected stories, we trace America's dramatic rise to economic supremacy following World War II and its subsequent challenges, as China's unprecedented economic growth begins to reshape the global trade landscape. By examining this historical data, we gain valuable insights into one of the most significant power shifts in modern economic history.

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

    <a href="{{ site.baseurl }}/stories/gdp-development" class="story-card">
        <img src="{{ site.baseurl }}/assets/images/gdp-development-thumb.png" alt="GDP Development" class="story-thumbnail">
        <div class="story-content">
            <h3>GDP Development</h3>
            <p>The economic rise of the world's major powers, with a focus on the US and China.</p>
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


<div style="background-color: #fff3e6; border: 1px solid #ffcc99; border-radius: 4px; padding: 20px; margin: 30px 0;">
    <h3 style="color: #995c00; margin-top: 0;">A Note on Data Interpretation</h3>
    <p>This project examines patterns and behaviors in historical trade data, attempting to align observed trends with known historical events. While we use major historical milestones to help explain patterns in the data, it's important to note that we are primarily observing correlations rather than proving causation.</p>
    <p>Our analysis makes certain assumptions about the relationships between data patterns and historical events, but these connections are interpretative rather than definitive. The goal is to use history as a lens through which to understand the data, not to use the data to rewrite or definitively explain historical events.</p>
    <p>We encourage readers to approach these visualizations as explorations of trade patterns that coincide with historical developments, while maintaining awareness that real-world economic and political dynamics are often more complex than data alone can reveal.</p>
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