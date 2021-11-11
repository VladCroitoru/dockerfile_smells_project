FROM golang:1

RUN curl https://glide.sh/get | sh
ADD . /go/src/github.com/prismatik/notify

WORKDIR /go/src/github.com/prismatik/notify

RUN glide install
RUN go install github.com/prismatik/notify
RUN touch .env

CMD /go/bin/notify
