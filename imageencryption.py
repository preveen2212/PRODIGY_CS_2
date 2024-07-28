from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("200x160")

def encrypt_image():
    file1 = filedialog.askopenfile(mode='rb', filetypes=[('jpg file', '*.jpg')])
    if file1 is not None:
        file_name = file1.name
        key = entry1.get(1.0, END).strip()  # Remove any extra newline or spaces
        print(file_name, key)
        if key.isdigit():  # Ensure the key is a number
            key = int(key)
            fi = open(file_name, 'rb')
            image = fi.read()  # Correctly read the image data
            fi.close()
            image = bytearray(image)
            for index, value in enumerate(image):
                image[index] = value ^ key
            fi1 = open(file_name, 'wb')
            fi1.write(image)
            fi1.close()
        else:
            print("Please enter a valid numeric key.")

b1 = Button(root, text="encrypt", command=encrypt_image)
b1.place(x=70, y=10)

entry1 = Text(root, height=1, width=10)
entry1.place(x=50, y=50)

root.mainloop()
