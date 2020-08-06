---
layout: post
title: How has the coronavirus impacted international travel from the UK?
date: 2020-08-03
category: makeover-monday
---

This #MakeoverMonday we're looking at publicly available travel statistics from the UK Office for National Statistics (ONS). Data is only available through March, but it shows the enormous impact of the coronavirus pandemic on international travel. <!--more-->

## 2020-08-03 #MakeoverMonday

## Data Cleaning and Preparation
The [original data](https://www.ons.gov.uk/peoplepopulationandcommunity/leisureandtourism/timeseries/gmax/ott) was in .xls format and it contained multiple aggregations (annual, quarterly, monthly) all listed together, so I used Python and [Pandas](https://pandas.pydata.org/) to clean and prepare the data.

The date column for the monthly travel data was in `1986 JAN` (YYYY MMM) format, and I was pleasantly surprised that `pd.to_datetime()` converted this with ease.

I wanted to see how international travel has grown on a per capita basis, so I pulled in [population data](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/timeseries/ukpop/pop) from the ONS to calculate the international trips per capita for UK residents.

My full code for data cleaning and preparation is on [Github](https://github.com/bbgatch/makeover-monday/blob/master/2020-08-03/clean-data.py).

## Results
### Coronavirus impact on international departures from UK
International trips from the UK dropped precipitously in March, down -37%. March last year was the high point in international trips at 8.3M and March this year saw 5.24M.

The month of March was only partially impacted as countries were realizing the extent of the spread, so April and May will likely show much more significant decline.

### Historical growth in international travel from the UK
On a brighter note, international trips from the UK have increased significantly over the past 34 years. In 1986 the average UK resident only took an international trip once every 2.5 years. In 2019 the average UK resident took 1.4 international trips a year, or one every 8.6 months.

While it will be a slow recovery for international travel, the desire for it was at an all-time high prior to the pandemic.


<div class='tableauPlaceholder' id='viz1596655190271' style='position: relative'><noscript><a href='http:&#47;&#47;localhost:4000&#47;makeover-monday&#47;2020&#47;08&#47;03&#47;mm-uk-visits-abroad.html'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ma&#47;MakeoverMonday2020-08-03UKVisitsAbroad&#47;UKVisitsAbroad&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='MakeoverMonday2020-08-03UKVisitsAbroad&#47;UKVisitsAbroad' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ma&#47;MakeoverMonday2020-08-03UKVisitsAbroad&#47;UKVisitsAbroad&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div> <script type='text/javascript'> var divElement = document.getElementById('viz1596655190271'); var vizElement = divElement.getElementsByTagName('object')[0]; if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='927px';} var scriptElement = document.createElement('script'); scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js'; vizElement.parentNode.insertBefore(scriptElement, vizElement); </script>


