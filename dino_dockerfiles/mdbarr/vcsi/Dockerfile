FROM alpine

RUN apk --no-cache add --virtual build-dependencies \
    build-base automake autoconf git && \
    apk --no-cache add readline-dev gdbm-dev && \
    mkdir /vcsi && \
    cd /vcsi && \
    git clone https://github.com/mdbarr/infostd.git && \
    cd infostd && \
    make && \
    make install && \
    cd .. && \
    git clone https://github.com/mdbarr/vcsi.git && \
    cd vcsi && \
    ./configure && \
    make && \
    make install && \
    cd / && \
    rm -rf /vcsi && \
    apk del build-dependencies

CMD ["/usr/local/bin/vcsi"]
