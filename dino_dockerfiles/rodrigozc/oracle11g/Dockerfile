FROM sath89/oracle-xe-11g
MAINTAINER Rodrigo Zampieri Castilho <rodrigo.zampieri@gmail.com>

RUN apt-get update
RUN apt-get -y install software-properties-common
RUN apt-get -y install build-essential openssh-server sudo man vim whois zip git

RUN mkdir /var/run/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

WORKDIR /tmp
RUN git clone https://github.com/rodrigozc/oracle11g
RUN cp -f /tmp/oracle11g/entrypoint.sh /
RUN rm -Rf /tmp/oracle11g

USER root
WORKDIR /

RUN usermod -a -G sudo oracle
RUN echo 'oracle:welcome1' | chpasswd

EXPOSE 22

ENTRYPOINT ["/entrypoint.sh"]
CMD [""]
