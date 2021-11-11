FROM alpine

MAINTAINER itzg

RUN apk add --update curl && rm -rf /var/cache/apk/*

ENV CARINA_CLI_ASOF 20160620

RUN curl -qsL https://download.getcarina.com/carina/latest/$(uname -s)/$(uname -m)/carina -o /usr/local/bin/carina && \
    chmod +x /usr/local/bin/carina

VOLUME /carina
WORKDIR /carina
ENV CARINA_HOME /carina

COPY entry.sh /entry

ENTRYPOINT ["/entry"]
