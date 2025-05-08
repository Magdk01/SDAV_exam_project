---
layout: story
title: "Understanding the Data"
subtitle: "A Deep Dive into Historical Trade Data Quality"
previous_story: 
next_story: trade-volumes
next_story_title: "Trade Volumes"
---


# Data source

To give the reader a understanding on the basis for this slideshow narrative diving into the development of global trade, this page tries to explain the data source as well as its shortcomings.

The data originates from the [Correlates of War](https://correlatesofwar.org/) International Trade dataset (v4.0), which covers bilateral trade flows from 1870-2014 [1,2].

Important for understanding the data, is that it is primarily a attempt to calculate the import and export between all countries since 1870. Of cause this is not without difficulties, and that is also why the dataset itself has been iterated several times, while still having short comings.

However the authors were great at listing the difficulties as different source codes in the data, which combined with the correct data, allowed creating the summary below:

<iframe src="../visualizations/data_quality_analysis.html" width="100%" height="1100px" frameborder="0"></iframe>

*Figure 1: Analysis of data quality and completeness in the Correlates of War International Trade dataset (1870-2014). The visualization shows the distribution of data sources, error types, and completeness metrics over time.*

The most important takeaway from these plots is that data become much more available in later years, as more and more countries begang properly participating in global trade, as well as having a proper way of tracking it. This is visable from both of the upper row plots, whereas the left-most plot also shows that, with increasing amount of data, there are also room for far more errors and issues. This is however less dire compared to the early years of the dataset, where there is more incomplete data, than later years.

This may seem counterintuitive, but comparing with the source code distribution shows that one of the major problems is simply missing data. Since the dataset attempts to map trade between any two countries that have any data in a given year, there will naturally be many empty entries when countries didn't trade. As such, the earlier years' data completeness is greatly affected by smaller trading communities - which is also visible in the [network analysis]({{ site.baseurl }}/stories/network-analysis) page.
Thus, you can discuss what if the missing data entries are actually incompletness or simply a quirk of the data structuring. Nevertheless, these entries of data was removed from the overall dataset, corresponding to a significant portion of the overall rows; as also seen from the "Data Quality Metrics" plot.



You might also notice that the majority of the source codes are "IMF import reports (2015)". This is not counted as an error, but rather indicates that entries in the dataset have been updated using the then-new IMF report.

These explanations and many more detailed data collection methodologies can be found in the dataset's comprehensive data cookbook [1].



# References
[1] Barbieri, Katherine and Omar M. G. Omar Keshk. 2016. Correlates of War Project Trade Data Set Codebook, Version 4.0. Online: https://correlatesofwar.org.

[2] Barbieri, Katherine, Omar M. G. Keshk, and Brian Pollins. 2009. "TRADING DATA: Evaluating our Assumptions and Coding Rules." Conflict Management and Peace Science. 26(5): 471-491.