from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import time
from PIL import Image


# ---------------------------- UPLOAD IMAGE / WATERMARK ------------------------------- #

def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '.jpeg'), ('Image Files', '.png')])
    if file_path is not None:
        pass

def watermark_applied():
    pb = Progressbar(
        window,
        orient=HORIZONTAL,
        length=300,
        mode='determinate'
        )
    pb1_window = canvas.create_window(260, 360, anchor='nw', window=pb)
    for i in range(5):
        window.update_idletasks()
        pb['value'] += 10
        time.sleep(1)
    pb.destroy()
    success = Label(window, text='Watermark Applied')
    success_window = canvas.create_window(255,70, anchor='nw', window=success)

# ---------------------------- APPLY WATERMARK ------------------------------- #
user_image = lambda: open_file()
user_image_w, user_image_h = (1000,1000)

watermark = lambda: open_file()
watermark_w, watermark_h = (250,250)


user_image.paste(watermark)
user_image.save('image.png')
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('H2oMarker')
window.config(padx=0, pady=0)
window.geometry('600x500')
window.resizable(width=False, height=False)
window.iconbitmap('window_icon.ico')
bg = PhotoImage(file='logo.png')

canvas = Canvas(window, width=600, height=500)
canvas.pack(fill='both', expand=True)

canvas.create_image(0, 0, image=bg, anchor='nw')

upload_image = Button(window, text='Upload Image', command=lambda: user_image())
upload_window = canvas.create_window(270, 110, anchor='nw', window=upload_image)

upload_watermark = Button(window, text='Upload Watermark', command=lambda: watermark())
upload_watermark_window = canvas.create_window(260, 160, anchor='nw', window=upload_watermark)

process = Button(window, text='Process', command=lambda: watermark_applied())
process_window = canvas.create_window(275, 250, anchor='nw', window=process)


window.mainloop()