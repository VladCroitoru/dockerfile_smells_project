FROM ubuntu:14.04

# env vars
ENV HOME /root
ENV GOPATH /root/go
ENV PATH /root/go/bin:/usr/local/go/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN mkdir -p /root/go

RUN mkdir -p /application

RUN apt-get update
RUN apt-get install -y build-essential mercurial git subversion wget curl bzr

RUN wget -qO- https://storage.googleapis.com/golang/go1.6.2.linux-amd64.tar.gz | tar -C /usr/local -xzf -

COPY ./ /application

# required packages for app
RUN go get github.com/gorilla/mux
RUN go get github.com/btcsuite/btcrpcclient
RUN go get github.com/skip2/go-qrcode
RUN go get golang.org/x/crypto/bcrypt
RUN go get github.com/go-sql-driver/mysql
RUN go get github.com/gorilla/websocket
RUN go get github.com/hunterlong/simplemailer

WORKDIR /application

RUN go build .

EXPOSE 8080

ENTRYPOINT ["/bin/bash", "-c", "./application"]