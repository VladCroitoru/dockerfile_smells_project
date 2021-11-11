FROM golang:alpine
RUN apk add --no-cache git
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN go get github.com/labstack/echo \
    && go get github.com/dgrijalva/jwt-go \
    && go build -o meuip

FROM alpine:latest
COPY --from=0 /usr/src/app/meuip /usr/local/bin/meuip

EXPOSE 3000
CMD ["/usr/local/bin/meuip"]