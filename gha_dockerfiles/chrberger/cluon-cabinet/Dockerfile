FROM alpine:3.14.0 as builder
MAINTAINER Christian Berger "christian.berger@gu.se"
RUN apk update && \
    apk --no-cache add \
        cmake \
        g++ \
        make \
        linux-headers
ADD . /opt/sources
WORKDIR /opt/sources
RUN mkdir build && \
    cd build && \
    cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/tmp .. && \
    make && make install

# Part to deploy.
#FROM alpine:3.14.0
#MAINTAINER Christian Berger "christian.berger@gu.se"
#
#WORKDIR /usr/bin
#COPY --from=builder /tmp/bin/cab??? .
#ENTRYPOINT ["/usr/bin/cab???"]
