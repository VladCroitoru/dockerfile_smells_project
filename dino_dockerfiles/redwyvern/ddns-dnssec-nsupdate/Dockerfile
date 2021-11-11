FROM docker.artifactory.weedon.org.au/redwyvern/runit
MAINTAINER Nick Weedon <nick@weedon.org.au>
RUN apt-get update && apt-get install --no-install-recommends -y \
    heirloom-mailx \
    curl \
    dnsutils \
    rsyslog

COPY ./etc /etc
COPY ./usr /usr
