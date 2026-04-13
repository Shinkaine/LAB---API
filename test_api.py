"""
test_api.py – Kiểm thử Translation API bằng thư viện requests.
Chạy lệnh: python test_api.py
(Đảm bảo server đang chạy tại http://localhost:8000 trước khi chạy file này)
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def separator(title: str = ""):
    print(f"\n{'─' * 60}")
    if title:
        print(f"  {title}")
        print(f"{'─' * 60}")

def print_result(resp: requests.Response):
    print(f"  Status : {resp.status_code}")
    print(f"  Body   : {json.dumps(resp.json(), ensure_ascii=False, indent=4)}")

# ── 1. GET / ──────────────────────────────────────────────────────────────────
separator("TEST 1 – GET /  (Thông tin hệ thống)")
resp = requests.get(f"{BASE_URL}/")
print_result(resp)

# ── 2. GET /health ────────────────────────────────────────────────────────────
separator("TEST 2 – GET /health  (Trạng thái hệ thống)")
resp = requests.get(f"{BASE_URL}/health")
print_result(resp)

# ── 3. Câu đơn giản ───────────────────────────────────────────────────────────
separator("TEST 3 – GET /translate  (Câu đơn giản)")
resp = requests.get(f"{BASE_URL}/translate", params={"message": "Hello, how are you?"})
print_result(resp)

# ── 4. Câu phức tạp hơn ───────────────────────────────────────────────────────
separator("TEST 4 – GET /translate  (Câu phức tạp)")
resp = requests.get(f"{BASE_URL}/translate", params={
    "message": "I got up early in the morning, had a cup of coffee, and then went for a jog in the park before starting my workday."
})
print_result(resp)

# ── 5. Đoạn văn ───────────────────────────────────────────────────────────────
separator("TEST 5 – GET /translate  (Đoạn văn)")
resp = requests.get(f"{BASE_URL}/translate", params={
    "message": "The University of Science is one of the leading universities in Vietnam, known for its strong programs in natural sciences and technology."
})
print_result(resp)

# ── 6. Câu ngắn ───────────────────────────────────────────────────────────────
separator("TEST 6 – GET /translate  (Câu ngắn)")
resp = requests.get(f"{BASE_URL}/translate", params={"message": "I love sea."})
print_result(resp)

# ── 7. Lỗi: message rỗng ──────────────────────────────────────────────────────
separator("TEST 7 – GET /translate  (Lỗi: message rỗng)")
resp = requests.get(f"{BASE_URL}/translate", params={"message": "   "})
print_result(resp)

# ── 8. Lỗi: thiếu tham số message ────────────────────────────────────────────
separator("TEST 8 – GET /translate  (Lỗi: thiếu tham số)")
resp = requests.get(f"{BASE_URL}/translate")
print_result(resp)

# ── 9. Lỗi: message quá dài ───────────────────────────────────────────────────
separator("TEST 9 – GET /translate  (Lỗi: message vượt 512 ký tự)")
resp = requests.get(f"{BASE_URL}/translate", params={"message": "word " * 200})
print_result(resp)

separator()
print("\n✓ Hoàn tất kiểm thử!\n")