FROM linuxserver/letsencrypt
EXPOSE 80
EXPOSE 443
RUN apk --update --no-cache add gettext nodejs git bash nodejs-npm&& npm install npm@latest -g && npm install -g bower

ENV BOWER_DIRECTORY=/run/bower
COPY ./bower/ $BOWER_DIRECTORY/
WORKDIR $BOWER_DIRECTORY
RUN /bin/bash bower_bash.sh

COPY ./config/ /config/

ENV PUID=1001
ENV PGID=1001
ENV URL=murphytech.net
ENV SUBDOMAINS=bower
ENV ONLY_SUBDOMAINS=true
ENV TZ=America/New_York
ENV EMAIL=air.jmurph@gmail.com

COPY ./50-config /etc/cont-init.d/50-config
COPY ./20-config /etc/cont-init.d/20-config
RUN chown -R root /etc/cont-init.d && chmod +x /etc/cont-init.d/*
COPY ./custom-components/ $BOWER_DIRECTORY/