FROM ventx/docker-alpine:3.6
LABEL maintainer="martin@ventx.de"

RUN apk --update add mongodb mongodb-tools && \
    mkdir -p /data/db

COPY ./entrypoint.sh /

VOLUME ["/data/db"]

WORKDIR /data

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 27017

CMD ["mongod"]
