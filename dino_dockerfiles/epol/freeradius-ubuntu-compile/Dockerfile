FROM ubuntu:xenial
MAINTAINER Enrico Polesel <epol@autistici.org>

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -qq install git devscripts quilt equivs debhelper fakeroot

COPY getsource.sh /root/
COPY compile.sh /root/
COPY getdeb.sh /root/
COPY all.sh /root/

CMD /root/all.sh
VOLUME /packages/