FROM fedora:latest

RUN set -x \
	&& yum install -y \
		pandoc \
		python2

RUN set -x \
	pip --no-cache-dir install --upgrade awscli

RUN yum clean all
