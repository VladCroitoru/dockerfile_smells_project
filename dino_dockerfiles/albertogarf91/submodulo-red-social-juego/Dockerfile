# Submodulo-Red-social-Juego 1.0

FROM    ubuntu:latest
MAINTAINER Alberto Garcia <albertogarf91@gmail.com> Version: 1.0

# Instalar todos los paquetes necesarios para poder realizar realizar el proyecto de CC
RUN apt-get -y install wget
RUN wget -qO- https://deb.nodesource.com/setup_4.x | sudo bash -
RUN sudo apt-get install -y git nodejs
RUN node -v
RUN git clone https://github.com/albertogarf91/Submodulo-Red-social-Juego.git /home/Submodulo-Red-social-Juego
RUN cd /home/Submodulo-Red-social-Juego && npm install
