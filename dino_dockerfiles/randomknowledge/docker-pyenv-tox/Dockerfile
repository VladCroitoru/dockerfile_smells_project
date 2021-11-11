FROM ubuntu:16.04

MAINTAINER Florian Finke <florian@finke.email>

ENV PYTHON_VERSIONS 2.7.13 2.7.14 2.7.15 2.7.16 2.7.17 2.7.18 3.0.0 3.0.1 3.1.0 3.1.1 3.1.2 3.1.3 3.1.4 3.1.5 3.2.0 3.2.1 3.2.2 3.2.3 3.2.4 3.2.5 3.2.6 3.3.0 3.3.1 3.3.2 3.3.3 3.3.4 3.3.5 3.3.6 3.3.7 3.4.0 3.4.1 3.4.2 3.4.3 3.4.4 3.4.5 3.4.6 3.4.7 3.4.8 3.4.9 3.4.10 3.5.0 3.5.1 3.5.2 3.5.3 3.5.4 3.5.5 3.5.6 3.5.7 3.5.8 3.5.9 3.5.10 3.6.0 3.6.1 3.6.2 3.6.3 3.6.4 3.6.5 3.6.6 3.6.7 3.6.8 3.6.9 3.6.10 3.6.11 3.6.12 3.7.0 3.7.1 3.7.2 3.7.3 3.7.4 3.7.5 3.7.6 3.7.7 3.7.8 3.7.9 3.8.0 3.8.1 3.8.2 3.8.3 3.8.4 3.8.5 3.8.6 3.9.0

ENV PYENV_ROOT /pyenv/
ENV PATH /pyenv/shims:/pyenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV PYENV_INSTALLER_ROOT /pyenv-installer/
ENV PYENV_REQUIRED_PYTHON_BASENAME python_versions.txt
ENV PYENV_REQUIRED_PYTHON /pyenv-config/$PYENV_REQUIRED_PYTHON_BASENAME

RUN apt-get update -q -y
RUN apt-get install --no-install-recommends --fix-missing -y build-essential \
    python2.7 python2.7-dev git make locales \
    libssl-dev libfontconfig libffi-dev libbz2-dev libreadline-dev libsqlite3-dev \
    python-pip libjpeg-dev zlib1g-dev python-imaging libxml2-dev \
    libxslt1-dev python-lxml openssh-client \
    curl rsync ruby-dev rubygems \
    && apt-get autoremove -y \
        && apt-get clean all \
        && rm -rf /var/lib/apt/lists/*

RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
        && locale-gen \
        && update-locale LANG=en_US.UTF-8

ENV LANG=en_US.UTF-8

RUN pip install --upgrade setuptools
RUN pip install --upgrade pip
RUN pip install --upgrade tox tox-pyenv "fabric<2.0" docker-fabric awscli awsebcli

RUN mkdir -p ~/.ssh
RUN echo "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash
RUN apt-get -y install nodejs

RUN npm install -g npm@latest yarn

RUN git clone https://github.com/pyenv/pyenv.git $PYENV_ROOT

COPY python_versions.txt $PYENV_REQUIRED_PYTHON
RUN while read line; do \
    pyenv install $line || exit 1 ;\
    done < $PYENV_REQUIRED_PYTHON

RUN pyenv global $PYTHON_VERSIONS
RUN pyenv local $PYTHON_VERSIONS
