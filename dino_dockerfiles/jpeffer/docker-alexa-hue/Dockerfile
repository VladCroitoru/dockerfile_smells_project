FROM jpeffer/docker-rvm:latest
MAINTAINER Jonathan Peffer <jpeffer.developer@gmail.com>

WORKDIR /code

# Install additional dependencies
RUN apt-get -y install git

# Retrieve / Configure Alexa-Hue
RUN mkdir -p /usr/local/www && \
    cd /usr/local/www && \
    git clone https://github.com/sarkonovich/Alexa-Hue.git && \
    cd Alexa-Hue && \
    /bin/bash -l -c "bundle install;"

ENV RACK_ENV production
EXPOSE 4567

WORKDIR /usr/local/www/Alexa-Hue
ADD run-alexa-hue .
RUN chmod 755 ./run-alexa-hue

ENTRYPOINT /bin/bash -l -c "./run-alexa-hue"