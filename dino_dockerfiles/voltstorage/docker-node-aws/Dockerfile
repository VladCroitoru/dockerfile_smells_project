FROM node:12.16.1-buster

MAINTAINER David Bauske <david.bauske@voltstorage.com>

RUN cd

RUN apt update
RUN apt install -y python-dev

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN rm get-pip.py

RUN pip install awscli

RUN apt install graphicsmagick -y

# locale used in our postgres collation
RUN apt install locales -y
# https://askubuntu.com/a/1027038
RUN echo "locales locales/default_environment_locale select en_US.UTF-8" | debconf-set-selections
RUN echo "locales locales/locales_to_be_generated multiselect en_US.UTF-8 UTF-8" | debconf-set-selections
RUN rm "/etc/locale.gen"
RUN dpkg-reconfigure --frontend noninteractive locales

# postgres
RUN apt install postgresql -y
RUN apt install sudo -y
