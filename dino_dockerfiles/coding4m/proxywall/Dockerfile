FROM python:2.7-slim
MAINTAINER coding4m@gmail.com

RUN apt-get update && apt-get install -y --no-install-recommends \
		gcc \
		python-dev \
	&& rm -rf /var/lib/apt/lists/*

ADD . /var/proxywall/
RUN cd /var/proxywall/ && python setup.py install && apt-get autoremove -y gcc python-dev