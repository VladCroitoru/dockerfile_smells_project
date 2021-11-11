FROM debian:jessie

RUN apt-get update && \
    apt-get install -y $buildDeps \
	git \
	make \
	python-pip \
	python3-pip \
	python3-setuptools \
	python-setuptools \
	python3-dev \
	python-dev \
	iptables \
 && rm -rf /var/lib/apt/lists/*
 
RUN pip3 install -e git+https://github.com/fail2ban/fail2ban.git#egg=fail2ban && \
	pip install -e git+https://github.com/fail2ban/fail2ban.git#egg=fail2ban && \
	mkdir /var/run/fail2ban && \
	mkdir /var/lib/fail2ban && \
	cd /src/fail2ban && \
	cp files/debian-initd /etc/init.d/fail2ban && \
	cp -r config /etc/fail2ban && \
	update-rc.d fail2ban defaults
 
ADD entrypoint.sh /entrypoint.sh

CMD ["/src/fail2ban/bin/fail2ban-client", "start"]
CMD ["/usr/bin/tail", "-f", "/dev/null"]