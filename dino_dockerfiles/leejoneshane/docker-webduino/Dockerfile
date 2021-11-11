FROM node:alpine
MAINTAINER leejoneshane@gmail.com

WORKDIR /usr/src/app
RUN apk add --no-cache git mosquitto mosquitto-clients vim \
    && npm install -g bower \
    && git clone https://github.com/webduinoio/webduino-blockly.git \
    && mv webduino-blockly/* . \
    && rm -rf webduino-blockly \
    && npm install && bower --allow-root install \
    && sed -ri -e 's/8080/80/g' /usr/src/app/webserver.js
    
ADD start.sh /sbin
RUN chmod 711 /sbin/start.sh

EXPOSE 80 1883
CMD ["/sbin/start.sh"]
