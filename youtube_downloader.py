from pytube import *
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("video download screen")


def main():
    main_screen()


# Tkinter screen setup
def main_screen():
    url_label = Label(root, text="URL: ").grid(column=0, row=0)
    text_box = Text(root, height=1, width=30).grid(column=1, row=0)

    save_label = Label(root, text="save to: ").grid(column=0, row=1)
    save_button = Button(root, text="...", command=save_location).grid(column=2, row=1)
    save_text = Label(root, text="c:\\").grid(column=1, row=1)

    download_button = Button(root, text="download", command=download_vid).grid(column=1, row=2)
    root.mainloop()

# grabs filepath and updates the label to display the new filepath.
def save_location():
    global filepath
    filepath = filedialog.askdirectory(initialdir=r"C:\Users")
    save_text = Label(root, text=filepath).grid(column=1, row=1)


# placeholder for now. Will update later to download the videos to the filepath.
def download_vid():
    try:
        yt = YouTube(text_box.get('1.0', 'end'))
        mp3Files = yt.filter('mp3')
        my_vid = youtube.streams.first()
        my_vid.download(filepath)


    except NameError:
        print("select a filepath, and insert a youtube URL in the URL box.")


if __name__ == "__main__":
    main()
