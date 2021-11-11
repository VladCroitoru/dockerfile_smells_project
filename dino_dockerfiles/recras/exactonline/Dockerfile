FROM golang:1.15

# Add project directory to Docker image.
ADD . /go/src/github.com/Recras/exactonline

ENV HTTP_ADDR 0.0.0.0:8888
ENV HTTP_DRAIN_INTERVAL 1s
ENV COOKIE_SECRET 4iKivAZAZORgZ3ya

WORKDIR /go/src/github.com/Recras/exactonline

ENV GOPATH /go

RUN go build ./cmd/koppeling

EXPOSE 8888
CMD ./koppeling
