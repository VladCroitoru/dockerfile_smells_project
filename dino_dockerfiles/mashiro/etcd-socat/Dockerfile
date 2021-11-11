FROM debian:latest
MAINTAINER mashiro <mail@mashiro.org>

ENV ETCD_VERSION 2.0.11
ENV ETCD_DIRECTORY etcd-v${ETCD_VERSION}-linux-amd64
ENV ETCD_ARCHIVE ${ETCD_DIRECTORY}.tar.gz
ENV ETCD_DOWNLOAD_URL https://github.com/coreos/etcd/releases/download/v${ETCD_VERSION}/${ETCD_ARCHIVE}

RUN apt-get update
RUN apt-get install -y curl socat
RUN apt-get clean
RUN rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

RUN curl -L ${ETCD_DOWNLOAD_URL} -o ${ETCD_ARCHIVE}
RUN tar xzvf ${ETCD_ARCHIVE}
RUN mv ${ETCD_DIRECTORY}/etcd* /usr/bin/
RUN rm -rf ${ETCD_ARCHIVE} ${ETCD_DIRECTORY}

ADD watch.sh .
ADD forward.sh .

EXPOSE 10000

ENTRYPOINT ["./watch.sh"]
CMD []
