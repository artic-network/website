---
title: "Setting up and using EPI2ME for MPXV analysis pipelines | EPI2ME"
keywords: protocol
layout: document
last_updated: 2024-08-22
tags: [protocol]
summary:
permalink: /mpxv/mpxv-epi2me-setup.html
folder: mpxv
title_text: "Setting up and using EPI2ME for MPXV analysis pipelines"
subtitle_text: "ARTIC pipelines | bioinformatics"
document_name: "ARTIC-MPXV-EPI2ME-Setup"
version: v1.0
creation_date: 2024-08-22
revision_date: 
forked_from: 
author: Lauren Lansdowne, Andrew Rambaut
citation: 
nav_menu: false
show_tile: false
category: mpxv-setup
---

{% include callout.html
type='default'
content="**Overview:** This document walks-through how to install and setup Oxford Nanopore Technology's EPI2ME software package so that it can be used to run ARTIC bioinformatics pipelines on a Desktop or Laptop computer without having to use a command-line interface. This document is part of the MPXV sequencing protocol package <a href='http://artic.network/mpxv'>http://artic.network/mpxv </a>"
%}

**Requirements:**

* The ability to install software on your desktop or laptop. This includes some extra packages like Java and Docker that may require administrator level privileges.   
* Internet access when first downloading each pipeline, and for the first time running it. After that, you should be able to run it offline.

---

## Installing the EPI2ME software

EPI2ME is a standard desktop software package available for Windows, Macintosh and Linux operating systems and is used to run 'NextFlow' pipelines in a simple easy-to-use environment without interacting with a command-line. It can be obtained from the EPI2ME website --- [https://labs.epi2me.io]() --- with downloads for each operating system available from the download page:

> [https://labs.epi2me.io/downloads/](https://labs.epi2me.io/downloads/)

Once you have downloaded the appropriate installer for your operating system, install it in the usual way.

## Initial setup of EPI2ME

When you run EPI2ME it will ask if you want to sign-up or sign-in to the Cloud-based service --- you can just click the `Continue without signing in` button.                               

The first time you run EPI2ME it may need to install some additional software. It will guide you through this process.

<img width="500" src="/assets/images/mpxv/epi2me-install/screenshot1.png" alt=""> 
                      
If you see a panel that says `Additional setup is required` then select it:

<img width="500" src="/assets/images/mpxv/epi2me-install/screenshot2.png" alt=""> 

You may need to install the `NextFlow` software and `Java` - in which case click the `Setup` button:

<img width="500" src="/assets/images/mpxv/epi2me-install/screenshot3.png" alt=""> 

Then click `Continue ->`. Unless it has already been installed it will next ask you to install the `Docker` software. Click on the link to `Docker Desktop Install` and follow the instructions there to install `Docker`:

<img width="500" src="/assets/images/mpxv/epi2me-install/screenshot3c.png" alt=""> 

When it says `Docker is ready`, click `Finish`. The EPI2ME window will now look like this:

<img width="500" src="/assets/images/mpxv/epi2me-install/screenshot4.png" alt=""> 

You are now ready to install an analysis pipeline in EPI2ME.

---

## Using an ARTIC analysis pipeline in EPI2ME

### **Import the workflow**

Open EPI2ME. On the main dashboard select “View workflows”.

<img width="500" src="/assets/images/mpxv/ont-sop/screenshot_1.png" alt="">
  
Then select “Import workflow”.

<img width="500" src="/assets/images/mpxv/ont-sop/screenshot_2.png" alt="">

A pop-up window will appear where you can enter the GitHub URL. Enter the URL and click “Download” --- the exact URL will depend on the pipeline you wish to install. For example, to install the ARTIC bioinformatics pipeline for nanopore sequence data use [`https://github.com/artic-network/artic-mpxv-nf`](https://github.com/BioWilko/artic-mpxv-nf) (details about running this pipeline can be [found here](/mpxv/mpxv-ont-epi2me-sop.html)):

<img width="500" src="/assets/images/mpxv/ont-sop/screenshot_3.png" alt="">

Once it has downloaded, it will be ready in the `Installed` tab:

<img width="500" src="/assets/images/mpxv/ont-sop/screenshot_4a.png">

Select it and you will be taken to a landing page for this workflow.

## Software credits

This resource depends on the [EPI2ME](https://labs.epi2me.io) desktop software provided by Oxford Nanopore Technologies.
The pipeline is written in [Nextflow](https://www.nextflow.io/) and relies on [Docker containers](https://hub.docker.com/).

## Running a pipeline

For instructions on running individual ARTIC pipelines in EPI2ME see the [list of documents here](/mpxv/resources).

---

{% include callout.html
type='default'
content="This document is part of the MPXV sequencing protocol package: [http://artic.network/mpxv](http://artic.network/mpxv)"
%}

<br /><br />

{% include wellcome-trust.html %}
<br />

<div class="pagebreak"> </div>
