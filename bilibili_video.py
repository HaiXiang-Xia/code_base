'''
下载bilibili视频,仅用于bilibili视频下载(Bv视频)
直接调用,url为传入视频网址
bilibili_video.main(url)
'''

import requests
import os
import json
import re

headers = {
    'referer': 'https://www.bilibili.com/',
    'user-agent': '',
}

#视频，音频 合并
def video_audio(video,audio,file_name):
    #cm = 'ffmpeg -i ' + video + ' -i ' + audio + ' -acodec copy -vcodec copy ' + file_name + '.mp4'
    #subprocess.call(cm,shell=True)
    print('下载完毕，音视频合成中')
    os.system('ffmpeg -i ' + video + ' -i ' + audio + ' -acodec copy -vcodec copy ' + file_name + '.mp4')
    true = True
    if true:
        try:
            os.remove(video)
            os.remove(audio)
            print('删除源文件')
        except:
            print('删除源文件失败')
    print('视频文件合成结束!')

#下载
def download(url,videourl,audiourl):
    print('视频下载中...')
    date_mp4 = requests.get(url=videourl,headers=headers).content
    date_mp3 = requests.get(url=audiourl,headers=headers).content
    file_name = url.split('/')[4]
    path = os.getcwd()+'/'
    video = path+file_name+'video.mp4'
    audio = path+file_name+'audio.mp3'
    with open(video,'wb') as f:
        f.write(date_mp4)
    with open(audio,'wb') as f:
        f.write(date_mp3)
    video_audio(video,audio,path+file_name)

#传入视频网址    
def main(url):
    date = requests.get(url=url,headers=headers).text
    str_date = re.findall('window.__playinfo__=(.*?)</script>',date)[0]
    content = json.loads(str_date)
    videourl = content['data']['dash']['video'][0]['baseUrl']
    audiourl = content['data']['dash']['audio'][0]['baseUrl']
    download(url,videourl,audiourl)

if __name__ == "__main__":
    url = input("请输入视频网址:")
    main(url)
