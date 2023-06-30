import tkinter as tk
from typing import Callable

from youtube.VideoMetadata import ImportanceLevel, VideoMetadata

class NewVideoFrame:
    """
    add a video to the list
    """
    def __init__(self, parent: tk.Tk, onFinish : Callable[[VideoMetadata], None]) -> None:
        """
        create a dialog window to add video to the list
        @params parent : the tk root
        @params onFinish : callback on finish
        """
        self.parent = parent
        self.onFinish = onFinish

        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Custom Dialog")
        self.dialog.protocol("WM_DELETE_WINDOW", self.on_close)

        self.__create_widgets()

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