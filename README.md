# ARTIC Website

## How To

### Write content

if you want it in the nav menu -

if you want to hide it on the main page
```
---
layout: post
title: Protocols
image: assets/images/aerial-shot.jpg
nav-menu: true

layout: post
title: RAMPART
description: description line
image: assets/images/rampart-placeholder.jpg
show_tile: false
permalink: /rampart


layout: post
title: WP 1
description: work package one description here
image: assets/images/mantis.jpg
show_tile: false
permalink: work-package-1


layout: allposts
title: All posts
landing-title: 'All posts'
nav-menu: true
description: null
image: null
author: null
show_tile: false
---



content here
```

### Add images

If you need an image to go with any content (e.g. an image for the software tiles), please upload it to `assets/images`.

In terms of image sizing, there are some templates in `assets/images/templates`. They are labelled according to their purpose on the site. So, for a new software tile, make sure your image is similar in dimensions to `assets/images/templates/software-tile.jpg`.

### Add new piece of software to the resources page

It's easiest just to copy an existing a `*.md` file from the `_software` directory. Change the software name in the filename and edit the file contents.


## TODO

* animate the software panes

* keep working on getting the protocols.io api to work

* fill in the about page
* get a list of software - incl logos/imgs/screenshots
* fill in the workpackages
* do we want to host slide decks and photos etc.?


---

> UNDER THIS LINE IS THE ORIGINAL README

---

# Forty - Jekyll Theme

A Jekyll version of the "Forty" theme by [HTML5 UP](https://html5up.net/).  

# How to Use

For those unfamiliar with how Jekyll works, check out [jekyllrb.com](https://jekyllrb.com/) for all the details, 
or read up on just the basics of [front matter](https://jekyllrb.com/docs/frontmatter/), [writing posts](https://jekyllrb.com/docs/posts/), 
and [creating pages](https://jekyllrb.com/docs/pages/).

- **GitLab**: Simply fork this repository and start editing the `_config.yml` file!  
- **GitHub**: Fork this repository and create a branch named `gh-pages`, then start editing the `_config.yml` file.

# Added Features

* **[Formspree.io](https://formspree.io/) contact form integration** - just add your email to the `_config.yml` and it works!
* Use `_config.yml` to **set whether the homepage tiles should pull pages or posts**, as well as how many to display.
* Add your **social profiles** easily in `_config.yml`. Only social profiles buttons you enter in `config.yml` show up on the site footer!
* Set **featured images** in front matter.

# Issues

If you would like to report a bug, ask a question, request a feature, feel free to do so on [the GitLab repository](https://gitlab.com/andrewbanchich/forty-jekyll-theme) and I will be more than happy to help!

Alternatively, you can open an issue via email by emailing [incoming+andrewbanchich/forty-jekyll-theme@incoming.gitlab.com](mailto:incoming+andrewbanchich/forty-jekyll-theme@incoming.gitlab.com).

The GitHub repository is simply a mirror of the GitLab repository.

# Credits

Original README from HTML5 UP:

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

Repository [Jekyll logo](https://github.com/jekyll/brand) icon licensed under a [Creative Commons Attribution 4.0 International License](http://choosealicense.com/licenses/cc-by-4.0/).
