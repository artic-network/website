---
title: Resources
layout: landing
description: A collection of Nanopore sequencing resources
image: assets/images/artic-meeting.jpg
nav_menu: true
show_tile: false
---

{% assign ebovDocs = site.resources | where_exp:"item", "item.category contains 'ebov'" | sort: 'title' %}
{% assign ncovDocs = site.resources | where_exp:"item", "item.category contains 'ncov'" | sort: 'title' %}

<section id="content" class="spotlights">
	<div class="inner">
			<header class="major">
				<h1>EBOV</h1>
			</header>
			<p>Some intro text on EBOV to go here.....</p>
			<ul>
			{% for doc in ebovDocs %}
				<li><a href="{{ doc.permalink }}">{{ doc.title }}</a></li>
			{% endfor %}
			</ul>
			<hr class="major"/>
			<header class="major">
				<h1>NCOV</h1>
			</header>
			<p>Some intro text on NCOV to go here.....</p>
			<ul>
			{% for doc in ncovDocs %}
				<li><a href="{{ doc.permalink }}">{{ doc.title }}</a></li>
			{% endfor %}
			</ul>
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
				<p>All our software is accesible via the GitHub ARTIC group</p>
				<ul class="actions">
					<li><a href="https://github.com/artic-network" class="button">visit GitHub</a></li>
				</ul>
			</div>
		</div>
	</section>
</section>