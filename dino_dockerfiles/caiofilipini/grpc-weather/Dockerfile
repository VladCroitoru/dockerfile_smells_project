FROM golang:latest
MAINTAINER Caio Filipini

# install build tools
RUN apt-get update && apt-get install -y git unzip autoconf libtool

# download and build protoc
RUN git clone https://github.com/google/protobuf /tmp/protobuf
RUN cd /tmp/protobuf && ./autogen.sh && ./configure --prefix=/usr && make && make check && make install

# install dependencies (e.g. protoc-gen-go, grpc)
RUN go get -u github.com/golang/protobuf/protoc-gen-go
RUN go get -u google.golang.org/grpc

# load our code
ADD . /go/src/github.com/caiofilipini/grpc-weather
WORKDIR /go/src/github.com/caiofilipini/grpc-weather

# build server and client
RUN make install-server
RUN make install-client

# run server
ENTRYPOINT /go/bin/weather_server

# expose server port
EXPOSE 9000
