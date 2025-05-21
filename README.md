# SIMULADOR DE CONSUMO DE ENERGIA 

CALCULAR CONSUMO DE ENERGIA EM HORAS E CONVERTER PARA REAIS


Simulação de consumo de energia de um eletrodoméstico de forma simples. Usar a seguinte fórmula: Consumo (kWh) = Potência (W) x Tempo de Uso (h) / 1000. É basicamente multiplicar a potência em watts pelo tempo de uso em horas e dividir o resultado por 1000 para obter o consumo em kWh.


Agora, para transformar esse consumo em reais, você vai multiplica a quantidade de kWh pela tarifa de energia elétrica da sua região. Essa informação você pode consultar na sua conta de luz ou no site da empresa.


# Calculadora Elétrica Web

Aplicação web simples para cálculo de consumo elétrico (kWh) e valor em reais, utilizando Python e Flask. Inclui interface HTML interativa.

---

### Debian/Linux

## 1. Instale os pré-requisitos do sistema:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```
## 2. Clone o repositório e crie um ambiente virtual:
```bash
git clone URL_DO_SEU_REPO
cd NOME_DO_REPO
python3 -m venv venv
source venv/bin/activate
```
## 3. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```
## 4. Execute a aplicação
```bash
flask run --host=0.0.0.0
```
## Para rodar via Docker:
```bash
docker build -t minha-app . --no-cache
docker run -p 5000:5000 minha-app
#Pode ser necessário usar "docker start --nome" para iniciar o container.
```
## 5. Acesse no navegador:
```bash
http://localhost:5000
```
## Estrutura esperada do projeto:
```bash
#seu-projeto/
├── app.py
├── calculos.py
├── requirements.txt
├── Dockerfile (opcional)
└── templates/
   └── index.html
```
## Tecnologias utilizadas:
```bash
Python 3
Flask
HTML5 + CSS3
Docker (opcional)
markdown
Copiar
Editar
```

### FIM.
