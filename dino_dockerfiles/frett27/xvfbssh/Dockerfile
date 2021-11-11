FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

ENV DISPLAY=0
ENV SCREEN=0
ENV DISPLAY_MODE=1024x768x16

EXPOSE 6000:6000

COPY xvfbssh.sh /usr/local/bin/
RUN chmod ug+x /usr/local/bin/xvfbssh.sh

RUN apt-get update
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd

RUN echo 'root:root' |chpasswd

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

EXPOSE 22

ENTRYPOINT ["/usr/local/bin/xvfbssh.sh"]
