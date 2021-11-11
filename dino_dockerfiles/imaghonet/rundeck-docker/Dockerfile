FROM ubuntu:14.04
ARG RUNDECK_VERSION=2.6.8


RUN apt-get update
RUN apt-get install -y openjdk-7-jre
RUN apt-get install -y \
		apt-transport-https \
		ca-certificates \
		subversion \
		git \
		python \
  	python-pip \
  	curl \
  	&& curl -sLo /usr/local/bin/ep \
		'https://github.com/kreuzwerker/envplate/releases/download/1.0.0-RC1/ep-linux' \
	&& chmod +x /usr/local/bin/ep \
	&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D \
	&& echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" > /etc/apt/sources.list.d/docker.list

RUN apt-get update
RUN apt-get install -y docker-engine \
	&& pip install docker-compose

RUN	curl -sLo /tmp/rundeck.deb http://dl.bintray.com/rundeck/rundeck-deb/rundeck-${RUNDECK_VERSION}-1-GA.deb \
	&& sudo dpkg -i /tmp/rundeck.deb \
	&& rm -f /tmp/rundeck.deb

COPY ./files /etc/rundeck
COPY rundeck.sh /rundeck.sh

RUN find /etc/rundeck -type f -exec chmod 644 {} \;;find /etc/rundeck -type d -exec chmod 755 {} \;; chown -R rundeck:rundeck /var/lib/rundeck/* \
	&& chmod +x /rundeck.sh

STOPSIGNAL SIGKILL

EXPOSE 4440

VOLUME ["/etc/rundeck", "/var/rundeck/projects", "/var/lib/rundeck/var", "/var/lib/rundeck/logs", "/opt/rundeck-plugins"]

CMD /rundeck.sh
