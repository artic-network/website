---
title: "MPXV Nanopore sequencing bioinformatics protocol | amplicon"
keywords: protocol
layout: document
last_updated: Dec 03 2024
tags: [protocol]
permalink: /mpxv/mpxv-bioinformatics-sop.html
folder: ncov
title_text: "MPXV Nanopore sequencing bioinformatics protocol"
subtitle_text: "Nanopore | bioinformatics"
document_name: "ARTIC-MPXV-bioinformatics-SOP"
version: v1.0.0
creation_date: 2024-08-20
forked_from: 
author: Sam Wilkinson
citation: "Loman *et al.* In Prep."
nav_menu: false
show_tile: false
category: mpxv-cli
---

{% include callout.html
type='default'
content='**Overview:** A complete bioinformatics protocol to take the output from the [sequencing protocol](/ebov/ebov-seq-sop.html) to consensus genome sequences. Includes basecalling, de-multiplexing, mapping, polishing and consensus generation.
'
%}

## Preparation

This SOP is purely for command line usage, if you are uncomfortable using the command line for bioinformatics data analysis do not worry! We have an SOP for performing the exact same steps using the Epi2me front end available here: [epi2me MPXV bioinformatics](https://artic.network/mpxv/mpxv-ont-epi2me-sop.html).

If you are using a windows PC we recommend that you do any bioinformatics in a WSL2 environment, a tutorial for installing WSL2 is available here: [Microsoft WSL Install Tutorial](https://learn.microsoft.com/en-us/windows/wsl/install), this will be required before moving to the next steps.

Firstly, you will need Conda >= v23.10.0 (or a lower version with mamba installed), this will handle installation of software that the pipeline needs to run. You can find the appropriate installer for miniforge (a conda distribution) by going to this link: [miniforge downloads](https://conda-forge.org/download/), if you are using WSL2 you should download the Linux version of the installer.

Once you have downloaded the installer you can install it by opening a terminal session, moving to the path where the file was downloaded, then running it, like this:

```bash
bash Miniforge3-Linux-x86_64.sh
```

You will then be asked to confirm the install location of miniforge, it defaults to the current users home directory (`~/miniforge3/`) which is fine for the majority of usecases. After, you will be asked to read and agree the end-user license agreement, once you have done so enter `yes` to agree. 
Miniforge will then install into the previously specified directory, after which you will be asked if you would like to automatically initialise Conda when starting a new terminal session, most users will want to select `yes` here.

Once this completes you should have a working Conda install and can move onto the next step.


### Install the latest version from bioconda

First time only, create a conda environment containing the pipeline:

```bash
conda create -n artic -c bioconda -c conda-forge artic
```

This may take a while to solve the environment and download the packages, if this takes a very long time or is unable to solve the environment ensure that you are using a version of conda >= v23.10.0.

<!-- ```bash
git clone https://github.com/artic-network/fieldbioinformatics.git
cd fieldbioinformatics
```

```bash
conda env create -f environment.yml
```

This has created a conda environment named ```artic``` containing all the software requirements for the fieldbioinformatics pipeline, you can activate this environment like so:

```bash
conda activate artic
```

Finally, to install the pipeline itself, we use pip install while inside the fieldbioinformatics directory:

```bash
pip install .
``` -->

## Make a new directory for analysis

Give your analysis directory a meaningful name, e.g.. analysis/run_name

```bash
mkdir analysis
cd analysis

mkdir run_name
cd run_name
```

## Activate the ARTIC environment:

All steps in this tutorial should be performed in the ```artic``` conda environment (if you have previously activated the environment in the previous steps you will not need to do so again):

```bash
conda activate artic
```

<!-- ### Basecalling with Guppy

If you did basecalling with MinKNOW, you can skip this step and go to *Demultiplexing*.

Run the Guppy basecaller on the new MinION run folder:

For fast mode basecalling:

```bash
guppy_basecaller -c dna_r9.4.1_450bps_fast.cfg -i /path/to/reads -s run_name -x auto -r
```

For high-accuracy mode basecalling:

```bash
guppy_basecaller -c dna_r9.4.1_450bps_hac.cfg -i /path/to/reads -s run_name -x auto -r
```

You need to substitute `/path/to/reads` to the folder where the FAST5 files from your
run are. Common locations are:

   - Mac: ```/Library/MinKNOW/data/run_name```
   - Linux: ```/var/lib/MinKNOW/data/run_name```
   - Windows ```c:/data/reads```

This will create a folder called `run_name` with the base-called reads in it.

### Demultiplexing

For the current version of the ARTIC protocol it is essential to demultiplex using strict parameters
to ensure barcodes are present at each end of the fragment.

Starting with this version of the protocol we are now recommending this is done with Guppy:

Guppy is not included with the computing environment and can be downloaded from the nanopore
community website (https://community.nanoporetech.com)

```bash
guppy_barcoder --require_barcodes_both_ends -i run_name -s output_directory --arrangements_files "barcode_arrs_nb12.cfg barcode_arrs_nb24.cfg"
``` -->

## Read filtering

Because ARTIC protocol can generate chimeric reads, we perform length filtering.

This step is performed for each barcode in the run.

We first collect all the FASTQ files into a single file.

To collect and filter the reads for barcode03, we would run:

```bash
artic guppyplex --min-length 1500 --max-length 3000 --directory output_directory/barcode03 --prefix run_name
```

This will perform a quality check. If you are only using "pass" reads you can speed up the process with:

```bash
artic guppyplex --skip-quality-check --min-length 1500 --max-length 3000 --directory output_directory/barcode03 --prefix run_name
```

We use a length filter here of between 1500 and 3000 to remove obviously chimeric reads.

You may need to change these numbers if you are using different length primer schemes. Try the minimum lengths of the amplicons as the minimum, and the maximum length of the amplicons plus 200 as the maximum. Also, the rapid barcoding reaction randomly fragments reads so your minimum read threshold should be adjusted accordingly, we have had good results with a limit of around a 1/4 of the amplicon length, e.g. for a 2000bp scheme, set a minimum length threshold of 500bp.

I.e. if your amplicons are 300 base pairs, use --min-length 300 --max-length 500

You will now have a files called: ``run_name_barcode03.fastq``

## Run the MinION pipeline

Fieldbioinformatics uses the [clair3 variant caller](https://www.nature.com/articles/s43588-022-00387-x), previously both medaka and clair3 were available but problems with medaka forced our adoption of clair3 as the only workflow. This requires the selection of an appropriate model based upon the flowcell chemistry, sequencing speed, basecaller preset, and version. The pipeline will try to select an appropriate model based upon the `basecall_model_version_id` flag in the read file header (the sequencing instrument adds this by default), if this is not present or the pipeline cannot decide on an appropriate model you should provide one using the `--model` parameter.

If you install the pipeline via conda by default only r9.4.1 models will be available, the pipeline can automatically fetch the pre-trained r10.4.1 models from the [ONT Rerio repository](https://github.com/nanoporetech/rerio/tree/master/clair3_models) by running the following command:

```sh
artic_get_models
```

By default models are stored in the users conda environment `$CONDA_PREFIX/bin/models` however this may be changed to another location if desired in the `artic_get_models` and `artic minion` commands by using the `--model-dir` argument.

The following command will automatically pull primer schemes from the [PrimalScheme primerschemes repository](https://github.com/quick-lab/primerschemes) based on the ```--scheme-name```, ```--scheme-version```, and ```--scheme-length``` arguments, the scheme length arg is optional in most cases since the vast majority of primer schemes are only available in a single amplicon length. If the scheme you specify in this command is available in multiple different lengths you will be prompted to specify which length should be downloaded.
If a scheme supports automatic reference selection (currently only artic-inrb-mpox) the pipeline will attempt to determine the most appropriate reference sequence for your data (e.g. clade-ib) and download a version of the scheme remapped to that reference during the pipeline.

For each barcode you wish to process (e.g. run this command 12 times for 12 barcodes), replacing the file name and sample name as appropriate:

E.g. for barcode03

```bash
artic minion --normalise 200 --threads 4 --scheme-directory ~/primer_schemes --scheme-name artic-inrb-mpox --scheme-length 2500 --scheme-version v1.0.0-cladeib --read-file run_name_barcode03.fastq samplename
```

## Custom primer schemes

If you wish to utilise a custom primer scheme not available in the PrimalScheme repository you may instead provide the scheme bedfile and reference fasta directly using the ```--bed``` and ```--ref``` arguments, for example:

```bash
artic minion --normalise 200 --threads 4 --bed ~/primer_schemes/some-scheme/some_virus.scheme.bed --ref ~/primer_schemes/some-scheme/some_virus.reference.fasta --read-file run_name_barcode03.fastq samplename
```

## Output files

   * ``samplename.rg.primertrimmed.bam`` - BAM file for visualisation after primer-binding site trimming
   * ```samplename.trimmed.bam``` - BAM file with the primers left on (used in variant calling)
   * ``samplename.normalised.vcf.gz`` - all detected variants in VCF format
   * ```samplename.pass.vcf``` - detected variants in VCF format passing quality filter
   * ```samplename.fail.vcf``` - detected variants in VCF format failing quality filter
   * ```samplename.primers.vcf``` - detected variants falling in primer-binding regions
   * ``samplename.consensus.fasta`` - consensus sequence
   * ``samplename.amplicon_depths.tsv`` - a TSV (tab delimited) file containing mean amplicon depths across the genome

To put all the consensus sequences in one file called ```my_consensus_genomes.fasta```, run

```bash
cat *.consensus.fasta > my_consensus_genomes.fasta
```

## Software credits
The ARTIC pipeline and [fieldbioinformatics](https://github.com/artic-network/fieldbioinformatics) software include a number of software packages:
- Reference alignment with [minimap2](https://github.com/lh3/minimap2)
- Variant calling with [clair3](https://www.nature.com/articles/s43588-022-00387-x)

---

{% include callout.html
type='default'
content="This document is part of the MPXV sequencing protocol package: [http://artic.network/mpxv](http://artic.network/mpxv)"
%}

<br /><br />

{% include wellcome-trust.html %}
<br />

<div class="pagebreak"> </div>
