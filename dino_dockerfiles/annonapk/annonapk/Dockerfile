FROM ubuntu:14.04

# apt-get
RUN apt-get update && apt-get install -y \
    curl \
    default-jre \
    git \
    python \
    python-setuptools

# apktool.jar
RUN curl -L -o /usr/local/bin/apktool.jar https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.0.0.jar

# androguard
RUN git clone https://github.com/androguard/androguard.git /tmp/androguard && \
    cd /tmp/androguard && \
    python setup.py install
