FROM rocker/shiny
MAINTAINER Wush Wu <wush978@gmail.com>

ENV LANG en_US.UTF-8

# compile and install R
RUN \
    locale-gen en_US.UTF-8 && \
    apt-get install -y --no-install-recommends fonts-arphic-ukai && \
    apt-get clean 

# locale
ADD locale /etc/default/locale


