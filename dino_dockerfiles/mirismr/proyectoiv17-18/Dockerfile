FROM ubuntu:14.04
MAINTAINER Míriam Mengíbar Rodríguez <mirismr@correo.ugr.es>

ARG TOKEN_BOT
ENV TOKEN_BOT=$TOKEN_BOT


#Instalamos git
RUN sudo apt-get -y update
RUN sudo apt-get install -y git

#Clonamos el repositorio
RUN sudo git clone https://github.com/mirismr/proyectoIV17-18.git


#Instalamos las herramientas de python necesarias
RUN sudo apt-get -y install python3-setuptools
RUN sudo apt-get -y install python3-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python3-psycopg2
RUN sudo apt-get -y install libpq-dev
RUN sudo apt-get -y install python3-pip

#Instalamos los requerimientos necesarios
RUN cd proyectoIV17-18 && make install

EXPOSE 80
CMD cd proyectoIV17-18 && ./scriptDespliegue.sh