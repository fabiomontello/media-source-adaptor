from media_source_adaptor.common import StreamAdaptor
import youtube_dl
from youtube_dl.extractor import SkylineWebcamsIE
import cv2


class SkylineWebcam(StreamAdaptor):
    """[summary]

    Args:
        StreamAdaptor ([type]): [description]
    """
    
    def __init__(self, url: str):
        """[summary]

        Args:
            url (str): [description]
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
        """[summary]

        Yields:
            [type]: [description]
        """
        while True:
            yield self.capture.read()
