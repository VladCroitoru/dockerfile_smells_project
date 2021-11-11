FROM mhart/alpine-node:latest

RUN rm -rf /tmp/node_modules
ADD package.json /tmp/package.json
RUN cd /tmp && npm install
RUN mkdir -p /opt/app && cp -a /tmp/node_modules /opt/app/

WORKDIR /opt/app
ADD . /opt/app

EXPOSE 4005
EXPOSE 27017

CMD ["npm", "start"]
