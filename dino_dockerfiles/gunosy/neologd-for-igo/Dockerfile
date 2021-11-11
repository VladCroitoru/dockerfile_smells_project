FROM java:alpine AS build-env

ENV MECAB_WORK=/tmp/mecab
ENV NEOLOGD_WORK=/tmp/neologd
ENV MECAB_DIC_PATH=/usr/lib/mecab/dic/neologd
ENV IGO_DIC_PATH=/usr/lib/igo/dic/neologd

# dependencies
RUN set -x && apk add --no-cache git wget bash build-base curl file openssl perl sudo
RUN mkdir -p ${MECAB_DIC_PATH} ${IGO_DIC_PATH}

# mecab
WORKDIR ${MECAB_WORK}
RUN git clone https://github.com/taku910/mecab.git ${MECAB_WORK} && \
    cd ./mecab && ./configure --enable-utf8-only && make && make install

# neologd
WORKDIR ${NEOLOGD_WORK}
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git ${NEOLOGD_WORK} && \
    ./bin/install-mecab-ipadic-neologd -n -y -p ${MECAB_DIC_PATH} && \
    cd ./build/mecab-ipadic-* && wget http://iij.dl.osdn.jp/igo/55029/igo-0.4.5.jar && \
    java -Xmx4096m -cp igo-0.4.5.jar net.reduls.igo.bin.BuildDic ${IGO_DIC_PATH} . "utf-8"

FROM alpine:latest
COPY --from=build-env ${IGO_DIC_PATH} ${IGO_DIC_PATH}

