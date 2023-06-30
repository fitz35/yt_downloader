import tkinter as tk

from gui.MainFrame import MainFrame

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Tkinter Example")

    # Create an instance of the MyWindow class
    window = MainFrame(root)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == '__main__':
    main()
