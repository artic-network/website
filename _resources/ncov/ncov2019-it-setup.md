---
title: "nCoV-2019 novel coronavirus Nanopore sequencing protocol | amplicon, native barcoding"
keywords: protocol
layout: document
last_updated: Jan 22, 2020
tags: [protocol] 
permalink: /ncov-2019/ncov2019-it-setup.html
folder: ncov
title_text: "nCoV-2019 novel coronavirus bioinformatics environment setup"
subtitle_text: "Nanopore | bioinformatics"
document_name: "ARTIC-nCoV-ITSetup"
version: v1.0.0
creation_date: 2020-01-22
forked_from: 
author: Nick Loman, Andrew Rambaut
citation: "Loman *et al.* In Prep."
nav_menu: false
show_tile: false
category: ncov
---

{% include callout.html
type='default'
content='**Overview:** Instructions for setting up the laptop computing environment for running the MinION sequencer and performing the bioinformatics and downstream phylogenetic analyses.'
%}

<br />

This document is part of the nCoV-2019 Nanopore sequencing protocol package:
: [http://artic.network/ncov-2019](http://artic.network/ncov-2019)

#### Related documents:

nCoV-2019 Nanopore bioinformatics protocol:
: [http://artic.network/ncov-2019/ncov2019-bioinformatics-sop.html](http://artic.network/ncov-2019/ncov2019-bioinformatics-sop.html)

<br /><br />

{% include wellcome-trust.html %}

<div class="pagebreak"> </div>

## Preparation

#### Equipment required:

Laptop requirements for MinION:
: Intel i7 or Xeon processor
: 16GB RAM
: 1TB SSD hard drive
: USB 3
: Full Oxford Nanopore Technologies [lab and computing requirements are here](https://nanoporetech.com/sites/default/files/s3/MinION-Computer-Requirements-March-17_Final.pdf).

## Software Setup

These protocols instructions assume a 64-bit UNIX, Linux or similar environment. This could be Mac OS X (Yosemite or later), Linux (e.g., Ubuntu 16 or later), or Windows 10  Subsystem for Linux. It assumes familiarity with a UNIX-like *bash* command-line. 

The steps in this document should be done and tested prior to sequencing, particularly if this will be done in an environment without internet access or where this is slow or unreliable. Once this is done, the bioinformatics and phylogenetics protocols can be performed largely off-line. 

### Conda

Software will be installed using [Conda](https://conda.io/) -- a cross-platform package and dependency installer.
 
For Conda installation instructions for your operating system go to: [https://conda.io/docs/user-guide/install/](https://conda.io/docs/user-guide/install/). We suggest installing the `Miniconda` version which is relatively small and quick to install. 

> *NOTE:* Install the `64-bit Python 3.6` version of Miniconda

### Installing ARTIC nCoV-2019 specific data and software

Install the ARTIC nCoV-2019 data and software repository:

```bash
git clone --recursive https://github.com/artic-network/artic-ncov2019.git
```

Create a custom Conda environment for running software. This may take some time as it will install the required packages and all their dependencies.

```bash
conda env create -f artic-ncov2019/environment.yml
```

Although not strictly necessary this will prevent any conflicts with other similar software installed and can be readily removed. You can use this command to activate the environment: 

```
conda activate artic-ncov2019
```

and then deactivate it again using this:

```bash
conda deactivate
```

The artic environment can be removed using this:

```bash
conda remove --name artic-ncov2019 --all
```

### Installing Oxford Nanopore MinKNOW software

The software for running the MinION and basecalling can be downloaded from the [Oxford Nanopore Technologies Community site](https://community.nanoporetech.com). Log in to find the `Software Downloads` button. Download `MinKNOW` (currently v19.12.2) appropriate to the system being used. Follow the `Installation guide` for each package.

MinKNOW is a graphical user-interface programme that will be installed in the application area of the system.

