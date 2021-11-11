FROM ubuntu:14.04

# Install extra packages.
RUN gpg --keyserver keyserver.ubuntu.com --recv-key 7D15AC5748C4321C
RUN gpg -a --export 48C4321C | apt-key add -
RUN set -x \
    && apt-get update --quiet \
    && apt-get dist-upgrade --quiet --yes --no-install-recommends \
    && apt-get install --quiet --yes --no-install-recommends \
	openssh-server \
	rsync  \
	htop

RUN adduser --home=/home/daintree --gecos "" daintree
RUN echo 'daintree:Password1' | chpasswd

# Extra environment.
ENV TERM xterm

EXPOSE 22

CMD /bin/sh -c 'chown -R daintree:daintree /home/daintree && mkdir -p /var/run/sshd && /usr/sbin/sshd -D'
