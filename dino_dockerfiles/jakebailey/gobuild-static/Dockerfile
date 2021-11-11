FROM golang:alpine

ENV CGO_ENABLED=0

# Pre-build the standard library
RUN go install -v -a -installsuffix static -ldflags '-s -w -extldflags "-static"' std

COPY static-build.sh /bin/

ENTRYPOINT [ "/bin/static-build.sh" ]
