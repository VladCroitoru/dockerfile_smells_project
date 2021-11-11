FROM alpine:latest

##/
 # Copy files
 #/
COPY rootfs /

RUN apk --no-cache add --virtual .build-deps bash curl tar libxml2-utils \
    && export JET_VERSION=$(/opt/scripts/jet-latest.sh) \
    && curl -SLO "https://s3.amazonaws.com/codeship-jet-releases/${JET_VERSION}/jet-linux_amd64_${JET_VERSION}.tar.gz" \
    && tar -xaC /usr/local/bin -f jet-linux_amd64_${JET_VERSION}.tar.gz \
    && chmod +x /usr/local/bin/jet \
    && apk del .build-deps \
    && rm -f jet-linux_amd64_${JET_VERSION}.tar.gz

WORKDIR /jet

ENTRYPOINT ["/usr/local/bin/jet"]