---
title: "MPXV Nanopore sequencing bioinformatics protocol | amplicon"
keywords: protocol
layout: document
last_updated: Aug 20 2024
tags: [protocol]
permalink: /mpxv/mpxv-bioinformatics-sop.html
folder: ncov
title_text: "MPXV Nanopore sequencing bioinformatics protocol"
subtitle_text: "Nanopore | bioinformatics"
document_name: "ARTIC-MPXV-bioinformaticsSOP"
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

This SOP is purely for command line usage, if you are uncomfortable using the command line for bioinformatics data analysis do not worry! We have an SOP for performing the exact same steps using the Epi2me front end available here: []().

If you are using a windows PC we recommend that you do any bioinformatics in a WSL2 environment, a tutorial for installing WSL2 is available here: [Microsoft WSL Install Tutorial](https://learn.microsoft.com/en-us/windows/wsl/install), this will be required before moving to the next steps.

Firstly, you will need Conda >= v23.10.0 (or a lower version with mamba installed), this will handle installation of software that the pipeline needs to run. You can find the appropriate installer for miniforge (a conda distribution) by going to this link: [miniforge downloads](https://conda-forge.org/download/), if you are using WSL2 you should download the Linux version of the installer.

Once you have downloaded the installer you can install it by opening a terminal session, moving to the path where the file was downloaded, then running it, like this:

```bash
bash Miniforge3-Linux-x86_64.sh
```

You will then be asked to confirm the install location of miniforge, it defaults to the current users home directory (`~/miniforge3/`) which is fine for the majority of usecases. After, you will be asked to read and agree the end-user license agreement, once you have done so enter `yes` to agree. 
Miniforge will then install into the previously specified directory, after which you will be asked if you would like to automatically initialise Conda when starting a new terminal session, most users will want to select `yes` here.

Once this completes you should have a working Conda install and can move onto the next step.


### Creating the environment

First time only, clone the fieldbioinformatics github repository and checkout the 1.4.0-dev branch, once 1.4.0 has been properly released this section will be updated to reflect this:

```bash
git clone https://github.com/artic-network/fieldbioinformatics.git
cd fieldbioinformatics
git checkout 1.4.0-dev
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
```

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

You may need to change these numbers if you are using different length primer schemes. Try the minimum lengths of the amplicons as the minimum, and the maximum length of the amplicons plus 200 as the maximum.

I.e. if your amplicons are 300 base pairs, use --min-length 300 --max-length 500

You will now have a files called: ``run_name_barcode03.fastq``

## Run the MinION pipeline (Medaka variant caller)

Fieldbioinformatics supports two variant callers, Clair3 and Medaka, in our testing both appear to perform well but we have far more experience with Medaka and therefore recommend it as the default variant caller, if you wish to try the experimental clair3 workflow, you can add the argument ```--clair3``` to the command below. The ```--model``` parameter should be changed to an appropriate clair3 model, information about these can be found [in the clair3 repository](https://github.com/HKU-BAL/Clair3?tab=readme-ov-file#pre-trained-models).

This command will automatically pull primer schemes from the [PrimalScheme primerschemes repository](https://github.com/quick-lab/primerschemes) based on the ```--scheme-name```, ```--scheme-version```, and ```--scheme-length``` arguments, the scheme length arg is optional in most cases since the vast majority of primer schemes are only available in a single amplicon length. If the scheme you specify in this command is available in multiple different lengths you will be prompted to specify which length should be downloaded.

For each barcode you wish to process (e.g. run this command 12 times for 12 barcodes), replacing the file name and sample name as appropriate:

E.g. for barcode03

```bash
artic minion --normalise 200 --threads 4 --scheme-directory ~/primer_schemes --scheme-name yale-mpox --scheme-version v1.0.1 --read-file run_name_barcode03.fastq --model r941_e81_hac_g514 samplename
```

Replace ``samplename`` as appropriate.

In this example ```--model r941_e81_hac_g514``` is provided which is the most recent medaka model for r9.4.1 flowcell, basecalled with a high accuracy model, on guppy 5.1.4 or later. This obviously is not applicable to all data so users should replace this with the most appropriate model for their data, guidance on doing so is available [here](https://github.com/nanoporetech/medaka?tab=readme-ov-file#models), a useful command is ```medaka tools list_models``` which will print a list of all models available to medaka.

It is **vitally** important that the correct medaka / clair3 model is chosen here, incorrect model choice can lead to systematic errors in the output sequence so this must be chosen with extreme care.

## Custom primer schemes

If you wish to utilise a custom primer scheme not available in the PrimalScheme repository you may instead provide the scheme bedfile and reference fasta directly using the ```--bed``` and ```--ref``` arguments, for example:

```bash
artic minion --normalise 200 --threads 4 --bed ~/primer_schemes/some-scheme/some_virus.scheme.bed --ref ~/primer_schemes/some-scheme/some_virus.reference.fasta --read-file run_name_barcode03.fastq --model r941_e81_hac_g514 samplename
```

## Output files

   * ``samplename.rg.primertrimmed.bam`` - BAM file for visualisation after primer-binding site trimming
   * ```samplename.trimmed.bam``` - BAM file with the primers left on (used in variant calling)
   * ``samplename.merged.vcf`` - all detected variants in VCF format
   * ```samplename.pass.vcf``` - detected variants in VCF format passing quality filter
   * ```samplename.fail.vcf``` - detected variants in VCF format failing quality filter
   * ```samplename.primers.vcf``` - detected variants falling in primer-binding regions
   * ``samplename.consensus.fasta`` - consensus sequence
   * ``samplename.amplicon_depths.tsv`` - a TSV (tab delimited) file containing mean amplicon depths across the genome

To put all the consensus sequences in one file called ```my_consensus_genomes.fasta```, run

```bash
cat *.consensus.fasta > my_consensus_genomes.fasta
```
