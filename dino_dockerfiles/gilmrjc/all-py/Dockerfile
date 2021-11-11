FROM ubuntu:14.04
MAINTAINER Gildardo Maravilla <gilmrjc@gmail.com>

RUN set -x \
    && pythonVersions='python2.7 python3.3 python3.4 python3.5' \
    && apt-get update \
    && apt-get install -y --no-install-recommends software-properties-common \
    && apt-get install -y --no-install-recommends make build-essential \
    && apt-get install -y --no-install-recommends libssl-dev zlib1g-dev \
    && apt-get install -y --no-install-recommends libbz2-dev libreadline-dev \
    && apt-get install -y --no-install-recommends libsqlite3-dev wget curl \
    && apt-get install -y --no-install-recommends curl llvm \
    && apt-get install -y --no-install-recommends libncurses5-dev xz-utils \
    && apt-get install -y --no-install-recommends git \
    && export PYENV_ROOT="$HOME/.pyenv" \
    && git clone --depth 1 https://github.com/yyuu/pyenv.git "$PYENV_ROOT" \
    && export PATH="$HOME/.pyenv/bin:$PATH" \
    && eval "$(pyenv init -)" \
    && pyenv install -s 2.7.12 \
    && pyenv install -s 3.5.2 \
    && pyenv install -s 3.4.5 \
    && pyenv install -s 3.3.6 \
    && pyenv install -s pypy-4.0.1 \
    && pyenv rehash \
    && pyenv global 2.7.12 3.5.2 3.4.5 3.3.6 pypy-4.0.1 \
    && apt-get remove -y --no-install-recommends libssl-dev zlib1g-dev \
    && apt-get remove -y --no-install-recommends libbz2-dev libreadline-dev \
    && apt-get remove -y --no-install-recommends libsqlite3-dev wget curl \
    && apt-get remove -y --no-install-recommends curl llvm \
    && apt-get remove -y --no-install-recommends libncurses5-dev xz-utils \
    && apt-get remove -y --no-install-recommends git \
    && apt-get install -y --no-install-recommends libtiff5-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk \
    && apt-get purge -y --auto-remove software-properties-common \
    && rm -rf /var/lib/apt/lists/*

CMD bash
