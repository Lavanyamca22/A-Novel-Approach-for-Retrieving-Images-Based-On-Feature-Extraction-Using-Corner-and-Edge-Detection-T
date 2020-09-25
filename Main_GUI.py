import tkinter as tk
from tkinter import filedialog, messagebox
import PIL.Image
import PIL.ImageTk
from tkinter import *
import Fetch_data_from_database
import Saving_gui_images

def openfilename():
    file=filedialog.askopenfilename(title='BROWSE')
    return file


def BROWSE_IMAGE():
    panels("Image")
    global filename
    filename=openfilename()
    Saving_gui_images.Morph(filename[-11:])
    fp = open(filename, "rb")
    img = PIL.Image.open(filename)
    img = img.resize((125, 125), PIL.Image.ANTIALIAS)
    img = PIL.ImageTk.PhotoImage(img)
    panel = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
    panel.image = img
    panel.place(x=30, y=50)

    Text_heading_1 = tk.Label(root,
                              text="QUERY IMAGE",
                              fg='black', bg="#E6DC8C",
                              font=('Gabriola', 10, 'bold italic'))
    Text_heading_1.place(x=65, y=10)
    labels("Image")

def change_dropdown(*args):
    global method_string
    global Morph_panel
    global label_3
    labels("Drop_down")
    panels("Drop_down")
    method_string = ""
    method_string = tkvar.get()
    var3 = StringVar()
    label_3 = Label(root, textvariable=var3,
                    fg='black', bg="#E6DC8C",
                    font=('Gabriola', 10, 'bold italic'),width=20)
    label_3.place(x=550, y=90)
    if(method_string == "Gradient"):
        filename = "gradient.jpg"
        fp = open(filename, "rb")
        img = PIL.Image.open(filename)
        img = img.resize((180, 180), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        Morph_panel = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        Morph_panel.image = img
        Morph_panel.place(x=520, y=130)
        var3.set("Gradient Image")
    if (method_string == "Tophat"):
        filename = "tophat.jpg"
        fp = open(filename, "rb")
        img = PIL.Image.open(filename)
        img = img.resize((180, 180), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        Morph_panel = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        Morph_panel.image = img
        Morph_panel.place(x=520, y=130)
        var3.set("Tophat Image")
    if (method_string == "Blackhat"):
        filename = "blackhat.jpg"
        fp = open(filename, "rb")
        img = PIL.Image.open(filename)
        img = img.resize((180, 180), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        Morph_panel = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        Morph_panel.image = img
        Morph_panel.place(x=520, y=130)
        var3.set("Blackhat Image")
    print(method_string)

def select_method(j):
    global images
    global var, var2, var3
    global label, label_2
    images = []
    labels("Selection")
    panels("Selection")
    if (method_string == "Gradient"):
        print(method_string)
        images = Fetch_data_from_database.Morphological(1,j, filename)
        print("GM:",images)
        Saving_gui_images.Corner_Edge(filename[-11:], "1")
    elif (method_string == "Tophat"):
        images = Fetch_data_from_database.Morphological(2,j, filename)
        if (images == 0):
            messagebox.showinfo("Title", "CORNERS AND EDGES ARE NOT EQUAL")
        print("TH:", images)
        Saving_gui_images.Corner_Edge(filename[-11:], "2")
    elif (method_string == "Blackhat"):
        images = Fetch_data_from_database.Morphological(3,j, filename)
        if (images == 0):
            messagebox.showinfo("Title", "CORNERS AND EDGES ARE NOT EQUAL")
        print("WS:",images)
        Saving_gui_images.Corner_Edge(filename[-11:], "3")
    var = StringVar()
    label = Label(root, textvariable=var,
                  fg='black', bg="#E6DC8C",
                  font=('Gabriola', 10, 'bold italic'))
    label.place(x=400, y=330)

    var2 = StringVar()
    label_2 = Label(root, textvariable=var2,
                    fg='black', bg="#E6DC8C",
                    font=('Gabriola', 10, 'bold italic'))
    label_2.place(x=650, y=330)

def GMCCED():
    global cpanel
    global epanel
    global Method
    labels("GMCCED")
    panels("GMCCED")
    select_method(0)
    Method = "GMCCED"
    if (images == 0):
        messagebox.showinfo("Title", "CORNERS AND EDGES ARE NOT EQUAL")
    else:
        if (method_string == "Gradient"):
            filename = "corner_4.jpg"
        elif (method_string == "Tophat"):
            filename = "corner_5.jpg"
        elif (method_string == "Blackhat"):
            filename = "corner_6.jpg"
        fp = open(filename, "rb")
        img = PIL.Image.open(filename)
        img = img.resize((180, 180), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        cpanel= tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        cpanel.image = img
        cpanel.place(x=350, y=370)
        var.set("GMCCED_CORNER")

        if(method_string == "Gradient"):
            filename = "GM_gradient_edge.jpg"

        elif(method_string == "Tophat"):
            filename = "GM_tophat_edge.jpg"
            #var2.set("THRESHOLD EDGE")
        elif(method_string == "Blackhat"):
            filename = "GM_blackhat_edge.jpg"
            #var2.set("WATERSHED EDGE")
        var2.set("GRADIENT MAGNITUDE")
        fp = open(filename, "rb")
        img = PIL.Image.open(filename)
        img = img.resize((180, 180), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        epanel = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        epanel.image = img
        epanel.place(x=620, y=370)

def THCCED():
    global cpanel
    global epanel
    global Method
    labels("THCCED")
    panels("THCCED")
    select_method(1)
    Method = "THCCED"
    if (images == 0):
        messagebox.showinfo("Title", "CORNERS AND EDGES ARE NOT EQUAL")
    else:
        if (method_string == "Gradient"):
            filename = "corner_4.jpg"
        elif (method_string == "Tophat"):
            filename = "corner_5.jpg"
        elif (method_string == "Blackhat"):
            filename = "corner_6.jpg"
        fp = open(filename, "rb")
        img = PIL.Image.open(filename)
        img = img.resize((180, 180), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        cpanel = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        cpanel.image = img
        cpanel.place(x=350, y=370)
        var.set("THCCED_CORNER")

        if (method_string == "Gradient"):
            filename = "TH_gradient_edge.jpg"
            #var2.set("GRADIENT MAGNITUDE")
        elif (method_string == "Tophat"):
            filename = "TH_tophat_edge.jpg"

        elif (method_string == "Blackhat"):
            filename = "TH_blackhat_edge.jpg"
            #var2.set("WATERSHED EDGE")
        var2.set("THRESHOLD EDGE")
        fp = open(filename, "rb")
        img = PIL.Image.open(filename)
        img = img.resize((180, 180), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        epanel= tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        epanel.image = img
        epanel.place(x=620, y=370)

def WSCCED():
    global cpanel
    global epanel
    select_method(2)
    global Method
    labels("WSCCED")
    panels("WSCCED")
    Method="WSCCED"
    if (images == 0):
        messagebox.showinfo("Title", "CORNERS AND EDGES ARE NOT EQUAL")
    else:
        if (method_string == "Gradient"):
            filename = "corner_4.jpg"
        elif (method_string == "Tophat"):
            filename = "corner_5.jpg"
        elif (method_string == "Blackhat"):
            filename = "corner_6.jpg"
        fp = open(filename, "rb")
        img = PIL.Image.open(filename)
        img = img.resize((180, 180), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        cpanel = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        cpanel.image = img
        cpanel.place(x=350, y=370)
        var.set("WSCCED_CORNER")

        if (method_string == "Gradient"):
            filename = "WS_gradient_edge.jpg"
            #var2.set("GRADIENT MAGNITUDE")
        elif (method_string == "Tophat"):
            filename = "WS_tophat_edge.jpg"
            #var2.set("THRESHOLD EDGE")
        elif (method_string == "Blackhat"):
            filename = "WS_blackhat_edge.jpg"
        var2.set("WATERSHED EDGE")
        fp = open(filename, "rb")
        img = PIL.Image.open(filename)
        img = img.resize((180, 180), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        epanel = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        epanel.image = img
        epanel.place(x=620, y=370)

def panels(string_1):
    global panel_1, panel_2, panel_3, panel_4, panel_5, panel_6, panel_7, panel_8, panel_9, panel_10, panel_11, panel_12, panel_13, panel_14, panel_15, panel_16, panel_17, panel_18, panel_19, panel_20, panel_21, panel_22, panel_23, panel_24, panel_25, panel_26, panel_27, panel_28, panel_29, panel_30
    global count
    global label_1

    if(count==1 and (string_1=="THCCED" or string_1 == "WSCCED" or string_1=="GMCCED" or string_1 == "Drop_down")):
        panel_1.place_forget()
        panel_2.place_forget()
        panel_3.place_forget()
        panel_4.place_forget()
        panel_5.place_forget()
        panel_6.place_forget()
        panel_7.place_forget()
        panel_8.place_forget()
        panel_9.place_forget()
        panel_10.place_forget()
        panel_11.place_forget()
        panel_12.place_forget()
        panel_13.place_forget()
        panel_14.place_forget()
        panel_15.place_forget()
        panel_16.place_forget()
        panel_17.place_forget()
        panel_18.place_forget()
        panel_19.place_forget()
        panel_20.place_forget()
        panel_21.place_forget()
        panel_22.place_forget()
        panel_23.place_forget()
        panel_24.place_forget()
        panel_25.place_forget()
        panel_26.place_forget()
        panel_27.place_forget()
        panel_28.place_forget()
        panel_29.place_forget()
        panel_30.place_forget()
    if (count > 1):
        panel_1.place_forget()
        panel_2.place_forget()
        panel_3.place_forget()
        panel_4.place_forget()
        panel_5.place_forget()
        panel_6.place_forget()
        panel_7.place_forget()
        panel_8.place_forget()
        panel_9.place_forget()
        panel_10.place_forget()
        panel_11.place_forget()
        panel_12.place_forget()
        panel_13.place_forget()
        panel_14.place_forget()
        panel_15.place_forget()
        panel_16.place_forget()
        panel_17.place_forget()
        panel_18.place_forget()
        panel_19.place_forget()
        panel_20.place_forget()
        panel_21.place_forget()
        panel_22.place_forget()
        panel_23.place_forget()
        panel_24.place_forget()
        panel_25.place_forget()
        panel_26.place_forget()
        panel_27.place_forget()
        panel_28.place_forget()
        panel_29.place_forget()
        panel_30.place_forget()
    return

def labels(string):
    global label_1
    global Method
    #var = Method+" Using "+string+" Distance"
    if(string == "Euclidean" or string == "Canberra" or string == "Jensenshanoon" or string=="Chebyshev" or string == "Jaccard"):
        label_1 = Label(root, text=Method+" Using "+string+" Distance",
                      fg='black', bg="#71F087",
                      font=('Gabriola', 15, 'bold italic'),width=45)
        label_1.place(x=450, y=25)
    else:
        label_state = Label(root, text="Feature Extraction Process",
                        fg='black', bg="#71F087",
                        font=('Gabriola', 15, 'bold italic'), width=45)
        label_state.place(x=450, y=25)

def euclidean():
    labels("Euclidean")
    global count
    count = count+1
    global panel_1, panel_2, panel_3, panel_4, panel_5, panel_6, panel_7, panel_8, panel_9, panel_10, panel_11, panel_12, panel_13, panel_14, panel_15, panel_16, panel_17, panel_18, panel_19, panel_20, panel_21, panel_22, panel_23, panel_24, panel_25, panel_26, panel_27, panel_28, panel_29, panel_30
    panels("Euclidean")
    label.place_forget()
    label_2.place_forget()
    label_3.place_forget()
    cpanel.place_forget()
    epanel.place_forget()
    Morph_panel.place_forget()
    list_1 = []
    try:
        eu=images[0]
        n = 190
        m = 80
        for i in range(0, 30):
            if (i == 8 or i == 16):
                n = 190
                m = m + 120
            elif(i==24):
                n = 300
                m = m+120
            list_1.append([n,m])
            n = n + 110
        m = list_1[0]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[0],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_1 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_1.image = img
        panel_1.place(x=m[0], y=m[1])
        m = list_1[1]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[1],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_2 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_2.image = img
        panel_2.place(x=m[0], y=m[1])
        m = list_1[2]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[2],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_3 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_3.image = img
        panel_3.place(x=m[0], y=m[1])
        m = list_1[3]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[3],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_4 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_4.image = img
        panel_4.place(x=m[0], y=m[1])
        m = list_1[4]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[4],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_5 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_5.image = img
        panel_5.place(x=m[0], y=m[1])
        m = list_1[5]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[5],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_6 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_6.image = img
        panel_6.place(x=m[0], y=m[1])
        m = list_1[6]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[6],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_7 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_7.image = img
        panel_7.place(x=m[0], y=m[1])
        m = list_1[7]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[7],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_8 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_8.image = img
        panel_8.place(x=m[0], y=m[1])
        m = list_1[8]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[8],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_9 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_9.image = img
        panel_9.place(x=m[0], y=m[1])
        m = list_1[9]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[9],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_10 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_10.image = img
        panel_10.place(x=m[0], y=m[1])
        m = list_1[10]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[10],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_11 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_11.image = img
        panel_11.place(x=m[0], y=m[1])
        m = list_1[11]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[11],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_12 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_12.image = img
        panel_12.place(x=m[0], y=m[1])
        m = list_1[12]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[12],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_13 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_13.image = img
        panel_13.place(x=m[0], y=m[1])
        m = list_1[13]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[13],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_14 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_14.image = img
        panel_14.place(x=m[0], y=m[1])
        m = list_1[14]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[14],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_15 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_15.image = img
        panel_15.place(x=m[0], y=m[1])
        m = list_1[15]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[15],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_16 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_16.image = img
        panel_16.place(x=m[0], y=m[1])
        m = list_1[16]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[16],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_17 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_17.image = img
        panel_17.place(x=m[0], y=m[1])
        m = list_1[17]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[17],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_18 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_18.image = img
        panel_18.place(x=m[0], y=m[1])
        m = list_1[18]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[18],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_19 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_19.image = img
        panel_19.place(x=m[0], y=m[1])
        m = list_1[19]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[19],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_20 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_20.image = img
        panel_20.place(x=m[0], y=m[1])
        m = list_1[20]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[20],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_21 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_21.image = img
        panel_21.place(x=m[0], y=m[1])
        m = list_1[21]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[21],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_22 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_22.image = img
        panel_22.place(x=m[0], y=m[1])
        m = list_1[22]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[22],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_23 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_23.image = img
        panel_23.place(x=m[0], y=m[1])
        m = list_1[23]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[23],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_24 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_24.image = img
        panel_24.place(x=m[0], y=m[1])
        m = list_1[24]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[24],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_25 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_25.image = img
        panel_25.place(x=m[0], y=m[1])
        m = list_1[25]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[25],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_26 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_26.image = img
        panel_26.place(x=m[0], y=m[1])
        m = list_1[26]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[26],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_27 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_27.image = img
        panel_27.place(x=m[0], y=m[1])
        m = list_1[27]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[27],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_28 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_28.image = img
        panel_28.place(x=m[0], y=m[1])
        m = list_1[28]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[28],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_29 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_29.image = img
        panel_29.place(x=m[0], y=m[1])
        m = list_1[29]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[29],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_30 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_30.image = img
        panel_30.place(x=m[0], y=m[1])

    except:
        count = count-1
        print("No data")

def canberra():
    labels("Canberra")
    global count
    count = count + 1
    global panel_1, panel_2, panel_3, panel_4, panel_5, panel_6, panel_7, panel_8, panel_9, panel_10, panel_11, panel_12, panel_13, panel_14, panel_15, panel_16, panel_17, panel_18, panel_19, panel_20, panel_21, panel_22, panel_23, panel_24, panel_25, panel_26, panel_27, panel_28, panel_29, panel_30
    panels("Canberra")
    label.place_forget()
    label_2.place_forget()
    cpanel.place_forget()
    epanel.place_forget()
    label_3.place_forget()
    Morph_panel.place_forget()
    list_1 = []
    try:
        eu=images[1]
        n = 190
        m = 80
        for i in range(0, 30):
            if (i == 8 or i == 16):
                n = 190
                m = m + 120
            elif (i == 24):
                n = 300
                m = m + 120
            list_1.append([n, m])
            n = n + 110
        m = list_1[0]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[0],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_1 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_1.image = img
        panel_1.place(x=m[0], y=m[1])
        m = list_1[1]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[1],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_2 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_2.image = img
        panel_2.place(x=m[0], y=m[1])
        m = list_1[2]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[2],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_3 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_3.image = img
        panel_3.place(x=m[0], y=m[1])
        m = list_1[3]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[3],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_4 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_4.image = img
        panel_4.place(x=m[0], y=m[1])
        m = list_1[4]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[4],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_5 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_5.image = img
        panel_5.place(x=m[0], y=m[1])
        m = list_1[5]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[5],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_6 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_6.image = img
        panel_6.place(x=m[0], y=m[1])
        m = list_1[6]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[6],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_7 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_7.image = img
        panel_7.place(x=m[0], y=m[1])
        m = list_1[7]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[7],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_8 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_8.image = img
        panel_8.place(x=m[0], y=m[1])
        m = list_1[8]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[8],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_9 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_9.image = img
        panel_9.place(x=m[0], y=m[1])
        m = list_1[9]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[9],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_10 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_10.image = img
        panel_10.place(x=m[0], y=m[1])
        m = list_1[10]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[10],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_11 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_11.image = img
        panel_11.place(x=m[0], y=m[1])
        m = list_1[11]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[11],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_12 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_12.image = img
        panel_12.place(x=m[0], y=m[1])
        m = list_1[12]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[12],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_13 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_13.image = img
        panel_13.place(x=m[0], y=m[1])
        m = list_1[13]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[13],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_14 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_14.image = img
        panel_14.place(x=m[0], y=m[1])
        m = list_1[14]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[14],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_15 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_15.image = img
        panel_15.place(x=m[0], y=m[1])
        m = list_1[15]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[15],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_16 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_16.image = img
        panel_16.place(x=m[0], y=m[1])
        m = list_1[16]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[16],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_17 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_17.image = img
        panel_17.place(x=m[0], y=m[1])
        m = list_1[17]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[17],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_18 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_18.image = img
        panel_18.place(x=m[0], y=m[1])
        m = list_1[18]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[18],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_19 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_19.image = img
        panel_19.place(x=m[0], y=m[1])
        m = list_1[19]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[19],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_20 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_20.image = img
        panel_20.place(x=m[0], y=m[1])
        m = list_1[20]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[20],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_21 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_21.image = img
        panel_21.place(x=m[0], y=m[1])
        m = list_1[21]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[21],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_22 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_22.image = img
        panel_22.place(x=m[0], y=m[1])
        m = list_1[22]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[22],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_23 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_23.image = img
        panel_23.place(x=m[0], y=m[1])
        m = list_1[23]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[23],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_24 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_24.image = img
        panel_24.place(x=m[0], y=m[1])
        m = list_1[24]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[24],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_25 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_25.image = img
        panel_25.place(x=m[0], y=m[1])
        m = list_1[25]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[25],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_26 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_26.image = img
        panel_26.place(x=m[0], y=m[1])
        m = list_1[26]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[26],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_27 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_27.image = img
        panel_27.place(x=m[0], y=m[1])
        m = list_1[27]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[27],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_28 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_28.image = img
        panel_28.place(x=m[0], y=m[1])
        m = list_1[28]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[28],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_29 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_29.image = img
        panel_29.place(x=m[0], y=m[1])
        m = list_1[29]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[29],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_30 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_30.image = img
        panel_30.place(x=m[0], y=m[1])
    except:
        count = count-1
        print("no data")


def jensha():
    labels("Jensenshanoon")
    global count
    count = count + 1
    global panel_1, panel_2, panel_3, panel_4, panel_5, panel_6, panel_7, panel_8, panel_9, panel_10, panel_11, panel_12, panel_13, panel_14, panel_15, panel_16, panel_17, panel_18, panel_19, panel_20, panel_21, panel_22, panel_23, panel_24, panel_25, panel_26, panel_27, panel_28, panel_29, panel_30
    panels("Jensenshanoon")
    label.place_forget()
    label_2.place_forget()
    cpanel.place_forget()
    epanel.place_forget()
    label_3.place_forget()
    Morph_panel.place_forget()
    list_1 = []
    try:
        eu=images[2]
        n = 190
        m = 80
        for i in range(0, 30):
            if (i == 8 or i == 16):
                n = 190
                m = m + 120
            elif (i == 24):
                n = 300
                m = m + 120
            list_1.append([n, m])
            n = n + 110
        m = list_1[0]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[0],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_1 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_1.image = img
        panel_1.place(x=m[0], y=m[1])
        m = list_1[1]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[1],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_2 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_2.image = img
        panel_2.place(x=m[0], y=m[1])
        m = list_1[2]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[2],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_3 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_3.image = img
        panel_3.place(x=m[0], y=m[1])
        m = list_1[3]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[3],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_4 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_4.image = img
        panel_4.place(x=m[0], y=m[1])
        m = list_1[4]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[4],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_5 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_5.image = img
        panel_5.place(x=m[0], y=m[1])
        m = list_1[5]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[5],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_6 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_6.image = img
        panel_6.place(x=m[0], y=m[1])
        m = list_1[6]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[6],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_7 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_7.image = img
        panel_7.place(x=m[0], y=m[1])
        m = list_1[7]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[7],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_8 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_8.image = img
        panel_8.place(x=m[0], y=m[1])
        m = list_1[8]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[8],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_9 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_9.image = img
        panel_9.place(x=m[0], y=m[1])
        m = list_1[9]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[9],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_10 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_10.image = img
        panel_10.place(x=m[0], y=m[1])
        m = list_1[10]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[10],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_11 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_11.image = img
        panel_11.place(x=m[0], y=m[1])
        m = list_1[11]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[11],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_12 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_12.image = img
        panel_12.place(x=m[0], y=m[1])
        m = list_1[12]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[12],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_13 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_13.image = img
        panel_13.place(x=m[0], y=m[1])
        m = list_1[13]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[13],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_14 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_14.image = img
        panel_14.place(x=m[0], y=m[1])
        m = list_1[14]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[14],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_15 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_15.image = img
        panel_15.place(x=m[0], y=m[1])
        m = list_1[15]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[15],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_16 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_16.image = img
        panel_16.place(x=m[0], y=m[1])
        m = list_1[16]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[16],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_17 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_17.image = img
        panel_17.place(x=m[0], y=m[1])
        m = list_1[17]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[17],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_18 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_18.image = img
        panel_18.place(x=m[0], y=m[1])
        m = list_1[18]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[18],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_19 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_19.image = img
        panel_19.place(x=m[0], y=m[1])
        m = list_1[19]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[19],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_20 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_20.image = img
        panel_20.place(x=m[0], y=m[1])
        m = list_1[20]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[20],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_21 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_21.image = img
        panel_21.place(x=m[0], y=m[1])
        m = list_1[21]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[21],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_22 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_22.image = img
        panel_22.place(x=m[0], y=m[1])
        m = list_1[22]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[22],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_23 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_23.image = img
        panel_23.place(x=m[0], y=m[1])
        m = list_1[23]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[23],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_24 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_24.image = img
        panel_24.place(x=m[0], y=m[1])
        m = list_1[24]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[24],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_25 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_25.image = img
        panel_25.place(x=m[0], y=m[1])
        m = list_1[25]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[25],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_26 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_26.image = img
        panel_26.place(x=m[0], y=m[1])
        m = list_1[26]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[26],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_27 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_27.image = img
        panel_27.place(x=m[0], y=m[1])
        m = list_1[27]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[27],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_28 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_28.image = img
        panel_28.place(x=m[0], y=m[1])
        m = list_1[28]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[28],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_29 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_29.image = img
        panel_29.place(x=m[0], y=m[1])
        m = list_1[29]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[29],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_30 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_30.image = img
        panel_30.place(x=m[0], y=m[1])
    except:
        count = count-1
        print("no data")

def chebyshev():
    labels("Chebyshev")
    global count
    count = count + 1
    global panel_1, panel_2, panel_3, panel_4, panel_5, panel_6, panel_7, panel_8, panel_9, panel_10, panel_11, panel_12, panel_13, panel_14, panel_15, panel_16, panel_17, panel_18, panel_19, panel_20, panel_21, panel_22, panel_23, panel_24, panel_25, panel_26, panel_27, panel_28, panel_29, panel_30
    panels("Chebyshev")
    label.place_forget()
    label_2.place_forget()
    cpanel.place_forget()
    epanel.place_forget()
    label_3.place_forget()
    Morph_panel.place_forget()
    list_1 = []
    try:
        eu=images[3]
        n = 190
        m = 80
        for i in range(0, 30):
            if (i == 8 or i == 16):
                n = 190
                m = m + 120
            elif (i == 24):
                n = 300
                m = m + 120
            list_1.append([n, m])
            n = n + 110
        m = list_1[0]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[0],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_1 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_1.image = img
        panel_1.place(x=m[0], y=m[1])
        m = list_1[1]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[1],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_2 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_2.image = img
        panel_2.place(x=m[0], y=m[1])
        m = list_1[2]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[2],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_3 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_3.image = img
        panel_3.place(x=m[0], y=m[1])
        m = list_1[3]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[3],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_4 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_4.image = img
        panel_4.place(x=m[0], y=m[1])
        m = list_1[4]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[4],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_5 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_5.image = img
        panel_5.place(x=m[0], y=m[1])
        m = list_1[5]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[5],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_6 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_6.image = img
        panel_6.place(x=m[0], y=m[1])
        m = list_1[6]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[6],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_7 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_7.image = img
        panel_7.place(x=m[0], y=m[1])
        m = list_1[7]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[7],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_8 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_8.image = img
        panel_8.place(x=m[0], y=m[1])
        m = list_1[8]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[8],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_9 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_9.image = img
        panel_9.place(x=m[0], y=m[1])
        m = list_1[9]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[9],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_10 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_10.image = img
        panel_10.place(x=m[0], y=m[1])
        m = list_1[10]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[10],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_11 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_11.image = img
        panel_11.place(x=m[0], y=m[1])
        m = list_1[11]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[11],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_12 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_12.image = img
        panel_12.place(x=m[0], y=m[1])
        m = list_1[12]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[12],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_13 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_13.image = img
        panel_13.place(x=m[0], y=m[1])
        m = list_1[13]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[13],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_14 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_14.image = img
        panel_14.place(x=m[0], y=m[1])
        m = list_1[14]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[14],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_15 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_15.image = img
        panel_15.place(x=m[0], y=m[1])
        m = list_1[15]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[15],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_16 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_16.image = img
        panel_16.place(x=m[0], y=m[1])
        m = list_1[16]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[16],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_17 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_17.image = img
        panel_17.place(x=m[0], y=m[1])
        m = list_1[17]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[17],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_18 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_18.image = img
        panel_18.place(x=m[0], y=m[1])
        m = list_1[18]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[18],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_19 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_19.image = img
        panel_19.place(x=m[0], y=m[1])
        m = list_1[19]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[19],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_20 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_20.image = img
        panel_20.place(x=m[0], y=m[1])
        m = list_1[20]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[20],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_21 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_21.image = img
        panel_21.place(x=m[0], y=m[1])
        m = list_1[21]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[21],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_22 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_22.image = img
        panel_22.place(x=m[0], y=m[1])
        m = list_1[22]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[22],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_23 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_23.image = img
        panel_23.place(x=m[0], y=m[1])
        m = list_1[23]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[23],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_24 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_24.image = img
        panel_24.place(x=m[0], y=m[1])
        m = list_1[24]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[24],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_25 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_25.image = img
        panel_25.place(x=m[0], y=m[1])
        m = list_1[25]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[25],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_26 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_26.image = img
        panel_26.place(x=m[0], y=m[1])
        m = list_1[26]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[26],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_27 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_27.image = img
        panel_27.place(x=m[0], y=m[1])
        m = list_1[27]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[27],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_28 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_28.image = img
        panel_28.place(x=m[0], y=m[1])
        m = list_1[28]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[28],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_29 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_29.image = img
        panel_29.place(x=m[0], y=m[1])
        m = list_1[29]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[29],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_30 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_30.image = img
        panel_30.place(x=m[0], y=m[1])
    except:
        count = count - 1
        print("no data")

def jaccard():
    labels("Jaccard")
    global count
    count = count + 1
    global panel_1, panel_2, panel_3, panel_4, panel_5, panel_6, panel_7, panel_8, panel_9, panel_10, panel_11, panel_12, panel_13, panel_14, panel_15, panel_16, panel_17, panel_18, panel_19, panel_20, panel_21, panel_22, panel_23, panel_24, panel_25, panel_26, panel_27, panel_28, panel_29, panel_30
    panels("Jaccard")
    label.place_forget()
    label_2.place_forget()
    cpanel.place_forget()
    epanel.place_forget()
    label_3.place_forget()
    Morph_panel.place_forget()
    list_1 = []
    try:
        eu=images[4]
        n = 190
        m = 80
        for i in range(0, 30):
            if (i == 8 or i == 16):
                n = 190
                m = m + 120
            elif (i == 24):
                n = 300
                m = m + 120
            list_1.append([n, m])
            n = n + 110
        m = list_1[0]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[0],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_1 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_1.image = img
        panel_1.place(x=m[0], y=m[1])
        m = list_1[1]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[1],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_2 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_2.image = img
        panel_2.place(x=m[0], y=m[1])
        m = list_1[2]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[2],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_3 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_3.image = img
        panel_3.place(x=m[0], y=m[1])
        m = list_1[3]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[3],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_4 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_4.image = img
        panel_4.place(x=m[0], y=m[1])
        m = list_1[4]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[4],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_5 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_5.image = img
        panel_5.place(x=m[0], y=m[1])
        m = list_1[5]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[5],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_6 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_6.image = img
        panel_6.place(x=m[0], y=m[1])
        m = list_1[6]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[6],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_7 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_7.image = img
        panel_7.place(x=m[0], y=m[1])
        m = list_1[7]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[7],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_8 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_8.image = img
        panel_8.place(x=m[0], y=m[1])
        m = list_1[8]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[8],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_9 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_9.image = img
        panel_9.place(x=m[0], y=m[1])
        m = list_1[9]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[9],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_10 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_10.image = img
        panel_10.place(x=m[0], y=m[1])
        m = list_1[10]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[10],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_11 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_11.image = img
        panel_11.place(x=m[0], y=m[1])
        m = list_1[11]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[11],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_12 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_12.image = img
        panel_12.place(x=m[0], y=m[1])
        m = list_1[12]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[12],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_13 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_13.image = img
        panel_13.place(x=m[0], y=m[1])
        m = list_1[13]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[13],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_14 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_14.image = img
        panel_14.place(x=m[0], y=m[1])
        m = list_1[14]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[14],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_15 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_15.image = img
        panel_15.place(x=m[0], y=m[1])
        m = list_1[15]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[15],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_16 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_16.image = img
        panel_16.place(x=m[0], y=m[1])
        m = list_1[16]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[16],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_17 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_17.image = img
        panel_17.place(x=m[0], y=m[1])
        m = list_1[17]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[17],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_18 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_18.image = img
        panel_18.place(x=m[0], y=m[1])
        m = list_1[18]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[18],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_19 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_19.image = img
        panel_19.place(x=m[0], y=m[1])
        m = list_1[19]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[19],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_20 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_20.image = img
        panel_20.place(x=m[0], y=m[1])
        m = list_1[20]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[20],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_21 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_21.image = img
        panel_21.place(x=m[0], y=m[1])
        m = list_1[21]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[21],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_22 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_22.image = img
        panel_22.place(x=m[0], y=m[1])
        m = list_1[22]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[22],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_23 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_23.image = img
        panel_23.place(x=m[0], y=m[1])
        m = list_1[23]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[23],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_24 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_24.image = img
        panel_24.place(x=m[0], y=m[1])
        m = list_1[24]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[24],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_25 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_25.image = img
        panel_25.place(x=m[0], y=m[1])
        m = list_1[25]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[25],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_26 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_26.image = img
        panel_26.place(x=m[0], y=m[1])
        m = list_1[26]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[26],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_27 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_27.image = img
        panel_27.place(x=m[0], y=m[1])
        m = list_1[27]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[27],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_28 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_28.image = img
        panel_28.place(x=m[0], y=m[1])
        m = list_1[28]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[28],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_29 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_29.image = img
        panel_29.place(x=m[0], y=m[1])
        m = list_1[29]
        fp = open("C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set\\" + eu[29],
                  "rb")
        img = PIL.Image.open(fp)
        img = img.resize((100, 100), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)
        panel_30 = tk.Label(root, image=img, highlightbackground="black", highlightthickness=2)
        panel_30.image = img
        panel_30.place(x=m[0], y=m[1])
    except:
        count = count - 1
        print("no data")


root = tk.Tk()
root.geometry("1080x680+200+5")
root.title("IMAGE_RETRIEVAL")
filename='Background_image_3.jpg'
img=PIL.Image.open(filename)
img = img.resize((1080, 680), PIL.Image.ANTIALIAS)
doge = PIL.ImageTk.PhotoImage(img)
x = tk.Label(root, image=doge)
x.grid(row = 0,column = 0)
global cpanel
global epanel
global Morph_panel
global panel_1, panel_2, panel_3, panel_4, panel_5, panel_6, panel_7,panel_8,panel_9,panel_10,panel_11,panel_12,panel_13,panel_14,panel_15,panel_16,panel_17,panel_18,panel_19,panel_20,panel_21,panel_22,panel_23,panel_24,panel_25,panel_26,panel_27,panel_28,panel_29,panel_30
global label_1
global Method
global count
Method = ""
#panels = [panel_1, panel_2, panel_3, panel_4, panel_5, panel_6, panel_7,panel_8,panel_9,panel_10,panel_11,panel_12,panel_13,panel_14,panel_15,panel_16,panel_17,panel_18,panel_19,panel_20,panel_21,panel_22,panel_23,panel_24,panel_25,panel_26,panel_27,panel_28,panel_29,panel_30]
count = 0
Browse_button = tk.Button(root,
                          text="BROWSE_IMAGE",
                            fg="black",
                            bg="#A9CCE3", borderwidth = 8,
                            activebackground = "#ABEBC6",activeforeground="#E74C3C",
                            font=('Gabriola', 9,'bold italic'),
                          command=BROWSE_IMAGE,
                          height=1,
                          width=13)
Browse_button.place(x=45,y=190)

label = Label(root, text="Choose Morphology Transform",
                  fg='black', bg="#71F087",
                  font=('Gabriola', 11, 'bold italic'))
label.place(x=15, y=250)

tkvar = StringVar(root)
distance_choice = {'Gradient','Tophat','Blackhat'}
tkvar.set('Morophology')

popupMenu = OptionMenu(root,tkvar,'Gradient','Tophat','Blackhat')
tkvar.trace('w',change_dropdown)
popupMenu.config(bg = "#D7BDE2",font=('Times new roman', 10, 'bold italic'),
                 activebackground = "#34495E", activeforeground="white")
popupMenu ["menu"] ["bg"] = "#EC7063"
popupMenu ["menu"] ["font"] = ('Times new roman', 10, 'bold italic')
popupMenu ["menu"] ["activebackground"] = "#34495E"
popupMenu ["menu"] ["borderwidth"] = 1

popupMenu.place(x=35, y=290)


label = Label(root, text="Select Retrieval Method",
                  fg='black', bg="#71F087",
                  font=('Gabriola', 10, 'bold italic'))
label.place(x=40, y=400)
GM_button = tk.Button(root,
                            text="GM_CCED",
                            fg="black",
                            bg="#EDBB99", borderwidth = 8,
                            activebackground = "#34495E",activeforeground="white",
                            font=('Gabriola', 10,'bold italic'),
                            command=GMCCED,
                            height=1,
                            width=13)
GM_button.place(x=45, y=450)

TH_button = tk.Button(root,
                          text="TH_CCED",
                            fg="black",
                            bg="#EDBB99", borderwidth = 8,
                            activebackground = "#34495E",activeforeground="white",
                            font=('Gabriola', 10,'bold italic'),
                          command=THCCED,
                          height=1,
                          width=13)
TH_button.place(x=45, y=520)

WS_button = tk.Button(root,
                            text="WS_CCED",
                            fg="black",
                            bg="#EDBB99", borderwidth = 8,
                            activebackground = "#34495E",activeforeground="white",
                            font=('Gabriola', 10,'bold italic'),
                            command=WSCCED,
                            height=1,
                            width=13)
WS_button.place(x=45, y=590)

label = Label(root, text="Select Similarity Matching",
                  fg='black', bg="#71F087",
                  font=('Gabriola', 10, 'bold italic'))
label.place(x=470, y=580)

Euclidean_button = tk.Button(root,
                            text="Euclidean",
                            fg="black",
                            bg="#D7BDE2", borderwidth = 8,
                            activebackground = "#34495E",activeforeground="white",
                            font=('Times new roman', 10,'bold italic'),
                            command=euclidean,
                            height=1,
                            width=13)
Euclidean_button.place(x=250, y=620)

Canberra_button = tk.Button(root,
                            text="Canberra",
                            fg="black",
                            bg="#D7BDE2", borderwidth = 8,
                            activebackground = "#34495E",activeforeground="white",
                            font=('Times new roman', 10,'bold italic'),
                            command=canberra,
                            height=1,
                            width=13)
Canberra_button.place(x=380, y=620)

Jensenshanoon_button = tk.Button(root,
                            text="Jensenshanoon",
                            fg="black",
                            bg="#D7BDE2", borderwidth = 8,
                            activebackground = "#34495E",activeforeground="white",
                            font=('Times new roman', 10,'bold italic'),
                            command=jensha,
                            height=1,
                            width=13)
Jensenshanoon_button.place(x=510, y=620)

Chebyshev_button = tk.Button(root,
                            text="Chebyshev",
                            fg="black",
                            bg="#D7BDE2", borderwidth = 8,
                            activebackground = "#34495E",activeforeground="white",
                            font=('Times new roman', 10,'bold italic'),
                            command=chebyshev,
                            height=1,
                            width=13)
Chebyshev_button.place(x=640, y=620)

Jaccard_button = tk.Button(root,
                            text="Jaccard",
                            fg="black",
                            bg="#D7BDE2", borderwidth = 8,
                            activebackground = "#34495E",activeforeground="white",
                            font=('Times new roman', 10,'bold italic'),
                            command=jaccard,
                            height=1,
                            width=13)
Jaccard_button.place(x=770, y=620)

root.resizable(0,0)
root.mainloop()
