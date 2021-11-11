FROM alpine:latest
MAINTAINER Samuel Warkenin <unclesamwk@googlemailc.com>

RUN apk add --update git lua-dev gcc make openssl-dev pcre-dev g++ bash curl jq tzdata

# set timezone
ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /root

RUN git clone https://github.com/lefcha/imapfilter.git

WORKDIR /root/imapfilter

RUN make all
RUN make install
RUN mkdir /root/.imapfilter

ADD run.sh /run.sh

CMD bash /run.sh
