FROM ubuntu:trusty
MAINTAINER Norbert Mozsar <mozsarn@5net.hu>

# apache
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    beanstalkd \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 11300

CMD ["beanstalkd","-V","-p","11300"]
