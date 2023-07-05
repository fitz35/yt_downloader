import tkinter as tk
from gui.NewVideoFrame import NewVideoFrame
from params.params import VIDEOS_LIST_FILE_PATH
from youtube.VideoMetadata import VideoMetadata

from utils.utils import load_list_of_video, save_list_of_videos, validate_youtube_link

class MainFrame:

    videos_list : list[VideoMetadata]

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.videos_list = load_list_of_video(VIDEOS_LIST_FILE_PATH)
        self.create_widgets()

    def create_widgets(self) -> None:
        self.label = tk.Label(self.root, text="")
        self.label.grid(row=0, column=0, columnspan = 2)
        self.__reset_label()

        # Create an Entry widget
        self.yt_link_entry = tk.Entry(self.root, width=50)
        self.yt_link_entry.grid(row=1, column=0, padx=10, pady=10)

        self.button = tk.Button(self.root, text="Validez !", command=self.__add_new_vieo_action)
        self.button.grid(row=1, column=1, padx=10, pady=10)


    # ------------------------------ ACTIONS ------------------------------

    def __add_new_vieo_action(self) -> None:
        # check if the link is valid
        videoId = validate_youtube_link(self.yt_link_entry.get())
        if videoId is None:
            self.label.config(text="Invalid link, repaste it !")
            self.__reset_entry()
            self.root.after(5000, self.__reset_label)
            return
        # open the new video frame and attache the callback
        self.diag = NewVideoFrame(self.root, videoId, lambda x : self.__new_video_closed(x))
        self.__reset_entry()

    def __new_video_closed(self, video_data : VideoMetadata):
        self.videos_list.append(video_data)
        save_list_of_videos(self.videos_list, VIDEOS_LIST_FILE_PATH)
        print("new video added !")


    # ------------------------------ UI ------------------------------

    def __reset_label(self) -> None:
        self.label.config(text="Video link :")

    def __reset_entry(self) -> None:
        self.yt_link_entry.delete(0, 'end')

    