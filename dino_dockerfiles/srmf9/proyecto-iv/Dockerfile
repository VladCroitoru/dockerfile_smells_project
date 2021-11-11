#Sistema operativo
FROM ubuntu:14.04
#Creador
MAINTAINER Salvador Rueda Molina <salviwui@gmail.com>
#Actualizamos los paquetes
RUN sudo apt-get -y update
#Instalamos herramienta GIT
RUN sudo apt-get install -y git
# Instalamos Python
RUN sudo apt-get -y install python-setuptools
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python-psycopg2
RUN sudo apt-get -y install libpq-dev
RUN sudo easy_install pip
#Nos bajamos la aplicacion
RUN sudo git clone https://github.com/srmf9/Proyecto-IV.git
#Instalamos las dependencias de la apliación
RUN cd Proyecto-IV/ && sudo pip install -r requirements.txt
RUN cd Proyecto-IV/ && python manage.py migrate --noinput
#Para poder comprobar si la aplicación funciona
RUN sudo apt-get -y install curl
