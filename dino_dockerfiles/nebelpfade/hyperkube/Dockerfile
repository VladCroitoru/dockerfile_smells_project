## We are going from official Alpine Linux image
FROM alpine:3.2
MAINTAINER Ivan Gaas <ivan.gaas@gmail.com>

## Set up env vars for easily maintenance in future
ENV TERM="xterm-color" KUBE_VER="v1.1.2"
ENV KUBE_MANIFESTS_URL="https://raw.githubusercontent.com/kubernetes/kubernetes/${KUBE_VER}/cluster/images/hyperkube"

## Build hyperkube from the source, so we need build tools, rsync and kernel headers
## Build only specific version of hyperkube from KUBE_VER and place manifests for fully compatibility with original image
## Also it requres iptables for hyperkube proxy and ca certs to work with TLS/SSL
RUN apk -q --no-progress add --update build-base autoconf libtool git mercurial go rsync linux-headers && \
    mkdir -p /build/src && export GOPATH="/build" && \
    go get -d github.com/kubernetes/kubernetes > /dev/null 2>&1 || true && \
    cd /build/src/github.com/kubernetes/kubernetes && git checkout -q ${KUBE_VER} && \
    ./hack/build-go.sh cmd/hyperkube && mv ./_output/local/bin/linux/amd64/hyperkube / && \
    apk -q --no-progress del --purge build-base autoconf libtool git mercurial go rsync linux-headers && \
    apk -q --no-progress add ca-certificates iptables && \
    mkdir -p /etc/kubernetes/manifests /etc/kubernetes/manifests-multi && \
    wget -qO- ${KUBE_MANIFESTS_URL}/master-multi.json | sed "s/gcr.io\/google_containers/nebelpfade/g;s/VERSION/${KUBE_VER}/g" > /etc/kubernetes/manifests-multi/master-multi.json && \
    wget -qO- ${KUBE_MANIFESTS_URL}/master.json | sed "s/gcr.io\/google_containers/nebelpfade/g;s/VERSION/${KUBE_VER}/g" > /etc/kubernetes/manifests/master.json && \
    cd / && rm -rf /var/cache/apk/* /tmp/* /build