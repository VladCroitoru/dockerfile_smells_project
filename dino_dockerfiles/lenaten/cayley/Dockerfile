FROM debian:jessie

MAINTAINER maman.nathaniel@gmail.com

ENV CAYLEY_VERSION=0.4.1 \
    CAYLEY_DIR=/opt/cayley \
    CAYLEY_CFG_DIR=/etc/cayley \
    CAYLEY_CFG=/etc/cayley/cayley.cfg

RUN apt-get update && \
    apt-get install -y wget
    
RUN mkdir ${CAYLEY_DIR} && \
    mkdir ${CAYLEY_CFG_DIR} && \
    wget https://github.com/google/cayley/releases/download/v${CAYLEY_VERSION}/cayley_${CAYLEY_VERSION}_linux_amd64.tar.gz && \
    tar xf cayley_${CAYLEY_VERSION}_linux_amd64.tar.gz -C ${CAYLEY_DIR} --strip-components 1 && \
    ln -s ${CAYLEY_DIR}/cayley /usr/local/bin/cayley && \
    rm cayley_${CAYLEY_VERSION}_linux_amd64.tar.gz

RUN echo '{\n "database": "leveldb",\n "db_path": "/tmp/cayley_test",\n "listen_host": "0.0.0.0"\n}' \
    >> ${CAYLEY_CFG}

VOLUME [ "/etc/cayley" ]

WORKDIR ${CAYLEY_DIR}

CMD cayley init && \
    cayley http

EXPOSE 64210
