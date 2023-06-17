# Utilizando uma imagem base com Python instalado
FROM python:3.8-slim-buster

# Definindo o diretório de trabalho no container
WORKDIR /App

# Copiando os arquivos de requerimentos para o container
COPY requirements.txt .

# Instalando as dependências
RUN pip install -r requirements.txt

# Copiando o restante dos arquivos para o container
COPY /App /App
COPY /tests /tests

# Executando os testes
RUN pytest

# Expondo a porta onde a aplicação estará rodando
EXPOSE 5000

# Definindo o comando para rodar a aplicação
CMD ["python", "/app/main.py"]