from pillowcase import fig_to_rgba
from pillowcase import write_mp4
from plot_world import plot_world
from datetime import datetime
import warnings

warnings.filterwarnings('ignore')

frames = []

for lon in range(180, -180, -5):
    start_time = datetime.now()
    print("plotting longitude {}".format(lon))
    frames.append(fig_to_rgba(plot_world(lon_0=lon)))
    print("duration: {}".format(datetime.now() - start_time))

write_mp4("spinning_globe.mp4", frames)
