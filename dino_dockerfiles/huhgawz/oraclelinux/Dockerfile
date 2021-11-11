FROM oraclelinux

MAINTAINER Huhgawz <huhgawz@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN yum update -y \
    && yum install -y nano unzip \
    && yum clean all \
    && rm -rf /var/cache/yum/*
