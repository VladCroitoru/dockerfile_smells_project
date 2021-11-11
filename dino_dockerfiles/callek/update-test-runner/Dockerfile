FROM ubuntu:vivid

RUN dpkg --add-architecture i386
RUN apt-get -q update
RUN apt-get install --yes -q \
    libc6:i386 \
    libncurses5:i386 \
    libstdc++6:i386
RUN apt-get install --yes -q \
    git \
    mercurial \
    python-dev \
    python3-dev \
    python-tox \
    pypy \
    python-pip \
    python3-pip \
    libffi-dev \
    libssl-dev \
    libyaml-dev \
    libmysqlclient-dev \
    curl \
    wget \
    libgtk2.0-0 \
    libgtk2.0-0:i386 \
    libgtk-3-0 \
    libgtk-3-0:i386 \
    && apt-get clean
