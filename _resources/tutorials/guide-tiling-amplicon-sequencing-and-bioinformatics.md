---
title: "A quick guide to tiling amplicon sequencing and downstream bioinformatics analysis"
keywords: tutorial
layout: document
last_updated: Feb 12, 2020
tags: [protocol] 
permalink: quick-guide-to-tiling-amplicon-sequencing-bioinformatics.html
folder: tutorials
title_text: "A quick guide to tiling amplicon sequencing and downstream bioinformatics analysis"
version: v1.0.0
creation_date: 2020-02-12
forked_from: 
author: Nicholas Loman
nav_menu: false
show_tile: false
category: tutorial
---

## Introduction

There are enough differences between analysing tiling amplicon data compared to regular whole-genome shotgun data to warrant writing this short guide.

For background information on how tiling amplicon sequencing works, please prefer to the original “PrimalSeq” protocol paper as tested on Zika [Quick et al. Nature Protocols](https://www.nature.com/articles/nprot.2017.066) and a follow-up paper [Grubaugh, Gangavaparu et al. Genome Biology](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-018-1618-7) that focuses on in-host variation and Illumina sequencing. This second paper also covers analysis of Illumina data.

However, for those getting started with amplicon sequencing data who have some experience analysing WGS data, here are some basic points to consider which may affect the downstream analysis.

To refresh on the reasons to use amplicon sequencing (compared to metagenomic sequencing):
* It can be made to work on samples with very low viral genome copy numbers (for example Ct of 36 in Zika) and with degraded RNA
* Most or all of the reads are on-target, this reduces the sequencing background and therefore reduces the cost of sequencing (permitting many samples to be amplified)

These benefits also directly result in several challenges that must be considered during the sequencing and analysis process:
* Contamination: very high sensitivity means that even small amounts of contaminating template (e.g. amplicons from previous work) can result in amplification of sequences not present in the sample
* Barcoding issues: small rates of barcode “cross-over” can result in the presence of sequences from other samples that confound the analysis

A third problem is that because PCR relies on synthetic primers, amplicons will contain synthetic sequences in the primer binding site. This is a problem that must be accounted for if the primer sequence contains mismatches compared to the template.

Through trial and error we have come up various steps in the protocol that addresses each of these issues which are detailed below:

## Contamination

The most powerful tool against the presence of contaminating sequences is the effective use of negative and positive controls during sequencing. The negative control is particularly important. In this case at least one water blank is passed through the same protocol as regular samples, including amplification. The total volume of the negative control is used (regardless of whether it is detectable by quantification e,g. Qubit) as a sequencing negative and barcoded as if it was another sample. Without this essential control it is impossible to estimate the potential impact of sample contamination on the sequence.

A positive control (typically. of a different organism) is also potentially useful to investigate the effect of barcode mismatching.

## Barcode mismatches

In nanopore sequencing, barcode misidentification is a common-place occurrence due to the presence of in silico chimera reads. Such chimeras occur when the end of a read is not properly detected by the MinKNOW control software. This can result in two different barcodes being present at each end of the read. With non-stringent demultiplexing, the “best” barcode is taken but this may not be the correct one.

The easiest mitigation for this problem is to insist during the demultiplex step that the same barcode is seen at the start and the end of each read. In our experience this removes most barcode misidentifications. Reads can also be filtered to ensure they are of the expected size (e.g. amplicon length + adaptor + barcode length, typically around 500bp for our schemes) as a second way of removing additional chimeras.

For Illumina sequencing, the more modern instruments that rely on patterned flowcell techniques associated with linear isothermal amplification (e.g. HiSeq 4000 and NovaSeq) are known to have significant problems with index swapping, requiring the use of unique dual indexes for multiplexing. For older instruments, dual barcoding without unique indexes can be used, but it may be necessary to change the stringency of bcl2fastq to reduce barcode misidentification (e.g. allow 0 mismatches).

## Primer-binding sites

Amplicon ends contain synthetic primer binding sites. Our preferred way of dealing with this is to remove them according to the information known about the primer scheme (contained in the BED file) using a script called align_trim. It might also be possible to remove them during the process of adaptor trimming, but care should be taken to ensure they are fully removed which is not easy without an alignment stage. 

## Consensus sequence generation

Our preferred method for consensus sequence generation is to perform reference alignment, variant calling and then edit a reference genome with the quality-filtered variants. Alternative approaches could be “reference-guided assembly”. De novo assembly is not recommended nor required for amplicon schemes due to the intrinsic assumptions made about genome structure conservation when designing a tiling scheme. It is unlikely that assembly methods would work well, and may produce erroneous results.

## FAQ

Why do you sequence short fragments?

 We have standardised on short amplicons. We do this because short amplicons are more likely to amplify with degraded RNA. Additionally, if regions fail to amplify in the scheme then less genome coverage is lost than it would be with a long amplicon. In an ideal world, amplicons would be as long as possible and it is often possible to sequence products longer than the 400 bp we typically use for intact RNA (we have tested up to 2kb with Ebola in the past). Aside from RNA fragment quality, PCR is less likely to work at very high fragment lengths.

Can you detect low-frequency variants using amplicon sequencing?

Yes, you can. However there is a major caveat which is that primer-binding site mismatches drastically affects the reliability of those frequencies. In the absence of primer-binding site mismatches the variant frequencies are fairly consistent with metagenomics approaches. For nanopore sequencing, low variant frequency detection is not particularly reliable but moderate frequencies should be detectable.

