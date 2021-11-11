#build stolon
FROM golang:1.9.0-stretch

WORKDIR /go/src/github.com/sorintlab
RUN git clone https://github.com/sorintlab/stolon.git

WORKDIR /go/src/github.com/sorintlab/stolon
RUN git checkout tags/v0.7.0
RUN ./build

#package postgres with stolon and wal-e
FROM postgres:10.1

RUN apt-get update
RUN apt-get install -qqy --no-install-recommends \
                  build-essential \
                  python3 \
                  python3-setuptools \
                  python3-pip \
                  python3-dev \
                  lzop pv \
                  $(apt-get -s dist-upgrade|awk '/^Inst.*ecurity/ {print $2}') &&\
                  apt-get clean

RUN pip3 install wheel \
                  python-swiftclient \
                  python-keystoneclient \
                  setuptools \
                  python-swiftclient \
                  python-keystoneclient \
                  wal-e \
                  envdir \
                  Flask


COPY --from=0 /go/src/github.com/sorintlab/stolon/bin/* /usr/local/bin/
RUN chmod +x /usr/local/bin/stolon-keeper /usr/local/bin/stolon-sentinel /usr/local/bin/stolon-proxy /usr/local/bin/stolonctl
RUN useradd -ms /bin/bash stolon

WORKDIR /usr/local/bin/

EXPOSE 5432
