import logging

import pytest

from media_source_adaptor.common import ImageAdaptor, VideoAdaptor

LOG = logging.getLogger(__name__)
VIDEOS_LIST = [
    "/workspace/montello/datasets/test_dataset/480p.mp4", "/workspace/montello/datasets/test_dataset/640p.mp4",
    "/workspace/montello/datasets/test_dataset/720p.mp4"
]
IMAGES_LIST = [
    '/workspace/montello/datasets/test_dataset/s1.jpg', '/workspace/montello/datasets/test_dataset/s2.jpg',
    '/workspace/montello/datasets/test_dataset/s3.jpg'
]


@pytest.mark.parametrize(("path"), VIDEOS_LIST)
def test_video(path: str):
    video = VideoAdaptor(path)

    cnt = 0
    for i, elem in enumerate(video.generator()):
        cnt = i

    LOG.debug(f'Number of frames read: {cnt}')
    assert cnt > 0, "No frame read"


@pytest.mark.parametrize(("path"), VIDEOS_LIST)
def test_video_details(path: str):
    video = VideoAdaptor(path)
    details = video.details()
    assert details, "Video details not retrieved"
    LOG.debug(f'Video details: {details}')


@pytest.mark.parametrize(("path"), IMAGES_LIST)
def test_image(path: str):
    image = ImageAdaptor(path)
    img_read = image.generator()
    LOG.debug(img_read.shape)
    assert len(img_read.shape) == 3, 'Image shape not correct'
