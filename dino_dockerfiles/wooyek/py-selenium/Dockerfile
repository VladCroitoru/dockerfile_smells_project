FROM ubuntu:17.04

MAINTAINER Janusz Skonieczny @wooyek
LABEL version="0.9.9"

# Install tooling for test debuging and libraries needed by geodjango.
# http://stackoverflow.com/a/27931669/260480
RUN apt-get update && apt-get -y upgrade && \
    apt-get install -y git unzip nano wget sudo curl build-essential \
    python python-dev python-pip python-virtualenv \
    python3 python3-dev python3-pip python3-venv \
    chromium-chromedriver chromium-browser libgconf2-4 xvfb && \
    python -m pip install pip -U && \
    python3 -m pip install pip -U && \
    apt-get clean && \
    pip2 install selenium pyvirtualdisplay invoke pytest pytest-xdist pytest-selenium pytest-dependency envparse tox coverage pylint factory-boy faker pathlib -U && \
    pip3 install selenium pyvirtualdisplay invoke pytest pytest-xdist pytest-selenium pytest-dependency envparse tox coverage pylint factory-boy faker -U && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV LANG en_US.UTF-8 \
    LANGUAGE en_US:en \
    LC_ALL en_US.UTF-8 \
    PYTHONIOENCODING utf-8

COPY py-selenium-entrypoint.sh chromedriver /usr/local/bin/
RUN chmod +x /usr/local/bin/py-selenium-entrypoint.sh
ENTRYPOINT ["py-selenium-entrypoint.sh"]
