from pytube import *
from tkinter import *

def main():

    main_screen()



#Tkinter screen setup
def main_screen():
    placeholder_text = "filepath"
    
    root = Tk()
    root.title("video download screen")
    url_label = Label(root, text = "URL: ").grid(column = 0, row = 0)
    text_box = Text(root, height = 1, width = 30).grid(column = 1, row = 0)
    save_label = Label(root, text = "save to: ").grid(column = 0, row = 1)
    save_button = Button(root, text = "...").grid(column = 2, row = 1)
    save_text = Label(root, text = placeholder_text).grid(column = 1, row = 1)
    download_button = Button(root, text = "download").grid(column = 1, row = 2)

    placeholder_text = "changed"    
    
    


main()
