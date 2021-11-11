FROM node:9-alpine

ENV LOG_LEVEL=info

COPY *.j* /neeo-driver-mystrom/
COPY config /neeo-driver-mystrom/config
COPY lib /neeo-driver-mystrom/lib

RUN cd /neeo-driver-mystrom && \
    npm install && \
    chown -R node:node *

USER node:node

VOLUME ["/neeo-driver-mystrom/config"]

WORKDIR /neeo-driver-mystrom
CMD [ "node", "index.js" ]

EXPOSE 6336 7979/UDP