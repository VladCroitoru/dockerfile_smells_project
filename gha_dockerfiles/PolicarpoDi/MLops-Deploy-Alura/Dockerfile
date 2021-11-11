# Informo tudo que a aplicação vai precisar utilizar #

FROM python:3.8-slim

# passando valor na criação do meu dockerfile #
ARG BASIC_AUTH_USERNAME_ARG
ARG BASIC_AUTH_PASSWORD_ARG

# Criando as variaveis de ambiente #
ENV BASIC_AUTH_USERNAME=${BASIC_AUTH_USERNAME_ARG}
ENV BASIC_AUTH_PASSWORD=${BASIC_AUTH_PASSWORD_ARG}

# Copiando os arquivos para o container #
COPY ./requirements.txt /usr/requirements.txt

# Criando meu diretorio de trabalho #
WORKDIR /usr

# Instalação das dependencias #
RUN pip3 install -r requirements.txt

# Copiando os arquivos necessários #
COPY ./src /usr/src
COPY ./models /usr/models

ENTRYPOINT ["python3"]

# Arquivo que será executado #
CMD ["src/app/main.py"]