from tkinter import *
import instaloader
test = instaloader.Instaloader()

def down():
    test.download_profile(user.get())
def pr():
    print(user)
def cap():
    root2=Tk()
    root2.config(bg="black")
    root2.minsize(250,250)
    root.title("Instagram Downloader")
    root2.maxsize(250,250)
    start=Label(root2,text=user.get(),font=("overlock",15),fg="white",bg="black")
    start.grid(row=0,column=0)
    find=Label(root2,text="Finded !",font=("overlock",15),fg="red",bg="black")
    find.grid(row=1,column=0,padx=70)
    b2=Button(root2,text="Download Whole Posts",command=down,font=("overlock",8),width=20)
    b2.grid(row=2,column=0,pady=20,padx=75)
    root2.mainloop()

    

    # root3.mainloop()
    test.download_profile(user.get())
    
root=Tk()
root.minsize(500,500)
root.maxsize(500,500)
root.title("Instagram Downloader ")
root.config(bg="black")
user=StringVar()
#heading frame 
frame = Frame(root,bg="black",height=100,width=500)
frame.grid(row=0,column=0)
heading=Label(frame,text="Download Instagram  Account Posts ",bg="black",fg="yellow",font=("overlock",20))
heading.grid(row=0,column=0,pady=15,padx=10)




username=Label(root,text="Enter The Url the below box",font=("overlock",15),bg="black",fg="white")
username.grid(row=1,column =0)
en=Entry(textvariable=user,font=("overlock",15),width=35,fg="blue")
en.grid(row=2,column=0,pady=25)
b1=Button(text="Find User ",command=cap,font=("overlock",15),width=10)
b1.grid(row=3,column=0,pady=15)
root.mainloop()