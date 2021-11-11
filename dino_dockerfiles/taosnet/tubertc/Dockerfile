FROM alpine:3.4
MAINTAINER Chris Batis <clbatis@taosnet.com>

COPY tubertc-master /app
WORKDIR /app
RUN apk --update --no-cache add nodejs \
    && npm install

EXPOSE 8080
ENTRYPOINT ["/usr/bin/npm"]
CMD ["start"]
