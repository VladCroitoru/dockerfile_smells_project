FROM ubuntu:20.04

ENV PYTHON_VERSION 3.9.6
ENV PYTHON_ROOT /tmp/Python/python-$PYTHON_VERSION
ENV PATH $PYTHON_ROOT/bin:$PATH
ENV PYENV_ROOT /tmp/.pyenv

WORKDIR /usr/src/app
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get install -y locales \
    && locale-gen ja_JP.UTF-8 \
    && echo "export LANG=ja_JP.UTF-8" >> ~/.bashrc \
    && apt install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libffi-dev \
    liblzma-dev \
    vim \
    ssh \
    wget \
    xz-utils \
    tk-dev \
    git \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# # Python環境構築
RUN git clone https://github.com/pyenv/pyenv.git $PYENV_ROOT
RUN $PYENV_ROOT/plugins/python-build/install.sh
RUN /usr/local/bin/python-build -v $PYTHON_VERSION $PYTHON_ROOT
RUN rm -rf $PYENV_ROOT

RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install -r requirements.txt

WORKDIR home/work
