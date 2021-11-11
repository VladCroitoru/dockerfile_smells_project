# toolbox just for fun, base ubuntu
#
# include sshd, java, mysql, node.js, golang, supervisord
# 

FROM ubuntu:14.10
MAINTAINER yinheli <me@yinheli.com>

## install wget tar git sshd mysql ...
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \
    apt-get update && apt-get install -y \
    curl vim iptables ufw telnet wget tar unzip make gcc git libc6-dev \
    mysql-server \
    supervisor && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    rm -rf /var/lib/mysql/mysql


RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    locale-gen en_US.UTF-8 && update-locale en_US.UTF-8


### install golang ###

RUN wget --progress=bar --no-check-certificate \
    -O /tmp/go.src.tar.gz \
    https://golang.org/dl/go1.4.2.linux-amd64.tar.gz && \
    cd /tmp && tar xzf go.src.tar.gz && \
    mv go /usr/local/go && \
    rm -rf go.src.tar.gz && \
    mkdir -p /data/gopath

ENV GOROOT /usr/local/go
ENV GOPATH /data/gopath


### install java ###

# download && install java
RUN wget --no-check-certificate \
    -O /tmp/jdk.tar.gz \
    --header "Cookie: oraclelicense=a" \
    http://download.oracle.com/otn-pub/java/jdk/7u72-b14/server-jre-7u72-linux-x64.tar.gz && \
    tar xzf /tmp/jdk.tar.gz && \
    mkdir -p /usr/local/jdk && \
    mv jdk1.7.0_72/* /usr/local/jdk/ && \
    rm -rf jdk1.7.0_72 && rm -f /tmp/jdk.tar.gz && \
    chown root:root -R /usr/local/jdk

ENV JAVA_HOME /usr/local/jdk


### install node.js ###

ENV NODE_VERSION 0.12.2
# ENV NODE_ENV develop
ENV NODE_ENV production

# Install nvm with node and npm
RUN rm -rf ~/.nvm && git clone https://github.com/creationix/nvm.git ~/.nvm && \
    cd ~/.nvm && git checkout `git describe --abbrev=0 --tags` && \
    echo 'source ~/.nvm/nvm.sh' >> ~/.bash_profile && \
    source ~/.bash_profile && \
    nvm install $NODE_VERSION && \
    nvm alias default $NODE_VERSION && \
    npm install -g cnpm --registry=https://registry.npm.taobao.org


### other ###

# set env
ENV PATH $PATH:$JAVA_HOME/bin:$GOROOT/bin

COPY start.sh /bin/start.sh
RUN chmod +x /bin/start.sh

CMD ["/bin/start.sh"]
