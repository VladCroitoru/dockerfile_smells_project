FROM fedora
MAINTAINER http://fedoraproject.org/wiki/Cloud

EXPOSE 22

RUN yum -y install \
	openssh-server \
	openssh-clients \
	openssh-clients \
	net-tools \
	telent \
	nmap-ncat \
	passwd \
	; yum clean all

#RUN  useradd user

#COPY keys/auth* /home/user/.ssh/
#COPY keys/id_rsa /home/user/.ssh/
#COPY keys/id_rsa.pub /home/user/.ssh/

RUN sed \
        -e 's/^#\?AllowTcpForwarding .*/AllowTcpForwarding remote/' \
        -i /etc/ssh/sshd_config

COPY entrypoint.sh /entrypoint.sh
COPY client.sh /client.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/usr/sbin/sshd", "-D"]
