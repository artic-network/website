title: "nCoV-2019 novel coronavirus Nanopore sequencing bioinformatics protocol | amplicon, native barcoding"
keywords: protocol
layout: document
last_updated: Mar 29, 2020
tags: [protocol]
permalink: /ncov-2019/ncov2019-bioinformatics-sop.html
folder: ncov
title_text: "nCoV-2019 novel coronavirus bioinformatics protocol"
subtitle_text: "Nanopore | bioinformatics"
document_name: "ARTIC-nCoV-bioinformaticsSOP"
version: v1.1.0
creation_date: 2020-01-23
forked_from: 
author: Nick Loman, Will Rowe, Andrew Rambaut
citation: "Loman *et al.* In Prep."
nav_menu: false
show_tile: false
category: ncov
---

{% include callout.html
type='default'
content='**Overview:** A complete bioinformatics protocol to take the output from the [sequencing protocol](/ebov/ebov-seq-sop.html) to consensus genome sequences. Includes basecalling, de-multiplexing, mapping, polishing and consensus generation.
'
%}

## Preparation

Set up the computing environment as described here in this document: [ncov2019-it-setup](ncov2019-it-setup.html). This should be done and tested prior to sequencing, particularly if this will be done in an environment without internet access or where this is slow or unreliable. Once this is done, the bioinformatics can be performed largely off-line. If you are already using the [lab-on-an-SSD](https://github.com/artic-network/fieldbioinformatics/tree/master/lab-on-an-ssd), you can skip this step.

### Updating the environment

First time only:

```bash
git checkout https://github.com/artic-network/artic-ncov2019
```

```
cd artic-ncov2019
conda env remove -n artic-ncov-2019
conda env create -f environment.yml
conda env create -f environment-medaka.yml
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

All steps in this tutorial should be performed in the ```artic-ncov2019``` conda environment:

```bash
source activate artic-ncov2019
```

### Basecalling with Guppy

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
```

## Read filtering

Because ARTIC protocol can generate chimeric reads, we perform length filtering.

This step is performed for each barcode in the run.

We first collect all the FASTQ files (typically stored in files each containing 4000 reads)
into a single file.

To collect and filter the reads for barcode03, we would run:

```bash
artic guppyplex --min-length 400 --max-length 700 --directory output_directory/barcode03 --prefix run_name
```

This will perform a quality check. If you are only using "pass" reads you can speed up the process with:

```bash
artic guppyplex --skip-quality-check --min-length 400 --max-length 700 --directory output_directory/barcode03 --prefix run_name
```

We use a length filter here of between 400 and 700 to remove obviously chimeric reads.

You may need to change these numbers if you are using different length primer schemes. Try the minimum lengths of the amplicons as the 
minimum, and the maximum length of the amplicons plus 200 as the maximum.

I.e. if your amplicons are 300 base pairs, use --min-length 300 --max-length 500

You will now have a files called: ``run_name_barcode03.fastq``

## Run the MinION pipeline

For each barcode you wish to process (e.g. run this command 12 times for 12 barcodes), replacing the file name and sample name as appropriate:

E.g. for barcode03

```bash
artic minion --normalise 200 --threads 4 --scheme-directory ~/artic-ncov2019/primer-schemes --read-file run_name_barcode03.fastq --fast5-directory path_to_fast5 --sequencing-summary path_to_sequencing_summary.txt nCoV-2019/V3 samplename
```

Replace ``samplename`` as appropriate.

## Output files

   * ``samplename.primertrimmed.bam`` - BAM file for visualisation after primer-binding site trimming
   * ``samplename.vcf`` - detected variants in VCF format
   * ``samplename.variants.tab`` - detected variants
   * ``samplename.consensus.fasta`` - consensus sequence

To put all the consensus sequences in one filei called my_consensus_genome, run

```bash
cat *.consensus.fasta > my_consensus_genomes.fasta
```

## To visualise genomes in Tablet

Open a new Terminal window:

```bash
conda activate tablet
tablet
```

Go to "Open Assembly"

Load the BAM (binary alignment file) as the first file.

Load the reference file (in artic/artic-ncov2019/primer_schemes/nCoV-2019/V1/nCoV-2019.reference.fasta) as the second file.

Select Variants mode in Color Schemes for ease of viewing variants.

## Experimental Medaka pipeline

An alternative to nanopolish to calling variants is to use medaka. Medaka is faster than nanopolish and seems to perform mostly equivalently in (currently limited) testing.

You'll need a different environment for Medaka, as it can't happily co-exist with nanopolish:

```
conda env create -f artic-ncov2019-medaka.yaml
```

```
source activate artic-ncov2019-medaka
```

If you want to use Medaka, you can skip the ``nanopolish index`` step, and add the parameter ``--medaka`` to the command, as below:

```bash
artic minion --medaka --normalise 200 --threads 4 --scheme-directory ~/artic-ncov2019/primer-schemes --read-file run_name_barcode01.fastq nCoV-2019/V1 samplename
```

Replace ``samplename`` as appropriate.

E.g. for barcode02

```bash
artic minion --medaka --normalise 200 --threads 4 --scheme-directory ~/artic/artic-ncov2019/primer-schemes --read-file run_name_barcode02.fastq nCoV-2019/V1 samplename
```


