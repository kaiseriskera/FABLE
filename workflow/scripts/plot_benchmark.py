import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("report/Benchmarks/benchfile2.csv")
# , names=["sample/process","FastQC", "Minimap2", "mm2_sam_to_bam", "NanoFilt", "Post-alignment_NanoPlot", "Pre-alignment_NanoPlot", "PoreChop"], header=None,skiprows=1)
xprocessvalues = df['process'].values
x = np.arange(len(xprocessvalues))
w = 0.15
plt.rcdefaults()
fig, ax = plt.subplots()

plt.bar(x, df['PoreChop'].values, width=w, label='PoreChop')
plt.bar(x+w, df['NanoFilt'].values, width=w, label='NanoFilt')
plt.bar(x+2*w, df["FastQC"].values, width=w, label='FastQC')
plt.bar(x+3*w, df["Pre-alignment_NanoPlot"].values, width=w, label='Pre-alignment_NanoPlot')
plt.bar(x+4*w, df["Minimap2"].values, width=w, label='Minimap2-alignment_NanoPlot')
plt.bar(x+5*w, df["mm2_sam_to_bam"].values, width=w, label='mm2_sam_to_bam')
plt.bar(x+6*w, df["Post-alignment_NanoPlot"].values, width=w, label='Post-alignment_NanoPlot')
plt.xticks(x, xprocessvalues)

#plt.ylim([0,500])
plt.tight_layout()
ax.set_xlabel('X label')
ax.set_xticklabels(xprocessvalues,rotation = 45)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, ncol=5)
plt.savefig("report/Benchmarks/dfbench.png", bbox_inches="tight")
#plt.show()