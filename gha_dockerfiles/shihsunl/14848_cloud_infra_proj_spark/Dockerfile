FROM ubuntu:18.04
ENV DEBIAN_FRONTEND noninteractive
MAINTAINER Shih-Sung-Lin
ENV PORT 8085

RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d
ENV JAVA_HOME=/usr/lib/jdk1.8.0_211
ENV PATH=$PATH:$JAVA_HOME/bin
EXPOSE 8080 22 443 8081 8088 8085

# setup
RUN apt-get update
RUN apt-get install -y git g++ software-properties-common build-essential language-pack-en unzip curl wget vim libpam0g-dev libssl-dev cmake cron libssl-dev openssl iputils-ping openssh-server sudo
RUN apt-get install -y python3
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get install -y python3-pip
RUN pip3 install Flask==2.0.1
RUN pip3 install gunicorn==20.1.0

# install jdk
RUN mkdir /temp
RUN mkdir /temp/install
WORKDIR /temp/install
RUN wget https://github.com/frekele/oracle-java/releases/download/8u211-b12/jdk-8u211-linux-x64.tar.gz
RUN tar -zxvf jdk-8u211-linux-x64.tar.gz
RUN cp -R /temp/install/jdk1.8.0_211 /usr/lib/jdk1.8.0_211
RUN ln -s /usr/lib/jdk1.8.0_211/bin/java /etc/alternatives/java

# install spark
RUN mkdir /temp/spark
WORKDIR /temp/spark
RUN curl -L https://dlcdn.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz -o spark-3.1.2-bin-hadoop3.2.tgz
RUN tar -zxvf spark-3.1.2-bin-hadoop3.2.tgz
ENV SPARK_HOME=/temp/spark/spark-3.1.2-bin-hadoop3.2

WORKDIR /temp
RUN git clone https://github.com/shihsunl/14848_cloud_infra_proj_spark.git
RUN cp -r /temp/14848_cloud_infra_proj_spark/* /temp/
RUN cp /temp/spark/spark-3.1.2-bin-hadoop3.2/conf/spark-defaults.conf.template /temp/spark/spark-3.1.2-bin-hadoop3.2/conf/spark-defaults.conf
RUN echo "spark.ui.proxyBase: /spark" >> /temp/spark/spark-3.1.2-bin-hadoop3.2/conf/spark-defaults.conf

# ssh
RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 test
RUN echo 'test:test' | chpasswd # sets the password for the user test to test

# web terminal
WORKDIR /temp
RUN wget https://github.com/yudai/gotty/releases/download/v2.0.0-alpha.3/gotty_2.0.0-alpha.3_linux_amd64.tar.gz &&\
    tar -zxvf gotty_2.0.0-alpha.3_linux_amd64.tar.gz &&\
    echo "/temp/gotty -a 0.0.0.0 -p 8081 --ws-origin '.*' -w bash > /temp/gotty.out >2&1 &" > /temp/gotty.sh && chmod 777 /temp/*

WORKDIR /temp
CMD /etc/init.d/ssh restart && nohup /temp/gotty.sh && /temp/run.sh

