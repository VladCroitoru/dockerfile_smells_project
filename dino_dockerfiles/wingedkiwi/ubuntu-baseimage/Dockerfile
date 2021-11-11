FROM ubuntu:14.04
MAINTAINER Chi Vinh Le <cvl@chinet.info>

ADD . /bd_build

RUN /bd_build/prepare.sh && \
    /bd_build/system_services.sh && \
    /bd_build/utilities.sh && \
    /bd_build/cleanup.sh

ENTRYPOINT ["/sbin/my_init", "--"]

