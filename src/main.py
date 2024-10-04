# main.py
from tkinter import Tk, Scale, Label, Button, HORIZONTAL
import os
from image_processing import process_image

# Đường dẫn đến ảnh cụ thể
IMAGE_PATH = "C:\\Users\\Admin\\XU-LY-ANH-PTIT-2024\\data\\ChessSet.jpg"

# Hàm xử lý sự kiện khi nhấn nút xử lý ảnh
def on_process_click(low_thresh_slider, high_thresh_slider):
    if os.path.exists(IMAGE_PATH):
        low_threshold = low_thresh_slider.get()
        high_threshold = high_thresh_slider.get()
        process_image(IMAGE_PATH, low_threshold, high_threshold)
    else:
        print(f"Không tìm thấy ảnh tại đường dẫn: {IMAGE_PATH}")

# Tạo giao diện
def create_gui():
    root = Tk()
    root.title("Canny Edge Detection")
    root.geometry("400x200")

    # Tạo thanh trượt cho low_threshold
    Label(root, text="Low Threshold").pack()
    low_thresh_slider = Scale(root, from_=0, to=255, orient=HORIZONTAL)
    low_thresh_slider.set(100)  # Giá trị mặc định
    low_thresh_slider.pack()

    # Tạo thanh trượt cho high_threshold
    Label(root, text="High Threshold").pack()
    high_thresh_slider = Scale(root, from_=0, to=255, orient=HORIZONTAL)
    high_thresh_slider.set(200)  # Giá trị mặc định
    high_thresh_slider.pack()

    # Nút để chọn và xử lý ảnh
    process_button = Button(root, text="Xử lý ảnh", command=lambda: on_process_click(low_thresh_slider, high_thresh_slider))
    process_button.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
