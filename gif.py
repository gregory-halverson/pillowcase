import base64

__author__ = 'Gregory Halverson'


class GIF(object):
    def __init__(self, input):
        self.filename = input

        self._bytes = None
        self._frames = None
        self._array = None

    def _repr_html_(self):
        return self.html

    @property
    def array(self):
        if self._array is None:
            try:
                self._array = np.array(imageio.imread(self.bytes))
                return self._array
            except:
                pass

        return self._array

    @property
    def bytes(self):
        if self._bytes is None:
            with open(self.filename, "rb") as f:
                self._bytes = f.read()

        return self._bytes

    #     @property
    #     def frames(self):
    #         pass

    @property
    def b64(self):
        return base64.b64encode(self.bytes).decode()

    @property
    def uri(self):
        return "data:image/gif;base64,{0}".format(self.b64)

    @property
    def html(self):
        return '<img src="{0}"/>'.format(self.uri)