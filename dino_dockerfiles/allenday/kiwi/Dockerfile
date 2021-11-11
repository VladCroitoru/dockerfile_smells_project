FROM node:0.12
MAINTAINER Allen Day "allenday@allenday.com"
EXPOSE 80
EXPOSE 443

RUN apt-get update
RUN apt-get -y install nano

WORKDIR /opt
RUN git clone https://github.com/prawnsalad/KiwiIRC.git 

WORKDIR /opt/KiwiIRC
ADD config.js /opt/KiwiIRC/config.js
ADD dev-server.key /opt/KiwiIRC/server.key
ADD dev-cert.pem /opt/KiwiIRC/cert.pem
ADD entrypoint.sh /opt/entrypoint.sh
ADD theme/manganese /opt/KiwiIRC/client/assets/themes/manganese
ADD theme/cobalt /opt/KiwiIRC/client/assets/themes/cobalt
ADD plugins/* /opt/KiwiIRC/client/assets/plugins/

RUN npm install
RUN ./kiwi build

ENTRYPOINT ["/bin/bash", "-c", "/opt/entrypoint.sh \"$@\"", "--"]
