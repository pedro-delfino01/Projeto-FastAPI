from datetime import datetime
import re, locale

class Resource:
    def validar_data(self, data_str):
        try:
            datetime.strptime(data_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def validar_processo(self, processo):
        padrao = r'^\d{7}$'
        if re.match(padrao, processo):
            return True
        else:
            return False

    def validar_empenho(self, empenho):
        padrao = r'^\d{7}$'
        if re.match(padrao, empenho):
            return True
        else:
            return False

    def validar_valor(self, valor):
        try:
            locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
            valor_float = locale.atof(valor.replace('R$ ', '').replace('R$', '').replace('.', '').replace(',', '.'))
            return True
        except ValueError:
            return False
