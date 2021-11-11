# =============================================================================
FROM ubuntu:14.04.4


RUN apt-get update \
	&& apt-get install -y \
	sudo \
	openssh-server \
	openssh-client \
	python-setuptools \
	wget \
	&& wget https://github.com/Yelp/dumb-init/releases/download/v1.0.1/dumb-init_1.0.1_amd64.deb \
	 && dpkg -i dumb-init_*.deb && rm dumb-init_*.deb \
	&& rm -rf /var/cache/apt/*

ADD run.sh /run.sh
RUN sed -i \
	-e 's~^PasswordAuthentication yes~PasswordAuthentication no~g' \
	-e 's~^#PermitRootLogin yes~PermitRootLogin no~g' \
	-e 's~^#UseDNS yes~UseDNS no~g' \
	-e 's~^\(.*\)/usr/libexec/openssh/sftp-server$~\1internal-sftp~g' \
	/etc/ssh/sshd_config

# -----------------------------------------------------------------------------
# Enable the wheel sudoers group
# -----------------------------------------------------------------------------
# RUN sed -i 's~^# %wheel\tALL=(ALL)\tALL~%wheel\tALL=(ALL) ALL~g' /etc/sudoers

# -----------------------------------------------------------------------------
# Copy files into place
# -----------------------------------------------------------------------------
ADD usr/sbin/sshd-bootstrap /usr/sbin/sshd-bootstrap
ADD etc/services-config/ssh/authorized_keys \
	etc/services-config/ssh/sshd-bootstrap.conf \
	etc/services-config/ssh/sshd-bootstrap.env \
	/etc/services-config/ssh/

RUN cp -pf /etc/ssh/sshd_config /etc/services-config/ssh/ \
	&& ln -sf /etc/services-config/ssh/sshd_config /etc/ssh/sshd_config \
	&& ln -sf /etc/services-config/ssh/sshd-bootstrap.conf /etc/sshd-bootstrap.conf \
	&& ln -sf /etc/services-config/ssh/sshd-bootstrap.env /etc/sshd-bootstrap.env \
	&& chmod +x /usr/sbin/sshd-bootstrap /run.sh \
	&& mkdir -p /var/run/sshd


EXPOSE 22

# -----------------------------------------------------------------------------
# Set default environment variables
# -----------------------------------------------------------------------------
ENV SSH_AUTHORIZED_KEYS ""
ENV SSH_CHROOT_DIRECTORY "%h"
ENV SSH_INHERIT_ENVIRONMENT false
ENV SSH_SUDO "ALL=(ALL) ALL"
ENV SSH_USER "app-admin"
ENV SSH_USER_FORCE_SFTP false
ENV SSH_USER_HOME "/home/%u"
ENV SSH_USER_PASSWORD ""
ENV SSH_USER_PASSWORD_HASHED false
ENV SSH_USER_SHELL "/bin/bash"
ENV SSH_USER_ID "500:500"

CMD dumb-init /run.sh
