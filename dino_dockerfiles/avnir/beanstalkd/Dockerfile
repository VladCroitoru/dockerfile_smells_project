FROM ubuntu:latest
MAINTAINER Avni Rexhepi <arexhepi@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV PATH /usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN apt-get update && \
    apt-get install -y \
            beanstalkd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

VOLUME ["/data"]

EXPOSE 11300

CMD ["/usr/bin/beanstalkd", "-f", "60000", "-b", "/data"]