---
layout: story
title: "GDP Development"
subtitle: "The Economic Rise of Major Powers"
previous_story: trade-volumes
previous_story_title: "Trade Volumes"
next_story: network-analysis
next_story_title: "Network Analysis"
---

Looking at the development in the other stories, we generally see booming exports, which could incidentially mean equvilant developments in global GDPs.

A look at the definitions (see <a href="https://www.britannica.com/money/gross-domestic-product">Britannica's primer on GDP</a>) reminds us that the number we call gross domestic product (GDP) folds in consumer spending, government outlays, investment, and only then the trade balance. Exports matter—but they are just one slice of a much larger pie.

So what does the data say?



<iframe src="../visualizations/GDP_development.html" width="100%" height="1050px" frameborder="0"></iframe>
From a first view it seems that China's GPD climb more steeply, which is reinforced if you look at the log-scaled y-axis.

A simple straight-line regression (in log-domain) predicts that China will overtake the American economy already in 2026, but it is also apperent that linear regression is properly too simply as it overshoots both series by the time we reach the latest observations. In other words, the turbo-charged growth of the 2000s and early 2010s has already cooled a little for both economies. (The fun part of using linear regression in log-domain is that it is visualized as exponential regression in the linear domain.)

Is this forecast reliable? Probably not in a world daily tarrif changes and fast-changing geopolitics. 



## How to read the chart above
- Linear vs. Log scale <br>
Click the button in the top-right corner. <br>
Linear shows the absolute size gap; 
<br>Log stretches the early decades so you can compare growth rates.

- Legend clicks
<br>Only China and the United States are visible at first. Click any other economy to bring it into view; click again to hide it.

- Dashed projections <br>
Each country also has a dashed line: a simple log-linear fit of its past growth, hidden by default. 
<br>Toggle it on to see how a straight-line extrapolation would look—but remember that such projections ignore policy shocks like new tariffs or recessions.

