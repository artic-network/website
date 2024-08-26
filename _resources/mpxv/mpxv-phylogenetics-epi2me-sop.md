---
title: "MPXV alignment and phylogenetics protocol | Squirrel"
keywords: protocol
layout: document
last_updated: 2024-08-26
tags: [protocol]
summary:
permalink: /mpxv/mpxv-phylogenetics-epi2me-sop.html
folder: mpxv
title_text: "Running the MPXV alignment and phylogenetics pipeline using Epi2Me"
subtitle_text: "Squirrel | phylogenetics"
document_name: "ARTIC-MPXV-squirrel-EPI2ME-SOP"
version: v1.0
creation_date: 2024-08-21
revision_date: 
forked_from: 
author: Áine O'Tool, Rachel Colquhoun
citation: https://github.com/aineniamh/squirrel
nav_menu: false
show_tile: false
category: mpxv-epi2me
---

{% include callout.html
type='default'
content='**Overview:** A complete protocol to take the output consensus genome sequences from the [sequencing protocol](/mpxv/mpxv-seq-sop.html) to a robust, interpretable phylogenetic tree with APOBEC3-editing reconstruction. Includes background dataset, alignment, maximum likelihood phylogenetics and ancestral reconstruction with IQTREE, figure generation and interpretation.

This document is part of the Mpox virus (MPXV) sequencing protocol package: [http://artic.network/mpxv](http://artic.network/mpxv)'
%}

### Credits / Acknowledgements

This workflow runs the [Squirrel pipeline](https://github.com/aineniamh/squirrel) written by [Áine O'Toole](https://github.com/aineniamh). Squirrel itself makes use of a number of open-source software packages, including [minimap2](https://academic.oup.com/bioinformatics/article/34/18/3094/4994778),  [gofasta](https://academic.oup.com/bioinformatics/article/38/16/4033/6631223) and [IQTREE2](https://doi.org/10.1093/molbev/msaa015), in addition to custom code for APOBEC3 analysis.

---

## Using the Squirrel MPXV phylogenetic analysis pipeline in EPI2ME

**Requirements:**

* A working installation of EPI2ME. For instructions for installing EPI2ME, [see this document](/mpxv/mpxv-epi2me-setup.html).
* Internet access to download the pipeline, and for the first time running it. After that, you should be able to run it offline.
* Details about how the data was generated including the primer scheme used and the base-caller specified within the MinKNOW software.


### Rationale
MPXV is a large poxvirus, with a complex dsDNA genome ~200kb in length. Alignment of sequences, and therefore phylogenetics, is challenging using classic due to tracts of low-complexity and repetitive regions. Squirrel provides an efficient map-to-reference alignment pipeline with masking of problematic regions of the genome. Full details of the pipeline and workflow can be found [here](#pipeline-description).

### Command line
Squirrel can be used as a command line tool, with full command-line documentation available on the squirrel GitHub repository at (github.com/aineniamh/squirrel)[https://github.com/aineniamh/squirrel].

### EPI2ME user interface
Squirrel can also be run through the [EPI2ME](https://labs.epi2me.io/downloads/) user interface. Please first install the EPI2ME desktop application using the provided link. You can then go to 'available workflows' then 'Import workflow' from [`https://github.com/artic-network/squirrel-nf`](https://github.com/artic-network/squirrel-nf) as shown below:

<img width="500" alt="link" src="/assets/images/mpxv/phylogenetics-sop/screen_shot_1.png">

Once the workflow has successfully downloaded, you can click the X to exit to download window, and select it from the list of available workflows. Next select `Run this workflow` from the available options, and then `Run on your computer`:

<img width="500" alt="launch" src="/assets/images/mpxv/phylogenetics-sop/screen_shot_2.png">
<img width="500" alt="run" src="/assets/images/mpxv/phylogenetics-sop/screen_shot_3.png">

This will bring up a menu where you can provide the inputs for your analysis. The only required file is a single FASTA file containing all the sequences and outgroups for your analysis and you must also select the clade (i or ii) from the drop down list:

<img width="500" alt="fasta" src="/assets/images/mpxv/phylogenetics-sop/screen_shot_4.png">

<img width="500" alt="clade" src="/assets/images/mpxv/phylogenetics-sop/screen_shot_5.png">

Running with just a FASTA file will generate an alignment of the input sequences. We recommend selecting the check box for `Seq QC` to check this alignment for problematic sites. 

<img width="500" alt="seqqc" src="/assets/images/mpxv/phylogenetics-sop/screen_shot_6.png">

Scrolling down the menu, select the box to `Run Phylo`. At this point you have 2 options. EITHER you can select the check box to `Include Background`, in which case a default panel of clade-specific outgroups sequences will be used.

<img width="500" alt="includebackground" src="/assets/images/mpxv/phylogenetics-sop/screen_shot_7.png">

OR you can specify a number of outgroups IDs. These outgroups must be present in the FASTA file you provided and will be pruned out of the final alignment. For Clade I we recommend outgroups KJ642617,KJ642615,KJ642616 and for Clade IIb we recommend KJ642617,KJ642615. If you also selected the `Include Background` option your specified outgroups will be ignored.

<img width="500" alt="outgroups" src="/assets/images/mpxv/phylogenetics-sop/screen_shot_8.png">

Optionally you can provide a different reference sequence, but this is usually unnecessary - a clade specific reference will be used by default. No Advanced Options or Nextflow Configuration options are required by default.

Click `Launch Workflow` and then `Launch`:

<img width="500" alt="launch2" src="/assets/images/mpxv/phylogenetics-sop/screen_shot_8b.png">
<img width="500" alt="launch2" src="/assets/images/mpxv/phylogenetics-sop/screen_shot_9.png">

This will start the workflow. A progress bar is displayed with the run status but you will not be able to see the stdout that is generated on the command line. 

<img width="500" alt="progress" src="/assets/images/mpxv/phylogenetics-sop/screen_shot_10.png">

Once the run is completed, a number of files will be available and you can double-click to view them:

<img width="500" alt="complete" src="/assets/images/mpxv/phylogenetics-sop/screen_shot_11.png">

This includes a suggested_mask.csv file generated by the run with potentially problematic sites. If you start a new run with the same inputs and additionally provide this mask file in the menu, it will improve the alignment and phylogeny.

## Pipeline description

### Alignment

Squirrel maps each query genome in the input file against a reference genome specific to each clade using [minimap2](https://academic.oup.com/bioinformatics/article/34/18/3094/4994778). Using [gofasta](https://academic.oup.com/bioinformatics/article/38/16/4033/6631223), the mapping file is then converted into a multiple sequence alignment. 

For Clade II, the reference used is `NC_063383` and for Clade I, we use `NC_003310`, these are the RefSeq references for each of the clades on NCBI Genbank. This means that all coordinates within an alignment will be relative to these references. A benefit of this is that within a clade, alignment files and be combined without having to recalculate the alignment. Note however that insertions relative to the reference sequence will not be included in the alignment.

### Masking

Before the final alignment is produced by squirrel, there are additional processing steps that include various masking options. By default, squirrel trims the alignment to 190788 at the end of the genome to mask out one of the inverted terminal repeat (ITR) regions and pads the end of the genome with `N`. This can be disabled with the `no itr mask` option.

Squirrel performs masking (replacement with `N`) on low-complexity or repetitive regions that have been characterised for Clade I and II. These regions are defined in [to_mask.cladeii.csv](https://github.com/aineniamh/squirrel/blob/main/squirrel/data/to_mask.cladeii.csv) and [to_mask.cladei.csv](https://github.com/aineniamh/squirrel/blob/main/squirrel/data/to_mask.cladei.csv) respectively, and the relevant mask file will be selected depending on the `clade` specified. This masking is on by default but can be toggled off.

Squirrel can also accept an additional mask file in csv format (`additional-mask`), if there are flagged sites that you wish to mask within the alignment. These sites will be masked in conjuntion with the default masking files within squirrel. The format of the mask file fits with the features format from Geneious and at a minimum should contain the following fields: "Maximum","Minimum". 

### QC mode

Squirrel can run quality control (QC) on the alignment and flag certain sites to the user that may need to be masked. We recommend that the user looks at these sites in an alignment viewer to judge whether the sites should be masked or not. If QC mode is toggled on, squirrel with check within the alignment for:
- <strong>Mutations that are adjacent to N bases</strong>
The rationale for this is that N sites are usually a product of low coverage regions. Mutations that occur directly adjacent to low coverage regions may be a result of mis-alignment prior to the low coverage masking and may not be real SNPs. 
- <strong>Unique mutations that clump together</strong>
If mutations are observed in only a single sequence in the genome, they are classed as unique mutations. <it>Usually</it> mutations do not clump closely together and may suggest an alignment or assembly issue. If these mutations are not shared with any other sequences, they are flagged for masking. 

### Phylogenetic inference
Tree vizualisations are rendered using [baltic](https://github.com/evogytis/baltic)

## References

Heng Li, Minimap2: pairwise alignment for nucleotide sequences, Bioinformatics, Volume 34, Issue 18, September 2018, Pages 3094–3100, https://doi.org/10.1093/bioinformatics/bty191<br>
Ben Jackson, gofasta: command-line utilities for genomic epidemiology research, Bioinformatics, Volume 38, Issue 16, August 2022, Pages 4033–4035, https://doi.org/10.1093/bioinformatics/btac424<br>
Bui Quang Minh, Heiko A Schmidt, Olga Chernomor, Dominik Schrempf, Michael D Woodhams, Arndt von Haeseler, Robert Lanfear, IQ-TREE 2: New Models and Efficient Methods for Phylogenetic Inference in the Genomic Era, Molecular Biology and Evolution, Volume 37, Issue 5, May 2020, Pages 1530–1534, https://doi.org/10.1093/molbev/msaa015<br>
Gytis Dudas (2016) https://github.com/evogytis/baltic


---

{% include callout.html
type='default'
content="This document is part of the MPXV sequencing protocol package: [http://artic.network/mpxv](http://artic.network/mpxv)"
%}

<br /><br />

{% include wellcome-trust.html %}
<br />

<div class="pagebreak"> </div>
