FROM golang:1.6

RUN go get github.com/bitly/oauth2_proxy

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 4180

ENTRYPOINT /entrypoint.sh
