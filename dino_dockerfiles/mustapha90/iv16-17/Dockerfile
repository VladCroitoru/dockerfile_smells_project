FROM ubuntu:14.04
MAINTAINER Mustapha Mayo <mj4ever001@gmail.com>

#Variable de entorno que indica que estamos en docker
ENV EN_DOCKER=true

#Instalar dependencias
RUN sudo apt-get -y update
RUN sudo apt-get install -y git
RUN sudo apt-get install -y build-essential python-setuptools python-dev libpq-dev
RUN sudo easy_install pip
RUN sudo pip install --upgrade pip

#Clonar el repositorio del proyecto
RUN sudo git clone https://github.com/Mustapha90/IV16-17.git

#Cambiar el directorio de trabajo al directorio del proyecto
WORKDIR IV16-17

#Instalar dependencias del proyecto
RUN make install_prod

#Permitir el acceso externo al puerto 8000 que será usado por la aplicación
EXPOSE 8000

#Punto de entrada, este script se ejecuta automáticamente al iniciar el contenedor
ENTRYPOINT ["./docker_entrypoint.sh"]




