FROM       centos:latest
MAINTAINER loutian "loutian@gmail.com"

RUN yum install -y openssh-server vim wget mysql
RUN yum groupinstall -y "Minimal Install"
RUN yum groupinstall -y "Development Tools"

WORKDIR /tmp/

RUN wget https://cmake.org/files/v3.4/cmake-3.4.3.tar.gz
RUN tar xvzf cmake-3.4.3.tar.gz

WORKDIR /tmp/cmake-3.4.3

RUN ./bootstrap && make -j8  && make install

WORKDIR /tmp/
RUN /bin/rm -rf cmake*

WORKDIR /root/

RUN        ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN        ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key

RUN echo 'root:123456' |chpasswd

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

EXPOSE 22

CMD    ["/usr/sbin/sshd", "-D"]
