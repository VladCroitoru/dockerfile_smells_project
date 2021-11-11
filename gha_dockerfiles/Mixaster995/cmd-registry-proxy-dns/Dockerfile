FROM golang:1.16-buster as go
ENV GO111MODULE=on
ENV CGO_ENABLED=0
ENV GOBIN=/bin
RUN go get github.com/go-delve/delve/cmd/dlv@v1.5.0
RUN go get github.com/edwarnicke/dl
RUN dl https://github.com/spiffe/spire/releases/download/v0.11.1/spire-0.11.1-linux-x86_64-glibc.tar.gz | \
    tar -xzvf - -C /bin --strip=3 ./spire-0.11.1/bin/spire-server ./spire-0.11.1/bin/spire-agent

FROM go as build
WORKDIR /build
COPY go.mod go.sum ./
COPY pkg ./pkg
RUN go build ./pkg/imports
COPY . .
RUN go build -o /bin/registry-proxy-dns .

FROM build as test
CMD go test -test.v ./...

FROM test as debug
CMD dlv -l :40000 --headless=true --api-version=2 test -test.v ./...

FROM alpine as runtime
COPY --from=build /bin/registry-proxy-dns /bin/registry-proxy-dns
ENTRYPOINT ["/bin/registry-proxy-dns"]