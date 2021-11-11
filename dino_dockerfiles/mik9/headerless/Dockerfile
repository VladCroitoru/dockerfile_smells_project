FROM golang:alpine

STOPSIGNAL SIGKILL
ENTRYPOINT /usr/app/headerless
EXPOSE 8000
ENV GOPATH="/usr/app"

COPY main.go bare.go /usr/app/src/headerless/
RUN apk add --no-cache git
RUN cd /usr/app/src/headerless && go get && go build -o /usr/app/headerless && rm main.go && rm -r /usr/app/src && apk del git
