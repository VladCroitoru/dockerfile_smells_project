FROM ubuntu:16.04

WORKDIR /tmp

ENV LANG C.UTF-8
ENV TERM xterm-256color

RUN apt-get update -y && apt-get install --no-install-recommends \
    wget unzip borgbackup gawk cron git python-pip rsyslog ntpdate -y

RUN ntpdate -q 2.pool.ntp.org
## install dumb-init
RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64.deb
RUN dpkg -i dumb-init_*.deb

##install jq
RUN wget https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64
RUN cp jq-linux64 /bin/jq
RUN chmod +x /bin/jq

## install consul-template
RUN wget https://releases.hashicorp.com/consul-template/0.18.1/consul-template_0.18.1_linux_amd64.zip
RUN unzip consul-template_0.18.1_linux_amd64.zip
RUN cp consul-template /bin/consul-template
RUN chmod +x /bin/consul-template

## install crontab checker 
RUN git clone https://github.com/lyda/chkcrontab.git
RUN cd chkcrontab; python setup.py install 

RUN wget http://downloads.rclone.org/rclone-v1.38-linux-amd64.zip
RUN unzip rclone-v1.38-linux-amd64.zip
RUN mv rclone-v1.38-linux-amd64/rclone /bin/rclone

RUN mkdir -p /volumes
WORKDIR /
RUN rm -rf /tmp/*
ADD bin /bin/
ADD templates /templates
RUN chmod +x -R /bin

VOLUME /volumes

ENTRYPOINT ["/bin/entrypoint.sh"]
