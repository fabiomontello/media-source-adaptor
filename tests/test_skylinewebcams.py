from media_source_adaptor.skylinewebcams import SkylineWebcam
import cv2

test_url = "https://www.skylinewebcams.com/it/webcam/italia/lazio/roma/piazza-di-spagna.html"
test_res = {"width": 1920.0, "height": 1080.0, "fps": 30.0}


def test_creation():
    sw = SkylineWebcam(url=test_url)
    res = {"width": sw.width, "height": sw.height, "fps": sw.fps}
    assert res == test_res


def test_generation():
    sw = SkylineWebcam(url=test_url)
    cv2.namedWindow('IMG', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
    frame_limit = 100
    for i, (r, frame) in enumerate(sw.generator()):
        if i > frame_limit:
            return
        assert r == True
        cv2.imshow("IMG", frame)
        ch = cv2.waitKey(1)
        if ch == 27 or ch == ord("q") or ch == ord("Q"):
            break