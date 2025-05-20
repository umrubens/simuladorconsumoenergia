def calcular_consumo(potencia, horas_por_dia, dias_no_mes):
    """
    Calcula o consumo em kWh
    Fórmula: CONSUMO (kWh) = potência (W) x horas/dia (h) x dias/mês / 1000
    """
    try:
        potencia = float(potencia)
        horas_por_dia = float(horas_por_dia)
        dias_no_mes = float(dias_no_mes)
        
        consumo_kwh = (potencia * horas_por_dia * dias_no_mes) / 1000
        return round(consumo_kwh, 2)
    except ValueError:
        return None

def calcular_valor(consumo_kwh, tarifa):
    """
    Calcula o valor em reais com base no consumo e tarifa
    """
    try:
        consumo_kwh = float(consumo_kwh)
        tarifa = float(tarifa)
        
        valor = consumo_kwh * tarifa
        return round(valor, 2)
    except ValueError:
        return None