FROM ubuntu:xenial
MAINTAINER Dmitry Ukov

ENV DEBIAN_FRONTEND=noninteractive LC_ALL=C.UTF-8 LANG=C.UTF-8 PIP_INDEX_URL=${pip_index_url:-https://pypi.python.org/simple/}

COPY .git            /project/.git
COPY containerizarion/files/entrypoint.sh /entrypoint.sh

RUN set -x \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
    apt-transport-https \
    ca-certificates \
  && apt-get update \
  && apt-get -o Dpkg::Options::="--force-confmiss" install -y --reinstall netbase \
  && apt-get install -y --no-install-recommends \
    build-essential \
    python \
    python-dev \
    python-pip \
    git \
    wget \
    libleveldb-dev \
  && pip --no-cache-dir --disable-pip-version-check install 'setuptools==32.3.1' \
  && cd /project \
  && git reset --hard \
  && pip install --no-cache-dir --disable-pip-version-check -r /project/requirements.txt \
  && pip install --no-cache-dir --disable-pip-version-check /project \
  && apt-get purge -y git python-pip python-dev \
  && apt-get clean \
  && apt-get autoremove --purge -y \
  && cd / \
  && rm -r /project \
  && rm -r /var/lib/apt/lists/*

ENTRYPOINT ["/entrypoint.sh"]
