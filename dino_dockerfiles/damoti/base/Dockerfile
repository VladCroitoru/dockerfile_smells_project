FROM ubuntu:17.04

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    apt-transport-https \
    curl \
    git \
    language-pack-en \
    libffi-dev \
    libjpeg-dev \
    libpq-dev \
    libssl-dev \
    libxml2-dev \
    libxslt-dev \
    libyaml-dev \
    mercurial \
    postgresql-client \
    python3 \
    python3-dev \
    python3-pip \
    vim

RUN curl -sL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN curl -sL https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list > /etc/apt/sources.list.d/dart_stable.list
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -

RUN apt-get install -y dart nodejs

RUN npm install gulp -g

RUN pip3 install --upgrade pip wheel
RUN pip3 install --upgrade requests uwsgi fabric3

ENV PYTHONUNBUFFERED 1
ENV PATH /usr/lib/dart/bin:$PATH
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
