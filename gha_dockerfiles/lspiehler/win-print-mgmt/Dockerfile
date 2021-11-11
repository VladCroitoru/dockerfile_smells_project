FROM node:lts-alpine
LABEL maintainer Lyas Spiehler

RUN mkdir -p /var/node/win-print-mgmt

ADD . /var/node/win-print-mgmt/

WORKDIR /var/node/win-print-mgmt

EXPOSE 80/tcp

CMD ["node", "./bin/www"]