import click
from pytube import YouTube,  exceptions
import playlist
import video

DOWNLOAD_TYPES = {
  "video": "Video",
  "playlist": "Playlist"
}

@click.command()
@click.argument("type", type=click.Choice(DOWNLOAD_TYPES.keys()), default="video")
@click.argument("url", type=str)
def yt_downloader(type, url):
  if type == "video":
    try:
      vid = YouTube(url)
      video.download(vid)
    except exceptions.RegexMatchError:
      print("[Error] URL tidak ditemukan!")
  elif type == "playlist":
    playlist.download(url)



if __name__ == "__main__":
  yt_downloader()