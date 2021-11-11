FROM registry.fedoraproject.org/fedora:latest AS builder

COPY . /src
WORKDIR /src

RUN yum install --assumeyes make && \
    make devcontainer-deps && \
    make

#
# Application Image
#

FROM registry.fedoraproject.org/fedora:latest

COPY hack /src/hack
COPY Makefile /src

RUN cd /src && \
    yum install --assumeyes make && \
    make image-deps && \
    rm -rf /src && \
    yum autoremove --assumeyes make

COPY --from=builder \
    /src/_output/chart-streams \
    /usr/local/bin/chart-streams

USER 10001

VOLUME [ "/var/lib/chart-streams" ]

ENTRYPOINT [ "/usr/local/bin/chart-streams", "serve" ]
