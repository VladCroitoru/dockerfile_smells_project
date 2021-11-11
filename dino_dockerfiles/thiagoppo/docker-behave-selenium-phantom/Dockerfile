FROM ubuntu:16.04

#Atualizado
RUN apt-get update

#Instalando Curl
RUN apt-get -y install curl

#Instalando Pip
RUN apt-get -y install python-setuptools python-dev build-essential libfontconfig
RUN easy_install pip

#Instalando Node
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get -y install nodejs
RUN apt-get install build-essential

#Instalando PhantamJS
RUN npm install -g phantomjs-prebuilt --upgrade --unsafe-perm
RUN npm install -g phantomjs --upgrade --unsafe-perm

#Instalando Chromium
RUN apt-get install -y chromium-browser

COPY ./requirements.txt /home/requirements.txt
RUN pip install -r /home/requirements.txt
