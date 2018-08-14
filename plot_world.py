from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


def plot_world(lat_0=0, lon_0=0, figsize=(8, 8), scale=0.5):
    fig = plt.figure(facecolor='white', figsize=figsize)
    m = Basemap(projection='ortho', resolution=None, lat_0=lat_0, lon_0=lon_0)
    m.bluemarble(scale=scale)

    return fig
