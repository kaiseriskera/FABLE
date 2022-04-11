# NanoNathair
<p align="center">
  <img width="366" height="280" src="img6.jpg">

**NanoNathair is an automated and reproducible snakemake workflow tailored to Oxford Nanopore Sequencing reads. After easy installation with conda, it is straightforward to run on local computers where low-quality reads are filtered out for the generation of high-quality alignments against a reference genome**

### Pre-requisite
```bash
conda activate snakemake 
```
make sure your snakemake environment includes the followings:
```bash
conda install -c bioconda graphviz nanoplot nanofilt
```

### Directory Structure

```
├── dag.svg
├── data
├── LICENSE
├── README.md
├── report
└── workflow
    └── Snakefile
```

### Snakemake
To execute with vulcan path
```bash
snakemake --config rule_opt="vulcan" -c8 
```
To execute with minimap2 path
```bash
snakemake --config rule_opt="mm2" -c8 
```

### DAG Flow
To generate DAGs:
```bash
snakemake --config rule_opt="mm2" -c8 --dag | dot -Tsvg > dag_mm2.svg 
snakemake --config rule_opt="vulcan" -c8 --dag | dot -Tsvg > dag_vulcan.svg
 ```    
<p align="left">
  <img src="dag_vulcan.svg" width="400" />
  <img src="dag_mm2.svg" width="400" />
</p>

## NanoNathair workflow

PoreChop and NanoFilt are performed on input fastq files, followed by FastQC and NanoPlot for QC analysis and visualisation. Next, alignment results achieved either by Vulcan or Minimap2 can be studied from reports generated. 

* PRE-ALIGNMENT:
    1. PoreChop
      - removes adapters from ONT's reads and merges multiple fastq files if directory is provided as input
    2. NanoFilt
      - filters reads depending on their quality + option for headcrop to trim nucleotides from start of read
      - default parameters filters out reads with quality score below 10 and trims the first 10 nucleotides from start of read
    3. FastQC and Pre-alignment NanoPlot
      - done in parallel
      - provides QC reports for trimmed and filtered data
 
* ALIGNMENT:
    1. Vulcan
      - leverages minimap2 to identify poorly aligned reads and performs realignment with the more accurate but computationally-expensive NGMLR
      - reference genome and query fastq file fed to input; outputs bam file 
    2. Minimap2
      - map long reads against reference genome
      - outputs sam file that is converted to bam file using samtools

* POST-ALIGNMENT:
    1. Post-alignment NanoPlot
      - visualises aligned data for comparison against unaligned data
    2. Generation of Samstats and benchmark reports
      - allows comparison between Vulcan and minimap2
    
