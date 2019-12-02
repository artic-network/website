---
title: Activities
layout: landing
description: Explore what we are up to
image: assets/images/artic-meeting.jpg
nav_menu: true
---

<!-- Main -->
<div id="main">

<!-- One 
<section id="one">
	<div class="inner">
		<header class="major">
			<h2>Overview</h2>
		</header>
		<p>overview text here</p>
	</div>
</section>
-->

<!-- Two -->
<section id="content" class="spotlights">
{% for item in site.activities %}
	<section>
		<a href="wp1.html" class="image">
			<img src="assets/images/mantis.jpg" alt="" data-position="center center" />
		</a>
		<div class="content">
			<div class="inner">
				<header class="major">
					<h3>{{ item.title }}</h3>
				</header>
				<p>{{ item.description}}</p>
				<ul class="actions">
					<li><a href="{{ item.permalink }}" class="button">Learn more</a></li>
				</ul>
			</div>
		</div>
	</section>
{% endfor %}
</section>

<!-- Three 
<section id="three">
	<div class="inner">
		<header class="major">
			<h2>Massa libero</h2>
		</header>
		<p>Nullam et orci eu lorem consequat tincidunt vivamus et sagittis libero. Mauris aliquet magna magna sed nunc rhoncus pharetra. Pellentesque condimentum sem. In efficitur ligula tate urna. Maecenas laoreet massa vel lacinia pellentesque lorem ipsum dolor. Nullam et orci eu lorem consequat tincidunt. Vivamus et sagittis libero. Mauris aliquet magna magna sed nunc rhoncus amet pharetra et feugiat tempus.</p>
		<ul class="actions">
			<li><a href="generic.html" class="button next">Get Started</a></li>
		</ul>
	</div>
</section>
-->

</div>
