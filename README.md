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
├── vercel.json             # Cấu hình tối ưu định tuyến và Clean URLs cho Vercel
├── api/                    # Vercel Serverless Functions
│   ├── submit.js           # Endpoint tiếp nhận nộp phiếu (/api/submit)
│   └── data.js             # Endpoint API trạng thái hệ thống (/api/data)
├── package.json            # Khai báo cấu hình dự án
├── server.py               # Dịch vụ backend Python / SQLite dự phòng cho VPS/Local
├── README.md               # Hướng dẫn sử dụng và triển khai
└── data/                   # Thư mục lưu trữ database SQLite & File Excel xuất bản
```

---

## 🔐 3. Thông tin tài khoản & Mật khẩu
* **Trang quản trị báo cáo:** `report.html` (hoặc `/report` trên Vercel)
* **Mật khẩu truy cập (Pass):** `TTP2026`

---

## ⚡ 4. Hướng dẫn Triển khai lên VERCEL

### Cách 1: Triển khai tự động từ GitHub (Khuyên dùng — 1 phút là xong)
1. Truy cập [https://vercel.com/new](https://vercel.com/new) và đăng nhập bằng tài khoản GitHub của bạn.
2. Tìm repository: **`locvutrunglvt/TruongThinhPhat2026`** và nhấn **Import**.
3. Tại màn hình cấu hình dự án:
   * **Project Name:** `truongthinhphat2026` (hoặc tên tùy chọn)
   * **Framework Preset:** `Other`
   * **Root Directory:** `./`
4. Bấm **Deploy**.
5. Vercel sẽ tự động build và cấp domain miễn phí tốc độ cao toàn cầu:
   👉 **`https://truongthinhphat2026.vercel.app`** (hoặc subdomain tương ứng của bạn).

### Cách 2: Triển khai trực tiếp từ máy tính bằng Vercel CLI
```bash
cd "g:\My Drive\GIS\FSC\Thai Nguyen\Van Han 2026\Dong Loi\TruongThinhPhat2026"
npx vercel
```
* Làm theo hướng dẫn đăng nhập và chọn xác nhận deploy lên tài khoản Vercel cá nhân.

---

## 📊 5. Xuất báo cáo Excel
* Tại trang `report.html` hoặc `/report` (sau khi mở khóa bằng mật khẩu `TTP2026`), bấm nút **"XUẤT BÁO CÁO EXCEL (.XLSX)"**.
* Hệ thống sẽ tự động xuất file `Bao_Cao_Tong_Hop_Tham_Van_Van_Han_TTP_2026.xlsx` chứa đầy đủ bảng dữ liệu, công thức tính tổng và thuộc tính tác giả: **Lộc Vũ Trung**.
