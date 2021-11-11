FROM golang:alpine

# Install required packages
RUN apk update
RUN apk add --no-cache curl bash git ca-certificates wget
RUN update-ca-certificates

# Install Golang package manager
RUN curl -sSO https://raw.githubusercontent.com/pote/gpm/v1.4.0/bin/gpm \
  && chmod +x gpm \
  && mv gpm /usr/local/bin

# Resolve manually crc32 dependancy
RUN go get github.com/klauspost/crc32

# Install Burrow
RUN go get github.com/linkedin/Burrow
WORKDIR /go/src/github.com/linkedin/Burrow
RUN gpm install && go install
RUN ln -s /go/bin/Burrow /bin/burrow

# Customize to container
RUN mkdir /config /var/log/burrow /burrow
WORKDIR /burrow
COPY burrow.cfg.template /burrow
COPY entrypoint.sh /burrow/entrypoint.sh
RUN chmod 755 /burrow/entrypoint.sh

EXPOSE 8000

VOLUME /var/log/burrow /config

# CMD definition
CMD ["/burrow/entrypoint.sh"]
