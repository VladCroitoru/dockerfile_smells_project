#
# Dockerfile
#
# Copyright (c) 2015-2016 Junpei Kawamoto
#
# This software is released under the MIT License.
#
# http://opensource.org/licenses/mit-license.php
#
FROM ubuntu:latest
MAINTAINER Junpei Kawamoto <kawamoto.junpei@gmail.com>

ENV TERM vt100

# Use a cache serve for apt-get and pip if given.
ARG APT_PROXY
RUN if [ -n "$APT_PROXY" ]; then \
      echo "Set apt proxy: $APT_PROXY"; \
      echo "Acquire::http { Proxy \"$APT_PROXY\"; };" >> /etc/apt/apt.conf.d/01proxy; \
    fi

ARG PIP_PROXY
RUN if [ -n "$PYPI_PROXY" ]; then \
      echo "Set pip proxy: $PYPI_PROXY"; \
      IPPORT=${PYPI_PROXY#*//}; \
      mkdir -p ~/.pip/; \
      echo "[global]\nindex-url=$PIP_PROXY/root/pypi\ntrusted-host=${IPPORT%:*}" >> ~/.pip/pip.conf; \
      cat ~/.pip/pip.conf; \
    fi

# Install packages.
RUN apt-get update && \
    apt-get install -y unzip libssl-dev python-pip python-dev libffi-dev && \
    apt-get upgrade -y && apt-get clean && \
    rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/
RUN pip install -U pip pip-tools

## Install python packages.
ADD ./requirements.in ./
RUN pip-compile && \
    pip install -r requirements.txt && \
    rm requirements.in requirements.txt

## Install gsutil.
ADD https://storage.googleapis.com/pub/gsutil.tar.gz /tmp
RUN tar -zxvf /tmp/gsutil.tar.gz -C /usr/local
ENV PATH $PATH:/usr/local/gsutil
RUN echo "[GoogleCompute]\nservice_account = default\n[GSUtil]\nparallel_composite_upload_threshold = 150M" >> /etc/boto.cfg

# Copy entrypoint
COPY bin /root
WORKDIR /data

# Change working directory
ENTRYPOINT ["/root/entrypoint.sh"]
