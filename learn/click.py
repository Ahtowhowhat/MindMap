import matplotlib.pyplot as plt

def callback(event):
    print(event.x, event.y)

fig, ax = plt.subplots()

fig.canvas.callbacks.connect('button_press_event', callback)
plt.show()
