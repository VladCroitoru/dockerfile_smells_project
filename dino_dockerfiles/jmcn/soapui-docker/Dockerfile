FROM ubuntu:14.04
MAINTAINER JMcn<411164348@qq.com>

RUN apt-get update
RUN apt-get -y install software-properties-common python-software-properties
RUN add-apt-repository ppa:openjdk-r/ppa
RUN apt-get update
RUN apt-get -y install openjdk-8-jdk

RUN update-alternatives --display java
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

ADD profile /profile

#安装中文语言包
RUN sudo apt-get install -y language-pack-gnome-zh-hans
RUN sudo apt-get install -y ttf-wqy-zenhei

# 处理中文问题
ENV LANG=zh_CN.UTF-8

# 处理时区问题
RUN echo "Asia/shanghai" > /etc/timezone
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime

RUN apt-get install -y wget

RUN \
  mkdir -p /opt && \
  cd /opt && \
  wget http://cdn01.downloads.smartbear.com/soapui/5.2.1/SoapUI-5.2.1-linux-bin.tar.gz && \
  tar xf SoapUI-5.2.1-linux-bin.tar.gz
RUN echo "export PATH=/opt/SoapUI-5.2.1/bin:$PATH" >> /etc/profile

ENTRYPOINT ["/bin/bash"]
