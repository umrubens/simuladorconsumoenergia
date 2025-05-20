FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie TODOS os arquivos necessários
COPY app.py calculos_eletricos.py .
COPY templates/ templates/

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
