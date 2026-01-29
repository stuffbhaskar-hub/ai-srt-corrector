from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI SRT File Corrector")

# Allow frontend calls from any domain (replace "*" with your site in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to AI SRT Fixer!"}

@app.post("/fix-srt")
async def fix_srt(srt_file: UploadFile = File(...)):
    # Dummy correction for testing
    content = await srt_file.read()
    fixed_content = content.decode("utf-8").replace("badword", "goodword")
    return {"fixed_srt": fixed_content}
