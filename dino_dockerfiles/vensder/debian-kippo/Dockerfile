FROM debian:buster-slim

MAINTAINER vensder vensder@gmail.com

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
	python-pip \
	python-setuptools \
	python-dev \
	python-pyasn1 \
	build-essential \
	git \
	ca-certificates \
	--no-install-recommends && \
update-ca-certificates && \
pip install twisted==15.1.0 && \
pip install pycrypto && \
useradd -d /home/kippo -s /bin/bash -m kippo && \
cd /home/kippo && \
git clone https://github.com/desaster/kippo.git tmp && \
mv tmp/* . && rm -rf tmp/ && \
apt-get autoremove -y git python-pip python-setuptools python-dev build-essential && \
cd /home/kippo && \
mv kippo.cfg.dist kippo.cfg && \
rm -rf /home/kippo/.git && \
chown -R kippo:kippo /home/kippo && \
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV HOME /home/kippo

EXPOSE 2222
USER kippo
WORKDIR /home/kippo
CMD ["twistd", "--nodaemon", "-y", "kippo.tac", "--pidfile=kippo.pid"]
