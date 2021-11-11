FROM alpine:3.3
MAINTAINER Simen Huuse - itelligence / NTT Data 
LABEL Simen Huuse - itelligence / NTT Data 

RUN apk add --update darkhttpd && rm -rf /var/cache/apk/*

ADD index.html /var/www/localhost/htdocs/index.html
ADD entrypoints.sh /entrypoints.sh

EXPOSE 443

ENTRYPOINT ["/entrypoints.sh"]