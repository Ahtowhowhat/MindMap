import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.axes import Axes

freqs = np.arange(2, 20, 3)

# fig, ax = plt.subplots()
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
# plt.subplots_adjust(bottom=0.2)
t = np.arange(0.0, 1.0, 0.001)
s = np.sin(2 * np.pi * freqs[0] * t)
l, = plt.plot(t, s, lw=2)


class Index:
    ind = 0

    def next(self, event, button):
        self.ind += 1
        i = self.ind % len(freqs)
        ydata = np.sin(2 * np.pi * freqs[i] * t)
        l.set_ydata(ydata)
        plt.draw()


    def prev(self, event):
        self.ind -= 1
        i = self.ind % len(freqs)
        ydata = np.sin(2 * np.pi * freqs[i] * t)
        l.set_ydata(ydata)
        plt.draw()


callback = Index()
axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(Axes(ax.figure, [0.81, 0.05, 0.1, 0.075]), 'Next', color=(0, 0, 0, 0), hovercolor=(.2, .2, .2, .5))
bnext.on_clicked(lambda event: callback.next(event, button=axprev))
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)



plt.show()

