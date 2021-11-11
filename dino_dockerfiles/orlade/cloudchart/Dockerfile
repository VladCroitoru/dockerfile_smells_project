FROM danieldent/meteor:latest
MAINTAINER Oliver Lade <oliver@urbanetic.net>

RUN npm install -g n && n v0.10

COPY . /opt/src
WORKDIR /opt/src

RUN meteor build .. --directory \
    && cd ../bundle/programs/server \
    && npm install \
    && rm -rf /opt/src

WORKDIR /opt/bundle
USER nobody
ENV PORT 3000
CMD ["/usr/local/bin/node", "main.js"]
