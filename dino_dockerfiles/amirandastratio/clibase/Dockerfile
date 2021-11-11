FROM debian:stretch-slim

USER root

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
	apt-get install -y sudo vim bsdtar make sshpass python-setuptools python-pip python-dev build-essential libxml2-utils wget curl adduser iputils-ping telnet krb5-user && \
	pip install pyyaml mdv virtualenv && \
	wget -O /usr/bin/jq "https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64" && \
	chmod ugo+r+x /usr/bin/jq && \
	curl -fLsS --retry 20 -Y 100000 -y 60 https://downloads.dcos.io/binaries/cli/linux/x86-64/dcos-1.8/dcos -o dcos && \
	mv dcos /usr/local/bin && \
	chmod +x /usr/local/bin/dcos && \
	adduser --disabled-password --gecos '' cli && \
	echo 'cli ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers && \
	echo 'alias ll="ls -la"' >> /home/cli/.bashrc && \
	echo 'PATH="$HOME:$PATH"' >> /etc/profile

WORKDIR /home/cli
USER cli

ENTRYPOINT ["/home/cli/entrypoint"]
CMD ["bash"]