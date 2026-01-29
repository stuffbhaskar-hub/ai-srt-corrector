from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="AI SRT File Corrector")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root test
@app.get("/")
def root():
    return {"status": "API is running"}

# Fix SRT endpoint
@app.post("/fix-srt")
async def fix_srt(
    srt_file: UploadFile = File(...),
    script_file: UploadFile = File(...)
):
    srt_text = (await srt_file.read()).decode("utf-8")
    fixed_srt = srt_text.replace("badword", "goodword")
    return {"fixed_srt": fixed_srt}

# Serve frontend (optional)
app.mount("/static", StaticFiles(directory="frontend"), name="static")
