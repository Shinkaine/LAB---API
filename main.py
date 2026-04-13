from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from transformers import MarianMTModel, MarianTokenizer

# ── Cấu hình ─────────────────────────────────────────────────────────────────
MODEL_NAME = "Helsinki-NLP/opus-mt-en-vi"

# ── Khởi tạo app ─────────────────────────────────────────────────────────────
app = FastAPI(
    title="English → Vietnamese Translation API",
    description="Web API dịch văn bản từ tiếng Anh sang tiếng Việt sử dụng mô hình Helsinki-NLP/opus-mt-en-vi",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Load model một lần khi khởi động ─────────────────────────────────────────
print(f"[INFO] Đang tải mô hình: {MODEL_NAME} ...")
tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
model     = MarianMTModel.from_pretrained(MODEL_NAME)
print("[INFO] Tải mô hình thành công!")


# ── Endpoints ─────────────────────────────────────────────────────────────────
@app.get("/", summary="Thông tin hệ thống")
def root():
    return {
        "service": "English → Vietnamese Translation API",
        "model": MODEL_NAME,
        "description": (
            "API dịch máy từ tiếng Anh sang tiếng Việt sử dụng mô hình "
            "MarianMT của Helsinki-NLP."
        ),
        "endpoints": {
            "GET  /":          "Thông tin hệ thống",
            "GET  /health":    "Kiểm tra trạng thái hoạt động",
            "GET  /translate": "Dịch văn bản từ tiếng Anh sang tiếng Việt",
        },
    }


@app.get("/health", summary="Kiểm tra trạng thái hệ thống")
def health():
    return {
        "status": "ok",
        "model_loaded": model is not None,
        "model": MODEL_NAME,
        "task": "translation_en_to_vi",
    }


@app.get("/translate", summary="Dịch tiếng Anh → tiếng Việt")
def translate(message: str):
    """
    Nhận văn bản tiếng Anh và trả về bản dịch tiếng Việt.

    - **message**: Văn bản tiếng Anh cần dịch (tối đa 512 ký tự)
    """
    if not message or not message.strip():
        raise HTTPException(status_code=422, detail="'message' không được để trống.")
    if len(message) > 512:
        raise HTTPException(status_code=422, detail="'message' không được vượt quá 512 ký tự.")

    try:
        inputs = tokenizer([message], return_tensors="pt", padding=True, truncation=True)
        translated_ids = model.generate(**inputs)
        translated_text = tokenizer.decode(translated_ids[0], skip_special_tokens=True)

        return {
            "source_language": "English",
            "target_language": "Vietnamese",
            "original_text":   message,
            "translated_text": translated_text,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi dịch thuật: {str(e)}")
