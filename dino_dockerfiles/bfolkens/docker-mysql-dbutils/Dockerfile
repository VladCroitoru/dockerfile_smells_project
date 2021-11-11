FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y mysql-client mytop wget python-mysqldb

RUN wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/openarkkit/openark-kit-196-1.deb && \
    dpkg -i openark-kit-196-1.deb

