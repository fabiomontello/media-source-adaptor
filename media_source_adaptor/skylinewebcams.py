from media_source_adaptor.common import StreamAdaptor
import youtube_dl
from youtube_dl.extractor import SkylineWebcamsIE
import cv2
import numpy


class SkylineWebcam(StreamAdaptor):
    """Adaptator for `skylinewebcams.com`
    """

    def __init__(self, url: str):
        """Adaptor constructor

        Args:
            url (str): URL of the SkylineWebcam to be extracted
        """
        ytd = youtube_dl.YoutubeDL()
        adaptator = SkylineWebcamsIE(ytd)
        info = adaptator.extract(url)
        self.real_url = info['url']
        self.capture = cv2.VideoCapture(self.real_url)
        self.fps = self.capture.get(cv2.CAP_PROP_FPS)
        self.width = self.capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def generator(self):
        """Iterator in forms of generator to get frames from the VideoCapture

        Yields:
            (bool, numpy.ndarray):  tuple with a boolean and the frame captured as Numpy array.
                                    The boolean reports if the gathering was successful or not
        """
        while True:
            yield self.capture.read()
