#Distribución y versión de ésta
FROM ubuntu:latest

#Autor
MAINTAINER Juan Jesús Tomás R.

#Actualiza repositorios e instala: python y herramientas, git,
#el paquete que contiene a ifconfig y postgresql
RUN apt-get update && apt-get install -y python3-setuptools python3-dev build-essential libpq-dev git net-tools

#Instala pip
RUN easy_install3 pip

#Descarga el proyecto
RUN git clone https://github.com/juanjetomas/ProyectoIV

#Instala las dependencias
RUN cd ProyectoIV && pip install -r requirements.txt

#Copia el script de ejecución a la raiz
ADD ejecucion_desde_docker.sh /

#Variable de entorno que indica el entorno de DOCKER
ENV USINGDOCKER=true
#Variable de entorno que indica que la base de datos se ejecutará en otro contenedor
ENV DOCKERMULTIPLE=true
