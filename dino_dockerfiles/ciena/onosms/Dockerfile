FROM onosproject/onos:1.3
MAINTAINER Ciena - BluePlanet <blueplant@ciena.com>

RUN apt-get update && \
    apt-get install -y curl git build-essential

# Save a clean tree
RUN mkdir -p /bp2/save && \
    tar -P -zcf /bp2/save/clean.tgz /root/onos

# Install Go
WORKDIR /usr/local
RUN curl https://storage.googleapis.com/golang/go1.5.1.linux-amd64.tar.gz | tar xzf - -C /usr/local && \
    ln -s /usr/local/go/bin/go /usr/local/bin/go

# Download and build the artifacts
RUN mkdir -p /root/build && \
    git clone http://github.com/ciena/onosms /root/build/onosms
WORKDIR /root/build/onosms
RUN GOPATH=/root/build/onosms go get github.com/tools/godep && \
    GOPATH=/root/build/onosms ./bin/godep restore && \
    make bp2/hooks/onos-hook bp2/hooks/onos-wrapper && \
    mkdir -p /bp2/hooks && \
    cp bp2/hooks/onos-hook /bp2/hooks/onos-hook && \
    cp bp2/hooks/onos-wrapper /bp2/hooks/onos-wrapper

WORKDIR /root/onos

ENV NBI_onos_port=8181
ENV NBI_onos_type=http
ENV NBI_onos_publish=true

ENV NBI_onosssh_port=8101
ENV NBI_onosssh_type=tcp
ENV NBI_onosshh_publish=true

ENV ONOS_APPS drivers,openflow,proxyarp,mobility,fwd

RUN ln -s /bp2/hooks/onos-hook /bp2/hooks/heartbeat && \
    ln -s /bp2/hooks/onos-hook /bp2/hooks/peer-update && \
    ln -s /bp2/hooks/onos-hook /bp2/hooks/peer-status

# Cleanup
RUN rm -rf /usr/local/bin/go && \
    rm -rf /usr/local/go && \
    rm -rf /root/build && \
    apt-get remove -y git build-essential && \
    apt-get autoremove -y && \
    apt-get purge -y && \
    apt-get clean

ENV BP2HOOK_heartbeat=/bp2/hooks/heartbeat
ENV BP2HOOK_peer-update=/bp2/hooks/peer-update
ENV BP2HOOK_peer-status=/bp2/hooks/peer-status

ENTRYPOINT ["/bp2/hooks/onos-wrapper","./bin/onos-service"]
