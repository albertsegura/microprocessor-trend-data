import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from collections import OrderedDict

matplotlib.rcParams['pdf.fonttype'] = 42


# Data input
cores       = [map(float,i.split()) for i in open("./data/cores.dat").readlines()]
frequency   = [map(float,i.split()) for i in open("./data/frequency.dat").readlines()]
specint     = [map(float,i.split()) for i in open("./data/specint.dat").readlines()]
transistors = [map(float,i.split()) for i in open("./data/transistors.dat").readlines()]
watts       = [map(float,i.split()) for i in open("./data/watts.dat").readlines()]

cores       = OrderedDict(cores)
frequency   = OrderedDict(frequency)
specint     = OrderedDict(specint)
transistors = OrderedDict(transistors)
watts       = OrderedDict(watts)

fig, ax = plt.subplots(figsize=(5,4))
plt.subplots_adjust(left=0.17, right=0.985, top=0.95, bottom=0.3)

tstart = 1970
tmulticore = 2004.25
tend = 2021

plt.title('Microprocessor Trends', fontsize=8)
# Plot data
ax.scatter(transistors.keys(),   transistors.values(),   color='0.5',   marker='s',   s=5, zorder=2,   label='Transistors ($10^{3}$)')
ax.scatter(specint.keys(),       specint.values(),       color='0.1',   marker='v',   s=5, zorder=2,   label='Single-Thread Perf.\n(SpecINT x $10^{3}$)')
ax.scatter(frequency.keys(),     frequency.values(),     color='0.625',   marker='^',   s=5, zorder=2,   label='Frequency (Mhz)')
ax.scatter(watts.keys(),         watts.values(),         color='0.3',   marker='D',   s=5, zorder=2,   label='Typical Power (W)')
ax.scatter(cores.keys(),         cores.values(),         color='0.8',   marker='o',   s=5, zorder=2,   label='Logical Cores')

# Multiprocessor era line
plt.plot([tmulticore, tmulticore], [-1, 1e8], '--', color='0', alpha=0.25, linewidth=1,   zorder=-1)

# x_start
xmargin=0.75
ymargin=0.35
ax.broken_barh([(tstart+xmargin,      tmulticore-tstart-2*xmargin)],   (-1+ymargin,   2-2*ymargin),   facecolors='0.7',   alpha=1,   zorder=1)
ax.broken_barh([(tmulticore+xmargin,   tend-tmulticore-2*xmargin)],   (-1+ymargin,   2-2*ymargin),   facecolors='0.7',   alpha=1,   zorder=1)
# ax.broken_barh([(tstart,      tmulticore-tstart)],   (1e7,   1e8),   facecolors='tab:red',    alpha=0.1,   zorder=-2)
# ax.broken_barh([(tmulticore,   tend-tmulticore)],   (1e7,   1e8),   facecolors='tab:blue',   alpha=0.1,   zorder=-2)

plt.text(tstart+(tmulticore-tstart)/2, -0.05, 'Single-core era', fontsize=7, horizontalalignment='center', verticalalignment='center', color='0.2')
plt.text(tmulticore+(tend-tmulticore)/2, -0.05, 'Multi-core era', fontsize=7, horizontalalignment='center', verticalalignment='center', color='0.2')

# plt.text(2021.5, 1e7, 'Transistors ($10^{3}$)', fontsize=8, horizontalalignment='left', verticalalignment='center')
# plt.text(2021.5, 1e5, 'Single-Thread\nPerformance\n(SpecINT x $10^{3}$)', fontsize=8, horizontalalignment='left', verticalalignment='center')
# plt.text(2021.5, 3*1e3, 'Frequency (Mhz)', fontsize=8, horizontalalignment='left', verticalalignment='center')
# plt.text(2021.5, 2*1e2, 'Typical Power\n(Watts)', fontsize=8, horizontalalignment='left', verticalalignment='center')
# plt.text(2021.5, 3*1e1, 'Logical Cores', fontsize=8, horizontalalignment='left', verticalalignment='center')

credits= "Data up to year 2010 collected by M. Horowitz, F. Labonte, O. Shacham, K. Olukotun, L. Hammond, and C. Batten.\n\
Data spanning 2010-2017 collected by K. Rupp. \
Data spanning 2017-2020 collected by A. Segura."
plt.text(1970,-5, credits, fontsize=4.5, horizontalalignment='left', verticalalignment='center')

# Axis configuration
ax.grid(True)
ax.set_axisbelow(True)

ax.set_yscale('symlog')
ax.set_xlim(tstart, tend)
ax.set_ylim(-1, 1e8)
ax.get_yaxis().set_ticks([1e0, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8])
# ax.set_yticklabels([ "1" if i==0 else "$10^{"+str(i)+"}$" for i in range(0,9)] )


plt.minorticks_off()
ax.tick_params(axis="x", grid_color="black", direction="in", which='both', bottom=True, top=False, labelbottom=True, labeltop=False, labelsize=8, grid_linestyle=(0,(1,4)), grid_alpha=0.25)
ax.tick_params(axis="y", grid_color="black", direction="in", which='both', left=True, right=False, labelleft=True, labelright=False, labelsize=8, grid_linestyle=(0,(1,4)), grid_alpha=0.25)

# Legend
ax.legend(loc='upper left', bbox_to_anchor=(0.025, 0.975), ncol=1, prop={'size':7}, fancybox=False, framealpha=1, edgecolor="black")


plt.savefig("processor_trends.pdf", bbox_inches='tight')
plt.savefig("processor_trends.png", bbox_inches='tight', dpi=300)

