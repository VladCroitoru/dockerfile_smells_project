FROM ubuntu:14.04
MAINTAINER levkov
ENV DEBIAN_FRONTEND noninteractive
RUN locale-gen en_US.UTF-8
 
RUN apt-get update
RUN apt-get install vim -y
RUN apt-get install openssh-server -y
RUN apt-get install supervisor -y
RUN apt-get install wget -y
RUN mkdir -p /var/run/sshd /var/log/supervisor
RUN echo 'root:borg1979' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY dfg.sh /usr/local/bin/dfg.sh
RUN  chmod +x /usr/local/bin/dfg.sh

RUN wget https://dl.influxdata.com/influxdb/releases/influxdb_0.13.0_amd64.deb
RUN dpkg -i influxdb_0.13.0_amd64.deb

EXPOSE 22 9001 8083 8086
CMD ["/usr/bin/supervisord"]
