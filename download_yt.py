import yt_dlp
import os


url='https://www.youtube.com/watch?v=hOGpFkEukjM&list=PLmOn9nNkQxJGuxM62QOkUwD_zroNZj-a7&index=2&pp=iAQB'
save_dir = './vedio'

    # 检查并创建目录
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 定义下载选项
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # 下载最高质量的视频和音频
    'outtmpl': os.path.join(save_dir, '%(title)s.%(ext)s'),  # 指定保存目录和文件命名格式
    #'merge_output_format': 'mp4',  # 合并视频和音频为mp4格式
    'progress_hooks': [lambda d: print(d['status']) if d['status'] == 'downloading' else None],
    # 'postprocessors': [{
    #     'key': 'FFmpegVideoConvertor',
    #     'preferedformat': 'mp4',  # 指定合并后的格式
    # }],
}

# 下载视频
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
