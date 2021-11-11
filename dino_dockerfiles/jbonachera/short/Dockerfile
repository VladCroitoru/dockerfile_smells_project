FROM jbonachera/arch

ENV GOPATH=/usr/local/go
RUN mkdir -p $GOPATH/src/github.com/jbonachera/short
COPY . $GOPATH/src/github.com/jbonachera/short
WORKDIR $GOPATH/src/github.com/jbonachera/short
RUN pacman -S --noconfirm go git && \
    go get ./...  && \
    go build -o /usr/local/bin/short  cmd/main.go && \
    chmod +x /usr/local/bin/short && \
    rm -rf $GOPATH && \
    pacman -Rcs --noconfirm go
WORKDIR /
ENTRYPOINT /usr/local/bin/short
