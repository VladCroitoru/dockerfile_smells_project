FROM docker.io/cevich/handy_ubuntu:latest
MAINTAINER cevich@redhat.com
ENV container="docker"
ADD ["/Dockerfile", "/more_pre_installed_debs", "/root/"]
RUN apt-get update -qq && \
    cat /root/more_pre_installed_debs | xargs apt-get install -qq && \
    apt-get clean
