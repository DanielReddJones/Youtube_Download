##################################################
# Author: Daniel Jones
# Interpreter: Python 11
# Operating System: Windows 10/Pop!_OS Linux
# Last edited: 9:19 AM 12/4/2022
# Editor: Pycharm/Vim
##################################################

from pytube import *
from tkinter import *
from tkinter import filedialog
from pytube.exceptions import *
import os

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

    download_button = Button(root, text="download", command=download_audio)
    download_button.grid(column=1, row=2)
    root.mainloop()


# grabs filepath and updates the label to display the new filepath.
def save_location():
    global filepath
    # if ran on Linux/macOS, will default to the original folder file is in. Otherwise, will open in C:\
    filepath = filedialog.askdirectory(initialdir=r"C:\Users")
    save_text = Label(root, text=filepath)
    save_text.grid(column=1, row=1)


# downloads audio to given filepath
def download_audio():

    try:
        yt_link = text_box.get('1.0', 'end')
        yt = YouTube(yt_link).streams.filter(only_audio=True)
        out_file = yt[0].download(filepath)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

    except NameError:
        err = Tk()
        err.geometry("150x100")
        err.anchor("center")
        err.title("Name Error")
        errlabel = Label(err, text="select a filepath,\n and insert a YouTube URL \nin the URL box.").grid(column=0, row=0)
        erbutt = Button(err, text="close", command=err.destroy).grid(column=0, row=1)
        err.mainloop()
    except RegexMatchError:
        err = Tk()
        err.geometry("150x100")
        err.anchor("center")
        err.title("Video Unavailable")
        errlabel = Label(err, text="invalid link.").grid(column=0, row=0)
        erbutt = Button(err, text="close", command=err.destroy).grid(column=0, row=1)
        err.mainloop()
    except VideoUnavailable:
        err = Tk()
        err.geometry("150x100")
        err.anchor("center")
        err.title("Video Unavailable")
        errlabel = Label(err, text="video unavailable").grid(column=1, row=0)
        erbutt = Button(err, text="close", command=err.destroy).grid(column=1, row=1)
        err.mainloop()
    except PermissionError:
        err = Tk()
        err.geometry("150x100")
        err.anchor("center")
        err.title("permissions Error")
        errlabel = Label(err, text="invalid path. \nSave somewhere else.").grid(column=0, row=0)
        erbutt = Button(err, text="close", command=err.destroy).grid(column=0, row=1)
        err.mainloop()
    except FileExistsError:
        err = Tk()
        err.geometry("150x100")
        err.anchor("center")
        err.title("permissions Error")
        errlabel = Label(err, text="File already exists!").grid(column=0, row=0)
        erbutt = Button(err, text="close", command=err.destroy).grid(column=0, row=1)
        err.mainloop()


if __name__ == "__main__":
    main()
