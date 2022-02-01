import os.path

import cv2


class ImageAdaptor:

    def __init__(self, image_dir: str):
        assert os.path.isfile(image_dir), "Image not found in the directory"
        self.capture = cv2.imread(image_dir)
        self.capture = cv2.cvtColor(self.capture, cv2.COLOR_RGB2BGR)

    def generator(self):
        return self.capture


class VideoAdaptor:

    def __init__(self, video_dir: str):

        assert os.path.isfile(video_dir), "Video not found in the directory"
        self.capture = cv2.VideoCapture(video_dir)
        assert self.capture.isOpened(), "File is not a video or is corrupted"

        self.fps = self.capture.get(cv2.CAP_PROP_FPS)
        self.width = self.capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def generator(self):
        success, frame = self.capture.read()
        while (success):
            yield frame
            success, frame = self.capture.read()

    def details(self):
        return {'fps': self.fps, 'width': self.width, 'height': self.height}


class StreamAdaptor:
    pass
