FROM debian:jessie-slim

MAINTAINER Ryoma Kawajiri <ryoma.edison@gmail.com>

# Install Pandoc
ENV PANDOC_VERSION "1.19.2.1"
ENV BUILD_DEPS="wget ca-certificates"
RUN set -ex \
&& apt-get update \
&& apt-get install -y --no-install-recommends ${BUILD_DEPS} \
&& wget -O pandoc.deb https://github.com/jgm/pandoc/releases/download/${PANDOC_VERSION}/pandoc-${PANDOC_VERSION}-1-amd64.deb \
&& dpkg -i pandoc.deb \
&& rm pandoc.deb \
&& apt-get remove -y ${BUILD_DEPS} \
&& rm -rf /var/lib/apt/lists/*

# Install latex packages
RUN set -ex \
 && apt-get update -y \
 && apt-get install -y --no-install-recommends \
    git \
    make \
    omake \
    gamin \
    context \
    fonts-texgyre \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /source
