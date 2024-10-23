import csv
from fastapi import HTTPException, status, UploadFile


class FileProcessor:

    """ Manager of data from imported csv data"""
    async def upload_file(self, file: UploadFile, month: int):
        final_content = []
        if month >= 1 and month <= 5:
            if file.filename.endswith(".csv"):
                try:
                    contents = await file.read()
                    decoded_file = contents.decode("utf-8").splitlines()
                    csv_reader = csv.DictReader(decoded_file)
                    # Variável "mes" corresponde ao mês do arquivo
                    # Verificar se terá algum uso dentro dessa rota do FastAPI
                    mes = month
                    for row in csv_reader:
                        del row['ï»¿""']
                        final_content.append(row)
                except:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro "
                                                                "ao ler o arquivo.")
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Formato "
                                                                "incorreto do arquivo.")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Mês "
                                                                "inválido.")
        print(final_content)
        return final_content
