import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pathlib, os

#Create an empty dataframe first.
df = pd.DataFrame()

# get list of benchmark files in the 
bench_files = pathlib.Path("benchmarks").glob("*.tsv")
bench_files = sorted(bench_files, key=os.path.getmtime)

#for bench_tsv_file in pathlib.Path('./workdir_mm2/benchmarks').glob("*.tsv"):
for bench_tsv_file in bench_files:
    #print(bench_tsv_file)
    tmp_df = pd.read_csv(bench_tsv_file, sep='\t')
    tmp_df.insert(0,"Ops",bench_tsv_file.stem)
    df = df.append(tmp_df,ignore_index=True)

# df['cumsum_s'] = df['s'].cumsum()
df['cumsum_cpu_time'] = df['cpu_time'].cumsum()
df['cumsum_max_vms'] = df['max_vms'].cumsum()

print(df)
x_idx = np.arange(df.shape[0])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3))

cpu_bar = ax1.bar(x=x_idx,
             height=df['cpu_time'],
             align='center',
             tick_label=df['Ops'],
             alpha=0.7
             )

cpu_line = ax1.plot(x_idx,
                df['cumsum_cpu_time'],
                ls='--',
                marker='o',
                color='r'
                )

vms_bar = ax2.bar(x=x_idx,
             height=df['max_vms'],
             align='center',
             tick_label=df['Ops'],
             alpha=0.7
             )

vms_line = ax2.plot(x_idx,
                df['cumsum_max_vms'],
                ls='--',
                marker='o',
                color='r'              
#plt.ylim([0,500])
plt.tight_layout()
ax1.set_xlabel('time_cpu_time')
ax1.set_xticklabels(df['Ops'],rotation = 90)
ax2.set_xlabel('time_max_vms')
ax2.set_xticklabels(df['Ops'],rotation = 90)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, ncol=5)
plt.savefig(snakemake.output[0], bbox_inches="tight")
#plt.show()