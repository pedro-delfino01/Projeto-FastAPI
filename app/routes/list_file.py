from flask import request, jsonify

from app.database.sessao import db
from app.model.pagamentos import Pagamentos

def register_routes(app):
    @app.route("/pagamentos/", methods=['GET'])
    def listar_pagamentos():
        pagamentos = Pagamentos.query.all()

        resultados = []
        for pagamento in pagamentos:
            result = {
                'orgao': pagamento.orgao,
                'unidade': pagamento.unidade,
                'data': pagamento.data,
                'empenho': pagamento.empenho,
                'processo': pagamento.processo,
                'credor': pagamento.credor,
                'pago': pagamento.pago,
                'retido': pagamento.retido,
                'anulacao': pagamento.anulacao,
                'nota': pagamento.nota,
                'cnpj': pagamento.cnpj,
                'ds_empenho': pagamento.ds_empenho,
                'ds_item_despesa': pagamento.ds_item_despesa
            }
            resultados.append(result)

        return jsonify(resultados), 200
