from pytube import YouTube
import os 
import time

url = input("\nMasukan link yt : ")
print("\nDownloading Audio...")
time.sleep(2)
print(".")
time.sleep(3)
print(".")
time.sleep(4)
print(".")
yt = YouTube(url)
result = yt.streams.filter(only_audio=True).first()
output_file = result.download("music")
path, _ = os.path.splitext(output_file)

os.rename(output_file, path + '.mp3')
print("\nDone")
print("\n")
time.sleep(2)
print(yt.title, "Succes Downloading This Audio From YouTube")
time.sleep(4)
print("\n\nCreated By ChinuLz\n\n\n\n")