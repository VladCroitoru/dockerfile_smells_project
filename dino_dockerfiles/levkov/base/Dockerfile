FROM ubuntu:14.04
MAINTAINER levkov
ENV DEBIAN_FRONTEND noninteractive
RUN locale-gen en_US.UTF-8

RUN apt-get update &&\
    apt-get install -y software-properties-common \
                       apt-transport-https \
                       supervisor \ 
                       curl \
                       wget \
                       openssh-server \
                       vim && \
    mkdir -p /var/run/sshd &&\
    mkdir -p /var/log/supervisor && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN echo 'root:ContaineR' | chpasswd

RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

COPY conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY conf/sshd.conf /etc/supervisor/conf.d/sshd.conf

EXPOSE 22 9001
CMD ["/usr/bin/supervisord"]
