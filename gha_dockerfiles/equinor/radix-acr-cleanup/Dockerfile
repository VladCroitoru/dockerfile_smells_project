FROM golang:alpine3.11 as builder

ENV GO111MODULE=on

RUN apk update && \
    apk add ca-certificates  && \
    apk add --no-cache gcc musl-dev && \
    go get -u golang.org/x/lint/golint

WORKDIR /go/src/github.com/equinor/radix-acr-cleanup/

# Install project dependencies
COPY go.mod go.sum ./
RUN go mod download

COPY . .
# run tests and linting
RUN golint `go list ./cmd/...` && \
    golint `go list ./pkg/...` && \
    go vet `go list ./cmd/...` && \
    go vet `go list ./pkg/...` && \
    CGO_ENABLED=0 GOOS=linux go test `go list ./cmd/...` && \
    CGO_ENABLED=0 GOOS=linux go test `go list ./pkg/...` 

# build
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags "-s -w" -a -installsuffix cgo -o /usr/local/bin/radix-acr-cleanup ./cmd/acr-cleanup/.

FROM mcr.microsoft.com/azure-cli:2.2.0

ARG UID=1000
ARG GID=1000

RUN addgroup -S -g $GID acr-cleanup
RUN adduser -S -u $UID -s /bin/sh -G acr-cleanup acr-cleanup 

WORKDIR /radix-acr-cleanup/
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /usr/local/bin/radix-acr-cleanup /radix-acr-cleanup/radix-acr-cleanup
COPY --from=builder /go/src/github.com/equinor/radix-acr-cleanup/run_acr_cleanup.sh /radix-acr-cleanup/run_acr_cleanup.sh

ENV TENANT=3aa4a235-b6e2-48d5-9195-7fcf05b459b0 \
    AZURE_CREDENTIALS=/radix-acr-cleanup/.azure/sp_credentials.json

EXPOSE 8080
RUN chmod +x /radix-acr-cleanup/run_acr_cleanup.sh
ENTRYPOINT [ "/radix-acr-cleanup/run_acr_cleanup.sh"]
USER 1000
CMD ["-c"]
