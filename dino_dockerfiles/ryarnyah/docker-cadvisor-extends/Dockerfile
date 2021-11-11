FROM golang:1.9 as builder

LABEL MAINTAINER ryarnyah@gmail.com

ENV BRANCH v0.28.3

WORKDIR /go/src/github.com/google

RUN git clone -b $BRANCH https://github.com/google/cadvisor.git

COPY ./build.sh /go/src/github.com/google/cadvisor/build.sh
COPY ./modules.go /go/src/github.com/google/cadvisor/modules.go
RUN cd /go/src/github.com/google/cadvisor && ./build.sh

FROM alpine:3.4
LABEL MAINTAINER ryarnyah@gmail.com

ENV GLIBC_VERSION "2.23-r3"

RUN apk --no-cache add ca-certificates wget device-mapper findutils && \
    apk --no-cache add zfs --repository http://dl-3.alpinelinux.org/alpine/edge/main/ && \
    apk --no-cache add thin-provisioning-tools --repository http://dl-3.alpinelinux.org/alpine/edge/main/ && \
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk && \
    wget https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk && \
    apk add glibc-${GLIBC_VERSION}.apk glibc-bin-${GLIBC_VERSION}.apk && \
    /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib && \
    echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf && \
    rm -rf /var/cache/apk/*

# Grab cadvisor from the staging directory.
COPY --from=builder /go/src/github.com/google/cadvisor/cadvisor /usr/bin/cadvisor

EXPOSE 8080
ENTRYPOINT ["/usr/bin/cadvisor", "-logtostderr"]
