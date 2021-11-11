FROM jreckner/docker-libsodium
MAINTAINER Ted Östrem <ted@t3d.one>
RUN apt-get update && apt-get install -y \
    wget \
    git \
		&& apt-get clean && apt-get autoremove --purge
ENV GOVERSION=go1.8 \
    GOPATH=/usr/local \
    CGO_ENABLED=1
RUN wget https://storage.googleapis.com/golang/${GOVERSION}.linux-amd64.tar.gz && \
    tar -C ${GOPATH} -xzf ${GOVERSION}.linux-amd64.tar.gz && \
    rm ${GOVERSION}.linux-amd64.tar.gz
ENV PATH=${PATH}:${GOPATH}/bin:${GOPATH}/go/bin
RUN go get github.com/shadowsocks/shadowsocks-go/cmd/shadowsocks-server
ADD entrypoint.sh /root
EXPOSE 1984
ENTRYPOINT ["/root/entrypoint.sh"]
