FROM ubuntu:18.04

RUN apt-get update && apt-get install -y libjpeg-dev curl git-core \
    build-essential make libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev pkg-config libffi-dev \
    && rm -rf /var/lib/apt/lists/*

COPY install.sh /install.sh
ADD PYTHON_VERSIONS /PYTHON_VERSIONS
RUN /bin/bash /install.sh && rm /install.sh /PYTHON_VERSIONS

ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
