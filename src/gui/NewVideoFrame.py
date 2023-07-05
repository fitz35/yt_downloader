import tkinter as tk
from typing import Callable
from pytube import YouTube

from youtube.VideoMetadata import ImportanceLevel, VideoMetadata

class NewVideoFrame:
    """
    add a video to the list
    """
    def __init__(self, parent: tk.Tk, videoId : str, onFinish : Callable[[VideoMetadata], None]) -> None:
        """
        create a dialog window to add video to the list
        @params parent : the tk root
        @params videoId : the new video id
        @params onFinish : callback on finish (take the video metadata as parameter)
        """
        self.parent = parent
        self.onFinish = onFinish

        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Custom Dialog")
        self.dialog.protocol("WM_DELETE_WINDOW", self.on_close)

        self.__create_widgets()

        # project yt
        yt = YouTube('http://youtube.com/watch?v={}'.format(videoId))
        print(yt.streams.filter(progressive=True, file_extension='mp4'))

    def __create_widgets(self) -> None:
        label = tk.Label(self.dialog, text="Enter your name:")
        label.pack()

        self.entry = tk.Entry(self.dialog)
        self.entry.pack()

        button = tk.Button(self.dialog, text="Submit", command=self.__submit_dialog)
        button.pack()

    def __submit_dialog(self) -> None:
        name = self.entry.get()
        self.onFinish(VideoMetadata("testUID", 720, ImportanceLevel.LOW))
        self.dialog.destroy()

    def on_close(self) -> None:
        self.dialog.destroy()