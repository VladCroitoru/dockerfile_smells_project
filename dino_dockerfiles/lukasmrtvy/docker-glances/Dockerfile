FROM alpine:3.7

ENV GLANCES_VERSION 2.11.1

RUN apk add --no-cache python3 tzdata && \
    apk update && apk upgrade && apk add --no-cache --virtual build-dependencies gcc musl-dev python3-dev linux-headers && \
    pip3 install glances==${GLANCES_VERSION} \
                psutil \
                netifaces \
                bottle \
                hddtemp \ 
                docker \
                py-cpuinfo  && \
    mkdir -p /config/ && touch /config/glances_custom.conf && \
    apk del build-dependencies


EXPOSE 61209
EXPOSE 61208

VOLUME /config/

LABEL version=${GLANCES_VERSION}
LABEL url=https://github.com/nicolargo/glances/

ENTRYPOINT python3 -m glances -w
