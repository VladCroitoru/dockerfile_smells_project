FROM ubuntu:14.04
ENV DEBIAN_FRONTEND noninteractive
ENV PATH /usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# update apt
RUN apt-get update
RUN apt-get -y dist-upgrade
RUN apt-get install -y beanstalkd

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

VOLUME ["/data"]
EXPOSE 11300
CMD ["/usr/bin/beanstalkd", "-f", "60000", "-b", "/data"]
