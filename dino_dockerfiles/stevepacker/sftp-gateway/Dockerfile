FROM stevepacker/nodejs-supervisor
MAINTAINER Stephen Packer <steve@stevepacker.com>

EXPOSE 2222

USER root

COPY package.json /tmp/package.json
RUN cd /tmp && npm install

COPY . /srv/

RUN mv /tmp/node_modules /srv/ \
    && rm /tmp/package.json \
    && chown -Rf node:node /srv \
    && ls -la /srv

USER node
WORKDIR /srv

CMD ["supervisor", "--non-interactive", "--timestamp", "--no-restart-on success", "index.js"]