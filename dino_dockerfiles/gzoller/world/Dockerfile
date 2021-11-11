FROM golang

# Docker-in-Docker concept from here: https://github.com/jamiemccrindle/dockerception

# Add the runtime dockerfile into the context as Dockerfile
COPY Dockerfile.run /go/bin/Dockerfile
COPY bin/* /go/bin/bin/

# Set the workdir to be /go/bin which is where the binaries are built
WORKDIR /go/bin

RUN \
  go get -d github.com/gzoller/portster && \
  cp /go/src/github.com/gzoller/portster/containerId.sh . && \
  go build -buildmode=exe github.com/gzoller/portster 

# Export the WORKDIR as a tar stream
CMD tar -cf - .
