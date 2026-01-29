from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to access backend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/fix-srt")
async def fix_srt(
    srt_file: UploadFile = File(...),
    script_file: UploadFile = File(None)
):
    # Read SRT file
    srt_content = (await srt_file.read()).decode("utf-8")

    # Basic fix logic: remove empty lines and extra spaces
    lines = [line.strip() for line in srt_content.split("\n") if line.strip() != ""]
    fixed_srt = "\n".join(lines)

    # Optional: you can later use script_file for advanced fixes

    return {"fixed_srt": fixed_srt}
