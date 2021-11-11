FROM node:alpine

WORKDIR /opt/app

RUN mkdir -p /opt/app/client /opt/app/server /opt/app/configuration
ENV NODE_ENV=production

ADD server/package.json server/yarn.lock /tmp/
RUN cd /tmp && yarn
RUN cd /opt/app/server && ln -s /tmp/node_modules

ADD server server
ADD client/dist client/dist

EXPOSE 3000

ENTRYPOINT [ "node", "./server/main.js" ]









