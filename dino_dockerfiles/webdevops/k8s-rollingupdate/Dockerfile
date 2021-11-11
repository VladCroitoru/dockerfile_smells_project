#############################################
# GET/CACHE GO DEPS
#############################################
FROM golang as go-dependencies
RUN go get github.com/tools/godep
RUN go get k8s.io/client-go/... \
    && cd $GOPATH/src/k8s.io/client-go \
    && git checkout v6.0.0 \
    && godep restore ./...
RUN go get github.com/jessevdk/go-flags

#############################################
# BUILD GO APP
#############################################
FROM golang as backend
WORKDIR /app
COPY . /app
COPY --from=go-dependencies /go /go
RUN set -x \
    && go build -o main .

#############################################
# FINAL IMAGE
#############################################
FROM alpine
RUN apk add --no-cache \
        libc6-compat \
    	ca-certificates
COPY --from=backend /app/ /app/
CMD ["/app/main"]
