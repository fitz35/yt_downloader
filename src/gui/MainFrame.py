import tkinter as tk

from utils.utils import validate_youtube_link

class MainFrame:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.create_widgets()

    def create_widgets(self) -> None:
        self.label = tk.Label(self.root, text="Video link :")
        self.label.pack()

        # Create an Entry widget
        self.yt_link_entry = tk.Entry(self.root, width=50)
        self.yt_link_entry.pack()

        self.button = tk.Button(self.root, text="Click Me", command=self.button_clicked)
        self.button.pack()

    def button_clicked(self) -> None:
        print("Button clicked")
        print(validate_youtube_link(self.yt_link_entry.get()))