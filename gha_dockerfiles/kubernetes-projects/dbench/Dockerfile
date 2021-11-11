FROM ubuntu:20.04

MAINTAINER Pratik raj (rajpratik71@gmail.com)

WORKDIR /tmp
RUN apt-get update && \
    apt-get install -y make gcc g++ git libaio-dev libaio1 zlib1g-dev && \
    git clone --depth 1 https://github.com/axboe/fio.git && \
    cd /tmp/fio && \
    ./configure && \
    make && \
    make install && \
    cd /tmp && \
    rm -rf /tmp/fio && \
    apt -y remove git make g++ gcc && \
    apt -y autoremove --purge && \
    rm -rf /var/lib/apt/lists/*

COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["fio"]
