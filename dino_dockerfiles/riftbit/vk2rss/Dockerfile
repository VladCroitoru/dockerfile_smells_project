
# STEP 1 build executable binary
FROM golang:alpine as builder
# Create appuser
RUN adduser -D -g '' appuser && apk update && apk add -U --no-cache ca-certificates git
COPY . $GOPATH/src/github.com/riftbit/vk2rss/
WORKDIR $GOPATH/src/github.com/riftbit/vk2rss/
#get dependancies
RUN go get -d -v
#build the binary
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build --ldflags "-w -s" -a -installsuffix cgo -o /go/bin/vk2rss


# STEP 2 build a small image
# start from scratch
FROM scratch
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /etc/passwd /etc/passwd
# Copy our static executable
COPY --from=builder /go/bin/vk2rss /go/bin/vk2rss
USER appuser
ENTRYPOINT ["/go/bin/vk2rss"]