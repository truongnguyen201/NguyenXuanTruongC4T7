from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    a = ydl.extract_info('https://www.youtube.com/watch?v=Wv2rLZmbPMA', download = False)
print(a)
