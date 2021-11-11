FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Oslo

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    python3-pip \
    python3-venv \
    libpq-dev \
    libssl-dev \
    libffi-dev \
    libpython3-dev \
    gnupg2 \
    wget \
    unzip \
    curl \
    git \
    vim

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Install chromedriver
RUN apt-get update && apt-get install -y \
    google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

ENV VIRTUAL_ENV /data/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH $VIRTUAL_ENV/bin:$PATH
ENV APP_HOME /app 

WORKDIR ${APP_HOME}

ADD requirements.txt ${APP_HOME}
RUN python -m pip install pip -U
RUN python -m pip install -r requirements.txt
