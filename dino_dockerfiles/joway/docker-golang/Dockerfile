FROM ubuntu:latest

# golang
RUN apt-get update && apt-get install -y wget git gcc g++ make python pkg-config && apt-get clean

RUN wget -P /tmp https://storage.googleapis.com/golang/go1.9.2.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf /tmp/go1.9.2.linux-amd64.tar.gz && \
    rm /tmp/go1.9.2.linux-amd64.tar.gz
ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"
WORKDIR $GOPATH
