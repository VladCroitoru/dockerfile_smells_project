FROM debian:latest
MAINTAINER polandj


RUN apt-get update && apt-get -y install openssh-server

RUN echo "Welcome to Debian! (polandj/debian-ssh image)" > /etc/motd

RUN echo "PubkeyAcceptedKeyTypes=+ssh-dss" > /etc/ssh/ssh_config

RUN echo "Protocol 2" > /etc/ssh/sshd_config \
	&& echo "PasswordAuthentication no" >> /etc/ssh/sshd_config \
	&& echo "ChallengeResponseAuthentication no" >> /etc/ssh/sshd_config \
	&& echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config \
	&& echo "HostKey /etc/ssh/ssh_host_ed25519_key" >> /etc/ssh/sshd_config \
	&& echo "HostKey /etc/ssh/ssh_host_rsa_key" >> /etc/sshd_config

RUN echo "KexAlgorithms curve25519-sha256@libssh.org,diffie-hellman-group-exchange-sha256" >> /etc/ssh/sshd_config
RUN echo "Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr" >> /etc/ssh/sshd_config
RUN echo "MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-512,hmac-sha2-256,umac-128@openssh.com" >> /etc/ssh/sshd_config

ADD run.sh /run.sh
RUN chmod +x /*.sh

EXPOSE 22
CMD ["sh", "/run.sh"]
