import time
from queue import Queue
from threading import Thread

import cv2
import youtube_dl
from youtube_dl.extractor import SkylineWebcamsIE

from media_source_adaptor.common import StreamAdaptor


class SkylineWebcam(StreamAdaptor):
    """Adaptator for `skylinewebcams.com`
    """

    def __init__(self, url: str, queue_size: int = 128, fps_overwrite=None):
        """Adaptor constructor

        Args:
            url (str): URL of the SkylineWebcam to be extracted
        """
        ytd = youtube_dl.YoutubeDL()
        adaptator = SkylineWebcamsIE(ytd)
        info = adaptator.extract(url)
        self.real_url = info['url']
        self.capture = cv2.VideoCapture(self.real_url)
        self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 2)
        self.fps = self.capture.get(cv2.CAP_PROP_FPS)
        if fps_overwrite is not None:
            self.fps = fps_overwrite
        self.width = self.capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.q = Queue(maxsize=queue_size)
        self.stopped = False
        self.spf = 1.0 / self.fps
        self.spf_ms = int(self.spf * 1000)
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def read(self):
        return self.q.get()

    def update(self):
        while True:
            if self.capture.isOpened():
                status, frame = self.capture.read()
                if status:
                    self.q.put(frame)
            time.sleep(self.spf)

    def generator(self):
        """Iterator in forms of generator to get frames from the VideoCapture

        Yields:
            (bool, numpy.ndarray):  tuple with a boolean and the frame captured as Numpy array.
                                    The boolean reports if the gathering was successful or not
        """
        # TODO: Remove True as returned element of the tuple in the future
        while True:
            yield True, self.read()
