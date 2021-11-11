FROM ubuntu:12.04
MAINTAINER bakins "brian@akins.org"
ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list && \
    echo "deb http://security.ubuntu.com/ubuntu precise-security main universe" > /etc/apt/sources.list && \
    apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*


