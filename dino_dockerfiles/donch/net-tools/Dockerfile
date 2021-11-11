FROM alpine:3.3
MAINTAINER David Donchez <david.donchez@gmail.com>


# Installing some net tools
RUN apk add --no-cache mtr
RUN apk add --no-cache netcat-openbsd
RUN apk add --no-cache wget
RUN apk add --no-cache curl
RUN apk add --no-cache bash
RUN apk add --no-cache htop
RUN apk add --no-cache tcpdump
RUN apk add --no-cache nmap
RUN apk add --no-cache iperf
RUN apk add --no-cache openssh-client
RUN apk add --no-cache postgresql-client
RUN apk add --no-cache mysql-client
#RUN apk add wrk --update-cache --repository http://dl-8.alpinelinux.org/alpine/edge/testing/ --allow-untrusted
RUN rm -rf /var/cache/apk/*

# Add static dig binary
ADD dig /usr/local/bin/dig
