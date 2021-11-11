#
# Phase 1: build the application
#
FROM w32blaster/go-govendor AS builder

# make right Go project structure
RUN mkdir -p /go/src/github.com/w32blaster/bot-tfl-next-departure/vendor && \
    export GOPATH && \
    GOPATH="/go" 

# copy sources (please refer to .dockerignore file to see what is ignored)
ADD . /go/src/github.com/w32blaster/bot-tfl-next-departure/

RUN cd /go/src/github.com/w32blaster/bot-tfl-next-departure && \
    #
    # download fresh dependencies
    govendor fetch -v +out && \
    #
    # and compile our application
    CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o bot .

#
# Phase 2: prepare the runtime container, ready for production
#
FROM scratch

# copy our bot executable
COPY --from=builder /go/src/github.com/w32blaster/bot-tfl-next-departure/bot /bot

# copy root CA certificate to set up HTTPS connection with Telegram
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt

# copy timezone databases to be able to find London location zone
COPY --from=builder /usr/local/go/lib/time/zoneinfo.zip /usr/local/go/lib/time/zoneinfo.zip

VOLUME "/storage"
CMD ["/bot"]
