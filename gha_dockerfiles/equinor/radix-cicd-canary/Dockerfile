FROM golang:alpine3.10 as builder

ENV GO111MODULE=on

RUN apk update && apk add git && apk add ca-certificates curl

WORKDIR /go/src/github.com/equinor/radix-cicd-canary/

# get go dependecies
COPY go.mod go.sum ./
RUN go mod download

# build app
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags "-s -w" -a -installsuffix cgo -o ./rootfs/radix-cicd-canary

RUN addgroup -S -g 1000 radix-cicd-canary
RUN adduser -S -u 1000 -G radix-cicd-canary radix-cicd-canary

FROM scratch
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /go/src/github.com/equinor/radix-cicd-canary/rootfs/radix-cicd-canary /usr/local/bin/radix-cicd-canary
USER 1000
ENTRYPOINT ["/usr/local/bin/radix-cicd-canary"]
