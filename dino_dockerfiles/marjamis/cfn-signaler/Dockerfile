FROM golang:1.10.0 as building

RUN curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh && mkdir cfn-signaler

WORKDIR /go/src/cfn-signaler/

COPY Gopkg.lock .
COPY Gopkg.toml .
RUN dep ensure -vendor-only

COPY main.go /go/src/cfn-signaler/
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o entrypoint cfn-signaler



FROM alpine:3.7

RUN apk --no-cache --update upgrade && apk add --no-cache ca-certificates && update-ca-certificates

COPY --from=building /go/src/cfn-signaler/entrypoint /entrypoint
COPY ./stylesheets/* /stylesheets/
COPY ./templates/* /templates/

WORKDIR /
EXPOSE 8080
ENTRYPOINT [ "/entrypoint" ]
