FROM golang:1.16.3-alpine3.13 as builder

RUN apk update
RUN apk add ca-certificates curl git && \
    apk add --no-cache gcc musl-dev
RUN go get -u \
    golang.org/x/lint/golint \
    github.com/frapposelli/wwhrd \
    github.com/nats-io/nats-server/v2

WORKDIR /go/src/github.com/equinor/radix-cost-allocation/

# Install project dependencies
COPY go.mod go.sum ./
RUN go mod download

# Check dependency licenses using https://github.com/frapposelli/wwhrd
COPY .wwhrd.yml ./
RUN wwhrd -q check

# Copy project code
COPY . .

# run tests and linting
RUN golint `go list ./...` && \
    go vet `go list ./...` && \
    CGO_ENABLED=0 GOOS=linux go test `go list ./...`

# Build
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags "-s -w" -a -installsuffix cgo -o ./rootfs/radix-cost-allocation
RUN addgroup -S -g 1000 radix-cost-allocation
RUN adduser -S -u 1000 -G radix-cost-allocation radix-cost-allocation

# Run operator
FROM scratch
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /go/src/github.com/equinor/radix-cost-allocation/rootfs/radix-cost-allocation /usr/local/bin/radix-cost-allocation
USER 1000

ENTRYPOINT ["/usr/local/bin/radix-cost-allocation"]
