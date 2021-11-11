FROM golang:1.6-alpine
MAINTAINER nic0d
RUN apk update \
  && apk add git gcc musl-dev \
  && go get github.com/constabulary/gb/... \
  && go get golang.org/x/tools/cmd/godoc

COPY . /app

WORKDIR /app 
RUN gb build github.com/matrix-org/go-neb
CMD BIND_ADDRESS=:4050 DATABASE_TYPE=sqlite3 DATABASE_URL=go-neb.db BASE_URL=$PUBLIC_FACING_HOST_URL bin/go-neb
