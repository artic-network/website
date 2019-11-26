# ARTIC Website

## How To Add Content

### Add a page using markdown

To add/edit a `post`, `workpackage` or `software` page, you just need to add a markdown file to the appropriate top-level directory of the same name.

One markdown file equates to one page on the site. Links to your new page will be added throughout the site.

Make sure the filename is in the format following format:

> YYYY-MM-DD-pagename.md

When adding a new page, you need to add some build tags to the top of your markdown file. Here are the allowed tags:

| tag         | choices                | explanation                                                                                         |
| ----------- | ---------------------- | --------------------------------------------------------------------------------------------------- |
| title       | free text              | the title to give the new page (will display on the page itself and in the links to the page)       |
| description | free text              | the decsription to give the new page (will display on the page itself and in the links to the page) |
| layout      | post/landing/home/page | how to structure the new page                                                                       |
| image       | free text              | file path to the image to tag this new page with                                                    |
| nav_menu    | true/flase             | display a link to the new page in the nav menu                                                      |
| show_tile   | true/flase             | display a tile to the new page on the homepage                                                      |
| permalink   | free text              | override the jekyll default web address for this page                                               |
| author      | free text              | your name (displayed alongside posts)                                                               |

You then use regular markdown, or html, to add content. Here is an example page:

```
---
title: RAMPART
description: description line
layout: post
image: assets/images/rampart-placeholder.jpg
nav_menu: false
show_tile: false
permalink: /rampart
---

## Introduction

Some content

## Methods

Some more content and a bullet list:

* item 1
* item 2
  * item 2a
  * item 2b

```

### Add images

If you need an image to go with any content (e.g. an image for the software tiles), please upload it to `assets/images`.

In terms of image sizing, there are some templates in `assets/images/templates`. They are labelled according to their purpose on the site. So, for a new software tile, make sure your image is similar in dimensions to `assets/images/templates/software-tile.jpg`.

### Add protocols

To collect all the protocols from the [protocols.io ARTIC group](https://www.protocols.io/groups/artic), clone the repo and run the python script:

```
python parse-protocols.py
```

This will add all the metadata for all the protcols from the ARTIC group to the `_protocols` directory. When you commit these files back to the repo, the site will populate the protocols page with thumbnails and links for each protocol.

***

## TODO

* keep working on getting the protocols.io api to work
* fill in the about page
* get a list of software - incl logos/imgs/screenshots
* fill in the workpackages
* do we want to host slide decks and photos etc.?

***

## Acknlowdgements

### Forty - Jekyll Theme

A Jekyll version of the "Forty" theme by [HTML5 UP](https://html5up.net/). Original README from HTML5 UP:

```
Forty by HTML5 UP
html5up.net | @ajlkn
Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)


This is Forty, my latest and greatest addition to HTML5 UP and, per its incredibly
creative name, my 40th (woohoo)! It's built around a grid of "image tiles" that are
set up to smoothly transition to secondary landing pages (for which a separate page
template is provided), and includes a number of neat effects (check out the menu!),
extra features, and all the usual stuff you'd expect. Hope you dig it!

Demo images* courtesy of Unsplash, a radtastic collection of CC0 (public domain) images
you can use for pretty much whatever.

(* = not included)

AJ
aj@lkn.io | @ajlkn


Credits:

	Demo Images:
		Unsplash (unsplash.com)

	Icons:
		Font Awesome (fortawesome.github.com/Font-Awesome)

	Other:
		jQuery (jquery.com)
		html5shiv.js (@afarkas @jdalton @jon_neal @rem)
		background-size polyfill (github.com/louisremi)
		Misc. Sass functions (@HugoGiraudel)
		Respond.js (j.mp/respondjs)
		Skel (skel.io)
```

### Jekyll port

The Jekyll port was made by [andrewbanchich](https://github.com/andrewbanchich/forty-jekyll-theme) and tweaked by [will-rowe](https://github.com/will-rowe).