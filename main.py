from __future__ import unicode_literals
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import os
import youtube_dl
from kivy.config import Config

Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '900')

class Root(BoxLayout):
    pass

    def download(self, url, path):

        if url:

            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',

                }],

            }

            if path != '.':
                file_path = path
            else:
                file_path = os.path.abspath(os.curdir)

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:

                info_dict = ydl.extract_info(url, download=True)
                fn = ydl.prepare_filename(info_dict)
                filename = os.path.splitext(fn)[0]+'.mp3'

                os.rename(os.path.abspath(os.curdir) + '/' + filename, file_path + '/' + filename)


class MyApp(App):
    def build(self):
        return Root()


if __name__ == '__main__':
    MyApp().run()