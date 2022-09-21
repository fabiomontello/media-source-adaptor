from media_source_adaptor.common import VideoAdaptor
import cv2


class WebcamStreamAdaptor(VideoAdaptor):
    def __init__(self, id=0):
        self.capture = cv2.VideoCapture(id)
        if not self.capture.isOpened():
            raise OSError("Cannot open the camera stream")

        self.fps = self.capture.get(cv2.CAP_PROP_FPS)
        self.width = self.capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT)