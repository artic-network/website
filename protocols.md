---
title: Protocols
layout: post
description: View and download our protocols
image: assets/images/aerial-shot.jpg
nav_menu: true
---

All our protocols are accesible via the [protocols.io ARTIC group](https://www.protocols.io/groups/artic). Click on the thumbnails below to view and download a protocol:

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






