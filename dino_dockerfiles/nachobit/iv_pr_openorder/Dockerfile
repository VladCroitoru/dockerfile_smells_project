FROM ubuntu:latest

#Autor
MAINTAINER Ignacio Romero Cabrerizo <nachotempus@gmail.com> 

#Actualizar sistema
RUN sudo apt-get -y update

#Instalar git y herramientas necesarias
RUN sudo apt-get install -y git
RUN sudo apt-get install -y build-essential
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get -y install libpq-dev

#Clonar repositorio
RUN sudo git clone https://github.com/nachobit/IV_PR_OpenOrder.git

#Instalar requerimientos necesarios
RUN cd IV_PR_OpenOrder && git pull
RUN cd IV_PR_OpenOrder && make install

