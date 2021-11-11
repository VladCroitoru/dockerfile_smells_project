# builder image
FROM golang:1.15-alpine as builder
WORKDIR /build
ADD *.go ./
ADD go.* ./
RUN go mod tidy
RUN CGO_ENABLED=0 GOOS=linux go build -a -o hello-world .

# generate clean, final image
FROM alpine:3.12
RUN addgroup -g 10001 -S nonroot && adduser -u 10000 -S -G nonroot -h /home/nonroot nonroot
RUN apk add --no-cache tini bind-tools
USER nonroot
COPY --from=builder /build/hello-world /sbin/
ENTRYPOINT ["/sbin/tini", "--", "hello-world"]