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
				<h1>Ebola virus Nanopore sequencing resources</h1>
			</header>
			<blockquote>A collection of resources and documents for the genome sequencing of Ebola virus (EBOV) using Oxford Nanopore Technology's MinION platform. Includes a tiled primer scheme, complete lab protocol & equipement/reagent list.</blockquote>
			<h3>Background</h3>
			<p>The ongoing outbreak of <a href="http://www.who.int/emergencies/crises/cod/en/">Ebola virus in the Democratic Republic of Congo</a> has highlighted the need for rapid sequencing ability to help with source attribution and to aid epidemiological investigations (including environmental reservoirs).</p>
			<p>These documents and resources are provided in the spirit of Open Science, to foster collaboration and sharing, and to benefit public health response to outbreaks. All written material is provided under the <a href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution (BY) license</a> which allows unrestricted sharing and modification of the material as long as appropriate credit is given.</p>
			<p>We  encourage the modification, improvement and re-purposing of these methods and protocols (under the permissive terms of the CC BY license). We would be happy to host modifications on this website or encourage posting to Open Science platforms such as <a href="http://virological.org/">http://virological.org/</a>.</p>
			<p>We also ask that use of this resource is credited in publications or reports to allow us to report this impact to our funding bodies.</p>
			<h3>Resources and documents</h3>
			<ul>
			{% for doc in ebovDocs %}
				<li>{{ doc.title_text }}</li>
				<blockquote>link: <a href="{{ doc.permalink }}">{{ doc.permalink }}</a></blockquote>
			{% endfor %}
			</ul>
			<hr class="major"/>
			<header class="major">
				<h1>NCOV</h1>
			</header>
			<blockquote>A collection of...</blockquote>
			<h3>Background</h3>
			<p>Text to go here....</p>
			<h3>Resources and documents</h3>
			<ul>
			{% for doc in ncovDocs %}
				<li>{{ doc.title_text }}</li>
				<blockquote>link: <a href="{{ doc.permalink }}">{{ doc.permalink }}</a></blockquote>
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