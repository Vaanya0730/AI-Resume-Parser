import os
import json
import sys

from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pypdf import PdfReader

from resumeparser import ats_extractor

sys.path.insert(0, os.path.abspath(os.getcwd()))

UPLOAD_PATH = "__DATA__"
os.makedirs(UPLOAD_PATH, exist_ok=True)

app = FastAPI(title="Resume Parser")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "data": None
        }
    )


@app.post("/process", response_class=HTMLResponse)
async def process_resume(
    request: Request,
    pdf_doc: UploadFile = File(...)
):

    file_path = os.path.join(UPLOAD_PATH, "file.pdf")

    with open(file_path, "wb") as f:
        f.write(await pdf_doc.read())

    data = read_file_from_path(file_path)

    extracted = ats_extractor(data)

    print("\n========== EXTRACTED ==========")
    print(repr(extracted))
    print("================================\n")

    try:
        parsed_data = json.loads(extracted)
    except Exception as e:
        parsed_data = {
            "error": "The AI did not return valid JSON.",
            "details": str(e),
            "raw_response": extracted
        }

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "data": parsed_data
        }
    )


def read_file_from_path(path):

    reader = PdfReader(path)

    text = ""

    for page in reader.pages:
        extracted_text = page.extract_text()

        if extracted_text:
            text += extracted_text

    return text


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )