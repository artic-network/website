---
title: "nCoV-2019 novel coronavirus Nanopore sequencing bioinformatics protocol | amplicon, native barcoding"
keywords: protocol
layout: document
last_updated: Jan 23, 2020
tags: [protocol]
permalink: /ncov-2019/ncov2019-bioinformatics-sop.html
folder: ncov
title_text: "nCoV-2019 novel coronavirus bioinformatics protocol"
subtitle_text: "Nanopore | bioinformatics"
document_name: "ARTIC-nCoV-bioinformaticsSOP"
version: v1.0.0
creation_date: 2020-01-23
forked_from: 
author: Nick Loman, Andrew Rambaut
citation: "Loman *et al.* In Prep."
nav_menu: false
show_tile: false
category: ncov
---

{% include callout.html
type='default'
content='**Overview:** this document is being revised and will be available shortly.'
%}

## Preparation

Set up the computing environment as described here in this document: [ncov2019-it-setup](ncov2019-it-setup.html). This should be done and tested prior to sequencing, particularly if this will be done in an environment without internet access or where this is slow or unreliable. Once this is done, the bioinformatics can be performed largely off-line. If you are already using [https://github.com/artic-network/fieldbioinformatics/tree/master/lab-on-an-ssd](lab-on-an-SSD), you can skip this step.

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

If you did basecalling with MinKNOW, you can skip this step and go to *Consensus sequence generation*.

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

### Consensus sequence generation

We first collect all the FASTQ files (typically stored in files each containing 4000 reads)
into a single file.

```bash
artic gather --min-length 400 --max-length 700 --prefix run_name
```

The command will show you the runs in /var/lib/MinKNOW/data and ask you to select one. If you know the path to the reads use:

```bash
artic gather --min-length 400 --max-length 700 --prefix run_name --directory /path/to/reads
```

Here `/path_to_reads` should be the folder in which MinKNOW put the base-called reads (i.e., `run_name` from the command above).

We use a length filter here of between 400 and 700 to remove obviously chimeric reads.

You may need to change these numbers if you are using different length primer schemes. Try the minimum lengths of the amplicons as the 
minimum, and the maximum length of the amplicons plus 200 as the maximum.

I.e. if your amplicons are 300 base pairs, use --min-length 300 --max-length 500

You will now have a file called: ``run_name_pass.fastq``
and a file called ``run_name_sequencing_summary.txt``, 
as well as individual files for each barcode (if previously demultiplexed).

### Demultiplex with Porechop with stringent settings

This stage is obligatory, even if you have already demultiplexed with Guppy, due to
significant barcoding misassignments that can confound results:

```bash
artic demultiplex --threads 4 run_name_pass.fastq
```

Now you will have new files called:

```bash
run_name_pass_NB01.fastq
run_name_pass_NB02.fastq
run_name_pass_NB03.fastq
```

### Create the nanopolish index (you only need this once per sequencing run):

```bash
nanopolish index -s run_name_sequencing_summary.txt -d /path/to/reads run_name_pass.fastq
```

Again, alter ``/path/to/reads`` to point to the original location of the FAST5 files.

## Run the MinION pipeline

For each barcode you wish to process (e.g. run this command 12 times for 12 barcodes), replacing the file name and sample name as appropriate:

E.g. for NB01

```bash
artic minion --normalise 200 --threads 4 --scheme-directory ~/artic-ncov2019/primer-schemes --read-file run_name_pass_NB01.fastq --nanopolish-read-file run_name_pass.fastq nCov-2019/V1 samplename
```

Replace ``samplename`` as appropriate.

E.g. for NB02

```bash
artic minion --normalise 200 --threads 4 --scheme-directory ~/artic/artic-ncov2019/primer-schemes --read-file run_name_pass_NB02.fastq --nanopolish-read-file run_name_pass.fastq nCov-2019/V1 samplename
```

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

Load the refernece file (in artic/artic-ncov2019/primer_schemes/nCoV-2019/V1/nCoV-2019.reference.fasta) as the second file.

Select Variants mode in Color Schemes for ease of viewing variants.

