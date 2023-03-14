from depoco.plot_results import *
path = '/content/deep-point-map-compression/depoco/experiments/results/kitti/'
files = sorted(glob.glob(path+'*.pkl'))

f, ax = plt.subplots(2, 2)
ax = ax.flatten()
f.suptitle('Kitti Results')
genPlots(files, f, ax, draw_line=True, label='our', x_key='bpp')
for a in ax:
    a.grid()
    # a.set_ylim([0,None])
    a.legend()
plt.tight_layout()
plt.show()