---
title: Protocols
layout: landing
description: View and download our protocols
image: assets/images/aerial-shot.jpg
nav_menu: true
---

<section id="content" class="spotlights">
		<div class="inner">
			<div class="box alt">
				<div class="row 50% uniform">
					{% for protocol in site.protocols %}
					{% assign mod = forloop.index | modulo: 3 %}
					{% if mod == 0 %}
						<div class="4u$">
					{% else %}
						<div class="4u">
					{% endif %}
							<iframe src="https://www.protocols.io/widgets/protocol/{{ protocol.uri }}"  style="width: 100%; height: 100%;"></iframe>
						</div>
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
				<p>All our protocols are accesible via the protocols.io ARTIC group</p>
				<ul class="actions">
					<li><a href="https://www.protocols.io/groups/artic" class="button">visit protocols.io</a></li>
				</ul>
			</div>
		</div>
	</section>
</section>










