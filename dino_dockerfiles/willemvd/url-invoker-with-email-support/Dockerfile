FROM alpine:3.7
MAINTAINER Willem willemvd@github

COPY invoker.sh /tmp/invoker.sh

RUN apk --no-cache add \
      curl \
      heirloom-mailx && \
      chmod -R 777 /tmp

CMD /tmp/invoker.sh