FROM alpine:3.5

MAINTAINER Jannik Winkel <jannik.winkel@kiney.de>

ENV VERSION "1"

RUN apk add --no-cache build-base linux-headers

COPY . /opt/rowhammer-test
RUN cd /opt/rowhammer-test && ./make.sh

CMD /opt/rowhammer-test/rowhammer_test
