FROM    lcamilo15/fedora-jdk
MAINTAINER  Luis Camilo <lcamilo15@gmail.com>
ENV         ACTIVATOR_VERSION 1.3.6

# INSTALL TYPESAFE ACTIVATOR
RUN cd /tmp \
    && wget -O typesafe-activator.zip http://downloads.typesafe.com/typesafe-activator/$ACTIVATOR_VERSION/typesafe-activator-$ACTIVATOR_VERSION.zip \
    && unzip typesafe-activator.zip -d /usr/local \
    && mv /usr/local/activator-dist-$ACTIVATOR_VERSION /usr/local/activator \
    && rm typesafe-activator.zip \ 
    && dnf -y install git \
    && ln -s /usr/local/activator/activator /usr/bin/activator \
    && mkdir /app \
    && activator new dummy_app play-java \
    && cd dummy_app && ./activator compile

EXPOSE 9000 8888
WORKDIR /app
