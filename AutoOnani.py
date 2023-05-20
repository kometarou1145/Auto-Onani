from PIL import ImageTk, Image
import tkinter as tk
import os
import random

folder = input("Folder: ")

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

root = tk.Tk()
root.title("")
root.geometry("600x600")

generateButton = tk.Button(root, text="generate", command=displayRandomImage)
generateButton.pack()

label = tk.Label(root)
label.pack()

root.mainloop()