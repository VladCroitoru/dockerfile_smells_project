FROM node:alpine
MAINTAINER Sebastian Pekarek <mail@sebbo.net>
EXPOSE 8080

RUN adduser -D -g "" app && \
    mkdir -p /home/app/app && \
    chown -R app:app /home/app/app && \
    chmod -R 740 /home/app/app && \
    apk add --update bash python make g++ && \
    npm install -g node-gyp grunt-cli bunyan 2>&1

COPY ./package.json /home/app/app/
WORKDIR /home/app/app
USER app
RUN npm install

USER root
COPY ./ /home/app/app/
RUN chown -R app:app /home/app/app && \
    chmod -R 740 /home/app/app

USER app
RUN NODE_ENV=production grunt production && \
    chmod +x /home/app/app/bin/*

ENV PATH /home/app/app/bin:$PATH
CMD [ "start" ]