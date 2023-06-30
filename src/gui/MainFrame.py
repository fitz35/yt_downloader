import tkinter as tk
from gui.NewVideoFrame import NewVideoFrame
from params.params import VIDEOS_LIST_FILE_PATH
from youtube.VideoMetadata import VideoMetadata, load_list_of_video, save_list_of_videos

from utils.utils import validate_youtube_link

class MainFrame:

    videos_list : list[VideoMetadata]

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.videos_list = load_list_of_video(VIDEOS_LIST_FILE_PATH)
        self.create_widgets()

    def create_widgets(self) -> None:
        self.label = tk.Label(self.root, text="Video link :")
        self.label.grid(row=0, column=0, columnspan = 2)

        # Create an Entry widget
        self.yt_link_entry = tk.Entry(self.root, width=50)
        self.yt_link_entry.grid(row=1, column=0, padx=10, pady=10)

        self.button = tk.Button(self.root, text="Validez !", command=self.button_clicked)
        self.button.grid(row=1, column=1, padx=10, pady=10)

    def button_clicked(self) -> None:
        print(validate_youtube_link(self.yt_link_entry.get()))
        # open the new video frame and attache the callback
        self.diag = NewVideoFrame(self.root, lambda x : self.newVideoClosed(x))

    def newVideoClosed(self, video_data : VideoMetadata):
        self.videos_list.append(video_data)
        save_list_of_videos(self.videos_list, VIDEOS_LIST_FILE_PATH)
        print("close new video closed")