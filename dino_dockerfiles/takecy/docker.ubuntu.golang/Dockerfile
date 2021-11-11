FROM ubuntu:latest

MAINTAINER takecy

RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y git

# Go
WORKDIR /tmp
RUN wget https://storage.googleapis.com/golang/go1.5.1.linux-amd64.tar.gz
RUN tar -C /usr/local -xf go1.5.1.linux-amd64.tar.gz
ENV PATH=$PATH:/usr/local/go/bin
ENV GOPATH=$HOME/go
ENV PATH=$GOPATH/bin:$PATH
RUN go version
RUN go env


# in your DOckerfike example FROM takecy/golang

# WORKDIR $GOPATH
# RUN pwd
# RUN go get github.com/tools/godep
# COPY . $GOPATH/src/github.com/takecy/some-appp
# WORKDIR $GOPATH/src/github.com/takecy/some-appp

# RUN godep restore
# RUN go build -o ./some-app ./*.go
# RUN cp ./some-app /usr/local/bin

# ENV DEBUG true
# EXPOSE 3000

# CMD ["/usr/local/bin/some-app"]
