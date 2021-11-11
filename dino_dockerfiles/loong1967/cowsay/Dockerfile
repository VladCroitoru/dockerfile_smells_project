# Cowsay Container - v0.6
FROM alpine:3.6

MAINTAINER loong1967@loong.org 

RUN apk add --no-cache perl 

COPY cowsay /usr/bin/cowsay 
COPY default.cow /usr/share/cowsay/default.cow 

CMD ["/usr/bin/cowsay","Docker is very good !"] 
