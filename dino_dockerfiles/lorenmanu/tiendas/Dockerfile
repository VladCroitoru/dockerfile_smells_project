FROM ubuntu:latest

#producto
MAINTAINER Lorenzo Manuel Rosas Rodríguez <lorenrr1@gmail.com>

#Actualizar Sistema Base
RUN sudo apt-get -y update

#Descargar aplicacion
RUN sudo apt-get install -y git
RUN sudo git clone https://github.com/lorenmanu/Tiendas.git

# Instalar Python y PostgreSQL
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get -y build-dep python-imaging --fix-missing
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python-psycopg2
RUN sudo apt-get -y install libpq-dev
RUN sudo apt-get install python2.7
RUN sudo easy_install pip
RUN sudo easy_install Pillow

#Instalar la app
RUN ls
RUN cd Tiendas/ && ls -l
RUN cd Tiendas/ && cat requirements.txt
RUN cd Tiendas/ && sudo pip install -r requirements.txt


#Migraciones
RUN cd Tiendas/ && python manage.py syncdb --noinput
