FROM phusion/baseimage:0.9.18
MAINTAINER Morton Jonuschat <m.jonuschat@mojocode.de>

ADD ./stack/build.sh /tmp/build.sh
ADD ./services/jira /etc/service/jira
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive /tmp/build.sh

EXPOSE 5000
