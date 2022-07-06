import shutil
from fastapi import FastAPI, File, UploadFile



app = FastAPI()

@app.post("/files/")
async def create_file(file: UploadFile = File(...)):
    if not file:
        return {"message": "No file sent"}
    else:
        with open(f'{file.filename}',"wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"filename": file.filename}