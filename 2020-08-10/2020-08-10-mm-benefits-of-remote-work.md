---
layout: post
title: What are the top benefits of remote work?
date: 2020-08-10
category: makeover-monday
---

The coronavirus pandemic has quickly made remote work a new reality for many, and this week's #MakeoverMonday looks at what the top-ranked benefits of remote work are. <!--more-->

## 2020-08-10 #MakeoverMonday
## Data Cleaning and Preparation
This week's data requires essentially no preparation or cleaning; it's just the aggregated results of a survey question.

I joked on Twitter:
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">They say 80% of a data scientist&#39;s time is spent on data prep. That is not the case for this week&#39;s <a href="https://twitter.com/hashtag/MakeoverMonday?src=hash&amp;ref_src=twsrc%5Etfw">#MakeoverMonday</a>. 😁 <a href="https://t.co/XtBZ057Ka7">pic.twitter.com/XtBZ057Ka7</a></p>&mdash; Ben (@bbgatch) <a href="https://twitter.com/bbgatch/status/1292844749322440706?ref_src=twsrc%5Etfw">August 10, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

Because the data is simple, I wanted to focus more on using graphic elements that I don't typically use like shaded backgrounds and bold colors and graphics. Thanks to [designwizard.com](https://www.designwizard.com/blog/design-trends/colour-combination) for the inspiration on what colors to try out.

## Stacked Bar Chart
The original #MakeoverMonday visualization is a stacked bar chart, and initially I followed the same approach:

![Initial Stacked Bar Chart](\assets\images\makeover-monday\2020-08-10_initial-chart.png)

One thing that these #MakeoverMonday exercises have allowed me to focus on is how vizzes perform on different screens. I want to make sure that the viz is easily viewable from a phone or tablet.

The stacked bar chart had three issues:
* It didn't scale down well to smaller screen sizes. The bar stays centered in the page, so when viewed on a phone it's almost completely cutoff.
* The mark labels don't wrap, so on a small screen almost all of the labels were cut off. There are probably workarounds to this, but workarounds add extra complexity.
* I was surprised to learn that mark labels on vertical stacked bars can't be aligned *vertically*. The mark label alignment can be changed horizontally from left to right, but not vertically. I wanted to move the labels to the top left of each section, but that's not possible - it would have to be done manually.
    * The same idea is true for horizontal stacked bars. A mark label's alignment can be moved *vertically* but not horizontally.
    * See this knowledge base article: https://kb.tableau.com/articles/issue/Label-Alignment-on-Stacked-Bar-Chart-Not-Applied

## Standard Horizontal Bar Chart
To keep things easily visible on mobile devices I switched to a regular horizontal bar chart. The label text wraps nicely and the viz adjusts well to different screen sizes.

The benefit of the *stacked* bar chart is that it quickly conveys our results are percentages out of 100%. The user could quickly comprehend that the top two choices represent over half of the responses, for example.

I'm ok to lose that benefit in this case. The horizontal bar chart still clearly conveys the top responses to the question, and my main goal is to create a bold, striking visual.

<div class='tableauPlaceholder' id='viz1597085382499' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;re&#47;remote-work&#47;RemoteWork&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='remote-work&#47;RemoteWork' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;re&#47;remote-work&#47;RemoteWork&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div> <script type='text/javascript'> var divElement = document.getElementById('viz1597085382499'); var vizElement = divElement.getElementsByTagName('object')[0]; if ( divElement.offsetWidth > 800 ) { vizElement.style.width='600px';vizElement.style.height='1027px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='600px';vizElement.style.height='1027px';} else { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*1.77)+'px';} var scriptElement = document.createElement('script'); scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js'; vizElement.parentNode.insertBefore(scriptElement, vizElement); </script>




