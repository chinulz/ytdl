from pytube import YouTube
import time

url = input("\nMasukan link yt : ")
print("\nDownloading Video...")
time.sleep(2)
print(".")
time.sleep(3)
print(".")
time.sleep(4)
print(".")
yt = YouTube(url)
yt.streams.get_highest_resolution().download('video')
print("\nDone")
print("\n")
time.sleep(2)
print(yt.title, "Succes Downloading This Video From YouTube")
time.sleep(4)
print("\n\nCreated By ChinuLz\n\n\n\n")