from tkinter import *
from PIL import Image, ImageTk

root = Tk()
# add title,width,heigh and color before popup
root.title("AI ASSISTANT")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#6F8FAF")

# Main Frame
Main_frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
Main_frame.config(bg="#6F8FAF")
Main_frame.grid(row=0, column=1, padx=55, pady=10)

# Text Label
Text_label = Label(Main_frame, text="AI Assistant", font=("Comic Sans MS", 14, "bold"), bg="#356696")
Text_label.grid(row=0, column=0, padx=20, pady=10)

# Image 
Display_Image = ImageTk.PhotoImage(Image.open("Image/AI-Assistant.jpeg"))
Image_Label = Label(Main_frame, image=Display_Image)
Image_Label.grid(row=1, column=0, pady=20)





#popup frame
root.mainloop()
