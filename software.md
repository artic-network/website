---
title: Software
layout: post
description: Check out our software
image: assets/images/minion.jpg
nav_menu: true
---

Intro to software here.

Underneath we will have a box per tool; each tool is collected from the `_software` directory

TODO: animate each panel on hover - give the name layover or something

<hr class="major" />

<h4>Software</h4>
<div class="box alt">
	<div class="row 50% uniform">
    	{% for page in site.software %}
	    {% assign mod = forloop.index | modulo: 3 %}
		{% if mod == 0 %}
			<div class="4u$"><span class="image fit">
		{% else %}
			<div class="4u"><span class="image fit">
		{% endif %}
			<figure class="imghvr-reveal-right"><img src="{{ page.image }}" alt=""/>
				<figcaption>
					<h3>{{ page.title }}</h3>
					<p>{{ page.description }}</p>
				</figcaption>
				<a href="{{ page.permalink }}"></a>
			</figure>
			</span></div>
        {% endfor %}
	</div>
</div>




