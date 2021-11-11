FROM ubuntu:14.04
MAINTAINER Rubén Jiménez Ortega

#Añadimos las variables de entorno
ARG token_bot
ARG usuario_db
ARG password_db
ARG database_db
ARG host_db
ENV token_bot=$token_bot
ENV usuario_db=$usuario_db
ENV password_db=$password_db
ENV database_db=$database_db
ENV host_db=$host_db

RUN apt-get -y update

#Primero de todo instalamos git y clonamos el directorio
RUN apt-get install -y git
RUN git clone https://github.com/rubenjo7/IV.git

#Instalamos herramientas necesarias
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python-psycopg2
RUN sudo apt-get -y install libpq-dev
RUN sudo easy_install pip
RUN sudo pip install --upgrade pip
RUN cd IV/ && make install

CMD cd IV/p_deportivas_bot && python p_deportivas_bot.py
