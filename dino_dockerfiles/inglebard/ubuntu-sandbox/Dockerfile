FROM ubuntu:focal

LABEL maintainer "David 'Inglebard' RICQ <davidricq87@orange.fr>"

ENV USER_PASSWD="ubuntu"
ENV ROOT_PASSWD="ubuntu"
ENV FTP_PORT_PASS_START="49000"
ENV FTP_PORT_PASS_END="49010"

RUN apt-get update \
&& apt-get install -y openssh-server mysql-client proftpd openssl


RUN mkdir /var/run/sshd \
&& useradd --shell /bin/bash --create-home user \
&& echo 'root:${ROOT_PASSWD}' | chpasswd \
&& echo 'user:${USER_PASSWD}' | chpasswd \
&& sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
&& sed -i 's/root//' /etc/ftpusers \
&& printf "<Global>\n\
	PassivePorts ${FTP_PORT_PASS_START} ${FTP_PORT_PASS_END}\n\
</Global>\n" > /etc/proftpd/conf.d/global-dynamic.conf



EXPOSE 21 22 23
#EXPOSE 21 22 23 ${FTP_PORT_PASS_START}-${FTP_PORT_PASS_END} # FTP port are useless because must be 1:1


COPY entrypoint.sh /entrypoint.sh
COPY global.conf /etc/proftpd/conf.d/global.conf
COPY sftp.conf /etc/proftpd/conf.d/sftp.conf

ENTRYPOINT ["sh", "/entrypoint.sh"]
