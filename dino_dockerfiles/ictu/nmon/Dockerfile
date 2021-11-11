FROM alpine:latest

ENV md5 165ce7e17745b0c70193ffe808e9c799

RUN apk update && apk add curl && \
    curl -f http://pilotfiber.dl.sourceforge.net/project/nmon/nmon16e_mr_nmon.tar.gz -o nmon.tar.gz && \
    sum=$(cat nmon.tar.gz | md5sum | cut -d ' ' -f 1) && \
    echo $sum && \
    if [ ! $sum == $md5 ]; then exit 1; fi && \
    mkdir /nmon && \
    tar -xvf nmon.tar.gz -C /nmon && \
    rm nmon.tar.gz && \
    chmod +x /nmon/*

VOLUME "/nmon"
