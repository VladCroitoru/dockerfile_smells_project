FROM python:3.6.1-alpine

MAINTAINER Mazedur Rahman <mazedur.rahman.liton@gmail.com>

# Adding bash to support BATS test framework based testing
RUN apk update \
	&& apk add bash \
	groff \
	less \
	py-pip

RUN python -m pip install -U pip \
	&& pip install --upgrade awscli \
	&& python -m pip uninstall -y pip \
	&& apk del py-pip

VOLUME ["~/.aws"]
CMD ["/bin/bash", "--login"]

