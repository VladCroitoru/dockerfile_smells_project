FROM golang:1.14

# Protoc version to install
ENV VERSION 3.3.0

# Install unzip, required to unzip the protoc zip
RUN apt-get update && \
    apt-get upgrade -y -o Dpkg::Options::="--force-confold" && \
    apt-get install -y unzip && \
    apt-get clean && apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Download and install protoc
RUN wget https://github.com/google/protobuf/releases/download/v$VERSION/protoc-$VERSION-linux-x86_64.zip && \
   unzip protoc-$VERSION-linux-x86_64.zip && \
   rm -f protoc-$VERSION-linux-x86_64.zip

RUN go get github.com/codegangsta/gin

RUN mkdir -p /go/src/github.com/rajdeol/go-micro-hello-world
COPY . /go/src/github.com/rajdeol/go-micro-hello-world
WORKDIR /go/src/github.com/rajdeol/go-micro-hello-world

EXPOSE 3000
