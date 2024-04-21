from bs4 import BeautifulSoup
import requests
import customtkinter as ctk
import pyperclip
import webbrowser

def build_frame():
    global root
    root = ctk.CTk()
    ctk.set_appearance_mode("dark")
    root.title('Root Scrapper')
    root.geometry(center_frame(root, 750, 750))
    entry(root)
    
    root.mainloop()

def center_frame(Screen: ctk.CTk, width: int, height: int):
    #fn to center frame upon launch
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int((screen_width/2) - (width/2))
    y = int((screen_height/2) - (height/1.5))
    return f"{width}x{height}+{x}+{y}"

def entry(root):
    global url_var
    global enter
    url_var = ctk.StringVar()
    enter = ctk.CTkEntry(root, width=500,height=25,corner_radius=5)
    enter.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)
    
    def llm_open():
        webbrowser.open("https://www.meta.ai/")
    
    b1 = ctk.CTkButton(root, text="LinkedIn", fg_color="#303030", command=copy_url)
    b1.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)
    b2 = ctk.CTkButton(root, text="Scrape Webpage",fg_color="#303030", command=scrape)
    b2.place(relx=0.3, rely=0.6, anchor=ctk.CENTER)
    b3 = ctk.CTkButton(root,text="LLM",fg_color="#303030", command=llm_open)
    b3.place(relx=0.7, rely=0.6, anchor=ctk.CENTER)
    
    
    global box
    box = ctk.CTkTextbox(root,height=100, width=500, corner_radius=2)
    box.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
    box.configure(state="disabled")
    

    
def copy_url():
    url = enter.get()
    pyperclip.copy(url)


def scrape():
    def scrape_fill(keyword):
        box.insert('0.0', keyword)  
        
    keywords_list = ["Database", "compTIA", "certify", 'division', 'Condominium', 'collection', 'Java'] #update this to all keywords for resumes/coverletters
    #scrape for keywords in pasted url into enter box
    #rewrite to scrape through list of linkedin keywords
    
    #currently - scrapes through pasted url and loops through keywords_list to match if keyword exists. prints which keywords exists to console.
    url = requests.get((enter.get())) 
    soup = BeautifulSoup(url.content, 'html.parser')
    
    counter = 0
    
    try:
        link = soup.find_all(['p', 'div', 'h1', 'h2', 'h3', 'h4'])
        keyword_counter = {}
        already_scraped = set()
        
        for word in link:
            for keyword in keywords_list:
                if keyword in word.text:
                    if keyword in keyword_counter:
                        keyword_counter[keyword] += 1
                    else:
                        keyword_counter[keyword] = 1
                    if keyword not in already_scraped:
                        box.configure(state="normal")
                        scrape_fill(keyword)
                        already_scraped.add(keyword)
                        box.configure(state="disabled")
    except:
        print("failed")
       
        

