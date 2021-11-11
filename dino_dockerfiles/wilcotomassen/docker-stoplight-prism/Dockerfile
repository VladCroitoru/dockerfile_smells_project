# Stoplight.io Prism
#
# VERSION 0.1.0

FROM alpine:3.5
MAINTAINER Wilco Tomassen <wilco@wilcotomassen.nl>

RUN apk add --no-cache curl
RUN curl https://raw.githubusercontent.com/stoplightio/prism/master/install.sh | sh

ENTRYPOINT ["prism"]
