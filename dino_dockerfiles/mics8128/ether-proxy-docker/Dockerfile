FROM alpine:3.5

ENV GOPATH /home/go

RUN apk --update add -ut build-deps \
    go \
    git \
    g++
	
RUN go get github.com/ethereum/ethash
RUN go get github.com/ethereum/go-ethereum/common
RUN go get github.com/goji/httpauth
RUN go get github.com/gorilla/mux
RUN go get github.com/yvasiyarov/gorelic

WORKDIR /opt

RUN git clone https://github.com/sammy007/ether-proxy.git

WORKDIR /opt/ether-proxy

RUN go build -o ether-proxy main.go

COPY run.sh /run.sh

WORKDIR /

CMD ["/run.sh"]

EXPOSE 8546
EXPOSE 8080
