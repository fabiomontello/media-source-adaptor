# Media Source Adaptor

This is a small tool to ease the creation of an iteratior indipendently from the media source input (image/video/stream).
Install the library with poetry.

Video Adaptor:
```
from media_source_adaptor.common import VideoAdaptor

adaptor = VideoAdaptor('path/to/.mp4/file')

for success, frame in adaptor.generator():
	...

```

Stream Adaptor
```
from media_source_adaptor.common import SkylineWebcam

adaptor = SkylineWebcam('https://www.skylinewebcams.com/en/webcam/italia/lazio/roma/piazza-di-spagna.html')

for success, frame in adaptor.generator():
	...

```