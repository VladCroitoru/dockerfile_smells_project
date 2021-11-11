FROM golang:1.9 as builder

# install build tools
RUN go get -v github.com/golang/dep/cmd/dep

WORKDIR /go/src/github.com/contiamo/pod-status-logger
COPY ./*.go ,/Gopkg.* ./
COPY ./vendor ./vendor
RUN dep ensure -v --vendor-only
RUN CGO_ENABLED=0 GOOS=linux go install -v -ldflags "-extldflags \"-static\"" github.com/contiamo/pod-status-logger

# create actual build artifact
FROM alpine
RUN apk --no-cache add ca-certificates
COPY --from=builder /go/bin/pod-status-logger /bin/pod-status-logger

RUN adduser -D contiamo
USER contiamo

CMD [ "/bin/pod-status-logger" ]
