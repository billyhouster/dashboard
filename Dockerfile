
# imagem base
FROM python:3.6.7

# cria e "muda" para diretório /app
WORKDIR /app

# copia o diretório para dentro do container
ADD . /app

# instala as dependências do projeto
RUN pip install -r requirements.txt

# roda a aplicação
CMD [ "python", "app.py" ]