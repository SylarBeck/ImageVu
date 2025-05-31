from tkinter import ttk
import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()

class ImageViewer:
    def __init__(self, master):
        
        self.master = master
        self.master.title("Image Viewer")

        self.master.geometry("800x600")
        self.master.resizable(False, False)
        self.master.configure(bg="#05081c")
        self.master.iconbitmap(self.master, 'src/img_vu/img_vu.ico')
        

app = ImageViewer(root)

root.mainloop()