FROM ubuntu:trusty
MAINTAINER Fernando Mayo <fernando@tutum.co>, Liverbool "nukboon@gmail.com"

# Install packages
RUN locale-gen en_US.UTF-8
RUN export LANG=en_US.UTF-8
RUN export LC_ALL=en_US.UTF-8

RUN echo 'Asia/Bangkok' | sudo tee /etc/timezone

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv C7917B12 && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y redis-server pwgen && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add scripts
ADD run.sh /run.sh

ENV REDIS_PASS **Random**
ENV REDIS_DIR /data
VOLUME ["/data"]

EXPOSE 6379
CMD ["/run.sh"]
