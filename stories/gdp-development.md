---
layout: story
title: "GDP Development"
subtitle: "The Economic Rise of Major Powers"
previous_story: trade-volumes
previous_story_title: "Trade Volumes"
next_story: network-analysis
next_story_title: "Network Analysis"
---

Looking at the development in the other stories, we generally see rapidly developing trade volumues and networks, which could incidentially mean equvilant developments in global GDPs.

A look at the definitions (see <a href="https://www.britannica.com/money/gross-domestic-product">Britannica's primer on GDP</a>) reminds us that the number we call gross domestic product (GDP) folds in consumer spending, government outlays, investment, and only then the trade balance. Exports matter—but they are just one slice of a much larger pie.

But how does this look in data?
<iframe src="../visualizations/GDP_development.html" width="100%" height="1050px" frameborder="0"></iframe>

*Figure 1: GDP development of major economies from 1870 to 2014, with a focus on the United States and China. The visualization includes both linear and logarithmic scales, with dashed lines showing log-linear projections of future growth.*

Again starting with a focus on the development of USA and China we generally see that China's GPD climb more steeply in recent years, which is further reinforced if you look at the log-scaled y-axis.

To make a guess on, if and when China would overtake USA as the largest economy, a simple straight-line regression (in log-domain) is used to estimated economic growth. This regression predicts that China will overtake the American economy already in 2026, but it is also apperent that linear regression is properly too simply as it overshoots both series by the time we reach the latest observations.
In other words, the turbo-charged growth of the 2000s and early 2010s has already cooled a little for both economies, making it a bit more difficult to model the economic growth using linear regression in log-domain.

Thus we can ask ourselves if this forecast reliable? Since I am no economic expert, I would properly say no, especially given the almost daily tarrif changes and fast-changing geopolitics. However the regression can serve as a quick insight into the economic strength and development of the existing economic super powers.

## How to read the chart above
- Linear vs. Log scale <br>
Click the button in the top-right corner. <br>
Linear shows the absolute size gap; 
<br>Log stretches the early decades so you can compare growth rates.<br>
A fun part of using linear regression in log-domain is that it is visualized as exponential regression in the linear domain.

- Legend clicks
<br>Only China and the United States are visible at first. Click any other economy to bring it into view; click again to hide it.

- Dashed projections <br>
Each country also has a dashed line: a simple log-linear fit of its past growth, hidden by default. 
<br>Toggle it on to see how a straight-line extrapolation would look—but remember that such projections ignore policy shocks like new tariffs or recessions.


## Data source
GDP data orginates from the Maddison Project Database[1], and is interacted with through the World Bank API for Python

# References
[1] Maddison Project Database, version 2020. Bolt, Jutta and Jan Luiten van Zanden (2020), "Maddison style estimates of the evolution of the world economy. A new 2020 update". Maddison Project Database, version 2020. Available at: https://www.rug.nl/ggdc/historicaldevelopment/maddison/releases/maddison-project-database-2020

[2] WBdata Python Package Documentation: https://wbdata.readthedocs.io/en/stable/

