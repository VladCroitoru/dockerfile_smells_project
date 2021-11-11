FROM golang:1.10.0-alpine3.7 as builder
RUN apk add --update --no-cache alpine-sdk ca-certificates \
      libressl \
      git openssh openssl build-base coreutils upx
WORKDIR /go/src/github.com/StevenACoffman/go-spew
RUN go get -d -v github.com/satori/go.uuid
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -ldflags '-w -s' -o main main.go
RUN upx --brute main

FROM scratch
ADD ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /go/src/github.com/StevenACoffman/go-spew/main /

ARG GIT_COMMIT=unknown
LABEL git-commit=$GIT_COMMIT
ARG GIT_BRANCH=unknown
LABEL git-branch=$GIT_BRANCH
ARG BUILD_TIME=unknown
LABEL build_time=$BUILD_TIME

CMD ["/main"]
