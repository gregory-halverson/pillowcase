import matplotlib
from six import string_types

matplotlib.use('Agg')

import imageio as io
import numpy as np
from PIL import Image
from matplotlib.figure import Figure


def fig_to_rgba(fig):
    """
    http://www.icare.univ-lille1.fr/wiki/index.php/How_to_convert_a_matplotlib_figure_to_a_numpy_array_or_a_PIL_image
    """
    # render the canvas
    fig.canvas.draw()

    # get canvas dimensions
    w, h = fig.canvas.get_width_height()

    # get ARGB array
    data = np.fromstring(fig.canvas.tostring_argb(), dtype=np.uint8)
    data.shape = (w, h, 4)

    # roll alpha channel from ARGB to RGBA
    data = np.roll(data, 3, axis=2)

    return data


def rgba_array_to_pillow(fig):
    """
    http://www.icare.univ-lille1.fr/wiki/index.php/How_to_convert_a_matplotlib_figure_to_a_numpy_array_or_a_PIL_image
    """
    # render figure to array
    data = fig_to_rgba(fig)

    # load array into pillow image
    image = Image.frombytes("RGBA", data.shape[:2], data.tostring())

    return image


def get_image_array(image):
    if isinstance(image, np.ndarray):
        return image
    elif isinstance(image, Figure):
        return fig_to_rgba(image)
    elif isinstance(image, Image.Image):
        return np.array(image)
    else:
        return np.array(image)


def write_gif(filename, frames, mode='I', duration=0.1):
    if not isinstance(filename, string_types) or not filename.endswith('.gif'):
        raise ValueError("invalid filename")

    if not isinstance(frames, (list, tuple)) or len(frames) == 0:
        raise ValueError("invalid frames")

    with io.get_writer(filename, mode=mode, duration=duration) as writer:
        for frame in frames:
            frame_array = get_image_array(frame)
            writer.append_data(frame_array)


def write_mp4(filename, frames, fps=20):
    if not isinstance(filename, string_types) or not filename.endswith('.mp4'):
        raise ValueError("invalid filename")

    if not isinstance(frames, (list, tuple)) or len(frames) == 0:
        raise ValueError("invalid frames")

    with io.get_writer(filename, fps=fps) as writer:
        for frame in frames:
            frame_array = get_image_array(frame)
            writer.append_data(frame_array)
