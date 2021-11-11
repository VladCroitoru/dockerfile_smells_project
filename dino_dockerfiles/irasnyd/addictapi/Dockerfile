FROM node:8-alpine

ENV ADDICTAPI_VERSION 0.1.6

EXPOSE 3000
ENTRYPOINT [ "/usr/local/bin/addict" ]

RUN npm install "addict-api@$ADDICTAPI_VERSION" -g \
        && npm cache clear --force
