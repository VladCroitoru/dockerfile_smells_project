FROM ubuntu:14.04
MAINTAINER Sergio Cáceres Pintor <sergiocaceres@correo.ugr.es>

ARG TOKENBOT
ARG PASS_BD
ARG USR_BD
ENV TOKENBOT=$TOKENBOT
ENV PASS_BD=$PASS_BD
ENV USR_BD=$USR_BD


#Instalamos git
RUN sudo apt-get -y update
RUN sudo apt-get install -y git

#Clonamos el repositorio
RUN sudo git clone https://github.com/sergiocaceres/IV.git

#Instalamos las herramientas de python necesarias
#Instalamos las herramientas de python necesarias
RUN sudo apt-get -y install python-setuptools
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python-psycopg2
RUN sudo apt-get -y install libpq-dev
#RUN sudo apt-get install libffi-dev libssl-dev
RUN sudo easy_install pip
RUN sudo pip install --upgrade pip
RUN sudo pip install pyopenssl ndg-httpsclient pyasn1

#Instalamos los requerimientos necesarios
RUN cd IV/ && make install


