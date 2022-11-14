##################################################
# Author: Daniel Jones
# Interpreter: Python 11
# Operating System: Windows 10/Pop!_OS Linux
# Last edited: 9:19 AM 11/14/2022
# Editor: Pycharm/Vim
##################################################

from pytube import *
from tkinter import *
from tkinter import filedialog
from pytube.exceptions import *

# global TK fields
root = Tk()
root.title("video download screen")
url_label = Label(root, text="URL: ")
url_label.grid(column=0, row=0)
text_box = Text(root, height=1, width=30)
text_box.grid(column=1, row=0)


def main():
    main_screen()


# Tkinter screen setup
def main_screen():
    save_label = Label(root, text="save to: ")
    save_label.grid(column=0, row=1)
    save_button = Button(root, text="...", command=save_location)
    save_button.grid(column=2, row=1)
    save_text = Label(root, text="c:\\")
    save_text.grid(column=1, row=1)

    download_button = Button(root, text="download", command=download_vid)
    download_button.grid(column=1, row=2)
    root.mainloop()


# grabs filepath and updates the label to display the new filepath.
def save_location():
    global filepath
    # if ran on Linux/macOS, will default to the original folder file is in. Otherwise, will open in C:\
    filepath = filedialog.askdirectory(initialdir=r"C:\Users")
    save_text = Label(root, text=filepath)
    save_text.grid(column=1, row=1)


# placeholder for now. Will update later to download the videos to the filepath.
def download_vid():

    try:
        yt_link = text_box.get('1.0', 'end')
        yt = YouTube(yt_link).streams.filter(only_audio=True)
        yt[0].download(filepath)

    except NameError:
        print("select a filepath, and insert a YouTube URL in the URL box.")
    except RegexMatchError:
        print("invalid link.")
    except VideoUnavailable:
        print("video unavailable")

if __name__ == "__main__":
    main()
