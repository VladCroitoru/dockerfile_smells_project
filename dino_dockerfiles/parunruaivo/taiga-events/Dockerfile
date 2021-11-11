FROM node
MAINTAINER Parun Rua Ivo <parunruaivo@gmail.com>

ENV TAIGA_HOME=/home/taiga \
    TAIGA_RUNTIME_DIR=/runtime

RUN apt-get update \
    && apt-get install -y git gettext-base \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/taigaio/taiga-events.git ${TAIGA_HOME}/

COPY assets/templates/config.json ${TAIGA_HOME}/config.json
COPY assets/runtime ${TAIGA_RUNTIME_DIR}/

WORKDIR ${TAIGA_HOME}

RUN npm install --production && npm install -g coffee-script

EXPOSE 80

COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["coffee", "index.coffee"]

