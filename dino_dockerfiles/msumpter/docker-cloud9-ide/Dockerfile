FROM phusion/baseimage:0.9.19
MAINTAINER Mat Sumpter <mat@matsumpter.com>

ENV DEBIAN_FRONTEND=noninteractive \
	LANG=en_US.UTF-8 \
	TERM=xterm

LABEL org.label-schema.url="https://github.com/msumpter/docker-cloud9-ide" \
	org.label-schema.name="Cloud9 IDE (phusion-baseimage)" \
	org.label-schema.license="MIT" \
	org.label-schema.vcs-url="https://github.com/msumpter/docker-cloud9-ide" \
	org.label-schema.schema-version="1.0"

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

ADD firstrun.sh /etc/my_init.d/firstrun.sh
ADD rc.local /etc/rc.local

# Install base
RUN apt-get update \
	&& apt-get install -y --no-install-recommends build-essential g++ curl libssl-dev apache2-utils git libxml2-dev sshfs tmux python sudo \
	&& curl -sL https://deb.nodesource.com/setup_4.x | bash - \
	&& apt-get install -y nodejs \
	&& git config --global url.https://.insteadOf git:// \
	&& mkdir /workspace \
	&& useradd -m cloud9 \
	&& mkdir /var/cloud9 \
	&& chown -R cloud9:cloud9 /var/cloud9 \
	&& rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh \
	&& chmod a+x /etc/rc.local \
	&& chmod +x /etc/my_init.d/firstrun.sh


VOLUME /workspace


# Drop to cloud9 user
USER cloud9
ENV HOME /home/cloud9

# Install Cloud9
WORKDIR /var/cloud9
RUN git clone --depth 1 -b master --single-branch https://github.com/c9/core.git /var/cloud9 \
	&& scripts/install-sdk.sh \
	&& sed -i -e 's/127.0.0.1/0.0.0.0/g' /var/cloud9/configs/standalone.js

# Switch back to root
USER root

# Clean up APT, extra packages, tmp dirs, and cloud9 user
RUN apt-get remove -y --purge build-essential g++ libssl-dev libxml2-dev python \
	&& apt-get -y --purge autoremove \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
	&& userdel cloud9

# Expose ports.
EXPOSE 3000
EXPOSE 8080
