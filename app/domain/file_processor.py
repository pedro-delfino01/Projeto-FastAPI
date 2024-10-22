import csv
from fastapi import HTTPException, status, UploadFile


class FileProcessor:
    """ Manager of data from imported csv data"""

    async def upload_file(self, file: UploadFile, month: int):
        if file.filename.endswith(".csv"):
            try:
                # esse "month" é o valor da variável correspondente ao mês do arquivo.
                mes = month
                print(mes)
                # creio que o erro esteja por aqui
                content = await file.read()
                decoded_content = content.decode("utf-8").splitlines()
                csv_reader = csv.DictReader(decoded_content)
                for row in csv_reader:
                    print(row)
            except:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro "
                                                            "ao ler o arquivo.")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Formato "
                                                            "incorreto do arquivo.")
        return {"message": "Finalizado", "content": csv_reader}
