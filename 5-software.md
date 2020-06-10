---
title: Software
layout: page
description: Check out our software
image: assets/images/rampart-screenshot.jpg
nav_menu: true
---


<!-- Main -->
<div id="main" class="alt">
	<!-- Content -->
	<section id="one">
		<div class="inner">
			<header class="major">
				<h1>Open source software</h1>
			</header>
		</div>
</section>

<section id="content" class="spotlights">
	<div class="inner">
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
				<p>All our software is accesible via the GitHub ARTIC group</p>
				<ul class="actions">
					<li><a href="https://github.com/artic-network" class="button">visit GitHub</a></li>
				</ul>
			</div>
		</div>
	</section>
</section>


