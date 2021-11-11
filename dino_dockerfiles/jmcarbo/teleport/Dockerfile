FROM golang:1.8

RUN wget https://github.com/gravitational/teleport/releases/download/v2.0.0-rc.2/teleport-v2.0.0-rc.2-linux-amd64-bin.tar.gz && \
    tar zxvf teleport*

RUN cd teleport && make install

VOLUME /var/lib/teleport
