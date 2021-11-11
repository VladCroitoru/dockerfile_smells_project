# Based on https://github.com/oskapt/docker-hugo
FROM debian:stretch as build

RUN apt-get -qq update \
	&& DEBIAN_FRONTEND=noninteractive apt-get -qq install -y --no-install-recommends libstdc++6 git ca-certificates curl \
	&& rm -rf /var/lib/apt/lists/*

# Configuration variables
ENV HUGO_VERSION 0.64.0
ENV HUGO_BINARY hugo_extended_${HUGO_VERSION}_Linux-64bit.deb
ENV SITE_DIR '/usr/share/blog'

# Download and install hugo
RUN curl -sL -o /tmp/hugo.deb \
    https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY} && \
    dpkg -i /tmp/hugo.deb && \
    rm /tmp/hugo.deb && \
    mkdir ${SITE_DIR}

WORKDIR ${SITE_DIR}

# Expose default hugo port
EXPOSE 1313

ADD . ${SITE_DIR}
WORKDIR ${SITE_DIR}/site

RUN hugo -d /usr/share/nginx/html/ --cleanDestinationDir

FROM nginx

COPY --from=0 /usr/share/nginx/html /usr/share/nginx/html

WORKDIR /usr/share/nginx/html

EXPOSE 80
