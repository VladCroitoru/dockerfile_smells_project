FROM kitpages/fizen-web:php72

MAINTAINER Kitpages <system [at] kibatic.com>

RUN apt-get -qqq update && DEBIAN_FRONTEND=noninteractive apt-get install -qqq -y \
    build-essential \
    curl \
    default-mysql-client \
 && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN curl -sSL https://get.docker.com | sh
