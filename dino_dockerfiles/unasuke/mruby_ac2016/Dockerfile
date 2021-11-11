FROM alpine

RUN apk add --no-cache --virtual=builddeps \
        bison           \
        ca-certificates \
        cmake           \
        curl            \
        gcc             \
        git             \
        g++             \
        libc-dev        \
        linux-headers   \
        make            \
        openssl         \
        perl            \
        ruby            \
        ruby-dev        \
        wget            \
        yaml-dev        \
        zlib-dev        \
    && git clone https://github.com/unasuke/h2o.git \
    && cd h2o \
    && git checkout mruby-yaml \
    && cmake -DWITH_BUNDLED_SSL=on -DWITH_MRUBY=on . \
    && make install \
    && cd .. \
    && rm -rf h2o-* \
    && apk del builddeps \
    && apk add --no-cache --virtual=rundeps \
        libstdc++ \
        perl

RUN mkdir /etc/h2o

WORKDIR /etc/h2o

EXPOSE 80 443

COPY . /etc/h2o
CMD ["h2o", "--mode=master", "-c", "h2o.conf"]
