# SIMULADOR DE CONSUMO DE ENERGIA 

CALCULAR CONSUMO DE ENERGIA EM HORAS E CONVERTER PARA REAIS


Simulação de consumo de energia de uma forma simples. Usar a seguinte fórmula: Consumo (kWh) = Potência (W) x Tempo de Uso (h) / 1000. Basicamente multiplicar a potência em watts pelo tempo de uso em horas e dividir o resultado por 1000 para obter o consumo em kWh.


Para transformar esse consumo em reais, você vai multiplica a quantidade de kWh pela tarifa de energia elétrica da sua região.

---

### Debian/Linux

## 1. Instale pré-requisitos do sistema:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```
## 2. Clone o repositório e crie um ambiente virtual:
```bash
git clone url
cd simuladorconsumoenergia
python3 -m venv venv
source venv/bin/activate
```
## 3. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```
## 4. Execute a aplicação (Se preferir, ignore esse passo e vá para o próximo.)
```bash
flask run --host=0.0.0.0
```
## Para rodar via Docker:
```bash
docker build -t minha-app . --no-cache
docker run -d -p 5000:5000 minha-app
#Pode ser necessário usar "docker start --nome" para iniciar o container.
```
## 5. Acesse no navegador:
```bash
http://localhost:5000
```
## Estrutura do projeto:
```bash
#projeto/
├── app.py
├── calculos.py
├── requirements.txt
├── Dockerfile (opcional)
└── templates/
   └── index.html
```
## Utilizado:
```bash
Python 3
Flask
HTML5 + CSS3
Docker (opcional)
markdown
```

![pagina web](https://github.com/user-attachments/assets/49be71d0-aabf-4a98-8551-23847ae31ea1)

