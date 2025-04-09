---
layout: home
title: SDAV Exam Project
---

# Welcome to the SDAV Exam Project

This website showcases the data visualizations created for the SDAV exam project.

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

The source code for this project is available on [GitHub](https://github.com/Magdk01/SDAV_exam_project). 