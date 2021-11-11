# base image
FROM node:4

ADD package.json /tmp/package.json
RUN cd /tmp && npm install --production && \
    mkdir -p /opt/app && cp -a /tmp/node_modules /opt/app/

WORKDIR /opt/app
ADD . /opt/app

EXPOSE 3000
CMD [ "node", "app","3000" ]
