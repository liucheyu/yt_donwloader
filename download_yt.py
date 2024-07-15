import yt_dlp
import os

savePath = './vedio'

# 定义下载选项
ydl_opts = {
    'format': 'bestvideo/best',  # 下载最佳视频和音频质量
    'outtmpl': os.path.join(savePath, '%(title)s.%(ext)s'),        # 下载后的文件命名格式
    'progress_hooks': [lambda d: print(d['status']) if d['status'] == 'downloading' else None]
}

# 下载视频
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=hOGpFkEukjM&list=PLmOn9nNkQxJGuxM62QOkUwD_zroNZj-a7&index=2&pp=iAQB'])
