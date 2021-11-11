FROM ubuntu:14.04

RUN apt-get update -y -q && \
apt-get install -y -q gcc libc6-dev curl git pkg-config apt-utils && \
mkdir -p tmp/go && \
curl https://storage.googleapis.com/golang/go1.3.1.src.tar.gz | tar xvzf - -C tmp/go --strip-components=1 && \
cd tmp/go/src && \
./make.bash && \
cd ../.. && \
mv go /usr/local && \
mkdir /gopath && \
export GOROOT=/usr/local/go && \
export GOPATH=/gopath && \
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin && \
go get github.com/laher/goxc && \
goxc -bc "linux darwin" -arch "amd64" -t && \
apt-get remove -y gcc libc6-dev curl python perl apt-utils && \
apt-get autoremove -y && \
apt-get autoclean -y && \
apt-get purge -y && \
apt-get install git -y && \
rm -rf /gopath/*

ENV GOROOT /usr/local/go
ENV GOPATH /gopath
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin
