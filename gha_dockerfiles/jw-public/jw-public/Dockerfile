FROM alpine:3 as prepare
COPY src/build/src.tar.gz /bundle/meteor.tar.gz
RUN cd /tmp/ && tar xvf /bundle/meteor.tar.gz
FROM node:12-alpine
COPY --from=prepare /tmp/bundle /bundle
WORKDIR /bundle
RUN apk add --no-cache --virtual .build-deps python make g++ && cd programs/server/ && npm install && apk del .build-deps
CMD [ "node", "main.js" ]
EXPOSE 8080
ENV PORT 8080
