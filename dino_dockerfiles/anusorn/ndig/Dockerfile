# sshd
#
# VERSION               0.0.2

FROM ubuntu:14.04
MAINTAINER  Anusorn Tantara <atantara@comnet.in.th>

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:screencast' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
RUN apt-get -y install build-essential
RUN apt-get -y install curl wget
RUN apt-get -y install tcpdump
RUN curl ftp://ftp.isc.org/isc/bind9/9.10.2/bind-9.10.2.tar.gz|tar -xzv \
        && cd bind-9.10.2 \
        && CFLAGS="-static" ./configure --without-openssl --disable-symtable \
        && make \
        && cp ./bin/dig/dig /usr/bin/
RUN rm -rf bind-9.10.2

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
