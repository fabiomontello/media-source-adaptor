import pytest

from media_source_adaptor.common import VideoAdaptor


@pytest.mark.parametrize(("url"), [
    "/workspace/montello/datasets/test_dataset/480p.mp4", "/workspace/montello/datasets/test_dataset/640p.mp4",
    "/workspace/montello/datasets/test_dataset/720p.mp4"
])
def test_video(url: str):
    video = VideoAdaptor(url)

    for elem in video.generator():
        print(elem.shape)
