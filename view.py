import tkinter as tk
from tkinter import *
import cv2 as cv
import numpy as np
from PIL import Image, ImageTk

root = tk.Tk()

root.title("Trần Đức Hiếu")
root.geometry("600x450+400+150")
root.iconbitmap("D:/_chuyenmon/Python/Tkinter/learn/hiu.ico")
root.attributes('-topmost', True)

text = Label(root, text="Nhập đường dẫn ảnh: ", font=('terminal', 10))
text.place(x=30, y=30)

entry = Entry(root, width=30, font=('Terminal', 10))
entry.place(x=190, y=30)
entry.focus()

def docanh():
    path_url = entry.get()
    img = cv.imread(path_url)
    readQR = cv.QRCodeDetector()
    v = readQR.detectAndDecode(img)
    a = v[1]
    
    points = np.array(a, dtype=np.float32)
    cv.polylines(img, [points.astype(np.int32)], isClosed=True, color=(0, 255, 0), thickness=2)
    
    # Chuyển đổi ảnh từ OpenCV sang PIL
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    
    # Chuyển đổi ảnh PIL sang định dạng có thể hiển thị trên Tkinter
    img_tk = ImageTk.PhotoImage(image=img_pil)
    
    # Hiển thị ảnh trên Label
    img_label = Label(root, image=img_tk)
    img_label.image = img_tk  # Giữ tham chiếu đến ảnh để không bị giải phóng
    img_label.place(x=70, y=100)
    
    if v[1] is not None:
        data = Label(root, text=f'Dữ liệu ảnh là : {v[0]}', font=('terminal', 10))
        data.place(x=30, y=380)
        print("Đọc Thành Công")
    else:
        print("Đọc thất bại")

but = Button(root, text='kiểm Tra', font=('Times News Roman', 11), bg='gray', command=docanh)
but.place(x=70, y=60)

root.mainloop()

# "C:/Users/ACER/AppData/Local/ZaloPC/114407125408739750/ZaloDownloads/picture/480739440366046107/a.jpg"