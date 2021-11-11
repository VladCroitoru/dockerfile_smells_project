# Nosso objetivo com esse dockerfile é usar uma imagem do ubuntu para rodar um código em python
# Não vamos usar uma imagem do java diretamente por questões de aprendizado, pois assim temos que
# instalar o java dentro do container com ubuntu

# Vamos começar usando a palavra reservada FROM
# É possível criar imagens do 0, porém, com a palavra FROM conseguimos reaproveitar uma imagem que já existe

FROM ubuntu:latest

# Uma outra palavra reservada é a LABEL
# O LABEL nos permite colocar metadados e documentar o Dockerfile de maneira flexível

LABEL maintainer="Wesley Lima"
LABEL projeto="docker_basico"

# Agora especificamos o que queremos que a imagem faça
# Como queremos trabalhar com um código que já existe temos que usar a palavra reservada COPY
# O COPY copia arquivos para alguma pasta do container
# A linha a seguir copia o conteúdo de volumes_java para /var/www

COPY volumes_java/. /var/www

# Vamos definir que esse seja nosso diretório de trabalho
# Para isso vamos usar a palavra reservada WORKDIR

WORKDIR /var/www

# Para que possamos realizar o que queremos é necessário que o container possua as dependências corretas
# Vamos usar a palavra reservada RUN que executa o comando que a segue
# Aqui vamos usar a RUN para installar o jdk dentro do container de ubuntu

RUN apt-get update && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant &&\
    apt-get clean;

# Setando a variável de ambiente JAVA_HOME através da palavra reservada ENV

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

# Aqui não vamos usar uma porta para expor o contéudo do projeto
# Caso seja necessário expor o conteúdo do container para algum lugar podemos usar a palavra reservada EXPOSE
# O comando comentado abaixo fala para o container usar a porta 3000

# EXPOSE 3000

# Agora, vamos compilar e executar o código java contido na pasta

RUN     javac exemplo.java && \
        java exemplo &&
