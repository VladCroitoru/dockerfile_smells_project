FROM hypoport/httpd-cgi

MAINTAINER Hypoport

RUN apk add --no-cache curl jq

ADD query /usr/local/apache2/cgi-bin/
ADD search /usr/local/apache2/cgi-bin/
ADD annotations /usr/local/apache2/cgi-bin/
ADD default /usr/local/apache2/cgi-bin/

