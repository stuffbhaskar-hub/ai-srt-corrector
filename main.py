from fastapi import FastAPI, UploadFile, File

app = FastAPI(title="AI SRT File Corrector")

@app.get("/")
def root():
    return {"message": "Welcome to AI SRT Fixer!"}

@app.post("/fix-srt")
async def fix_srt(
    srt_file: UploadFile = File(...),
    script_file: UploadFile = File(...)
):
    # placeholder logic for now
    content = await srt_file.read()
    return {
        "status": "success",
        "message": "SRT received successfully",
        "filename": srt_file.filename
    }
