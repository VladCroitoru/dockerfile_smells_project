FROM ubuntu:xenial
LABEL maintainer="wale soyinka <wsoyinka@gmail.com>"

#MAINTAINER wale soyinka <wsoyinka@gmail.com>

ENV TERM=xterm-256color

# Set dpkg mirror to closer Canadian mirror in sources.list

#RUN sed -i "s/http:\/\/archive./http:\/\/ca.archive./g" /etc/apt/sources.list

RUN	apt-get update && \
	apt-get install -y \
	-o APT:Install-Recommend=false -o APT::Install-Suggests=false \
	python python-virtualenv libpython2.7 libmysqlclient-dev

RUN	virtualenv /appenv && \
	. /appenv/bin/activate && \
	pip install pip --upgrade

ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
  
LABEL application=remindmebackend
