FROM ubuntu:latest

MAINTAINER Pedro Gazquez Navarrete <pedrogazqueznavarrete@gmail.com>


# Añadiendo herramientas Python
RUN apt-get -y update
RUN apt-get -y install python-setuptools
RUN apt-get -y install python-dev
RUN apt-get -y install python-pip
RUN apt-get -y install supervisor

#Instalando la API de BOTS de Telegram
RUN pip install pyTelegramBotAPI

#Añadiendo usuario
RUN useradd -m docker && echo "docker:docker" 

USER docker
CMD /bin/bash
