FROM ubuntu:18.04
MAINTAINER Filipe Silva <silvam.filipe@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# System update
RUN apt-get update && apt-get upgrade -y

# Intall python-sphinx
RUN set -eux; \
    apt-get install curl python-setuptools python-dev python-pip build-essential gosu -y; \
    rm -rf /var/lib/apt/lists/*; \
    gosu nobody true

RUN pip install -U Sphinx sphinx-autobuild sphinxcontrib-phpdomain

# Create the user sphinx
RUN useradd -ms /bin/bash -d /docs sphinx

WORKDIR /docs
