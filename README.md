# simuladorconsumoenergia
CALCULAR CONSUMO DE ENERGIA HORAS/REAIS

Passos para usar no Debian (terminal):
Instale as dependências do sistema (pré-requisitos):

bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
Clone seu repositório e crie um ambiente virtual:

bash
git clone URL_DO_SEU_REPO
cd NOME_DO_REPO
python3 -m venv venv
source venv/bin/activate
Instale as dependências otimizadas:

bash
pip install -r requirements.txt
Execute a aplicação:

# Para ambiente local:
flask run --host=0.0.0.0

# Para Docker:
docker build -t minha-app . --no-cache
docker run -p 5000:5000 minha-app

Acesse:
Abra http://localhost:5000 no navegador.
