# simuladorconsumoenergia
CALCULAR CONSUMO DE ENERGIA HORAS/REAIS

Neste arquivo calcule o consumo de energia de um eletrodoméstico, utilize a seguinte fórmula: Consumo (kWh) = Potência (W) x Tempo de Uso (h) / 1000. Em resumo, multiplique a potência em watts pelo tempo de uso em horas e divida o resultado por 1000 para obter o consumo em kWh. Para transformar kWh em reais, basta multiplicar a quantidade de kWh consumido pela tarifa de energia elétrica de sua região. A tarifa é o valor cobrado por cada kWh consumido, e pode variar de acordo com o distribuidor e o tipo de consumidor (residencial, comercial, industrial, etc.).


# Calculadora Elétrica Web

Aplicação web simples para cálculo de consumo elétrico (kWh) e valor em reais, utilizando Python e Flask. Inclui interface HTML interativa.

---

## 🚀 Como usar no Debian/Linux

### 📦 1. Instale os pré-requisitos do sistema:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```
### 🔁 2. Clone o repositório e crie um ambiente virtual:
```bash
git clone URL_DO_SEU_REPO
cd NOME_DO_REPO
python3 -m venv venv
source venv/bin/activate
```
📥 3. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```
▶️ 4. Execute a aplicação
```bash
flask run --host=0.0.0.0
```
### Para rodar via Docker:
```bash
docker build -t minha-app . --no-cache
docker run -p 5000:5000 minha-app
```
### 🌐 5. Acesse no navegador:
```bash
http://localhost:5000
```


### 🧩 Estrutura esperada do projeto:

#seu-projeto/
├── app.py
├── calculos.py
├── requirements.txt
├── Dockerfile
└── templates/
   └── index.html

### 🛠 Tecnologias utilizadas:
Python 3
Flask
HTML5 + CSS3
Docker (opcional)
markdown
Copiar
Editar

