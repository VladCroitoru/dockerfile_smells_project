FROM node:10

ENV YJS_RESOURCE_PATH "/socket.io"
ENV PORT 8070

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install -y --allow-unauthenticated --no-install-recommends supervisor git nginx dos2unix
RUN npm_config_user=root npm install -g grunt-cli grunt polymer-cli gulp

ARG src="Utilities Frontend/docker/supervisorConfigs"
ARG srx="Utilities Frontend"
COPY ${src} /etc/supervisor/conf.d


WORKDIR /usr/src/app
COPY ${srx}/syncmeta syncmeta


WORKDIR /usr/src/app/syncmeta
RUN npm install
RUN cp -a node_modules/@rwth-acis/syncmeta-widgets/. widgets/
RUN cp -a node_modules/. widgets/node_modules/
COPY ${srx}/docker/_bot_widget.tpl /usr/src/app/syncmeta/widgets/src/widgets/partials/
COPY ${srx}/docker/bot_widget.js /usr/src/app/syncmeta/widgets/src/js/
COPY ${srx}/docker/Gruntfile.js /usr/src/app/syncmeta/widgets/
COPY ${srx}/docker/yjs-sync.js /usr/src/app/syncmeta/widgets/src/js/lib/
WORKDIR /usr/src/app/syncmeta
RUN cd widgets && npm install

WORKDIR /usr/src/app
COPY ${srx} .
WORKDIR /usr/src/app/app
ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache
RUN npm install

WORKDIR /usr/src/app
ARG srt="Utilities Frontend/docker/docker-entrypoint.sh"
COPY ${srt} docker-entrypoint.sh
RUN dos2unix docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
