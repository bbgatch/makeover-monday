---
layout: post
title: Where are digital companies based in Scotland?
date: 2020-08-17
category: makeover-monday
---

Great Scott! This week's #MakeoverMonday looks at where digital companies are located in Scotland. <!--more-->

## 2020-08-17 #MakeoverMonday
## Original Visualization
Here's the original visualization that we're making over:

![Original Viz](\2020-08-17_original.jpg)

There are a few things we can do to clean up the visualization.

* Remove the colors from the circles, they aren't adding much to the visual. The main message is how the size of the circles differs.

* Remove the lines connecting the circles to the labels, we can simply adjust the labels to fit closer in.

* Let's be consistent about using "&" or "and" in labels.

## Recreated Viz

### Dual Axis Maps
I've opted for a larger map with overlaid circles representing the number of companies in each location. In order to do this we need to use dual-axis maps, and I found this Tableau Knowledge Base article very helpful: [Tableau Dual Axis Maps](https://help.tableau.com/current/pro/desktop/en-us/maps_dualaxis.htm)

### Matching Unknown Locations
I added an additional `Country` field to the data populated with "Scotland" so that Tableau could map the country. The `Region` field contains location names that most closely match to `County` in Tableau, and not all of the names match exactly.

I had to manually select Matching Locations for the unknown regions - this was an imperfect process as the `Region` field in the data contains some combinations of locations that Tableau has listed separately. For this visual, that is ok. If we wanted to be extra precise about where the labels are placed, we could add lat/long coordinates in the data.

![Matching Unknown Locations](\2020-08-17_edit-locations.png)

### Wrapping Labels
Some of the `Region` names are very long and make it difficult to fit the mark labels together on the map. Sadly, turning on "Wrap" in the Label Alignment does nothing.

I forced the labels with two names to wrap using the calculated field below. Big thanks to @dataunjaded's [blog](https://alanajade3.wixsite.com/dataunjaded/post/need-to-wrap-text-labels-in-tableau-just-press-enter) for the help on this wrapping calculated field.

```
// Only operates on labels with "&".
if contains([Region], "&") then

// Split on "& " and add in a new line between the two names.
split([Region], "& ", 1)
+ "&" +
'
'
+ split([Region], "& ", 2)

else Region
end
```

### Final Viz:
<div class='tableauPlaceholder' id='viz1598389189147' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;sc&#47;scotland-digital-companies&#47;DigitalCompaniesinScotland&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='scotland-digital-companies&#47;DigitalCompaniesinScotland' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;sc&#47;scotland-digital-companies&#47;DigitalCompaniesinScotland&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div> <script type='text/javascript'> var divElement = document.getElementById('viz1598389189147'); var vizElement = divElement.getElementsByTagName('object')[0]; vizElement.style.width='600px';vizElement.style.height='1027px'; var scriptElement = document.createElement('script'); scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js'; vizElement.parentNode.insertBefore(scriptElement, vizElement); </script>

<br>

Thanks to [tailorbrands.com](https://www.tailorbrands.com/blog/logo-color-combinations) for the color inspiration. 