---
layout: page
title: Resources
description: Download stuff
show_tile: false
nav_menu: true
---

<!-- Main -->
<div id="main" class="alt">
	<!-- One -->
	<section id="one">
		<div class="inner">
			<header class="major">
				<h1>Resources</h1>
			</header>
			<!-- Elements -->
			<h2 id="elements">Slide Decks</h2>
			<div class="row 200%">
				<div class="6u 12u$(medium)">
					<!-- Text stuff -->
					<p>This is <b>bold</b> and this is <strong>strong</strong>. This is <i>italic</i> and this is <em>emphasized</em>.
					This is <sup>superscript</sup> text and this is <sub>subscript</sub> text.
					This is <u>underlined</u> and this is code: <code>for (;;) { ... }</code>.
					Finally, this is a <a href="#">link</a>.</p>

{% assign my_files = site.static_files | where: "file", true %}
{% for file in my_files %}
  <p>{{ file.path }}</p>
  <p>{{ file }}</p>
{% endfor %}

				</div>
				<div class="6u$ 12u$(medium)">
					<!-- Table -->
					<div class="table-wrapper">
						<table>
							<thead>
								<tr>
									<th>Name</th>
									<th>Description</th>
									<th>Price</th>
								</tr>
							</thead>
							<tbody>
								<tr>
									<td>Item1</td>
									<td>Ante turpis integer aliquet porttitor.</td>
									<td>29.99</td>
								</tr>
								<tr>
									<td>Item2</td>
									<td>Vis ac commodo adipiscing arcu aliquet.</td>
									<td>19.99</td>
								</tr>
								<tr>
									<td>Item3</td>
									<td> Morbi faucibus arcu accumsan lorem.</td>
									<td>29.99</td>
								</tr>
								<tr>
									<td>Item4</td>
									<td>Vitae integer tempus condimentum.</td>
									<td>19.99</td>
								</tr>
								<tr>
									<td>Item5</td>
									<td>Ante turpis integer aliquet porttitor.</td>
									<td>29.99</td>
								</tr>
							</tbody>
						</table>
					</div>
				</div>
			</div>
			<hr class="major" />

			<!-- Elements -->
			<h2 id="elements">Photos</h2>
			<div class="row 200%">
				<div class="6u 12u$(medium)">
					<!-- Text stuff -->
					<p>This is <b>bold</b> and this is <strong>strong</strong>. This is <i>italic</i> and this is <em>emphasized</em>.
					This is <sup>superscript</sup> text and this is <sub>subscript</sub> text.
					This is <u>underlined</u> and this is code: <code>for (;;) { ... }</code>.
					Finally, this is a <a href="#">link</a>.</p>
				</div>
				<div class="6u$ 12u$(medium)">
					<div class="box alt">
						<div class="row 50% uniform">
							<div class="4u"><span class="image fit"><img src="assets/images/stock-images/pic08.jpg" alt="" /></span></div>
							<div class="4u"><span class="image fit"><img src="assets/images/stock-images/pic09.jpg" alt="" /></span></div>
							<div class="4u$"><span class="image fit"><img src="assets/images/stock-images/pic10.jpg" alt="" /></span></div>
							<!-- Break -->
							<div class="4u"><span class="image fit"><img src="assets/images/stock-images/pic10.jpg" alt="" /></span></div>
							<div class="4u"><span class="image fit"><img src="assets/images/stock-images/pic08.jpg" alt="" /></span></div>
							<div class="4u$"><span class="image fit"><img src="assets/images/stock-images/pic09.jpg" alt="" /></span></div>
							<!-- Break -->
							<div class="4u"><span class="image fit"><img src="assets/images/stock-images/pic09.jpg" alt="" /></span></div>
							<div class="4u"><span class="image fit"><img src="assets/images/stock-images/pic10.jpg" alt="" /></span></div>
							<div class="4u$"><span class="image fit"><img src="assets/images/stock-images/pic08.jpg" alt="" /></span></div>
						</div>
					</div>
				</div>
			</div>

		</div>
	</section>
</div>
