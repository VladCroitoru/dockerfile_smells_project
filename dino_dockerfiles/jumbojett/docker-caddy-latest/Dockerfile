FROM golang:1.6

RUN mkdir -p /go/src/app
RUN git clone https://github.com/mholt/caddy.git /go/src/app

WORKDIR /go/src/app

RUN go-wrapper download
RUN go-wrapper install

# Install dep
RUN cd /go/src/app/caddy && go get ./...
# Run included build script
RUN /go/src/app/caddy/build.bash /bin/caddy
# Execute /bin/caddy
CMD ["caddy", "--conf", "/etc/Caddyfile"]
