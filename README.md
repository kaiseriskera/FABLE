# ngs_bench
### Pre-requisite
conda install graphviz

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
snakemake -c8 data/pc_FAR12603_pass_255c3309_11.fastq.gz 

1. prepare sample data
   copy fastq file (temporary hardcoded to kai_lambda/fastqgz_files.fastq.gz) to the snakemake data directory

2. porechop from sample data


### DAG Flow
To generate DAG:
snakemake --dag -c8 data/pc_FAR12603_pass_255c3309_11.fastq.gz | dot -Tsvg > dag.svg

<p align="left"><img src="dag.svg" alt="DAG" width="500"></p>


