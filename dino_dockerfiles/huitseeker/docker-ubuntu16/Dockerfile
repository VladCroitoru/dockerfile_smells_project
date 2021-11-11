FROM ubuntu:16.04
MAINTAINER François Garillot <francois@garillot.net>

RUN find /etc/systemd/system \
         /lib/systemd/system \
         -path '*.wants/*' \
         -not -name '*journald*' \
         -not -name '*systemd-tmpfiles*' \
         -not -name '*systemd-user-sessions*' \
         -exec rm \{} \;

RUN systemctl set-default multi-user.target

RUN apt-get update && apt-get install -y openssh-server python-all
RUN mkdir /var/run/sshd
RUN echo 'root:docker.io' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN systemctl enable ssh.service

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
COPY setup /sbin/

CMD ["/sbin/init"]
