from tkinter import *
from PIL import Image, ImageTk
import action 
import spech_to_text 

def User_send():
    send = entry1.get()
    bot = action.Action(send)
    text.insert(END, "Me --> " + send + "\n", "user")
    if bot is not None:
        text.insert(END, "Bot <-- " + str(bot) + "\n", "bot")
    if bot == "ok sir":
        root.destroy()  

def ask():
    ask_val = spech_to_text.spech_to_text()
    bot_val = action.Action(ask_val)
    text.insert(END, "Me --> " + ask_val + "\n", "user")
    if bot_val is not None:
        text.insert(END, "Bot <-- " + str(bot_val) + "\n", "bot")
    if bot_val == "ok sir":
        root.destroy()


def delete_text():
    text.delete("1.0", "end")

root = Tk()

# add title,width,heigh and color before popup
root.title("AI ASSISTANT")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#1f6767")

# Main Frame
Main_frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
Main_frame.config(bg="#FFFFFF")
Main_frame.grid(row=0, column=1, padx=55, pady=10)

# Text Label
Text_label = Label(Main_frame, text="AI Assistant", font=("Comic Sans MS", 14, "bold"), bg="#356696", fg="white")
Text_label.grid(row=0, column=0, padx=20, pady=10)

# Image 
Display_Image = ImageTk.PhotoImage(Image.open("Image/AI-Assistant.jpeg"))
Image_Label = Label(Main_frame, image=Display_Image)
Image_Label.grid(row=1, column=0, pady=20)

# Add a text widget
text=Text(root , font= ('Courier 10 bold') , bg = "#356696",fg="white", bd=2, relief=RIDGE)
text.grid(row = 2,  column= 0)
text.place(x= 100, y= 375, width= 375, height= 100) 


#Add Entry widget
entry1=Entry(root,justify="center" ,font=("Comic Sans MS", 12), bg="#FFFFFF", fg="#000000", relief=GROOVE, bd=2)
entry1.place(x=100,y=500,width=370,height=30)

# Configure text tags to mimic CSS-like styling for conversation bubbles
text.tag_config("user", foreground="#00ff00", font=("Courier", 10, "bold"))  # User messages: bright green, bold
text.tag_config("bot", foreground="#ffcc00", font=("Courier", 10, "italic"))  # Bot messages: golden, italic

# Add a text button ask
button1 =  Button(root,  text="ASK", bg="#356696",fg="white",activebackground="#1f6767",activeforeground="white" ,bd=5, pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=ask)
button1.place(x= 70, y= 575)

# Add a text button send
button2 =  Button(root,  text="Send" , bg="#347719" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=User_send)
button2.place(x= 400, y= 575)

# Add a text button delete text
button3 = Button(root, text="Delete", bg="#bd1c11" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,command=delete_text)
button3.place(x= 225, y= 575)

#popup frame
root.mainloop()
