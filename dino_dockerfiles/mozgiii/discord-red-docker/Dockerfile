FROM debian:stretch

RUN apt-get update \
 && apt-get install -y \
      build-essential \
      libssl-dev \
      libffi-dev \
      git \
      ffmpeg \
      libopus-dev \
      unzip \
      wget \
      zlib1g-dev \
 && rm -rf /var/lib/apt/lists/*

ARG PYTHON_VERSION=3.6.3

RUN mkdir -p /python \
 && cd /python \
 && wget "https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz" \
 && tar xvf "Python-$PYTHON_VERSION.tgz" \
 && cd "Python-$PYTHON_VERSION" \
 && ./configure --enable-optimizations \
 && make "-j$(nproc)" \
 && make altinstall \
 && rm -rf /python

ARG PYTHON_EXECUTABLE=python3.6
ENV PYTHON_EXECUTABLE="$PYTHON_EXECUTABLE"

RUN wget https://bootstrap.pypa.io/get-pip.py \
 && "$PYTHON_EXECUTABLE" get-pip.py

RUN git clone -b develop --single-branch \
      https://github.com/Cog-Creators/Red-DiscordBot.git \
      /usr/src \
 && cd /usr/src \
 && "$PYTHON_EXECUTABLE" -m pip install -r requirements.txt
WORKDIR /usr/src
COPY run /usr/local/bin/
CMD run
