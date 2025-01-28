# music-video-tools
Tools for Generating Music Video 

## audio_to_video.py
This script takes an input audio file (mp3, wav) and slices it into chunks.
Each chunk is graphed using matplotlib, and then stitched together using ffmpeg via moviepy

I personally like having the graph colors change, so I added a list of hex colors to pass
into matplotlib when plotting graphs.  I also prefer putting two identical graphs one above the other -
it seems more visually appealing.  For that reason I added a "start color offset", so I can experiment
with having two colors simultaneously.

### Usage
$ python audio_to_video.py
```shell
Filename: ..\sample.mp3
Need to process 225100 frames
Start color offset [0|1]: 0
Total Counts:  409
MoviePy - Building video audio_visualization.webm.
MoviePy - Writing video audio_visualization.webm

MoviePy - Done !
MoviePy - video ready audio_visualization.webm
```

This script generates files such as <a href="sample/sample.webm" alt="Sample output">

## Examples
I use this in tandem with a background video, and the originating audio file to generate videos like these:
- https://www.youtube.com/watch?v=1Q24-CfulRc&list=PL6jPzfWSvpLiG38fv6MB4q3eljghlKZaJ
