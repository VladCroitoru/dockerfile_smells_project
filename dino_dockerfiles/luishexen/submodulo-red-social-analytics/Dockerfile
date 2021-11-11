# Submodulo-Red-social-Analytics 1.0

FROM    ubuntu:latest
MAINTAINER Luis Garcia <luisgarfu@gmail.com> Version: 1.0

# Instalar todos los paquetes necesarios para poder realizar realizar el proyecto de CC
RUN apt-get -y install wget
RUN wget -qO- https://deb.nodesource.com/setup_4.x | sudo bash -
RUN sudo apt-get install -y git nodejs
RUN node -v
RUN git clone https://github.com/luishexen/Submodulo-Red-social-Analytics.git /home/Submodulo-Red-social-Analytics
RUN cd /home/Submodulo-Red-social-Analytics && npm install
