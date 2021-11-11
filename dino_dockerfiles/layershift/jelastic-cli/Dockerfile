FROM java:openjdk-8-jre-alpine
MAINTAINER "Layershift" <jelastic@layershift.com>

RUN apk add --update curl bash jq && \
    rm -rf /var/cache/apk/*

WORKDIR /root
RUN curl -s ftp://ftp.jelastic.com/pub/cli/jelastic-cli-installer.sh | bash 
COPY ./entry.sh /
COPY ./jelastic.properties /root/.config/jelastic/jelastic.properties

ENTRYPOINT ["/entry.sh"]
