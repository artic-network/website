---
title: Team Members
layout: landing
description: Find out who's part of the network
image: assets/images/artic-meeting.jpg
nav_menu: true
show_tile: false
---

<section id="content" class="spotlights">
	<div class="inner">
		<div class="box alt">
			<div class="row 50% uniform">
				{% assign sortedTeam = site.people | sort: 'title' %}
				{% for page in sortedTeam %}
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
						<a href="{{ page.link }}"></a>
					</figure>
					</span></div>
				{% endfor %}
			</div>
		</div>
	</div>
	<section>
		<a href="wp1.html" class="image">
			<img src="assets/images/mantis.jpg" alt="" data-position="center center" />
		</a>
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


