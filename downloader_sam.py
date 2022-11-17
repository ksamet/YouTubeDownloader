import time
from pytube import YouTube

print("YouTube Downloader")
link = input("Link:   ")

yt = YouTube(link)

ys = yt.streams.get_highest_resolution()

print("indiriliyor....")
print("Lütfen Bekleyiniz.")

ys.download()

print("indirildi!")

time.sleep(10)