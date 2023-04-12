from tkinter import *
import pyshorteners
#Defining shortener function
def shorten_url():
    if short_entry.get():
        short_entry.delete(0,END)
     #Processing to Shortener url
    if long_url_entry.get():
        short_url = pyshorteners.Shortener().tinyurl.short(long_url_entry.get())
        short_entry.insert(END,short_url)

root = Tk()
root.title("URL Shortener")
root.geometry("600x500")
long_url_label = Label(root, text="Enter your URL : ",font="Arial 24 bold",fg="red")
long_url_label.pack()

long_url_entry = Entry(root, width=50,bg="lightgreen",bd=3,font="Arial 15 ")
long_url_entry.pack(pady=25)

shorten_button = Button(root, text="SHORT",command=shorten_url,bg="blue",height=1,font="Arial 12 bold",bd=3,fg="white")
shorten_button.pack(pady=25)

short_url_label = Label(root, text="Printing here Shortened URL :",font="Arial 15 ",fg="black")
short_url_label.pack()

short_entry = Entry(root,justify=CENTER,bd=2,width=30,font="Arial 18",fg="blue")
short_entry.pack(pady=20)

quitButton=Button(text="Press to Quit GUI",command=quit,bg="red",fg="white",height=1,font="Arial 10")
quitButton.pack(side=BOTTOM)


root.mainloop()
