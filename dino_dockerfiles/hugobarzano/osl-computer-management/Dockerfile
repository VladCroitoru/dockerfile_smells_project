FROM ubuntu:latest

#Autor
MAINTAINER Hugo Barzano Cruz <hugobarzano@gmail.com>
ENV PYTHONUNBUFFERED 1
#Actualizar Sistema Base
RUN sudo apt-get -y update

#Descargar aplicacion
RUN sudo apt-get install -y git
RUN sudo git clone https://github.com/hugobarzano/osl-computer-management.git

# Instalar Python y PostgreSQL
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python-psycopg2
RUN sudo apt-get -y install libpq-dev
RUN sudo easy_install pip
RUN sudo pip install --upgrade pip

#Instalamos la aplicacion
RUN ls
RUN cd osl-computer-management/ && ls -l
RUN cd osl-computer-management/ && cat requirements.txt
RUN cd osl-computer-management/ && ls -l
RUN cd osl-computer-management/ && sudo pip install -r requirements.txt




