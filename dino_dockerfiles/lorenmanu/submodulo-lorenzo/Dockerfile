FROM ubuntu:latest

#producto
MAINTAINER Lorenzo Manuel Rosas Rodríguez <lorenrr1@gmail.com>

#Actualizar Sistema Base
RUN sudo apt-get -y update

#Descargar aplicacion
RUN sudo apt-get install -y git
RUN sudo git clone https://github.com/lorenmanu/submodulo-lorenzo.git

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
RUN cd submodulo-lorenzo/ && ls -l
RUN cd submodulo-lorenzo/ && cat requirements.txt
RUN cd submodulo-lorenzo/ && sudo pip install -r requirements.txt


#Migraciones
RUN cd submodulo-lorenzo/ && python manage.py syncdb --noinput
