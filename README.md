# ngs_bench
### Pre-requisite
```bash
conda active snakemake 
```
make sure your snakemake environment includes the followings:
```bash
conda install graphviz
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
To execute:
```bash
snakemae -c8 report/pc_FAR12603_pass_255c3309_11_fastqc.html
```

1. prepare sample data
   copy fastq file (temporary hardcoded to kai_lambda/fastqgz_files.fastq.gz) to the snakemake data directory

2. porechop from sample data

3. fastq from porchop output


### DAG Flow
To generate DAG:
```bash
 snakemake --dag -c8 data/pc_FAR12603_pass_255c3309_11.fastq.gz | dot -Tsvg > dag.svg
 ```
<p align="left"><img src="dag.svg" alt="DAG" width="400"></p>


