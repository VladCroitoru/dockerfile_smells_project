FROM abernix/meteord:node-4-base

RUN apt-get update
RUN apt-get install -y wget libjpeg62-turbo libxrender1 xfonts-base xfonts-75dpi

RUN mkdir /setup
RUN wget -O /setup/wkhtmltopdf.tar.xz https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
RUN cd /setup && tar vxf wkhtmltopdf.tar.xz
RUN cd /setup && cp wkhtmltox/bin/wk* /usr/local/bin/
