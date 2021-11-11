FROM alpine:latest

RUN apk add --no-cache socat

EXPOSE 1234
CMD socat -t 100000000 TCP4-LISTEN:1234,fork,reuseaddr UNIX:/ssh_auth_sock
