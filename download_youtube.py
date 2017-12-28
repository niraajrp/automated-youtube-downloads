import requests
from bs4 import BeautifulSoup
import subprocess
import sys
import os

def getVideoInfo():
    query = input("Enter the Song \n")
    query = query.lower().split()
    query = "+".join(query)
    # print(query)
    url = "https://www.youtube.com/results?search_query="+query
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "lxml")
    # print(soup.prettify())
    tag = soup.find('a', {'rel': 'spf-prefetch'})
    title = tag.text
    video_url = "https://www.youtube.com" + tag.get('href')
    return video_url
    pass

def downloadSong():
    link = getVideoInfo()
    print(link)
    subprocess.call('youtube-dl.exe -i ' + link, shell=True)
    # subprocess.call('youtube-dl.exe -i --extract-audio --audio-format mp3 ' + link, shell=True)
    pass

def deleteIncomplete():
    dir_name = "C:/Users/niraj.pandey/PycharmProjects/YouTube/testing_123/"
    test = os.listdir(dir_name)
    for item in test:
        if item.endswith(".part"):
            os.remove(os.path.join(dir_name, item))
            pass
        pass
    pass

if __name__ == '__main__':
    # result = getVideoInfo()
    # print(result)
    downloadSong()
    deleteIncomplete()


