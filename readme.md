# 下載youtube影片的工具

[來源](https://github.com/yt-dlp/yt-dlp)

可以直接下載下來執行，不需要透過python

指令:
```
yt-dlp.exe -P "要儲存的目錄" -f "bestvideo+bestaudio/best" URL "要下載的url"
```

似乎有依賴ffmpeg，下載指定bestvideo+bestaudio/best不會合併時，要裝一下
[ffmpeg](https://ffmpeg.org/download.html)


要自行編寫的話，
套件
```
pip install yt-dlp
```
