import os
from tkinter import *
from time import sleep
import qrcode

# functions
def clear_url_box():
    content.set("")
def update_status(temp):
    statusvar.set(temp)
    sbar.update()
def create_qr():
    update_status("Creating QR Code")
    sleep(0.3)
    data = content.get()
    qr = qrcode.QRCode(version = 5,box_size = 15,border = 2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(data+".png")
    update_status("QR Code Saved at "+ download_path.get())
    sleep(0.5)
    update_status("Ready to Create New QR Code")

# main body
if __name__=="__main__":
    root = Tk()
    # window size
    root.title("Elite Insta Profile Photo Downloader")
    root.geometry("850x520")
    root.minsize(800,400)
    

    # Variables
    content = StringVar()
    downloads_location=StringVar()
    download_path=StringVar()
    temp_path = os.getcwd()
    temp_path = os.path.join(temp_path,"Created_QR_Codes")
    try:
        os.mkdir("Created_QR_Codes")
    except:
        pass
    os.chdir(temp_path)
    download_path.set(temp_path)
    downloads_location.set(f"Downloads path :- {download_path.get()}")
    statusvar = StringVar()
    statusvar.set("Ready to Create New QR Code")


    # code to download a video
    heading1=Label(root,text="ELITE AKSHAY",font="calibre 40 bold",relief=RAISED,padx=10,pady=9)
    heading1.pack()
    space=Label(root,text="",font="calibre 2 bold")
    space.pack()
    heading2=Label(root,text="QR Code Generator",font="Times 25 bold",relief=RAISED,background="cyan",padx=10,pady=9,)
    heading2.pack()
    f1=Frame(root)
    f1.pack(side=TOP,fill=BOTH,expand=True,pady=10)
    name=Label(f1,text="ENTER TEXT",font="calibre 20 bold italic",relief=FLAT,padx=8,pady=5,)
    name.pack()
    space=Label(f1,text="",font="calibre 1 bold")
    space.pack()
    content_name=Entry(f1,textvariable=content,font="calibre 25 normal",fg="blue",relief=SUNKEN)
    content_name.pack()
    download_loacation_display=Label(f1,textvariable=downloads_location,font="calibre 10 bold italic",relief=FLAT,padx=18,pady=3)
    download_loacation_display.pack()
    download_btn=Button(f1,text="Create QR",command=create_qr,bd=5,fg="blue",font="calibre 18 bold")
    download_btn.pack(side = LEFT, expand = True, fill = X)
    clear_url_btn=Button(f1,text="CLEAR URL",command=clear_url_box,bd=5,font="calibre 18 bold")
    clear_url_btn.pack(side = LEFT, expand = True, fill = X)
    # statusbar
    sbar = Label(root,textvariable=statusvar, anchor="w",padx=10,pady=7,background="cyan",fg="red",font="calibre 12 bold")
    sbar.pack(side=BOTTOM, fill=X)



    root.mainloop()