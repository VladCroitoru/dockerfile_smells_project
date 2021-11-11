FROM nginx
MAINTAINER Parun Rua Ivo <parunruaivo@gmail.com>

ENV TAIGA_HOME=/home/taiga \
    TAIGA_RUNTIME_DIR=/runtime

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends --no-install-suggests -y git subversion \
    && rm -rf /var/lib/apt/lists/*

RUN git clone -b stable --single-branch https://github.com/taigaio/taiga-front-dist.git ${TAIGA_HOME}/taiga-front

COPY assets/templates/conf.json ${TAIGA_HOME}/taiga-front/dist/conf.json
COPY assets/templates/taiga.conf /etc/nginx/conf.d/default.conf

COPY assets/runtime ${TAIGA_RUNTIME_DIR}/

RUN mkdir ${TAIGA_HOME}/media \
    && mkdir ${TAIGA_HOME}/static \
    && mkdir ${TAIGA_HOME}/taiga-front/dist/plugins

WORKDIR ${TAIGA_HOME}/taiga-front/dist/plugins

RUN svn export "https://github.com/taigaio/taiga-contrib-slack/tags/2.1.1/front/dist" "slack"

WORKDIR ${TAIGA_HOME}/taiga-front

EXPOSE 80

COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]


