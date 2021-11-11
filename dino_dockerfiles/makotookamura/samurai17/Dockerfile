FROM alpine
LABEL maintainer makotookamura

RUN apk add --no-cache build-base boost-dev vim tzdata git && \
    ln -sf /usr/local/bin/gcc-6 /usr/local/bin/gcc && \
    ln -sf /usr/local/bin/g++-6 /usr/local/bin/g++ && \
    ln -sf vim /usr/bin/vi && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata

WORKDIR /samurai

ADD run_samurai.sh /

ENTRYPOINT [ "sh", "/run_samurai.sh" ]