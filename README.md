# 🌲 Hệ Thống Tham Vấn Ý Kiến Các Bên Liên Quan — FSC Văn Hán Trường Thịnh Phát 2026

**Nhóm Chứng chỉ Rừng Văn Hán — Trường Thịnh Phát**  
**Mã chứng chỉ FSC:** `FSC-C183027`  
**Chủ thể:** Công ty TNHH Thương mại và Đầu tư Trường Thịnh Phát  
**Tác giả hệ thống:** Lộc Vũ Trung  

---

## 📌 1. Giới thiệu tổng quan
Hệ thống web tham vấn ý kiến các bên liên quan được xây dựng nhằm phục vụ công tác đánh giá cấp và duy trì chứng chỉ Quản lý rừng bền vững theo tiêu chuẩn quốc tế FSC (FSC-STD-VN-01-2020) cho diện tích **3.804,59 ha** rừng trồng Keo sản xuất của **1.674 hộ gia đình** tại 04 xã: Văn Hán, Văn Lăng, Quang Sơn, Đồng Hỷ (tỉnh Thái Nguyên), cùng **628,40 ha rừng đặc dụng liên kết bảo vệ** (Rừng Mẫu đại diện theo Thỏa thuận phối hợp ngày 25/03/2025 với Ban QLR Đặc dụng Thần Sa - Phượng Hoàng).

Hệ thống cung cấp đầy đủ:
1. **Tài liệu tóm tắt 03 trang A4 chuẩn mực**: Tóm tắt Phương án QLRBV (2025–2031), Đánh giá Tác động Môi trường (EIA), Tác động Xã hội (SIA), Rừng có Giá trị Bảo tồn Cao (HCVF) & Rừng Nguyên vẹn (IFL).
2. **Phiếu tham vấn trực tuyến đầy đủ nội dung**: Thu thập ý kiến qua 06 tiêu chí FSC cốt lõi, có cam kết đã đọc hiểu và chấp thuận hoàn toàn.
3. **Trang báo cáo thống kê kết quả (Dashboard)**: Bảo mật bằng mật khẩu `TTP2026`, hiển thị biểu đồ Chart.js trực quan, bộ lọc đa năng và danh sách phản hồi chi tiết.
4. **Xuất báo cáo Excel (.xlsx)**: Tạo file Excel chuẩn mực với thuộc tính tác giả `Author = "Lộc Vũ Trung"` và công thức tự nhiên.

---

## 📂 2. Cấu trúc thư mục dự án

```text
TruongThinhPhat2026/
├── index.html              # Trang chủ: Phiếu tham vấn trực tuyến & Tóm tắt 3 trang
├── tai-lieu-tom-tat.html   # Bản in A4 độc lập: Toàn văn tài liệu tóm tắt 03 trang
├── report.html             # Dashboard báo cáo & thống kê (Mật khẩu: TTP2026)
├── server.py               # Dịch vụ backend Python / SQLite cho VPS hoặc Localhost
├── README.md               # Tài liệu hướng dẫn sử dụng và triển khai
└── data/                   # Thư mục lưu trữ database SQLite & File Excel xuất bản
```

---

## 🔐 3. Thông tin tài khoản & Mật khẩu
* **Trang quản trị báo cáo:** `report.html`
* **Mật khẩu truy cập (Pass):** `TTP2026`

---

## 🚀 4. Hướng dẫn triển khai

### A. Triển khai miễn phí trên GitHub Pages (Khuyên dùng)
1. Đẩy mã nguồn lên repository: `https://github.com/locvutrunglvt/TruongThinhPhat2026`
2. Vào tab **Settings** của repository trên GitHub.
3. Chọn mục **Pages** (bên menu trái).
4. Tại mục **Build and deployment** -> **Branch**: Chọn `main` và thư mục `/(root)` -> Nhấn **Save**.
5. Sau 1–2 phút, website sẽ hoạt động trực tiếp tại địa chỉ:  
   👉 **`https://locvutrunglvt.github.io/TruongThinhPhat2026/`**

### B. Chạy trên máy tính cá nhân hoặc máy chủ VPS
Nếu muốn lưu trữ dữ liệu tập trung qua SQLite và API backend:
```bash
python server.py
```
Truy cập hệ thống tại: `http://localhost:8086/`

---

## 📊 5. Xuất báo cáo Excel
* Tại trang `report.html` (sau khi mở khóa bằng mật khẩu `TTP2026`), bấm nút **"XUẤT BÁO CÁO EXCEL (.XLSX)"**.
* Hệ thống sẽ tự động xuất file `Bao_Cao_Tong_Hop_Tham_Van_Van_Han_TTP_2026.xlsx` chứa đầy đủ bảng dữ liệu, công thức tính tổng và thuộc tính tác giả: **Lộc Vũ Trung**.
