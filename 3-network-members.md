---
title: Who we are
layout: page
description: 
image: assets/images/artic-meeting.jpg
nav_menu: true
show_tile: true
---

<!-- Main -->
<div id="main" class="alt">
	<!-- Content -->
	<section id="one">
		<div class="inner">
			<header class="major">
				<h1>Who we are</h1>
			</header>
		</div>
</section>

<section id="content" class="spotlights">
	<div class="inner">
		<div class="box alt">
			<div class="row 50% ">
				{% assign sortedTeam = site.people | sort: 'title' %}
				{% for page in sortedTeam %}
				{% assign mod = forloop.index | modulo: 5 %}
				{% if mod == 0 %}
					<div class="2u$"><span class="image fit">
				{% else %}
					<div class="2u"><span class="image fit">
				{% endif %}
					<figure class="imghvr-reveal-right"><img src="{{ page.image }}" alt=""/>
						<figcaption>
							<h4>{{ page.title }}</h4>
							<p>{{ page.description }}</p>
						</figcaption>
						<a href="{{ page.link }}"></a>
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
				<p>Follow the ARTIC BlueSky account to see what the team is up to</p>
				<ul class="actions">
					<li><a href="{{ site.bsky_url }}" class="button">visit BlueSky</a></li>
				</ul>
			</div>
		</div>
	</section>
</section>


