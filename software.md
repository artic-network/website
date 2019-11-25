---
layout: post
title: Software
description: Check out our software
image: assets/images/minion.jpg
nav-menu: true
---

Intro to software here.

Underneath we will have a box per tool; each tool is collected from the `_software` directory

TODO: animate each panel on hover - give the name layover or something



<h4>Software</h4>
<div class="box alt">
	<div class="row 50% uniform">
    	{% for page in site.software %}
            <div class="4u"><span class="image fit"><a href="{{ page.permalink }}"><img src="{{ page.image }}" alt="" /></a></span></div>
        {% endfor %}

		<div class="4u"><span class="image fit"><img src="assets/images/pic08.jpg" alt="" /></span></div>
		<div class="4u"><span class="image fit"><img src="assets/images/pic09.jpg" alt="" /></span></div>
		<div class="4u"><span class="image fit"><img src="assets/images/pic10.jpg" alt="" /></span></div>
		<!-- Break -->
		<div class="4u"><span class="image fit"><img src="assets/images/pic10.jpg" alt="" /></span></div>
		<div class="4u"><span class="image fit"><img src="assets/images/pic08.jpg" alt="" /></span></div>
	</div>
</div>