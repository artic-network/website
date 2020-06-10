---
title: Resources
layout: page
description: A collection of Nanopore sequencing resources
image: assets/images/lab-in-a-suitcase.jpg
nav_menu: true
show_tile: true
---

<!-- Main -->
<div id="main" class="alt">
	<!-- Content -->
	<section id="one">
		<div class="inner">
			<header class="major">
				<h1>Resources</h1>
				<h3 id="content">A collection of Nanopore sequencing resources</h3>
			</header>
		</div>
</section>

<section id="content" class="spotlights">
	<div class="inner">
		<div class="box alt">
			<div class="row 50% uniform">
				{% assign resources = site.resources | where_exp:"item", "item.category contains 'menu'" | sort: 'title' %}
				{% for page in resources %}
				{% assign mod = forloop.index | modulo: 3 %}
				{% if mod == 0 %}
					<div class="4u$"><span class="image fit">
				{% else %}
					<div class="4u"><span class="image fit">
				{% endif %}
					<figure class="imghvr-reveal-right"><img src="{{ page.image }}" alt=""/>
						<figcaption>
							<h2>{{ page.title }}</h2>
							<!-- <p>{{ page.description }}</p> -->
						</figcaption>
						<a href="{{ page.permalink }}"></a>
					</figure>
					</span></div>
				{% endfor %}
			</div>
		</div>
	</div>
	<section>
		<!-- <a href="wp1.html" class="image">
			<img src="assets/images/mantis.jpg" alt="" data-position="center center" />
		</a> -->
		<div class="content">
			<div class="inner">
				<header class="major">
						<h1>Find out more</h1>
				</header>
				<p>Follow the ARTIC twitter account to see what the team is up to</p>
				<ul class="actions">
					<li><a href="{{ site.twitter_url }}" class="button">visit Twitter</a></li>
				</ul>
			</div>
		</div>
	</section>
</section>


