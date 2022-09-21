"""Main script to test the code

This script can be run with `python main.py` and it can be used as template to interact
with the library.
"""

import cv2

from media_source_adaptor.skylinewebcams import SkylineWebcam
from media_source_adaptor.webcam import WebcamStreamAdaptor


def test_webcam():
    web = WebcamStreamAdaptor()
    print(web.details())
    cv2.namedWindow('IMG', cv2.WINDOW_KEEPRATIO)
    for _, frame in web.generator():
        cv2.imshow("IMG", frame)
        ch = cv2.waitKey(1)
        if ch == 27 or ch == ord("q") or ch == ord("Q"):
            break


def test_stream():
    url = "https://www.skylinewebcams.com/it/webcam/italia/lazio/roma/piazza-di-spagna.html"
    sw = SkylineWebcam(url=url)
    print(sw.width, sw.height, sw.fps)
    cv2.namedWindow('IMG', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
    for _, frame in sw.generator():
        cv2.imshow("IMG", frame)
        ch = cv2.waitKey(1)
        if ch == 27 or ch == ord("q") or ch == ord("Q"):
            break


if __name__ == "__main__":
    test_webcam()
