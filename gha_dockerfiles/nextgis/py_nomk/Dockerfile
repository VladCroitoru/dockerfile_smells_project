FROM ubuntu:bionic

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
	apt-get -y install --no-install-recommends --yes language-pack-ru \
	apt-transport-https ca-certificates curl gnupg && \
	echo "deb https://rm.nextgis.com/api/repo/11/deb bionic main" | tee -a /etc/apt/sources.list && \
	curl -s -L https://rm.nextgis.com/api/repo/11/deb/key.gpg | apt-key add - && \
	apt-get update -y && \
	apt-get -y install --no-install-recommends --yes python3 python3-pip gdal-bin python3-gdal python3-setuptools && \
	update-locale LANG=ru_RU.UTF-8 && \
	pip3 install --upgrade pip

ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU:ru
ENV LC_ALL ru_RU.UTF-8
ENV PYTHONUNBUFFERED 0

ADD . /opt/py_test

RUN pip3 install pytest
WORKDIR /opt/py_test
