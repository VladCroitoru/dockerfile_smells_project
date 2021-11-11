FROM mono

MAINTAINER Heerschop

ENV TARGET_HOST 127.0.0.1
ENV PING_TIMEOUT 1000
ENV STATUS_THRESHOLD 4000

RUN apt-get update && apt-get install  -y tzdata

ADD host-ping.exe        /usr/local/bin/

CMD mono /usr/local/bin/host-ping.exe $TARGET_HOST $PING_TIMEOUT $STATUS_THRESHOLD -l /var/log/host-ping/host-ping.log
