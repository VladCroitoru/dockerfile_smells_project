FROM debian:wheezy

ADD . /docker-registry-ui
RUN \
	echo deb http://http.debian.net/debian wheezy-backports main >> /etc/apt/sources.list \
	&& echo 'APT::Install-Recommends "0";' > /etc/apt/apt.conf.d/99norecommends \
	&& sed -i 's/deb/deb [arch=amd64]/' /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get -t wheezy-backports -f -y dist-upgrade \
	&& apt-get -t wheezy-backports -f -y upgrade \
	&& apt-get -t wheezy-backports install -y python-flask python-dateutil \
	&& apt-get clean \
	&& rm /var/lib/apt/lists/*.*

EXPOSE 8080
CMD ["/usr/bin/python", "/docker-registry-ui/run.py"]
