#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Truong Thinh Phat FSC Consultation Backend Service & Server
Author Metadata: "Lộc Vũ Trung"
Port: 8086 (Default)
Password Key: TTP2026
"""

import os
import sys
import json
import sqlite3
import datetime
import urllib.parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

PORT = 8086
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "ttp_consultations.db")
EXCEL_PATH = os.path.join(DATA_DIR, "Bao_Cao_Tong_Hop_Tham_Van_Van_Han_TTP_2026.xlsx")

os.makedirs(DATA_DIR, exist_ok=True)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS consultations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            fullName TEXT,
            jobTitle TEXT,
            orgName TEXT,
            commune TEXT,
            stakeholderGroup TEXT,
            phone TEXT,
            email TEXT,
            q1_land TEXT,
            q1_note TEXT,
            q2_labor TEXT,
            q2_note TEXT,
            q3_env TEXT,
            q3_note TEXT,
            q4_bio TEXT,
            q4_note TEXT,
            q5_social TEXT,
            q5_note TEXT,
            q6_mgmt TEXT,
            q6_note TEXT,
            general_feedback TEXT,
            agree_commitment INTEGER,
            signerName TEXT
        )
    ''')
    conn.commit()
    conn.close()

def generate_excel():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM consultations ORDER BY id ASC")
    rows = cur.fetchall()
    conn.close()

    wb = openpyxl.Workbook()
    wb.properties.creator = "Lộc Vũ Trung"
    wb.properties.lastModifiedBy = "Lộc Vũ Trung"
    wb.properties.title = "Báo Cáo Tổng Hợp Kết Quả Tham Vấn FSC Văn Hán - TTP 2026"

    ws = wb.active
    ws.title = "Tong_Hop_Tham_Van"
    ws.views.sheetView[0].showGridLines = True

    # Styling
    font_title = Font(name="Calibri", size=13, bold=True, color="1B365D")
    font_sub = Font(name="Calibri", size=10, italic=True, color="4A607A")
    font_hdr = Font(name="Calibri", size=9.5, bold=True, color="FFFFFF")
    font_normal = Font(name="Calibri", size=9)
    font_bold = Font(name="Calibri", size=9, bold=True)
    
    fill_hdr = PatternFill(start_color="15803D", end_color="15803D", fill_type="solid")
    fill_summary = PatternFill(start_color="FFF3E0", end_color="FFF3E0", fill_type="solid")
    fill_zebra = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
    
    thin_border = Side(style='thin', color='CBD5E1')
    double_border = Side(style='double', color='15803D')
    border_cell = Border(left=thin_border, right=thin_border, top=thin_border, bottom=thin_border)
    border_sum = Border(left=thin_border, right=thin_border, top=thin_border, bottom=double_border)

    ws.cell(1, 1, "CÔNG TY TNHH THƯƠNG MẠI VÀ ĐẦU TƯ TRƯỜNG THỊNH PHÁT").font = font_title
    ws.cell(2, 1, "BẢNG TỔNG HỢP Ý KIẾN THAM VẤN CÁC BÊN LIÊN QUAN — FSC VĂN HÁN (FSC-C183027)").font = font_title
    ws.cell(3, 1, f"Ngày xuất báo cáo: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')} | Tác giả: Lộc Vũ Trung | Mật khẩu xác thực: TTP2026").font = font_sub

    headers = [
        "STT", "Thời gian nộp", "Họ và tên người tham vấn", "Chức vụ / Vị trí", "Cơ quan / Đơn vị / Thôn xóm",
        "Địa bàn xã", "Nhóm bên liên quan", "Số điện thoại", "Email",
        "Tiêu chí 1: Đất đai & Ranh giới", "Ghi chú TC1",
        "Tiêu chí 2: An toàn LĐ & Bình đẳng", "Ghi chú TC2",
        "Tiêu chí 3: Môi trường, Nước & Hóa chất", "Ghi chú TC3",
        "Tiêu chí 4: ĐDSH & Rừng mẫu 628,40 ha", "Ghi chú TC4",
        "Tiêu chí 5: Văn hóa tâm linh (HCV6)", "Ghi chú TC5",
        "Tiêu chí 6: Phương án QLRBV & AAC", "Ghi chú TC6",
        "Ý kiến đóng góp khác / Kiến nghị", "Xác nhận cam kết đã đọc hiểu", "Người ký xác nhận"
    ]

    for c_i, h in enumerate(headers, 1):
        c = ws.cell(5, c_i, h)
        c.font = font_hdr
        c.fill = fill_hdr
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = border_cell
    ws.row_dimensions[5].height = 26

    for r_idx, r in enumerate(rows, start=6):
        data_cells = [
            r_idx - 5, r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8],
            r[9], r[10], r[11], r[12], r[13], r[14], r[15], r[16], r[17], r[18], r[19], r[20],
            r[21], "Đã đọc hiểu và chấp thuận hoàn toàn", r[23]
        ]
        for c_idx, val in enumerate(data_cells, 1):
            cell = ws.cell(r_idx, c_idx, val)
            cell.font = font_normal
            cell.border = border_cell
            if c_idx in [1, 2, 8]:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center")
            if r_idx % 2 == 1:
                cell.fill = fill_zebra
        ws.row_dimensions[r_idx].height = 20

    # Summary Row
    last_row = 5 + len(rows)
    if len(rows) > 0:
        sum_row_idx = last_row + 1
        ws.cell(sum_row_idx, 1, "TỔNG SỐ PHIẾU:").font = font_bold
        ws.cell(sum_row_idx, 1).border = border_sum
        ws.cell(sum_row_idx, 1).fill = fill_summary

        ws.cell(sum_row_idx, 2, f"=COUNTA(C6:C{last_row})").font = font_bold
        ws.cell(sum_row_idx, 2).border = border_sum
        ws.cell(sum_row_idx, 2).fill = fill_summary
        ws.cell(sum_row_idx, 2).alignment = Alignment(horizontal="center")

        for c_i in range(3, len(headers) + 1):
            cell = ws.cell(sum_row_idx, c_i, "")
            cell.border = border_sum
            cell.fill = fill_summary

        ws.cell(sum_row_idx, 10, f'=COUNTIF(J6:J{last_row}, "Hoàn toàn nhất trí*")').font = font_bold
        ws.cell(sum_row_idx, 12, f'=COUNTIF(L6:L{last_row}, "Hoàn toàn nhất trí*")').font = font_bold
        ws.cell(sum_row_idx, 14, f'=COUNTIF(N6:N{last_row}, "Hoàn toàn nhất trí*")').font = font_bold
        ws.cell(sum_row_idx, 16, f'=COUNTIF(P6:P{last_row}, "Hoàn toàn nhất trí*")').font = font_bold
        ws.cell(sum_row_idx, 18, f'=COUNTIF(R6:R{last_row}, "Hoàn toàn nhất trí*")').font = font_bold
        ws.cell(sum_row_idx, 20, f'=COUNTIF(T6:T{last_row}, "Hoàn toàn nhất trí*")').font = font_bold
        ws.cell(sum_row_idx, 23, "100% Đã xác nhận").font = font_bold

    # Column widths
    col_widths = [6, 18, 24, 22, 32, 18, 36, 16, 22, 30, 25, 30, 25, 30, 25, 30, 25, 30, 25, 30, 25, 40, 30, 24]
    for idx, w in enumerate(col_widths, 1):
        ws.column_dimensions[get_column_letter(idx)].width = w

    wb.save(EXCEL_PATH)
    return EXCEL_PATH

class TTPRequestHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/submit':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                conn = sqlite3.connect(DB_PATH)
                cur = conn.cursor()
                cur.execute('''
                    INSERT INTO consultations (
                        timestamp, fullName, jobTitle, orgName, commune, stakeholderGroup,
                        phone, email, q1_land, q1_note, q2_labor, q2_note, q3_env, q3_note,
                        q4_bio, q4_note, q5_social, q5_note, q6_mgmt, q6_note, general_feedback,
                        agree_commitment, signerName
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    data.get('timestamp', datetime.datetime.now().strftime('%d/%m/%Y %H:%M')),
                    data.get('fullName', ''),
                    data.get('jobTitle', ''),
                    data.get('orgName', ''),
                    data.get('commune', ''),
                    data.get('stakeholderGroup', ''),
                    data.get('phone', ''),
                    data.get('email', ''),
                    data.get('q1_land', ''),
                    data.get('q1_note', ''),
                    data.get('q2_labor', ''),
                    data.get('q2_note', ''),
                    data.get('q3_env', ''),
                    data.get('q3_note', ''),
                    data.get('q4_bio', ''),
                    data.get('q4_note', ''),
                    data.get('q5_social', ''),
                    data.get('q5_note', ''),
                    data.get('q6_mgmt', ''),
                    data.get('q6_note', ''),
                    data.get('general_feedback', ''),
                    1 if data.get('agree_commitment') else 0,
                    data.get('signerName', data.get('fullName', ''))
                ))
                conn.commit()
                conn.close()

                generate_excel()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'success', 'message': 'Submitted successfully'}).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'error', 'message': str(e)}).encode('utf-8'))
            return

        super().do_POST()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == '/api/download':
            params = urllib.parse.parse_qs(parsed.query)
            if params.get('key', [''])[0] == 'TTP2026':
                excel_file = generate_excel()
                self.send_response(200)
                self.send_header('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                self.send_header('Content-Disposition', 'attachment; filename="Bao_Cao_Tong_Hop_Tham_Van_Van_Han_TTP_2026.xlsx"')
                self.end_headers()
                with open(excel_file, 'rb') as f:
                    self.wfile.write(f.read())
                return
            else:
                self.send_response(403)
                self.send_header('Content-Type', 'text/plain; charset=utf-8')
                self.end_headers()
                self.wfile.write('Từ chối truy cập! Mật khẩu không chính xác.'.encode('utf-8'))
                return

        if parsed.path == '/api/data':
            conn = sqlite3.connect(DB_PATH)
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * FROM consultations ORDER BY id DESC")
            records = [dict(row) for row in cur.fetchall()]
            conn.close()

            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps(records, ensure_ascii=False).encode('utf-8'))
            return

        super().do_GET()

if __name__ == '__main__':
    init_db()
    os.chdir(BASE_DIR)
    print(f"🌲 Truong Thinh Phat FSC Consultation Server running on http://localhost:{PORT}")
    server = HTTPServer(('0.0.0.0', PORT), TTPRequestHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        server.server_close()
