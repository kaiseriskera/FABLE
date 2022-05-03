import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pathlib, os

#Create an empty dataframe first.
df = pd.DataFrame()

# get list of benchmark files in the 
bench_files = pathlib.Path("benchmarks").glob("*.tsv")
# bench_files = sorted(bench_files, key=os.path.getmtime)

#for bench_tsv_file in pathlib.Path('./workdir_mm2/benchmarks').glob("*.tsv"):
for bench_tsv_file in bench_files:
    #print(bench_tsv_file)
    tmp_df = pd.read_csv(bench_tsv_file, sep='\t')
    tmp_df.insert(0,"Process",bench_tsv_file.stem)
    df = df.append(tmp_df,ignore_index=True)
    df['Process'] = pd.Categorical(df.Process, categories=["Porechop", "NanoQ", "FastQC", "Pre-alignment_NanoPlot", "Vulcan", "Post-alignment_NanoPlot" ], ordered=True)
    df=df.sort_values('Process')
    df = df.reset_index(drop=True)
    
df['cumsum_cpu_time'] = df['cpu_time'].cumsum()
df['cumsum_max_vms']=df['max_vms'].cumsum()

print(df)
x_idx = np.arange(df.shape[0])

fig, (ax1,ax2)= plt.subplots(nrows=1, ncols=2, figsize=(12, 4))

# c = ['hotpink','palevioletred', 'pink', 'plum','thistle','lavender']
c = ['thistle','palevioletred','pink','lavender','lightsteelblue','powderblue']


# bar plot for cpu_time on ax1
df.plot(x='Process', y='cpu_time', kind='bar', color=c, ax=ax1)

# line plot for cumsum_cpu_time on ax1
df.plot(x='Process', y='cumsum_cpu_time', kind='line', marker='o', markersize=2, color='black', ax=ax1)

# bar plot for max_vms on ax2
df.plot(x='Process', y='max_vms', kind='bar', color=c, ax=ax2)

# line plot for cumsum_max_vms on ax2
df.plot(x='Process', y='cumsum_max_vms', kind='line', marker='o', markersize=2, color='black', ax=ax2)

plt.tight_layout()
ax1.title.set_text('CPU time')
ax2.title.set_text('Maximum VMS')
ax1.set_xticklabels(df['Process'],rotation = 30, horizontalalignment='right', fontsize='small')
ax1.set_ylabel('Seconds')
ax2.set_xticklabels(df['Process'],rotation = 30, horizontalalignment='right', fontsize='small')
ax2.set_ylabel('MegaBytes')
ax1.legend(loc='upper left', bbox_to_anchor=(0, 1.17), fontsize=7, fancybox=True, ncol=1)
ax2.legend(loc='upper left', bbox_to_anchor=(0, 1.17), fontsize=7, fancybox=True, ncol=1)
plt.savefig(snakemake.output[0], bbox_inches="tight")