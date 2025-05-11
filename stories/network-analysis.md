---
layout: story
title: "Trade Networks"
subtitle: "Network Analysis of Global Trade Relationships"
previous_story: gdp-development
previous_story_title: "GDP Development"
next_story: 
---

Another intresting way to approach developments in trade, is to model trading as networks, to see who trades with who, and how these communities change over time.
In this interactive visualization, we visualize global trade networks, where each circle represents a country, growing larger as that nation's trade expands. Lines connect trading partners, thickening as commerce between them increases. You can decide to move through the development as a movie using "play" or just go to significant time periodes such as World Wars or Economic crashes.
As you move through time, you'll see the rise and fall of trading powers, the formation of economic blocs, and the ever-shifting patterns of international commerce.

   <iframe src="../visualizations/trade_network.html" width="100%" height="1250px" frameborder="0"></iframe>

*Figure 1: Interactive visualization of global trade networks from 1870 to 2014. Each circle represents a country, with size indicating total trade volume. Connecting lines show trade relationships, with thickness proportional to trade volume. Use the timeline slider to observe key historical events like World Wars and economic crises.*

## Network Analysis of Global Trade

### Historical Patterns

Britain dominates the early decades. From the late-1800s until well into the war period the United Kingdom sits at the centre of the inner circle. Its large node reflects the reach of an economy that once ran a  empire and controlled many of the worlds most important trade routes. 

War years empty the network. Advance the slider to 1916 or 1943 and the graph contracts sharply. Many nodes shrink and the edge-web thins to almost nothing. Part of that is genuine disruption: trading routes were blockaded and resources diverted to the war effort. Part of it is data quality. For example, the dataset shows no recorded trade between the United States and the United Kingdom in 1943 — obviously an undercount for two allies coordinating supply chains - while small flows still appear between the UK and Germany. Sparse records, rationing, and secrecy all left gaps that the raw numbers does not fill.

They also shows the limits of the underlying data: missing or misreported flows become easiest to spot precisely when the graph is at its emptiest, as we can see the lack of connections we would otherwise expect.

Fast forward to 2014, and we see a striking visual representation of the shifting global economic landscape. The United States and China appear nearly equal in size on the network graph, their nodes "dominating" the visualization with similar prominence. This visual parity reflects the remarkable economic convergence between these two superpowers, with China's rapid economic growth bringing it to a level of global trade influence that rivals the United States.

## Centrality Analysis: Understanding Trade Power Dynamics

To better understand the shifting patterns of global trade influence over time, we can examine two key measures of network centrality: degree and betweenness centrality. These serves as metrics allowing us to summarize the development in the networks rather that having to only look at the graphs themselves. Also notice that both centralities are normalized, so they express their y-axis' as a fraction of the total possible centrality in each respective centrality type.

   <iframe src="../visualizations/centralities.html" width="100%" height="700px" frameborder="0"></iframe>

*Figure 2: Evolution of degree and betweenness centrality measures for major trading nations (1870-2014). The top graph shows degree centrality (percentage of available trade partners), while the bottom graph displays betweenness centrality (importance as a trade intermediary).*

### Degree Centrality: How many trade partners?

Degree centrality can be used to express the percentage of the available trade partners a country trades with. The United Kingdom's early dominance is particularly visual here - it maintained a normalized degree centrality close to 1 even in the late 1800s, meaning it traded with nearly every available partner already then. In contrast, the United States traded with only about 50% of available countries in 1870, while China's degree centrality was below 20%.

The visualization reveals an interesting pattern in how countries responded to World War I. While the United States and UK showed immediate effects in their trade relationships, China's degree centrality declined later, reflecting its delayed entry into the war in 1917. This temporal difference highlights how global conflicts have had varying impacts on different regions of the world, due to different regional/national or even international effects.

### Betweenness Centrality: Trade Hubs

Betweenness centrality reveals which countries has acted as intermediaries in global trade. The United Kingdom's historical role as a trade hub is particularly evident here - it maintained high betweenness centrality until World War I, showing its position as a critical middleman in global trading. This dominance could partially be explained by institutions like the East India Company, though we can observe a notable decline around 1874 when the company was disbanded.[1]

The post-World War II period shows a dramatic shift in global trade patterns. Betweenness centrality scores for all countries approach zero, indicating that the era of dominant trade intermediaries has ended. Instead, countries began trading more directly with each other, creating a more interconnected and less hierarchical global trade network.

### China's Rise to Importance

Perhaps the most striking trend in the centrality analysis is China's degree centrality transformation. After experiencing a temporary setback in the late 1950s, China began a rapid ascent in degree centrality. By 2014, it had achieved the highest normalized degree centrality of any country, becoming the most "central" market in the global trade network. This development reflects not just the volume of China's trade, but the scope of its trading relationships across the globe.

This centrality analysis complements the other observations about node sizes, providing a more nuanced understanding of how countries' roles in global trade have evolved over time. While node sizes show the volume of trade, centrality measures reveal the structural importance of each country in the global trade network.

Likewise this is yet another important factor, showing how China overtook USA in trade already in the early 2010's and most likely have continued like that.


# References
[1] "East India Company and Raj 1785-1858." UK Parliament. Accessed May 2025. https://www.parliament.uk/about/living-heritage/evolutionofparliament/legislativescrutiny/parliament-and-empire/parliament-and-the-american-colonies-before-1765/east-india-company-and-raj-1785-1858/