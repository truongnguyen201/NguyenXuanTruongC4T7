from __future__ import unicode_literals
import youtube_dl

lisy_download = ['https://www.youtube.com/watch?v=LPSRZQ58lXM', 'https://www.youtube.com/watch?v=XFL-HutxeFo']
list_info= []
for link in lisy_download:
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        a = ydl.extract_info(link, download = False)
        list_info.append(a)
    print(a)