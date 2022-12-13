import click
import os
from pytube import Playlist
import video

def download(url):
  os.system("cls")
  video.generate_title("YouTube Downloader by rivldy")
  playlist = Playlist(url)
  click.echo(f"Judul Playlist: {playlist.title}")
  click.echo(f"Diupload Oleh: {playlist.owner}\n")

  count = 1
  playlist_dict = {}
  for p in playlist.videos:
    playlist_dict[count] = p.title
    count += 1
  
  for key in playlist_dict:
    click.echo(f"[{key}] {playlist_dict[key]}")
  
  try:
    playlist_choice = int(input("\nMasukkan pilihan >> ")) - 1
    vid = playlist.videos[playlist_choice]
    click.echo(f"\nJudul: {vid.title}")
    is_sure = input("Apakah kamu yakin (Y/n) >> ").lower()
    if is_sure == "n": return click.echo("Program keluar!")
    elif is_sure == "" or is_sure == "y":
      video.download(vid)
    else:
      click.echo("[Error] Pilihan tidak tersedia!")
      
  except IndexError:
    click.echo("[Error] Pilihan tidak tersedia!")