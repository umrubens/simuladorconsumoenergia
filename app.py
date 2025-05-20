from flask import Flask, request, render_template, jsonify
from calculos_eletricos import calcular_consumo, calcular_valor

app = Flask(__name__)

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Erro ao carregar template: {str(e)}", 500

@app.route('/calcular-consumo', methods=['POST'])
def calcular_consumo_route():
    data = request.get_json()
    potencia = data.get('potencia')
    horas = data.get('horas')
    dias = data.get('dias')
    
    consumo = calcular_consumo(potencia, horas, dias)
    
    if consumo is not None:
        return jsonify({
            'success': True,
            'consumo_kwh': consumo
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Valores inválidos fornecidos'
        }), 400

@app.route('/calcular-valor', methods=['POST'])
def calcular_valor_route():
    data = request.get_json()
    consumo = data.get('consumo')
    tarifa = data.get('tarifa')
    
    valor = calcular_valor(consumo, tarifa)
    
    if valor is not None:
        return jsonify({
            'success': True,
            'valor_reais': valor
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Valores inválidos fornecidos'
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
