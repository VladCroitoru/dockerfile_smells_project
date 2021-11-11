FROM golang:alpine

ENV AWS_ACCESS_KEY_ID ""
ENV AWS_SECRET_ACCESS_KEY ""

RUN mkdir AWS-Metrics/

WORKDIR /go/src/AWS-Metrics/

COPY . .

RUN apk add --no-cache ca-certificates git wget

RUN go get -u github.com/labstack/echo/
RUN go get -u github.com/dgrijalva/jwt-go
RUN go get -u github.com/aws/aws-sdk-go/

WORKDIR /go/src/AWS-Metrics/src/main/

EXPOSE 1323

CMD ["go", "run", "main.go"]