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

df['cumsum_s'] = df['s'].cumsum()

print(df)
x_idx = np.arange(df.shape[0])

fig, ax = plt.subplots()

bar = ax.bar(x=x_idx,
             height=df['s'],
             align='center',
             tick_label=df['Ops'],
             alpha=0.7
             )

line = ax.plot(x_idx,
                df['cumsum_s'],
                ls='--',
                marker='o',
                color='r'
                )
#plt.ylim([0,500])
plt.tight_layout()
ax.set_xlabel('time_s')
ax.set_xticklabels(df['Ops'],rotation = 90)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, ncol=5)
plt.savefig(snakemake.output[0], bbox_inches="tight")
#plt.show()