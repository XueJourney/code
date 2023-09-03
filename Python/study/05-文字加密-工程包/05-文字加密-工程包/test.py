import qrcode
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import filedialog

def generate_qr_code():
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(text_entry.get())
    qr.make(fit=True)
    img = qr.make_image(fill_color=color_entry.get(), back_color="white")
    img.save("qrcode.png")
    qr_image = Image.open("qrcode.png")
    qr_image = qr_image.resize((250, 250), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=photo)
    qr_label.image = photo

def save_qr_code():
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    if file_path:
        qr_image = Image.open("qrcode.png")
        qr_image.save(file_path)

root = tk.Tk()
root.title("QR Code Generator")

text_label = tk.Label(root, text="Text:")
text_label.pack()

text_entry = tk.Entry(root)
text_entry.pack()

color_label = tk.Label(root, text="Color:")
color_label.pack()

color_entry = tk.Entry(root)
color_entry.pack()

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

qr_label = tk.Label(root)
qr_label.pack()

save_button = tk.Button(root, text="Save QR Code", command=save_qr_code)
save_button.pack()

root.mainloop()
