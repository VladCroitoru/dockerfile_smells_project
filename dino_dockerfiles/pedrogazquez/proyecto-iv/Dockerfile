FROM ubuntu:latest

#Autor
MAINTAINER Pedro Gazquez Navarrete <pedrogazqueznavarrete@gmail.com>

#Actualizar Sistema Base
RUN sudo apt-get -y update

#Descargar app
RUN sudo apt-get install -y git
RUN git clone https://github.com/pedrogazquez/Proyecto-IV.git

#Instalar python
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get -y build-dep python-imaging --fix-missing
RUN sudo apt-get -y install libffi-dev
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python-psycopg2
RUN sudo apt-get -y install libpq-dev
RUN sudo apt-get -y install python2.7
RUN sudo easy_install pip
RUN sudo easy_install Pillow
RUN sudo pip install --upgrade pip

#Instalar app
RUN cd Proyecto-IV && make install
