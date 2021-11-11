# Sistema operativo
FROM ubuntu:latest

# Autor
MAINTAINER Miguel Angel Garcia Villegas <magvugr@gmail.com>

#Actualizar Sistema Base
RUN sudo apt-get -y update

# Instalacion 
RUN sudo apt-get install -y git
RUN sudo git clone https://github.com/magvugr/InsertaLogo

#Instalar python
RUN sudo apt-get -y install python-dev
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get install -y build-essential
RUN sudo apt-get -y install libpq-dev
RUN sudo easy_install pip
RUN sudo pip install --upgrade pip

WORKDIR InsertaLogo
# Instalacion de las dependencias del proyecto
RUN pip install -r requirements.txt

EXPOSE 1112
CMD python manage.py runserver 









