FROM anapsix/alpine-java:jre8

RUN apk upgrade --update && \
    apk add --update tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime &&\
    echo "Asia/Shanghai" > /etc/timezone&&\
    date &&\
    rm -fr /tmp/* /var/cache/apk/*