FROM debian:jessie
MAINTAINER anazawa yasuhiro <yasuhiro@humming-code.com>

RUN apt-get update && \
    apt-get install -y ca-certificates git vim build-essential autoconf bison \
                       libtool flex re2c texinfo curl libxml2-dev libicu-dev \
                       libssl-dev libcurl4-openssl-dev\
                    --no-install-recommends && \
    rm -r /var/lib/apt/lists/*

RUN mkdir ~/.php-nabe
RUN cd ~/.php-nabe && \
    git clone https://github.com/kawahara/php-nabe && \
    $HOME/.php-nabe/php-nabe/php-nabe setup

ENV PATH ~/.php-nabe/php-nabe/bin:$PATH
