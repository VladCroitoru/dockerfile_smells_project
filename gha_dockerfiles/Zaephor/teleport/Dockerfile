## This approach appears to timeout on travis... oh well
#FROM golang:1.9.7-alpine3.8 AS build
#ARG REMOTE_BRANCH=master
#RUN echo "=== ${REMOTE_BRANCH}" && \
#    uname -a && \
#    apk add --no-cache \
#      git make gcc musl-dev zip tar && \
#    git clone -q --depth=1 --branch=${REMOTE_BRANCH} https://github.com/gravitational/teleport.git /go/src/github.com/gravitational/teleport && \
#    cd /go/src/github.com/gravitational/teleport && git checkout -qf ${REMOTE_BRANCH} && \
#    go env && \
#    make release && \
#    mkdir temp/ && tar -xvf teleport-*.tar.gz -C ./temp --strip-components=1 teleport/teleport teleport/tctl teleport/tsh

FROM lsiobase/ubuntu:bionic
EXPOSE 3022 3023 3024 3025 3026 3080
VOLUME /config
#COPY temp/* /usr/sbin/
COPY s6/ /
ARG RELEASE
RUN /pull-teleport.sh
#COPY --from=build /go/src/github.com/gravitational/teleport/temp/* /usr/sbin/
