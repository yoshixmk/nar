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
youtube-dl -f 160 <your-video-url>
ffmpeg -i "<your>.mp4" -vf fps=1 ./<output-dir>/output%04d.png

```
