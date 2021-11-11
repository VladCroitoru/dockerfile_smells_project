FROM semtech/mu-nginx-spa-proxy:1.0.1

MAINTAINER Sam Landuydt <sam.landuydt@gmail.com>

ENV STATIC_FOLDERS_REGEX "^/(assets|font|images)/"

RUN apt-get update; apt-get upgrade -y; apt-get install -y unzip wget;
COPY package.json /package.json
RUN mkdir /app; cd /app; wget https://github.com/samldd/my-workforce-frontend/releases/download/v0.1.1/dist.zip
RUN cd /app; unzip dist.zip; mv dist/* .
RUN rm /app/dist.zip package.json
