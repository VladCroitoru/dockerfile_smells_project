## BUILDING
##   (from project root directory)
##   $ docker build -t go-1-7-1-on-ubuntu .
##
## RUNNING
##   $ docker run go-1-7-1-on-ubuntu

FROM gcr.io/stacksmith-images/ubuntu-buildpack:14.04-r10

MAINTAINER Emil Hammarstrom <emil.a.hammarstrom@gmail.com>

ENV STACKSMITH_STACK_ID="jeosaoe" \
    STACKSMITH_STACK_NAME="Go 1.7.1 on Ubuntu" \
    STACKSMITH_STACK_PRIVATE="1"

RUN bitnami-pkg install go-1.7.1-0 --checksum 8752194d34afa4cf01da9109f559bf30da8bd487bd8ec237f54c9b18bb1bc279

ENV GOPATH=/gopath
ENV PATH=$GOPATH/bin:/opt/bitnami/go/bin:$PATH

# Go base template
COPY . /app
WORKDIR /app

RUN go get github.com/initiumsrc/binary
RUN go get github.com/initiumsrc/celltomaton
RUN go build main.go

# Add Tini
ENV TINI_VERSION v0.10.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

CMD ["./main"]
