from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI SRT File Corrector")

# Enable CORS for frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your site domain for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route for testing
@app.get("/")
def root():
    return {"message": "Welcome to AI SRT Fixer!"}

# Main endpoint
@app.post("/fix-srt")
async def fix_srt(
    srt_file: UploadFile = File(...),
    script_file: UploadFile = File(...)
):
    # Read uploaded files
    srt_content = await srt_file.read()
    script_content = await script_file.read()

    # Dummy fix logic: replace "badword" with "goodword"
    # You can replace this with your actual AI/script correction logic
    fixed_srt = srt_content.decode("utf-8").replace("badword", "goodword")

    return {"fixed_srt": fixed_srt}
