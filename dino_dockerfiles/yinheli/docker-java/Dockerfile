# pure java env base ubuntu
#
# include java
# 

FROM ubuntu:14.10
MAINTAINER yinheli <me@yinheli.com>

## install wget tar git sshd mysql ...
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \
    apt-get update && apt-get install -y \
    curl vim iptables telnet wget tar unzip make git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    locale-gen en_US.UTF-8 && update-locale en_US.UTF-8


### install java ###

# download && install java
RUN wget --no-check-certificate \
    -O /tmp/jdk.tar.gz \
    --header "Cookie: oraclelicense=a" \
    http://download.oracle.com/otn-pub/java/jdk/8u31-b13/jdk-8u31-linux-x64.tar.gz && \
    tar xzf /tmp/jdk.tar.gz && \
    mkdir -p /usr/local/jdk && \
    mv jdk1.8.0_31/* /usr/local/jdk/ && \
    rm -rf jdk1.8.0_31 && rm -f /tmp/jdk.tar.gz && \
    chown root:root -R /usr/local/jdk

ENV JAVA_HOME /usr/local/jdk

# set env
ENV PATH $PATH:\$JAVA_HOME/bin

CMD ["bash"]
