FROM golang:1.12-alpine

RUN \
	apk add --no-cache --virtual .build-deps \
		git \
		libc-dev

# Git configuration
RUN git config --global http.followRedirects true

# Install tools which will be used by go generate
RUN \
	go get -v \
		github.com/jteeuwen/go-bindata/... \
		golang.org/x/tools/cmd/goimports

# Copy app source, fetch dependencies and build all binaries
WORKDIR /usr/src/app
COPY . .
RUN go generate -v ./...
RUN \
	CGO_ENABLED=0 \
	GOBIN="/usr/local/bin" \
	go install -v -a -installsuffix cgo ./cmd/...

RUN ls -lAh /usr/local/bin

###

FROM alpine

# Copy built binaries into this image
COPY --from=0 /usr/local/bin/ /usr/local/bin/

ENTRYPOINT ["workreportmgr"]
