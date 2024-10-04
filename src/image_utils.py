# src/image_utils.py
import cv2

def read_image(image_path):
    """Đọc ảnh từ đường dẫn."""
    image = cv2.imread(image_path)
    if image is None:
        print("Không thể đọc ảnh. Vui lòng kiểm tra lại đường dẫn hoặc tên tệp.")
    return image

def convert_to_grayscale(image):
    """Chuyển đổi ảnh sang màu xám."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_gaussian_blur(image, kernel_size=(5, 5)):
    """Làm mờ ảnh bằng Gaussian Blur."""
    return cv2.GaussianBlur(image, kernel_size, 0)

def apply_adaptive_threshold(image, max_value=255, method=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, block_size=11, C=2):
    """Áp dụng ngưỡng thích ứng (adaptive thresholding) để phân tách đối tượng."""
    return cv2.adaptiveThreshold(image, max_value, method, cv2.THRESH_BINARY, block_size, C)

def apply_morphology(image, kernel_size=(5, 5)):
    """Áp dụng phép toán hình thái học Closing để loại bỏ nhiễu."""
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

def apply_canny_edge_detection(image, lower_threshold=100, upper_threshold=200):
    """Phát hiện cạnh sử dụng thuật toán Canny Edge Detection."""
    return cv2.Canny(image, lower_threshold, upper_threshold)

def find_and_count_contours(image, min_area=500):
    """Tìm và đếm số lượng đường viền (contours) trong ảnh, chỉ đếm những đường viền có diện tích lớn hơn min_area."""
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Lọc các đường viền có diện tích lớn hơn giá trị min_area
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]
    
    return filtered_contours, len(filtered_contours)

def draw_contours(image, contours):
    """Vẽ đường viền quanh các đối tượng trên ảnh."""
    return cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2)

def save_image(image, file_path):
    """Lưu ảnh vào đường dẫn đã cho."""
    cv2.imwrite(file_path, image)
    print(f"Đã lưu ảnh tại: {file_path}")
