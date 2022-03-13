import tkinter as tk
from tkinter import ttk
import tkinter.filedialog
import pandas as pd

from excel_func import excel_read
from excel_func import excel_write
from google_find import google_find_func

class Application(tkinter.Frame):
    def __init__(self, root=None):
        super().__init__(root,
                     width = 800,
                     height = 600,
                     borderwidth = 5,
                     relief = "groove")
        self.pack()
        self.pack_propagate(0)
        self.csv_pass = tk.StringVar()
        self.root = root
        self.createWidgets()
    
    def createWidgets(self):
        csv_box = ttk.Entry(width=40, textvariable= self.csv_pass)
        csv_box.place(x=30, y=150)
        buttonA = ttk.Button(root, text= "参照", width= 10, command= self.openfile).place(x=600, y=150)
        buttonB = ttk.Button(root, text= "実行", width= 10, command= self.excel_view).place(x=600, y=200)

    def openfile(self):
        f = tkinter.filedialog.askopenfilename(
            title= "ファイル選択（csv）",
            filetypes= [("csv files","*.csv")]
            )
        self.csv_pass.set(f)
    
    def excel_view(self):
        excel_pass = self.csv_pass.get()
        cam_list = excel_read(excel_pass)
        find_result_list = google_find_func(cam_list)
        excel_write(excel_pass, find_result_list)
                

if __name__ == "__main__":
    root = tk.Tk()
    root.title("タイトル")
    root.geometry("820x620")
    app = Application(root=root)
    app.mainloop()