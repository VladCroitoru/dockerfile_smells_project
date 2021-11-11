FROM alpine:3.3

ENV CONFD_VERSION=0.11.0
ENV CONFD_PACKAGE="http://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-amd64"

RUN apk add --update ca-certificates \
  && mkdir /etc/confd \
  && wget $CONFD_PACKAGE -O /bin/confd \
  && chmod +x /bin/confd

VOLUME ["/etc/confd"]

ENTRYPOINT ["/bin/confd"]
