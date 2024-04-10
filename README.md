# nar

- Convert devided image from video.
- The image is seached simurary image.

## Install

```sh
pip3 install -r requirements.txt
```

## Prepare

For example `youtube-dl`:

```sh
brew install youtube-dl
```

and

```sh
brew install ffmpeg
```

## How

```sh
youtube-dl --no-part -f 160 -o "./video/%(id)s.%(ext)s" <your-video-url>
id=$(basename $(ls -t ./video/ | tail -n 1) .mp4)
mkdir $id
ffmpeg -i "video/$id.mp4" -vf fps=1 ./$id/output%04d.png
python3 measure_distance.py $id
```
