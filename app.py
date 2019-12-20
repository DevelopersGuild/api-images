from typing import List
from fastapi import (FastAPI, File, UploadFile)
from starlette.responses import (HTMLResponse, RedirectResponse, PlainTextResponse, JSONResponse)
from starlette.status import (HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK)
from utilities import (generate_unique_name, filename_validation)

app = FastAPI()

# CREATE routes for image uploads

# Multi File Upload (FastAPI UploadFile)
@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    try:
        [filename_validation(file.filename) for file in files]
        return JSONResponse(status_code=HTTP_200_OK, content={"filenames": [file.filename for file in files]})
    except Exception as e:
        print(e)
        return PlainTextResponse(status_code=HTTP_500_INTERNAL_SERVER_ERROR,content=str(e))
        

# Single File Upload (FastAPI UploadFile)
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    try:
        filename_validation(file.filename)
        return JSONResponse(status_code=HTTP_200_OK, content={"filename": file.filename })
    except Exception as e:
        print(e)
        return PlainTextResponse(status_code=HTTP_500_INTERNAL_SERVER_ERROR,content=str(e))


# For Testing the endpoints
@app.get("/")
async def main():
    content = """
<body>
    <div align="center">
            <br/>
            <h1> UploadFile test  (Multiple)</h1>
            <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
                <input name="files" type="file" multiple>
                <input type="submit">
            </form>
            <br/>
            <h1> UploadFile test (Single)</h1>
            <form action="/uploadfile/" enctype="multipart/form-data" method="post">
                <input name="files" type="file">
                <input type="submit">
            </form>
    </div>
</body>

    """
    return HTMLResponse(content=content)