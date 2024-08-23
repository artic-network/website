---
title: "Setting up and using EPI2ME for ARTIC pipelines | EPI2ME"
keywords: protocol
layout: document
last_updated: 2024-08-22
tags: [protocol]
summary:
permalink: /mpxv/mpxv-ont-epi2me-sop.html
folder: mpxv
title_text: "Running the ARTIC MPXV analysis pipelines using EPI2ME"
subtitle_text: "ARTIC pipelines | bioinformatics"
document_name: "ARTIC-MPXV-EPI2ME-Setup"
version: v1.0
creation_date: 2024-08-22
revision_date: 
forked_from: 
author: Lauren Lansdowne
citation: 
nav_menu: false
show_tile: false
category: mpxv-setup
---

{% include callout.html
type='default'
content="**Overview:** This document walks-through how to install and setup Oxford Nanopore Technology's EPI2ME software package so that it can be used to run ARTIC bioinformatics pipelines on a Desktop or Laptop computer without having to use a command-line interface."
%}

**Requirements:**

* The ability to install software on your desktop or laptop. This includes some extra packages like Java and Docker that may require administrator level privileges.   
* Internet access to download the pipeline, and for the first time running it. After that, you should be able to run it offline.
* Details about how the data was generated including the primer scheme used and the base-caller specified within the MinKNOW software.

---

## Installing the EPI2ME software

EPI2ME is a standard desktop software package available for Windows, Macintosh and Linux operating systems and is used to run 'NextFlow' pipelines in a simple easy-to-use environment without interacting with a command-line. It can be obtained from the EPI2ME website --- [https://labs.epi2me.io]() --- with downloads for each operating system available from the download page:

> [https://labs.epi2me.io/downloads/](https://labs.epi2me.io/downloads/)

Once you have downloaded the appropriate installer for your operating system, install it in the usual way.

## Initial setup of EPI2ME

The first time you run EPI2ME it may need to install some additional software. It will guide you through this process.

## Using an ARTIC MPXV analysis pipeline in EPI2ME

## ---

### **Import the workflow**

Open EPI2ME. On the main dashboard select “View workflows”.

<img width="500" src="/assets/images/mpxv/ont-sop/screenshot_1.png">
  
Then select “Import workflow”.

<img width="500" src="/assets/images/mpxv/ont-sop/screenshot_2.png">

A pop-up window will appear where you can enter the GitHub URL. Enter the URL and click “Download” ([https://github.com/artic-network/artic-mpxv-nf](https://github.com/BioWilko/artic-mpxv-nf)):

<img width="500" src="/assets/images/mpxv/ont-sop/screenshot_3.png">
 
Once it has downloaded, it will be ready in the Available Workflows tab. Select it and you will be taken to a landing page for this workflow.

### **Running the workflow**

From the workflow landing page, click “Run this workflow”.

<img width="500" src="/assets/images/mpxv/ont-sop/screenshot_4b.png">

Then select “Run on your computer” and click “Continue”.

<img width="500" src="/assets/images/mpxv/ont-sop/screenshot_5.png">

It will then ask you to select your fastq folders. Select the ones you want and continue.  

<img width="500" src="/assets/images/mpxv/ont-sop/screenshot_6.png">

Go to the Primer Scheme Selection tab and **make sure that the primer scheme matches the one you used**. If your scheme is not listed, you can use the “Custom scheme” section to provide the full path to the directory containing your appropriately named scheme bed and fasta files; \<SCHEME\_NAME\>.bed and \<SCHEME\_NAME\>.fasta.

<img width="500" src="/assets/images/mpxv/ont-sop/screenshot_7.png">

Finally click “Launch workflow”. It will then start running. The runtime will depend on the size of your files and the speed of your computer, but 10-30 minutes is common. While it is running you will see a series of progress bars, and at the top a blue ‘Running’ icon. This will change to green and ‘Complete’ when it has finished.

<img width="500" src="/assets/images/mpxv/ont-sop/screenshot_8.png">

When it has finished you will have a collection of outputs for both consensus and individual barcodes.

## Advanced Options

### **Changing the pipeline version**

If you need to use a previous or a development version of the pipeline, this can be selected from the workflow landing page.

<img width="500" src="/assets/images/mpxv/ont-sop/screenshot_9a.png">
<img width="500" src="/assets/images/mpxv/ont-sop/screenshot_9b.png">

### **Changing the basecaller**

Medaka runs within the pipeline to call variants between the reads provided and the reference. It will try to auto-select. If it is unable to auto-select (for example if your data was basecalled with a version of MinKNOW which is no longer supported) you may need to choose an option from this drop down list of available models in “Advance Options” (scroll down).

<img width="500" src="/assets/images/mpxv/ont-sop/screenshot_10.png">

**We recommend you use a supported version of MinKNOW**. As a work around, you should select an option from this list of models which matches the flowcell chemistry and sequencing speed.

{% include wellcome-trust.html %}

<div class="pagebreak"> </div>
