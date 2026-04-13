# English → Vietnamese Translation API

> LAB - API
> Môn: \*\*Tư Duy Tính Toán\*\* | Khoa Công Nghệ Thông Tin – ĐHKHTN TP.HCM

\---

## Thông tin

|Họ và tên|MSSV|
|-|-|
|*Nguyễn Thành Đạt*|*24120173*|

\---

## Mô hình sử dụng

|Thông tin|Chi tiết|
|-|-|
|**Tên mô hình**|`Helsinki-NLP/opus-mt-en-vi`|
|**Hugging Face**|https://huggingface.co/Helsinki-NLP/opus-mt-en-vi|
|**Loại tác vụ**|Machine Translation – Dịch máy (Anh → Việt)|
|**Kiến trúc**|MarianMT (encoder-decoder Transformer)|
|**Dữ liệu huấn luyện**|OPUS corpus (hàng triệu cặp câu song ngữ Anh–Việt)|

\---

## Mô tả hệ thống

API nhận một đoạn văn bản tiếng Anh và trả về bản dịch tiếng Việt tương ứng.

**Ví dụ:**

* Input: `"Artificial intelligence is changing the worl"`
* Output: `"Trí tuệ nhân tạo đang thay đổi thế giới."`

\---

## Cấu trúc project

```
lab1-api/
├── main.py           # FastAPI application chính
├── test_api.py       # File kiểm thử API bằng requests
├── requirements.txt  # Danh sách thư viện cần cài
├── notebook.ipynb    # File notebook chạy trên Notebook Google Colab
└── README.md         # Tài liệu dự án
```

\---

## Hướng dẫn cài đặt

### Yêu cầu

* Python **3.9+**

### Các bước

```bash
# 1. Clone repository
git clone https://github.com/Shinkaine/LAB---API.git
cd LAB---API

# 2. Cài đặt thư viện
pip install -r requirements.txt
```

\---

## Hướng dẫn chạy chương trình

```bash
uvicorn main:app --reload
```

Server khởi động tại: **http://localhost:8000**

> \*\*Lưu ý:\*\* Lần đầu chạy, mô hình (\~300MB) sẽ được tải về tự động. Chờ đến khi terminal hiển thị `Tải mô hình thành công!`

Swagger UI: **http://localhost:8000/docs**

\---

## Hướng dẫn gọi API

### `GET /` – Thông tin hệ thống

```bash
curl http://localhost:8000/
```

**Response mẫu:**

```json
{
  "service": "English → Vietnamese Translation API",
  "model": "Helsinki-NLP/opus-mt-en-vi",
  "description": "API dịch máy từ tiếng Anh sang tiếng Việt...",
  "endpoints": {
    "GET  /": "Thông tin hệ thống",
    "GET  /health": "Kiểm tra trạng thái hoạt động",
    "GET  /translate": "Dịch văn bản từ tiếng Anh sang tiếng Việt"
  }
}
```

\---

### `GET /health` – Kiểm tra trạng thái

```bash
curl http://localhost:8000/health
```

**Response mẫu:**

```json
{
  "status": "ok",
  "model\_loaded": true,
  "model": "Helsinki-NLP/opus-mt-en-vi",
  "task": "translation\_en\_to\_vi"
}
```

\---

### `GET /translate` – Dịch văn bản

**Request 1:**

```bash
curl "http://localhost:8000/translate?message=Hello%2C+how+are+you%3F"
```

**Response mẫu:**

```json
{
  "source\_language": "English",
  "target\_language": "Vietnamese",
  "original\_text": "Hello, how are you?",
  "translated\_text": "Xin chào, bạn có khỏe không?"
}
```

**Request 2:**

```bash
curl "http://localhost:8000/translate?message=Artificial+intelligence+is+changing+the+world."
```

**Response mẫu:**

```json
{
  "source\_language": "English",
  "target\_language": "Vietnamese",
  "original\_text": "Artificial intelligence is changing the world.",
  "translated\_text": "Trí tuệ nhân tạo đang thay đổi thế giới."
}
```

\---

### Xử lý lỗi

|Trường hợp|HTTP Status|Mô tả|
|-|-|-|
|Thiếu tham số `message`|422|Dữ liệu đầu vào không hợp lệ|
|`message` rỗng|422|Không được để trống|
|`message` > 512 ký tự|422|Vượt quá giới hạn ký tự|
|Lỗi mô hình|500|Lỗi trong quá trình dịch thuật|

\---

## Chạy kiểm thử

```bash
# Đảm bảo server đang chạy trước
python test_api.py
```

\---

## Google Colab

Mở `notebook.ipynb` trên Google Colab để chạy pipeline đầy đủ:  
cài thư viện → tạo config → load model → test model → khởi động API → gọi API.

\---

## Video Demo

> \*\*\[Xem video demo tại đây](#)\*\*  


https://github.com/user-attachments/assets/95247c1b-0c74-48c4-a5aa-21d2ce2414a3







\---

