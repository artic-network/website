---
title: "Mpox virus sequencing | A guide to sequencing for genomic epidemiology"
keywords: protocol
layout: document
last_updated: 2024-12-12
tags: [protocol] 
permalink: /mpxv/artic-mpxv-guide.html
folder: mpxv
title_text: "Mpox virus sequencing"
subtitle_text: "A guide to sequencing for genomic epidemiology"
document_name: "ARTIC-MPXV-guide"
version: v1.0.2
creation_date: 2024-08-20
forked_from: 
author: ARTIC team
citation: "Loman *et al.* In Prep."
nav_menu: false
show_tile: false
category: mpxv-guide
---

{% include callout.html
type='default'
content='**Overview:** This document is part of the Mpox virus (MPXV) sequencing protocol package: [http://artic.network/mpxv](http://artic.network/mpxv)'
%}

<hr />

### Why do sequencing of Mpox?

In contrast to clade-specific PCR tests, monkeypox virus (MPXV) genome sequencing provides a much more fine-scale characterisation of the virus and insights into the unfolding situation of an epidemic. Specifically, for MPXV, whole genome sequencing allows:

* **Clade typing** — The ability to distinguish Clade Ia vs Ib vs IIb. Thus far, Clade Ia is associated with zoonotic infections from animal reservoirs, with limited household transmission and secondary infections. Clade Ib is currently associated with a fast growing outbreak of human-to-human transmission. Clade IIb is responsible for a large epidemic starting in 2022 associated with sexual transmission with cases still being reported in countries worldwide.
* **Genomic epidemiology** — Within human outbreaks a host enzyme, APOBEC3F, induces mutations in the virus, hugely increasing the rate of accumulation of mutations (MPXV as a double stranded DNA virus has a low rate of evolution in other contexts). These mutations mean that genome sequencing can be used as a tool for genomic epidemiology on a relatively short timescale. Estimates from Clade IIb suggest that we expect approximately 20 mutations to accumulate per year \- a similar rate to many RNA viruses.
* **Tracking changes in the virus** — although most observed mutations within an outbreak are driven by APOBEC3, other mutations are observed including amino acid changes and deletions. In most cases the phenotypic properties of these changes will be unknown and difficult to infer due to the large and complex nature of the MPXV genome. It is possible that changes associated with more rapidly spreading lineages could be identified for further investigation. Changes may affect the performance diagnostic assays (i.e., the large deletion in Clade Ib).

### How best to perform sequencing of Mpox?

Choice of sequencing instrument and protocol is likely to depend on local availability of instruments, expertise and reagents, and therefore vary between laboratories. Employing a diversity of approaches increases accessibility of sequencing for laboratories globally, although care must be taken to generate sequences that can be reliably compared.

For the purposes of genomic epidemiology including clade typing, where the goal is to reliably detect single nucleotide changes working directly from clinical samples, we recommend using a multiplex amplicon sequencing protocol such as the ARTIC protocol. Amplicon sequencing has been shown to be cost-effective during the SARS-CoV-2 pandemic, with 96 or more samples able to be sequenced on an individual flowcell, and permits results to be generated with samples with low viral genome copy numbers (typically down to around 10,000-100,000 genome copies/ml, or a PCR cycle threshold value up to around 30-35). Amplicon sequencing does have limitations however: one important challenges for MPXV is that the design of the primer scheme assumes that the target genome is closely related: amplicon schemes tend to perform less well when applied to target sequences that have large number of mismatches to the primers, meaning that genome coverage will fall. Additionally, amplicon schemes assume gene order conservation, i.e. that the target genome and the genome used to create the scheme are more or less co-linear. This limitation means that amplicon sequencing cannot reliably be used to generate *de novo* assemblies. This may limit their use when characterising divergent novel clades of MPXV, or related poxviruses.

For such *de novo* applications where a close reference is not available, a metagenomics approach may be used instead. These approaches have the advantage that whole genomes can be reconstructed with a *de novo* assembly algorithm. This approach is aided further by the use of long read sequencing, which is able to resolve repetitive regions. However, metagenomics approaches have lower sensitivity  particularly for DNA viruses where DNase treatment cannot be exploited to reduce background, and is not recommended for Ct values above around 20\. Because of this high host background, sequencing from clinical samples ends up being significantly more costly to generate individual sequences, and therefore metagenomics is not recommended as an approach for high-throughput genomic epidemiology.

A further approach to sequencing is target enrichment (also known as bait capture) using specific probes. This approach has intermediate sensitivity between amplicon sequencing and metagenomics (up to a Ct value of around 25), and may be more tolerant of genome structure changes, but is typically more expensive and laborious and we do not recommend it for labs that are not already set up for this technique.

We emphasise that the process of generating sequence data for genomic epidemiology is fundamentally different to the generation of reference-grade MPXV viruses. This process, whilst important, is fundamentally a low throughput method which involves long read sequencing, de novo assembly, optionally short read polishing and manual finishing and curation techniques.

### Primer schemes for amplicon schemes

[Amplicon sequencing of](https://www.protocols.io/view/monkeypox-virus-multiplexed-pcr-amplicon-sequencin-5qpvob1nbl4o) MPXV relies on a set of PCR primers (typically divided into two pools) that tile across the genome. Given the large genome size (200kb), a large amplicon fragment size (typically 2000, 2500 or 5000 bases) is targeted to divide the genome into 100, 80 or 40 fragments respectively. Generally speaking, longer amplicon schemes produce a result that results in more even sequencing coverage. However, as there are fewer long fragments in a typical sample than short fragments, this comes at the expense of sensitivity (i.e. samples with higher Ct values do not sequence as well). Uneven coverage from preferential amplification can be mitigated to a limited extent by changing the relative quantities of primers used during PCR, as shown in [this protocol from BCCDC/ARTIC](https://www.protocols.io/view/bccdc-artic-mpox-v2-3-4-2500bp-amplicon-generation-n2bvj34nnlk5/v1).

<div class="pagebreak"> </div>

Amplicon schemes can be designed against single reference genomes, in which case they are clade-specific, or against a broader range of references to permit them to be clade-independent. We found that most publicly available MPXV primer schemes are designed against clade II references. More recently, ARTIC has developed a pan-clade primer scheme:

| Scheme | Clade reference | Size (bases) | Link |
| :---- | :---- | :---- | :---- |
| ARTIC/INRB (Clinical) | I and II | 2500 | [Primal Scheme Labs](https://labs.primalscheme.com/detail/artic-inrb-mpox/2500/v1.0.0/?q=) |
| ARTIC/INRB (Wastewater) | I and II | 400 | [Primal Scheme Labs](https://labs.primalscheme.com/detail/artic-inrb-mpox/400/v1.0.0/?q=) |
| Yale – Chen *et al.* | IIb | 2000 | [Primal Scheme Labs](https://labs.primalscheme.com/detail/grubaugh-mpox/2000/v1.0.0/?q=Mpox), [Manuscript](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3002151), [Primer Request Link](https://go.idtdna.com/Yale-Mpox-Amplicon-Panel-Request-Consult.html) |
| INRB | IIb | 2000 | [Link](https://github.com/inrb-labgenpath/DRC\_MPXV\_primers) (NB: identical Primal Scheme to Yale) |
| Welkers *et al.* | IIb | 2500 | [Link](https://www.protocols.io/view/monkeypox-virus-whole-genome-sequencing-using-comb-n2bvj6155lk5/v1?step=1), [Primer Scheme Repository](https://github.com/pha4ge/primer-schemes/tree/main/schemes/mpxv/erasmus/2500/v1.0.0) |
| ARTIC/BCCDC | IIb | 2500-3000 | [Protocol](https://www.protocols.io/view/bccdc-artic-mpox-v2-3-4-2500bp-amplicon-generation-n2bvj34nnlk5/v1), [Primer Scheme Repository](https://github.com/BCCDC-PHL/artic-mpxv2022/tree/main/primer_schemes/mpxv-2022/V2.3) |

**Table 1** | Publicly available MPXV primer schemes.

Given the large amplicon size, for Illumina applications there needs to be an additional fragmentation stage (typically using Nextera XT/Flex) before sequencing can occur. For Oxford Nanopore sequencing, an optional fragmentation step can be introduced by using the rapid barcoding kit (SQK-RBK004) on the barcoded products. This is colloquially referred to as the “Midnight” protocol. Generally, although fragmentation is a convenient sequencing step, it results in less confidence about whether a sequence read has been generated from an intact PCR product, with the potential for technical artefacts to be generated. In practice, this is unlikely to have a big impact on phylogenetic analysis but should be considered if unusual mutations, e.g. homoplasies are detected.

#### Use of clade II primer schemes for global MPXV genomic epidemiology

ARTIC in collaboration with INRB have recently developed and tested a clade-independent primer scheme that is able to generate complete genomes from both clades I and II using the same primer set. Two versions of this scheme is available: 400 bp (optimised for wastewater applications) and 2500 bp versions (optimised for clinical samples).

We found that primer schemes designed against Clade II references are likely to generate adequate results on Clade I/Ib genomes, therefore covering the clades of interest. With reference to the Yale (Chen *et al.*) scheme, 83% of the primer sites are unaffected, with 14% containing one SNP, and 3% containing multiple mutations or indels. In our testing this results in typically around 85-90% genome coverage, which is sufficient for genomic epidemiology.

We recommend that users visit [Primal Scheme Labs](https://labs.primalscheme.com/) to find validated primer schemes that have accompanying BED files that permit analysis using standardised bioinformatics pipelines. We also encourage users who have generated and validated schemes to contribute them to Primal Scheme Labs for the wider community to benefit.

### Specific considerations when sequencing Mpox with amplicons

The \~200 kilobase DNA genome of the Monkeypox virus (MPXV) that causes mpox provides some challenges, specifically:

* It has a low [GC content of \~33%](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9670986/) which translates to a higher frequency of A/T homopolymeric tract regions. Homopolymeric tracts pose particular challenges to sequencing instruments. The Oxford Nanopore platform using R9 chemistry is poor at resolving homopolymeric tracts above 6 bases. This has been improved with the latest R10 (R10.4.1) chemistry which has improved homopolymer calling to make it reliable up to around 9-10 bases by the improved R10 nanopore. This problem also affects flow-based chemistry instruments such as Ion Torrent. Errors in homopolymer regions can introduce false positive SNPs and short indels that may confound accurate phylogenetic reconstruction, if not accounted for in the analysis stage.
* The MPXV genome contains a [large (6.5 \- 17.5kb) inverted tandem repeat](https://www.frontiersin.org/journals/cellular-and-infection-microbiology/articles/10.3389/fcimb.2024.1360586/full) (ITR) at each end of the genome. As this region is typically not captured within a single sequencing read, it is impossible to determine which copy a sequencing read relates to. However, in practice, both copies of the ITR will be identical. The 3’ copy of this region is typically ignored when performing phylogenetic analysis.
* Given the large accessory genome, large deletions are commonly observed (e.g. a large deletion distinguishes Clade I and Clade Ib). Amplicon methods may not easily differentiate between biological deletions and amplicon drop-outs (where the PCR product fails to amplify).
* The MPXV genome contains short tandem repeats that undergo expansion and contraction. Whilst these typically will sequence correctly with long read sequencing approaches, certain alignment packages may fail to correctly align this region, leading to sequencing errors. Additionally, [these genomic accordions](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11026394/) can be variable within a sample.
* On a longer evolutionary timescale, the genome can undergo rearrangements. Rearrangements pose difficulties to amplicon sequencing approaches that rely on genome synteny (the order of genes) being conserved.

### Sequencing handling and bioinformatics and quality control

Regardless of the exact sequencing protocol employed, bioinformaticians analysing amplicon sequencing data must be aware of common analytical pitfalls.

The most important step is the correct handling of primer sequences. Because amplicon sequencing introduces synthetic primer sequences into the sequencing data which do not necessarily reflect the sequence of the target, these must be systematically identified and removed from analysis. This is most commonly done by using a bioinformatics pipeline that is specific for amplicon sequencing analysis, and supplying information about the primer scheme and reference genome at the point of analysis. **It is absolutely vital that the correct primer scheme and reference genome are specified, or results may not be correct.** The most common side-effect of not correctly removing primers are frequent, systematically occurring reversions or “calls for reference” which can have a dramatic negative impact on phylogenetic analysis.

A second, common and pervasive problem with amplicon sequencing is that laboratory contamination with PCR amplification products can render sequencing results unreliable, because sequences may spill between different samples. This is most commonly seen in low genome copy number samples (high Ct), or in regions that have dropped-out due to mutations in the primer-binding site. The most common way of detecting contamination is to ensure that positive and negative controls are included in each sequencing batch. Positive control sequences should be checked that they are the expected sequence on each sequencing run, and negative controls should be generally “clean” (the total number of reads in a negative control acceptable is hard to specify, but generally it should be \<0.1% of the average number of reads in a real sample).

Failure to correctly handle these situations is a common scenario that hampered SARS-CoV-2 genomics and results in low quality consensus genomes that may make false inferences from genomic epidemiology.

### Bioinformatics recommendations for consensus sequence generation

For nanopore amplicon sequence data generated with the ARTIC protocol, or with the ARTIC protocol using the rapid kit (“Midnight”) we recommend using fieldbioinformatics 1.4.0. This can be run easily through the EPI2Me Labs interface by installing  [artic-mpxv-nf](https://github.com/artic-network/artic-mpxv-nf), which is currently undergoing field testing in collaboration with INRB. We have made it easy to switch between a clade I and clade II reference, for sequences generated using the Yale or INRB primers.

For nanopore metagenomics sequence data, the wf-mpx workflow can be used.

For Illumina amplicon sequence, the ARTIC team recommend using [artic-mpxv-illumina-nf](https://github.com/artic-network/artic-mpxv-illumina-nf) which is an EPI2ME wrapper for the [BCCDC’s Illumina amplicon bioinformatics pipeline](https://github.com/BCCDC-PHL/mpxv-artic-nf).

An overview of some other options for bioinformatics pipelines can be found at the PHA4GE Github: [https://github.com/pha4ge/pipeline-resources/blob/main/docs/mpxv-bioinfo-solutions.md](https://github.com/pha4ge/pipeline-resources/blob/main/docs/mpxv-bioinfo-solutions.md)

### Recommendations for downstream processing, QC and phylogenetics

Phylogenetic reconstruction is confounded by erroneous mutations being included in analysis, with false positive SNPs particularly likely to create erroneous inferences. Therefore, a conservative approach to phylogenetic reconstruction focuses on trying to generate a trusted set of SNPs and reducing the influence of error-prone regions of the genome. This generally means the need to mask the parts of genomes that are likely to contain errors, particularly low-complexity and repetitive areas.

We have devised a software package, [*Squirrel*](https://github.com/aineniamh/squirrel), that automates downstream alignment to a set of reference genomes, including quality control information. Optionally (recommended) it can perform sequence qc to identify mutations that are adjacent to ambiguous ‘N’ bases and unique mutations that clump together as these are likely to be as a result of sequencing or bioinformatic errors. This results in a mask file which can be input to Squirrel to improve phylogenetic inferences in phylogenetic mode.

Signatures of APOBEC3-editing are characteristic of MPXV evolution when sustained transmission in the human population (see O'Toole et al 2023). Squirrel can be run in phylogenetic mode to combine maximum-likelihood phylogenetics and an ancestral reconstruction pipeline that characterises the APOBEC3-like and non-APOBEC3 mutations that have occurred across the evolutionary history of the virus sequences provided. In QC mode Squirrel is able to flag additional problematic sites based on this analysis.

An EPI2ME version of squirrel is also available from [https://github.com/artic-network/squirrel-nf](https://github.com/artic-network/squirrel-nf)

### Further Reading / Viewing

> ARTIC list of MPXV sequencing and bioinformatics resources:
: [https://artic.network/mpxv/resources](https://artic.network/mpxv/resources)

> Oxford Nanopore Technologies' EPI2ME Labs:
: [https://labs.epi2me.io/](https://labs.epi2me.io/)

> ARTIC-CLIMB workshop videos (covering SARS-CoV-2 but generally applicable to MPXV): 
: [https://www.climb.ac.uk/artic-and-climb-big-data-joint-workshop-2/](https://www.climb.ac.uk/artic-and-climb-big-data-joint-workshop-2/)

> Chen *et al.* Yale amplicon sequencing protocol:
: [https://www.protocols.io/view/monkeypox-virus-multiplexed-pcr-amplicon-sequencin-5qpvob1nbl4o](https://www.protocols.io/view/monkeypox-virus-multiplexed-pcr-amplicon-sequencin-5qpvob1nbl4o)

> Squirrel MPXV alignment and phylogenetics tool:
: [https://github.com/aineniamh/squirrel](https://github.com/aineniamh/squirrel)

 ---

{% include callout.html
type='default'
content="This document is part of the MPXV sequencing protocol package: [http://artic.network/mpxv](http://artic.network/mpxv)"
%}

<br /><br />

{% include wellcome-trust.html %}
<br />

<div class="pagebreak"> </div>

