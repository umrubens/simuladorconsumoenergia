# simuladorconsumoenergia
CALCULAR CONSUMO DE ENERGIA HORAS/REAIS

Neste arquivo calcule o consumo de energia de um eletrodoméstico, utilize a seguinte fórmula: Consumo (kWh) = Potência (W) x Tempo de Uso (h) / 1000. Em resumo, multiplique a potência em watts pelo tempo de uso em horas e divida o resultado por 1000 para obter o consumo em kWh. Para transformar kWh em reais, basta multiplicar a quantidade de kWh consumido pela tarifa de energia elétrica de sua região. A tarifa é o valor cobrado por cada kWh consumido, e pode variar de acordo com o distribuidor e o tipo de consumidor (residencial, comercial, industrial, etc.).



#(terminal)#
Instale as dependências do sistema 

#sudo apt update
#sudo apt install python3 python3-pip python3-venv
#Clone seu repositório e crie um ambiente virtual:


git clone URL_DO_SEU_REPO
cd NOME_DO_REPO

python3 -m venv venv
source venv/bin/activate
Instale as dependências otimizadas:

pip install -r requirements.txt
Execute a aplicação:

Para ambiente local:
flask run --host=0.0.0.0

Para Docker:
docker build -t minha-app . --no-cache
docker run -p 5000:5000 minha-app

Acesse:
Abra http://localhost:5000 no navegador.
