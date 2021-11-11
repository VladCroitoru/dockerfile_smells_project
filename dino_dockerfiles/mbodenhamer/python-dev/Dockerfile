FROM debian:stretch
MAINTAINER Matt Bodenhamer <mbodenhamer@mbodenhamer.com>

# Install pyenv dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    libbz2-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libssl-dev \
    libreadline-dev \
    libsqlite3-dev \
    llvm \
    python-dev \
    python-pip \
    wget \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -U \
    depman \
    pip \
    PyYAML \
    setuptools \
    && rm -rf .cache/pip

# Install pyenv
ENV HOME /root
ENV PYENVPATH $HOME/.pyenv
ENV PATH $PYENVPATH/shims:$PYENVPATH/bin:$PATH
RUN curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

# Setup docker app
RUN mkdir /setup
COPY .bashrc /root/.bashrc
COPY bin/ /usr/local/bin/
COPY docker-entrypoint.sh /docker-entrypoint.sh

ENV BE_UID=1000 BE_GID=1000

VOLUME /app
WORKDIR /app
ENTRYPOINT ["/docker-entrypoint.sh"]

ONBUILD ARG reqs=requirements.yml
ONBUILD ARG versions=2.7.14,3.6.2
ONBUILD ENV PYVERSIONS=$versions

ONBUILD RUN pyversions $versions

ONBUILD COPY $reqs /setup/requirements.yml
ONBUILD RUN depman -f /setup/requirements.yml satisfy all
