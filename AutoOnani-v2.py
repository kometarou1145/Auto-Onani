from PIL import ImageTk, Image
import tkinter as tk
import os
import random

folder = input("Folder: ")
delayData = int(input("Delay: "))

delay = delayData * 1000

def displayRandomImage():

    imageFolder = folder
    imageFiles = [file for file in os.listdir(imageFolder) if file.endswith((".png", ".jpg", ".jpeg", ".gif"))]
    
    if imageFiles:

        randomImage = random.choice(imageFiles)

        imagePath = os.path.join(imageFolder, randomImage)
        image = Image.open(imagePath)
        photo = ImageTk.PhotoImage(image)

        label.config(image=photo)
        label.image = photo

    else:
        print("Error")
    
    startButton.pack_forget()
    root.after(delay, displayRandomImage)

def black():
    root.configure(bg="black")
    blackButton.pack_forget()
    whiteButton.pack()
    air.configure(bg="black")

def white():
    root.configure(bg="white")
    whiteButton.pack_forget()
    blackButton.pack()
    air.configure(bg="white")

root = tk.Tk()
root.title("")
root.geometry("600x600")
root.configure(bg="white")

startButton = tk.Button(root, text="start", command=displayRandomImage)
startButton.pack()

air = tk.Label(root)
air.pack()
air.configure(bg="white")

label = tk.Label(root)
label.pack()

blackButton = tk.Button(root, text="black", command=black)
whiteButton = tk.Button(root, text="white", command=white)
blackButton.pack()

root.mainloop()
