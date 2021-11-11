FROM yodlr/nodejs
MAINTAINER Ross Kukulinski <ross@getyodlr.com>

WORKDIR /src


ENV PATH $PATH:/usr/local/go/bin
ENV GOPATH /usr/local/go/
RUN apt-get -qq update && \
    apt-get install -yqq wget ca-certificates build-essential git mercurial && \
    wget --no-verbose https://storage.googleapis.com/golang/go1.3.3.src.tar.gz && \
    tar -v -C /usr/local -xzf go1.3.3.src.tar.gz && \
    cd /usr/local/go/src && ./all.bash --no-clean 2>&1 \
    cd /root && \
    git clone https://github.com/coreos/fleet.git && \
    cd fleet && ./build

RUN cd /root && git clone https://github.com/coreos/fleet.git && \
    cd fleet && git checkout v0.9.2 && ./build && cp /root/fleet/bin/fleetctl /usr/bin/fleetctl && \
    rm -Rf /usr/local/go/src && \
    rm -Rf /root/fleet

ADD package.json /src/
RUN npm install

ADD . /src/

ENTRYPOINT ["bin/fleet-deploy"]
