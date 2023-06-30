import tkinter as tk
from gui.NewVideoFrame import NewVideoFrame

from utils.utils import validate_youtube_link

class MainFrame:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
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
        self.diag = NewVideoFrame(self.root, lambda : self.newVideoClosed())

    def newVideoClosed(self):
        print("close new video closed")