FROM node:0.12
MAINTAINER so0k <vincent.drl@gmail.com>
RUN adduser --disabled-password --gecos "" sinopia && \
    mkdir -p /opt/sinopia/storage && \
    mkdir /opt/sinopia/config
WORKDIR /opt/sinopia

RUN npm install js-yaml sinopia && \
    npm cache clean

ADD conf/config.yaml /opt/sinopia/config/
RUN chown -R sinopia:sinopia /opt/sinopia
USER sinopia

CMD ["/opt/sinopia/node_modules/sinopia/bin/sinopia","--config","/opt/sinopia/config/config.yaml"]
EXPOSE 4873
VOLUME ["/opt/sinopia/storage","/opt/sinopia/config"]