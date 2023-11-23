from colored import fg, attr
import pytube

# By Mubarak
print(f"""{fg(4)}      
 /$$     /$$ /$$$$$$$$
|  $$   /$$/|__  $$__/
 \  $$ /$$/    | $$   
  \  $$$$/     | $$   
   \  $$/      | $$   
    | $$       | $$   
    | $$       | $$   
    |__/       |__/    
      
      IG : myoubarak | GitHub: myoubarak{attr(0)}""")
print ("                                                               ")
youtube_link = input(f"{fg(4)}Enter the YouTube video link : {attr(0)}")

try:
    youtube = pytube.YouTube(youtube_link)
    audio = youtube.streams.filter(only_audio=True).first()
    audio.download()
    print ("                                                               ")
    print(f"{fg(4)}The audio file has been successfully downloaded!{attr(0)}")
except pytube.exceptions.VideoUnavailable:
    print(f"{fg(4)}The video is not available.{attr(0)}")