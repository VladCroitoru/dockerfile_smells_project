FROM alpine:latest
MAINTAINER Gerben Wiersma <gerbenwiersma21@gmail.com>
ADD rundownload.sh /
RUN apk add --no-cache git
RUN apk add --update bash && rm -rf /var/cache/apk/*
RUN ["chmod", "+x", "/rundownload.sh"]
CMD ["/rundownload.sh"]
