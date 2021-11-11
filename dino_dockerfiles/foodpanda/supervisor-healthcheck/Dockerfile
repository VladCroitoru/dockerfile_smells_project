FROM golang:1.7-onbuild

ENV HOST=localhost \
	PORT=9001

EXPOSE 8080

COPY . /go/src/app

RUN go get -d -v \
	&& go install -v
