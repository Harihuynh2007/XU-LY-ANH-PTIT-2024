# image_processing.py
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Ghi log thông tin vào thư mục chỉ định
def log_info(image_path, object_count, low_threshold, high_threshold):
    log_path = "C:\\Users\\Admin\\XU-LY-ANH-PTIT-2024\\notebook\\log.txt"
    with open(log_path, "a") as log_file:
        log_file.write(f"Image: {image_path}, Objects: {object_count}, Low Threshold: {low_threshold}, High Threshold: {high_threshold}\n")
    print(f"Thông tin đã được ghi vào {log_path}")

# Xử lý ảnh và đếm đối tượng
def process_image(image_path, low_threshold, high_threshold):
    # Đọc ảnh
    image = cv2.imread(image_path)

    # Chọn vùng ROI
    roi = cv2.selectROI("Select ROI", image, fromCenter=False, showCrosshair=True)
    cv2.destroyWindow("Select ROI")
    
    # Cắt ảnh theo vùng ROI
    roi_image = image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

    # Chuyển ảnh ROI sang thang độ xám
    gray_image = cv2.cvtColor(roi_image, cv2.COLOR_BGR2GRAY)

    # Làm mờ ảnh để giảm nhiễu
    blurred_image = cv2.GaussianBlur(gray_image, (7, 7), 0)

    # Áp dụng ngưỡng màu
    _, threshold_image = cv2.threshold(blurred_image, 127, 255, cv2.THRESH_BINARY)

    # Phát hiện cạnh sử dụng Canny với ngưỡng điều chỉnh từ giao diện
    edges = cv2.Canny(threshold_image, low_threshold, high_threshold)

    # Tìm đường bao (contours)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Lọc các contours dựa trên kích thước để loại bỏ những contours quá nhỏ
    min_contour_area = 200  # Ngưỡng diện tích tối thiểu cho contour để được tính
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]

    # Đếm số lượng đối tượng sau khi lọc
    object_count = len(filtered_contours)

    # Vẽ đường bao lên ảnh gốc ROI
    cv2.drawContours(roi_image, filtered_contours, -1, (0, 255, 0), 2)

    # Hiển thị kết quả
    print(f"Số lượng đối tượng trong ảnh: {object_count}")
    plt.figure(figsize=(10, 5))

    # Hiển thị ảnh gốc với đường bao
    plt.subplot(1, 2, 1)
    plt.title("Original ROI Image with Contours")
    plt.imshow(cv2.cvtColor(roi_image, cv2.COLOR_BGR2RGB))

    # Hiển thị ảnh sau khi áp dụng Canny
    plt.subplot(1, 2, 2)
    plt.title("Edge Detected Image")
    plt.imshow(edges, cmap='gray')

    plt.show()

    # Ghi log thông tin
    log_info(image_path, object_count, low_threshold, high_threshold)
