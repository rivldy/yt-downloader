import click
import os

def generate_title(title):
  stroke = len(title) * "-"
  print(f"\n{stroke}")
  print(title)
  print(f"{stroke}\n")

def download(video):
  os.system("cls")
  generate_title("YouTube Downloader by rivldy")
  click.echo(f"Judul Video: {video.title}\n")
  click.echo("Harap tunggu...\n")
  
  streams_list = []
  
  count = 1
  for q in video.streams.filter(progressive=True, file_extension="mp4"):
    streams_list.append(q)
    count += 1

  click.echo("Pilih kualitas :")
  for strm in streams_list:
    size = strm.filesize / 1000000
    click.echo(f"[{streams_list.index(strm) + 1}] {strm.resolution} - " + "%.2f MB" % size)
  
  stream_choice = int(input("Masukkan pilihan >> ")) - 1
  stream = streams_list[stream_choice]
  itag = stream.itag
  vid = video.streams.get_by_itag(itag)
  click.echo("Video sedang didownload, harap tunggu...")
  vid.download()
  click.echo("[Success] Video telah didownload!")