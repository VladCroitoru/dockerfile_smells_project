FROM alpine:latest

# Upgrade for any patches, install bash, freetds, and mysql-client. Cleanup cache.
RUN apk update && apk upgrade --available &&\
    apk add --update bash freetds mysql-client postgresql-client && rm -rf /var/cache/apk/*
CMD /bin/bash
