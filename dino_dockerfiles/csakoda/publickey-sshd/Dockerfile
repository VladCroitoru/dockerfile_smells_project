FROM       ubuntu:14.04
MAINTAINER Chuck Sakoda <cms235@gmail.com>

RUN apt-get update

RUN apt-get install -y openssh-server
RUN apt-get install curl vim dnsutils jq -y
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN mkdir /var/run/sshd
RUN curl https://get.docker.com/builds/Linux/x86_64/docker-1.6.2 -o /usr/bin/docker
RUN chmod +x /usr/bin/docker

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

EXPOSE 22
ENV PUBLIC_KEY ""
RUN mkdir /root/.ssh

ADD config_and_run.sh /root/
CMD ["/root/config_and_run.sh"]
