FROM resin/raspberry-pi-alpine-node

LABEL maintainer="joseba.io"

RUN [ "cross-build-start" ]

RUN apk --update add --no-cache git

RUN git clone https://github.com/seejohnrun/haste-server.git /opt/haste
WORKDIR /opt/haste
RUN sed -i '/padding-right: 360px/d' /opt/haste/static/application.css
RUN sed -i '/textarea {/a\\tmargin: 0;' /opt/haste/static/application.css
RUN npm install
COPY config.js /opt/haste/

RUN [ "cross-build-end" ]

EXPOSE 7777
CMD ["npm", "start"]
