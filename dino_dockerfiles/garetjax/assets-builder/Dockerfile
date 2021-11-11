FROM ubuntu:14.04
MAINTAINER Jonathan Stoppani "jonathan.stoppani@wsfcomp.com"

ENV DEBIAN_FRONTEND noninteractive
RUN /usr/sbin/locale-gen en_US.UTF-8 && \
	/usr/sbin/update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN /usr/bin/apt-get update && /usr/bin/apt-get -y upgrade

RUN /usr/bin/apt-get install -y \
		build-essential \
		rubygems1.9.1 libffi-dev ruby1.9.1-dev \
		coffeescript

RUN /usr/bin/gem install --no-rdoc --no-ri \
		compass \
		bootstrap-sass \
		guard \
		guard-livereload \
		guard-compass \
		guard-coffeescript \
		guard-coffeedripper

WORKDIR /src
EXPOSE 35729
CMD ["guard"]
