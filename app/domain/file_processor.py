import csv, re
from fastapi import HTTPException, status, UploadFile
from app.resources.validate import Resource

validacao = Resource()

class FileProcessor:

    """ Manager of data from imported csv data"""
    async def upload_file(self, file: UploadFile, month: int):
        final_content = []
        if month >= 1 and month <= 5:
            if file.filename.endswith(".csv"):
                contents = await file.read()
                decoded_file = contents.decode("utf-8").splitlines()
                csv_reader = csv.DictReader(decoded_file)
                # Variável "mes" corresponde ao mês do arquivo
                # Verificar se terá algum uso dentro dessa rota do FastAPI
                for row in csv_reader:
                    del row['ï»¿""']
                    validate_regex = int(re.search('\\d{2}(?=/\\d{4}$)', row["Data"]).group())
                    print(validate_regex)
                    if validate_regex == month:
                        # Validação dos dados vindos do arquivo csv
                        resultado_data = validacao.validar_data(row['Data'])
                        resultado_processo = validacao.validar_processo(row['Processo'])
                        resultado_empenho = validacao.validar_empenho(row['Empenho'])
                        resultado_pago = validacao.validar_valor(row['Pago'])
                        resultado_retido = validacao.validar_valor(row['Retido'])
                        resultado_anulacao = validacao.validar_valor(row['Anulação'])
                        if not (resultado_data and resultado_processo and resultado_empenho and resultado_pago and resultado_retido and resultado_anulacao):
                            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Dados não "
                                                                                                "validados.")
                    else:
                        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Mês "
                                                                               "inválido.")
                    final_content.append(row)
                else:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro "
                                                                "ao ler o arquivo.")
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Formato "
                                                                "incorreto do arquivo.")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Mês "
                                                                "inválido.")
        return final_content
