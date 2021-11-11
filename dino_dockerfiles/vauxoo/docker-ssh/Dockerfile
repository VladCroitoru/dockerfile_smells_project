FROM ubuntu:14.04
MAINTAINER Jesus Zapata <jesus@vauxoo.com>

# Configure locale
RUN locale-gen en_US.UTF-8; update-locale LANG=en_US.UTF-8 LANGUAGE=en_US.UTF-8 LC_ALL=en_US.UTF-8;
RUN echo 'LANG="en_US.UTF-8"' > /etc/default/locale

# Install OpenSSH
RUN apt-get update && apt-get upgrade -y && apt-get install -y openssh-server git

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
