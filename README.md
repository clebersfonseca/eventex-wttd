# Eventex

Sistema de Eventos encomendado pela morena.

[![Build Status](https://travis-ci.org/clebersfonseca/eventex-wttd.svg?branch=master)](https://travis-ci.org/clebersfonseca/eventex-wttd)


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
1. Crie uma instância do heroku
2. Envie as configuração para o heroku
3. Define uma SECRET_KEY segura para a instância
4. Define DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configure o email
git push heroku master --force
```