FROM ubuntu
MAINTAINER hobbyqhd “liubingxin1030@outlook.com”
ENV REFRESHED_AT 2017_06_17

RUN apt-get update
RUN apt-get -y install redis-server redis-tools
EXPOSE 6379
ENTRYPOINT ["/usr/bin/redis-server"]
CMD []
