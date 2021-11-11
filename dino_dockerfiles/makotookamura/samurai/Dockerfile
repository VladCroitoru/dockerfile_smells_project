FROM alpine
LABEL maintainer makotookamura

WORKDIR /temp_samurai

RUN apk add --no-cache --virtual .buildlibs build-base boost-dev && \
    ln -sf /usr/local/bin/gcc-6 /usr/local/bin/gcc && \
    ln -sf /usr/local/bin/g++-6 /usr/local/bin/g++ && \
    wget http://samuraicoding.info/software/samurai-software-20170930.zip && \
    unzip samurai-software-20170930.zip && \
    rm samurai-software-20170930.zip && \
    make && \
    apk del --no-cache .buildlibs && \
    apk add --no-cache libstdc++ libgcc vim && \
    ln -sf vim /usr/bin/vi

ADD cp_source.sh /

VOLUME [ "/samurai" ]

WORKDIR /samurai

CMD [ "sh", "/cp_source.sh" ]