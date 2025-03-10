from fastapi import FastAPI, File, UploadFile
import shutil
import os
from spire.doc import *
from spire.doc.common import *

from spire.doc import *
from spire.pdf import *
from spire.xls import *
from spire.presentation import *
from spire.pdf.common import License as pdfLicense
from spire.doc.common import License as docLicense
from spire.xls.common import License as xlsLicense
from spire.presentation.common import License as pptLicense

from dotenv import load_dotenv
load_dotenv()

key = os.getenv("LICENSE_KEY")

pdfLicense.SetLicenseKey(key)
docLicense.SetLicenseKey(key)
xlsLicense.SetLicenseKey(key)
pptLicense.SetLicenseKey(key)


app = FastAPI()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "output"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/convert/")
async def convert_word_to_pdf(file: UploadFile = File(...)):
    input_path = os.path.join(UPLOAD_DIR, file.filename)
    output_filename = os.path.splitext(file.filename)[0] + ".pdf"
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    document = Document()
    document.LoadFromFile(input_path)
    document.SaveToFile(output_path, FileFormat.PDF)
    document.Close()
    
    return {"message": "Conversion successful", "pdf_path": output_path}