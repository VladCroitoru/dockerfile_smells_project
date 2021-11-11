FROM node:alpine

ENV PLEX_SERVER "http://localhost:32400"

COPY plex-status.js /
COPY docker-entrypoint.sh /

RUN npm i wreck@7.0.0 lodash@3.10.1 xml2js@0.4.17
CMD ["/docker-entrypoint.sh"]
