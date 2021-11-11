FROM ubuntu:16.04
MAINTAINER Juan Hernández Cañaveras

#Añadimos las variables de entorno
ARG token_bot



ENV TOKEN=$token_bot



RUN apt-get update
RUN apt-get install -y python-setuptools
RUN apt-get install -y python-dev
RUN apt-get install -y build-essential
RUN apt-get install -y libpq-dev
RUN apt-get install -y python-pip
RUN pip install --upgrade
RUN apt-get install net-tools

RUN apt-get install -y git
RUN git clone https://github.com/MagicJHC10/Proyecto-IV.git


RUN pip install -r Proyecto-IV/requirements.txt

EXPOSE 80
WORKDIR Proyecto-IV/
CMD ./script.sh
