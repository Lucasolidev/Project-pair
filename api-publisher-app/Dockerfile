# Utilizando uma imagem base com Python instalado
FROM python:3.8-slim-buster

# Definindo o diretório de trabalho no container
WORKDIR /app

# Copiando os arquivos de requerimentos para o container
COPY requirements.txt .

# Instalando as dependências
RUN pip install -r requirements.txt

# Copiando o restante dos arquivos para o container
COPY /app /app
COPY /tests /tests

# Expondo a porta onde a aplicação estará rodando
EXPOSE 5000

# Dando permissão de execução ao script entrypoint.sh
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Definindo o comando para rodar a aplicação
CMD ["./entrypoint.sh"]

