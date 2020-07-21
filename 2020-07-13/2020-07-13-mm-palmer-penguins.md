---
layout: post
title: When do palmer penguins lay their eggs?
date: 2020-07-13
category: makeover-monday
---

# 2020-07-13 #MakeoverMonday

For my very first #MakeoverMonday I'm keeping it simple and looking at how egg laying differs across the three different species of penguins.

Adelie penguins lay their eggs around mid-November, Chinstraps in the latter-half of November, and Gentoos throughout November but somewhat bimodal at the beginning and end of the month. It's easiest to see the distribution of Gentoo egg laying by filtering out the other two species in the dashboard below.

The only backend work needed to make this visualization was a simple `Unique ID` calculated field to give an identifier for each row. The data includes three different `Study Name`s and many penguin `Individual ID`s were included in multiple studies, so we need to combine them for a unique key.

```
Unique ID = [Study Name] + [Individual ID]
```

<div class='tableauPlaceholder' id='viz1595285027266' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pa&#47;palmer-penguins&#47;egg-laying-timeline&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='palmer-penguins&#47;egg-laying-timeline' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pa&#47;palmer-penguins&#47;egg-laying-timeline&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div><script type='text/javascript'> var divElement = document.getElementById('viz1595285027266'); var vizElement = divElement.getElementsByTagName('object')[0]; if ( divElement.offsetWidth > 800 ) { vizElement.style.width='900px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='900px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='727px';} var scriptElement = document.createElement('script'); scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js'; vizElement.parentNode.insertBefore(scriptElement, vizElement);</script>

