FROM ubuntu:14.04
MAINTAINER mayacher
ENV DEBIAN_FRONTEND noninteractive
ENV NOTVISIBLE "in users profile" 
RUN locale-gen en_US.UTF-8


RUN apt-get update && apt-get upgrade -y && \
    rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*

RUN apt-get update && apt-get install supervisor wget openssh-server -y && \
    mkdir -p /var/run/sshd /var/log/supervisor && \
    echo 'root:grafana' | chpasswd && \
    sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd && \
    echo "export VISIBLE=now" >> /etc/profile && \
    rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*

RUN cd /root && wget https://grafanarel.s3.amazonaws.com/builds/grafana_2.0.2_amd64.deb && \
    apt-get update && apt-get install -y adduser libfontconfig && \
    dpkg -i /root/grafana_2.0.2_amd64.deb && \
    apt-get install postgresql -y && \
    rm -rf /var/lib/apt/lists/* && rm -rf /tmp/* 


COPY conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY conf/grafana.ini /etc/grafana/grafana.ini

VOLUME ["/grafana", "/usr/share/grafana/public"]

EXPOSE 9001 80 22
CMD ["/usr/bin/supervisord"]
