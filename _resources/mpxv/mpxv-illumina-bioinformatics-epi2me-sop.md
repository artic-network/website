---
title: "Running a bioinformatics pipeline for Illumina data using EPI2ME | bioinformatics"
keywords: protocol
layout: document
last_updated: 2024-08-22
tags: [protocol]
summary:
permalink: /mpxv/mpxv-illumina-epi2me-sop.html
folder: mpxv
title_text: "Running a bioinformatics pipeline for Illumina data using EPI2ME"
subtitle_text: "ARTIC pipelines | bioinformatics"
document_name: "ARTIC-MPXV-Illumina-bioinformatics-EPI2ME-SOP"
version: v1.0
creation_date: 2024-08-22
revision_date: 
forked_from: 
author: Lauren Lansdowne
citation: 
nav_menu: false
show_tile: false
category: mpxv-epi2me
---

{% include callout.html
type='default'
content="**Overview:** This document walks-through how to install and run a bioinformatics pipeline for analysing Illumina data generated from the ARTIC amplicon protocol within the ONT EPI2ME desktop software."
%}
## Background

Nextflow Pipeline created by:

**Requirements:**

* A working installation of EPI2ME. For instructions for installing EPI2ME, [see this document](/mpxv/mpxv-epi2me-setup.html).   
* Internet access to download the pipeline, and for the first time running it. After that, you should be able to run it offline.
* Details about how the data was generated including the primer scheme used.

---

### **Import the workflow**

Open EPI2ME. On the main dashboard select “View workflows”.  
![][image1]

Then select “Import workflow”.

![][image2]

A pop-up window will appear where you can enter the GitHub URL. Enter the URL and click “Download” ([https://github.com/artic-network/artic-mpxv-illumina-nf](https://github.com/artic-network/artic-mpxv-illumina-nf) ):

![][image3]

Once it has downloaded, it will be ready in the Available Workflows tab. Select it and you will be taken to a landing page for this workflow.

### **Running the workflow**

From the workflow landing page, click “Run this workflow”.

![][image4]

Then select “Run on your computer” and click “Continue”.

![][image5]

It will then ask you to select your fastq folders under the tab ‘Input Options’. Select the ones you want to analyse.

![][image6]

Go to the Primer Scheme Selection tab and **make sure that the primer scheme matches the one you used**. If your scheme is not listed, you can use the “Custom scheme” section to provide the full path to the directory containing your appropriately named scheme bed and fasta files; \<SCHEME\_NAME\>.bed and \<SCHEME\_NAME\>.fasta.

![][image7]

Go to the ‘Output Options’ tab and select your desired output folder, and the prefix you want for your output files.

![][image8]

The ‘Advanced Options’ have been set to defaults which are suitable for most cases, but can be changed if you wish.

Once you have selected everything you need, click ‘Launch workflow’.

It will then start running. The runtime will depend on the size of your files and the speed of your computer, but \>30 minutes is common. While it is running you will see a series of progress bars, and at the top a blue ‘Running’ icon. This will change to green and ‘Complete’ when it has finished.

![][image9]  
![][image10]

Fasta files can be found in the output alignConsensusToReference folder.

## Advanced Options

### **Changing the pipeline version**

If you need to use a previous or a development version of the pipeline, this can be selected from the workflow landing page.

---

## Related documents:

This pipeline can also be run in a command-line environment. [See this document for detailed instructions for doing this](https://artic.network/mpxv/mpxv-bioinformatics-sop.html).

This document is part of the MPXV sequencing protocol package:
: [http://artic.network/mpxv](http://artic.network/mpxv)

<br /><br /><br />

{% include wellcome-trust.html %}
<br />

<div class="pagebreak"> </div>