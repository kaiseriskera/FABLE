# ngs_bench
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

