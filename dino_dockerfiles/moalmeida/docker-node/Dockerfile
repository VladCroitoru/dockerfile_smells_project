FROM node:8
MAINTAINER "moalmeida" <moalmeida@koinosystems.com>

RUN mkdir -p /app
WORKDIR /app

RUN npm install -g gulp
RUN \
  apt-get autoremove && \
  apt-get autoclean && \
  apt-get clean && \
  du -sh /var/cache/apt/archives && \
  rm -rf /var/lib/apt/lists/*


VOLUME ["/app"]

CMD ["npm", "start"]
