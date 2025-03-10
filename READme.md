# b1: Run `pip install -r requirements.txt`

# b2: Run Script `uvicorn ServicesWord2PDF:app --host 0.0.0.0 --port 8000 --reload` doi port theo server hien co

# b3: Test run CURL or refulAPI: `curl -X POST "http://127.0.0.1:8000/convert/" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@\"D:\ShuffeWordExam\FileTest\(Mẫu) đề TN THPT 2025 - OLM.docx\""`