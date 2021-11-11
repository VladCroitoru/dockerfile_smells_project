FROM node:6
MAINTAINER Vianney Rancurel <vr@scality.com>

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN apt-get update \
    && apt-get install -y jq python git build-essential supervisor --no-install-recommends \
    && mkdir -p /var/log/supervisor \
    && npm install --production
#    && apt-get autoremove --purge -y python git build-essential \
#    && rm -rf /var/lib/apt/lists/* \
#    && npm cache clear \
#    && rm -rf ~/.node-gyp \
#    && rm -rf /tmp/npm-*

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

VOLUME ["/usr/src/app/localData","/usr/src/app/localMetadata"]

EXPOSE 9990
EXPOSE 9991

CMD [ "/usr/bin/supervisord" ]
