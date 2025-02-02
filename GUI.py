from tkinter import *
from PIL import Image, ImageTk

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
Text_label = Label(Main_frame, text="AI Assistant", font=("Comic Sans MS", 14, "bold"), bg="#356696")
Text_label.grid(row=0, column=0, padx=20, pady=10)

# Image 
Display_Image = ImageTk.PhotoImage(Image.open("Image/AI-Assistant.jpeg"))
Image_Label = Label(Main_frame, image=Display_Image)
Image_Label.grid(row=1, column=0, pady=20)

# Add a text widget
text=Text(root , font= ('Courier 10 bold') , bg = "#356696")
text.grid(row = 2,  column= 0)
text.place(x= 100, y= 375, width= 375, height= 100) 





#popup frame
root.mainloop()
