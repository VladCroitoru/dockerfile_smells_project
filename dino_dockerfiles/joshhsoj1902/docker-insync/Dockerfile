FROM debian:jessie
MAINTAINER Christophe Burki, christophe.burki@gmail.com

# install system requirements
RUN apt-get update && apt-get install -y --no-install-recommends \
    locales \
    wget && \
    apt-get autoremove -y

RUN echo "deb http://apt.insynchq.com/ubuntu trusty non-free contrib" > /etc/apt/sources.list.d/insync.list && \
    wget --no-check-certificate -O - https://d2t3ff60b2tol4.cloudfront.net/services@insynchq.com.gpg.key | apt-key add - && \
    apt-get update && apt-get install -y --no-install-recommends \
    insync-headless

# configure locales and timezone
RUN locale-gen en_US.UTF-8 && \
    cp /usr/share/zoneinfo/US/Eastern /etc/localtime && \
    echo "US/Eastern" > /etc/timezone

# s6 install and config
COPY bin/* /usr/bin/
COPY configs/etc/s6 /etc/s6/
RUN chmod a+x /usr/bin/s6-* && \
    chmod a+x /etc/s6/.s6-svscan/finish /etc/s6/insync/run /etc/s6/insync/finish

# install scripts
COPY scripts/* /usr/local/bin/
RUN chmod a+x /usr/local/bin/*

CMD ["/usr/bin/s6-svscan", "/etc/s6"]
