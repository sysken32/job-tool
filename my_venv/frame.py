from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
import requests
import tkinter as tk
import pyperclip
    
def build_frame():#
    # building the root frame
    global root
    root = Tk()
    root.title = ("Root Scrapper")
    root.geometry(center_frame(root, 300, 300))
    entry(root)

    root.mainloop()

def center_frame(Screen: Tk, width: int, height: int):
    #fn to center frame upon launch
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int((screen_width/2) - (width/2))
    y = int((screen_height/2) - (height/1.5))
    return f"{width}x{height}+{x}+{y}"

def copy_url():
    url = url_var.get()
    pyperclip.copy(url)
    

def entry(root):
    # url placement enter
    global url_var
    global enter 
    url_var = tk.StringVar()
    enter = tk.Entry(root, textvariable=url_var, font=('times new roman', 10, 'normal'))
    enter.place(relx=0.5, rely=0.5, anchor=CENTER)
    b = Button(root, text="LinkedIn", command=copy_url)
    b.place(relx=0.5, rely=0.6, anchor=CENTER)
    b = Button(root, text="scrape", command=scrape)
    b.place(relx=0.5, rely=0.7, anchor=CENTER)

def scrape():
    keywords_list = ["Database", "compTIA", "certify", 'division', 'Condominium'] #update this to all keywords for resumes/coverletters
    #scrape for keywords in pasted url into enter box
    #rewrite to scrape through list of linkedin keywords
    
    #currently - scrapes through pasted url and loops through keywords_list to match if keyword exists. prints which keywords exists to console.
    url = requests.get((enter.get())) 
    soup = BeautifulSoup(url.content, 'html.parser')
    
    try:
        link = soup.find_all(['p', 'div', 'h1', 'h2', 'h3', 'h4'])
        for word in link:
            for keyword in keywords_list:
                if keyword in word.text:
                    print(keyword)

    except:
        print("failed")

    