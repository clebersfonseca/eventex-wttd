# Eventex

Sistema de Eventos encomendado pela morena

## Como desenvolver?
1. Clone o repositorio
2. Crie um virtualenv com python 3.5
3. Ative o virtualenv
4. Instale as dependencias
5. Configure a instancia com o .env
6. Execute os testes

```console
git clone https://github.com/clebersfonseca/eventex-wttd.git wttd
cd wttd
python -m venv .
source bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```


## Como fazer o deploy