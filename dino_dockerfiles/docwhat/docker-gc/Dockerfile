# Requires docker 17.06 to build

##### Build image #####
FROM golang:1.7 as builder

# Bootstrap requirements
COPY ./script/ /script/
RUN /script/bootstrap

# Get source in place
COPY ./ /go/src/docwhat.org/docker-gc/
WORKDIR /go/src/docwhat.org/docker-gc

# Test
RUN ./script/test

# Lint
RUN ./script/lint

# Build binary
RUN ./script/build docker

##### Run image #####
FROM scratch

ENV COLUMNS 80

COPY --from=builder /go/src/docwhat.org/docker-gc/docker-gc_linux_amd64 /docker-gc

ENTRYPOINT ["/docker-gc"]

# vim: set ft=dockerfile :
