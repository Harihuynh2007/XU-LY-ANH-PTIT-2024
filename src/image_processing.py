# src/image_processing.py
import cv2
from image_utils import read_image, convert_to_grayscale, apply_gaussian_blur, apply_adaptive_threshold, apply_morphology, find_and_count_contours, draw_contours, save_image

def main():
    # Đường dẫn tới ảnh quân cờ
    image_path = 'data/ChessSet.jpg'
    
    # Đọc ảnh
    image = read_image(image_path)
    if image is None:
        return
    
    # Hiển thị ảnh gốc
    cv2.imshow('Ảnh gốc', image)
    cv2.waitKey(0)

    # 1. Chuyển đổi ảnh sang màu xám
    gray_image = convert_to_grayscale(image)

    # 2. Làm mờ ảnh để giảm nhiễu
    blurred_image = apply_gaussian_blur(gray_image)

    # 3. Áp dụng ngưỡng thích ứng (Adaptive Thresholding)
    block_size = 11  # Điều chỉnh giá trị này để tối ưu kết quả
    C = 2  # Điều chỉnh giá trị này để tối ưu kết quả
    adaptive_threshold_image = apply_adaptive_threshold(blurred_image, block_size=block_size, C=C)
    
    # 4. Áp dụng phép toán hình thái học (Morphology) để loại bỏ nhiễu
    morph_image = apply_morphology(adaptive_threshold_image)

    # 5. Tìm và đếm các đường viền, với diện tích tối thiểu để lọc nhiễu
    min_area = 500  # Điều chỉnh giá trị này để lọc nhiễu
    contours, num_objects = find_and_count_contours(morph_image, min_area=min_area)
    print(f"Số lượng đối tượng được phát hiện (min_area = {min_area}): {num_objects}")

    # 6. Vẽ đường viền quanh các đối tượng
    image_with_contours = draw_contours(image, contours)
    cv2.imshow('Ảnh với đường viền quanh đối tượng', image_with_contours)
    cv2.waitKey(0)

    # 7. Lưu ảnh đã xử lý
    output_path = '/mnt/data/output_image.jpg'
    save_image(image_with_contours, output_path)

    # Đóng tất cả các cửa sổ hiển thị
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
