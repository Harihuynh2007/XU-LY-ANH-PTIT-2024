# Xử Lý Ảnh - Đồ Án Môn Học - PTIT 2024
- Liên hệ
  - Tác giả: Harihuynh2007
  - Email: Hminhhai2000@gmail.com
## Giới thiệu
Đây là đồ án môn học Xử lý ảnh của HUỲNH MINH HẢI tại PTIT. Mục tiêu của đồ án là xây dựng một ứng dụng xử lý ảnh để nhận diện và đếm số lượng đối tượng trong ảnh. Dự án này giúp các bạn làm quen với các kỹ thuật xử lý ảnh cơ bản như ngưỡng màu, phát hiện cạnh và đếm đối tượng. Ứng dụng được mình xây dựng bằng Python, sử dụng thư viện OpenCV để xử lý ảnh và Tkinter để tạo giao diện đơn giản.

## Mục tiêu của dự án
- Áp dụng các kỹ thuật xử lý ảnh cơ bản như:
  - Ngưỡng màu (Thresholding).
  - Phát hiện cạnh (Edge Detection) bằng thuật toán Canny.
  - Phân đoạn và đếm số lượng đối tượng trong ảnh.
- Xây dựng một ứng dụng đơn giản để xử lý ảnh theo yêu cầu của đề tài.
- Tìm hiểu và sử dụng các thư viện Python cho xử lý ảnh như OpenCV, NumPy, và Matplotlib.

## Cấu trúc dự án
- src/: Thư mục chứa mã nguồn của dự án:
  - image_processing.py: Chứa các hàm xử lý ảnh, phát hiện và đếm số lượng đối tượng.
  - main.py: Tạo giao diện người dùng và gọi các hàm từ image_processing.py.
- data/: Thư mục chứa các ảnh mẫu.
- notebook/: Thư mục chứa tệp log (log.txt) ghi lại thông tin của các ảnh đã xử lý.
- README.md: Tài liệu hướng dẫn sử dụng và tìm hiểu về đồ án.


## Các thuật toán sử dụng
- Ngưỡng màu (Thresholding): Chuyển đổi ảnh sang dạng nhị phân (đen trắng) để dễ dàng phát hiện đối tượng.
- Phát hiện cạnh (Canny Edge Detection): Dùng để tìm kiếm các cạnh trong ảnh. Các cạnh này sẽ được sử dụng để xác định các đường bao (contours) của các đối tượng.
- Đếm đối tượng: Sau khi phát hiện các đường bao, chương trình sẽ đếm số lượng đường bao có diện tích lớn hơn một ngưỡng nhất định để xác định số lượng đối tượng trong ảnh.
## Điều chỉnh thông số
- Bạn có thể điều chỉnh các ngưỡng low_threshold và high_threshold của thuật toán Canny Edge Detection thông qua giao diện để phù hợp với ảnh cần xử lý.
- Giá trị mặc định:
  - Low threshold: 100
  - High threshold: 200
- Bạn cũng có thể thay đổi ngưỡng diện tích tối thiểu (min_contour_area) trong mã để loại bỏ các đối tượng nhỏ không cần thiết.
## Ghi log
- Kết quả xử lý, bao gồm đường dẫn ảnh, số lượng đối tượng được đếm, và các tham số ngưỡng đã sử dụng, sẽ được ghi lại trong tệp log.txt nằm trong thư mục notebook.
## Lưu ý
- Khi chọn vùng ROI, hãy chọn khu vực chứa các đối tượng cần đếm để tránh nhiễu từ các vùng khác trong ảnh.
- Để có kết quả chính xác hơn, bạn có thể thử nghiệm với các ngưỡng của Canny Edge Detection và ngưỡng diện tích contours.
- 
## Yêu cầu phần cứng và phần mềm
- **Phần cứng:** 
  - Laptop: Cấu hình tối thiểu: CPU Intel Core i5, RAM 8GB, ổ cứng SSD 256GB.
  - Camera có độ phân giải tối thiểu 8MP để chụp ảnh mẫu (tùy chọn).

- **Phần mềm:**
  - Python 3.x
  - Các thư viện Python: OpenCV, NumPy, Matplotlib, Tkinter (tích hợp sẵn trong Python).
  - Hệ điều hành: Windows, Linux, hoặc macOS.

## Cài đặt
### 1. Cài đặt Python
- Tải và cài đặt Python từ trang chủ: [https://www.python.org/downloads/](https://www.python.org/downloads/).

### 2. Cài đặt các thư viện cần thiết
Mở Terminal (hoặc Command Prompt) và chạy lệnh sau để cài đặt các thư viện cần thiết:
```bash
pip install opencv-python numpy matplotlib



