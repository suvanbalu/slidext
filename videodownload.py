from pytube import YouTube  
import os
import re
import urllib



def download_yvideo(dest,links):
  for i in range(len(links)):
      try:  
          yt = YouTube(links[i])  
          title=yt.title
          title=title.split("|")
          title=title[0]
          print(title)
      except:         
          #to handle exception  
          print("Connection Error, Check your connectivity")  
      d_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
      try:  
          # downloading the video  
          d_video.download(dest,filename=title+".mp4")  
      except:  
          print(f"There is some Error for video no. {i+1}!")  
      print(f'Video {i+1} Download Successfully!') 
  return title

def download_ovideo(dest,links):
  for i in range(len(links)):
    try:
      urllib.request.urlretrieve(links[i], f"{dest}/video{i+1}.mp4")
      print(f"Video {i+1} Downloaded Successfully!")
    except:
      print(f"There is some Error for other video no. {i+1}!")


def read_file(file):
    try:
        with open(file,"r") as f:
            return f.read().splitlines()
    except:
        print("File not found!")
        return []

def checkyoutube(links):
  ylinks=[]
  olinks=[]
  for i in links:
    if re.search(r"youtube",i):
      ylinks.append(i)
    else:
      olinks.append(i)
  return ylinks,olinks

def videodownload(dest,links=None,file=False,filename=None):
  if file:
    links=read_file(filename)
  try:
    ylinks,olinks=checkyoutube(links)
  except:
    print("No links found!")

  if len(ylinks)>0:
    title=download_yvideo(dest,ylinks)
  if len(olinks)>0:
    try:
      download_ovideo(dest,olinks)
    except:
      print("Other links are not supported yet!")
  return title
    