FROM golang:1.9-alpine as builder

RUN mkdir -p /go/src/github.com/MOZGIII/aws-ecr-login
WORKDIR /go/src/github.com/MOZGIII/aws-ecr-login

COPY . .
RUN go install ./cmd/aws-ecr-login

FROM alpine

RUN apk add --no-cache ca-certificates
COPY --from=builder /go/bin/aws-ecr-login /usr/local/bin/aws-ecr-login

CMD [ "aws-ecr-login" ]
