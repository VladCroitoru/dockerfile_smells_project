FROM node:6.11.0
MAINTAINER Dan Lynn <docker@danlynn.org>

WORKDIR /myapp

# run wkhtmltos3.js script using node on container start
ENTRYPOINT ["node", "src/wkhtmltos3.js"]

# install dependencies
RUN \
    apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install build-essential xorg libssl-dev libxrender-dev wget

# install wkhtmltopdf for rendering html pages into images
RUN \
    wget https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && \
    tar xf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz -C / && \
    rm wkhtmltox-0.12.4_linux-generic-amd64.tar.xz

ENV PATH="/wkhtmltox/bin:${PATH}"

# install imagemagick in order to support the --trim command line option
# as well as everything else that imagemagick can do
RUN \
    apt-get install -y imagemagick=8:6.8.9.9-5+deb8u9 --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

COPY src src
ADD package.json /myapp/

RUN \
    npm install
