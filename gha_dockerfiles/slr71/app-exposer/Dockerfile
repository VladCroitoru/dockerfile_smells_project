### First stage
FROM quay.io/goswagger/swagger as swagger

FROM golang:1.16 as build-root

WORKDIR /build

COPY go.mod .
COPY go.sum .
COPY --from=swagger /usr/bin/swagger /usr/bin/

COPY . .

ENV CGO_ENABLED=0
ENV GOOS=linux
ENV GOARCH=amd64

RUN go install -v ./...
RUN swagger generate spec -o ./docs/swagger.json --scan-models

ENTRYPOINT ["app-exposer"]

EXPOSE 60000
