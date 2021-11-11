FROM ubuntu:14.04
RUN echo "server 172.17.42.1" > /etc/resolv.conf
RUN echo "server 8.8.8.8" >> /etc/resolv.conf
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install nginx wget unzip syslogd dnsutils curl jq git
RUN wget https://dl.bintray.com/mitchellh/consul/0.5.0_linux_amd64.zip -P /usr/local/src/
RUN unzip /usr/local/src/0.5.0_linux_amd64.zip -d /usr/local/bin/
RUN mkdir -p /opt/consul/conf
RUN mkdir -p /opt/consul/dat
RUN mkdir -p /opt/consul/webui
RUN mkdir -p /opt/consul/scripts
RUN wget https://dl.bintray.com/mitchellh/consul/0.5.0_web_ui.zip -P /usr/local/src/
RUN unzip /usr/local/src/0.5.0_web_ui.zip -d /opt/consul/webui/
RUN git clone https://github.com/bsmile/consul-handson.git /opt/consul/git
RUN mv /opt/consul/git/opt/consul/scripts/* /opt/consul/scripts/
RUN mv /opt/consul/git/opt/consul/conf/* /opt/consul/conf/
RUN chmod +x /opt/consul/scripts/*.sh