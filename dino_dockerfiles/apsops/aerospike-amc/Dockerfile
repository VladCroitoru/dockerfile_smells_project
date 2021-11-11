FROM busybox
MAINTAINER Amanpreet Singh<aps.sids@gmail.com>

ENV AMC_VERSION 4.0.13
RUN wget -O aerospike-amc-community-${AMC_VERSION}-linux.tar.gz https://www.aerospike.com/download/amc/${AMC_VERSION}/artifact/linux && \
    tar xvzf aerospike-amc-community-${AMC_VERSION}-linux.tar.gz && \
    rm -rf aerospike-amc-community-${AMC_VERSION}-linux.tar.gz

EXPOSE 8081

CMD ["/opt/amc/amc"]

