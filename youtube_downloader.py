from pytube import *
from tkinter import *
from tkinter import filedialog


root = Tk()
root.title("video download screen")

def main():

    main_screen()



#Tkinter screen setup
def main_screen():
    
    

    url_label = Label(root, text = "URL: ").grid(column = 0, row = 0)
    text_box = Text(root, height = 1, width = 30).grid(column = 1, row = 0)

    save_label = Label(root, text = "save to: ").grid(column = 0, row = 1)
    save_button = Button(root, text = "...", command = save_location).grid(column = 2, row = 1)
    save_text = Label(root, text = "c:\\").grid(column = 1, row = 1)

    download_button = Button(root, text = "download").grid(column = 1, row = 2)

def save_location():
    filepath = filedialog.askdirectory(initialdir=r"C:\Users")
    save_text = Label(root, text = filepath).grid(column = 1, row = 1)
    return filepath
    
    

def download_vid():
    print("placeholder for pytube code")

main()
