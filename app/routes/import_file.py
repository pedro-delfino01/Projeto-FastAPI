from fastapi import APIRouter, UploadFile, File
from app.domain.file_processor import FileProcessor

router = APIRouter()

@router.post('/importar-pagamentos/')
async def upload_file(file: UploadFile , month: int):
    return await FileProcessor().upload_file(file, month)

