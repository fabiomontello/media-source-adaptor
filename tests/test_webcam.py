from media_source_adaptor.webcam import WebcamStreamAdaptor
import cv2


def test_creation():
    sw = WebcamStreamAdaptor()
    res = {"width": sw.width, "height": sw.height, "fps": sw.fps}
    assert res


def test_generation():
    sw = WebcamStreamAdaptor()
    cv2.namedWindow('IMG', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
    for i, (r, frame) in enumerate(sw.generator()):
        assert r
        cv2.imshow("IMG", frame)
        ch = cv2.waitKey(1)
        if ch == 27 or ch == ord("q") or ch == ord("Q"):
            break