FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    wget xz-utils unzip ca-certificates \
    libx11-dev libxext-dev libxrender-dev fontconfig \
    && wget http://download.gna.org/wkhtmltopdf/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
    && tar -xvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
    && rm wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
    && apt-get purge -y xz-utils \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

VOLUME /wkhtmltox