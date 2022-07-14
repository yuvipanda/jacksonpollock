""""""
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.axes import Axes
import inspect

def get_cmap(name):
    """
    Return one true cmap no matter what is being asked for
    """
    return cm.jet


old_get_title = Axes.get_title

def get_title(self, *args, **kwargs):
    old_title = old_get_title(self, *args, **kwargs)
    if not old_title:
        self.set_title("LABEL YOUR DAMN THINGS")
        old_title = old_get_title(self, *args, **kwargs)
    return old_title

Axes.get_title = get_title


old_plot = Axes.plot
def plot(self, *args, **kwargs):
    if not self.title._text:
        self.set_title("LABEL iYOUR DAMN CHARTS PLEASE OK?")
    return old_plot(self, *args, **kwargs)

Axes.plot = plot

from matplotlib import figure
old_getattribute = figure.Figure.__getattribute__

def fig_attribute(self, attr):
    old_value = old_getattribute(self, attr)
    calling_function_name = inspect.stack()[1].function
    stack = inspect.stack()
    if attr == '_suptitle' and any(s.function == 'suptitle' for s in stack):
        if old_value is None:
            self.suptitle("LABEL YOUR DAMN GRAPHS")
            return old_getattribute(self, attr)
        print("AHWHHAR")
        print(old_value)
    return old_getattribute(self, attr)

# figure.Figure.__getattribute__ = fig_attribute
plt.get_cmap = get_cmap

for cmap in plt.colormaps:
    if cmap != 'jet':


cmap_names = sorted(m for m in plt.colormaps if not m.endswith("_r"))

