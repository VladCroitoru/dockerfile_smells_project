FROM debian:testing

LABEL maintainer="Sven Höper" \
  org.label-schema.name="shoeper/latex" \
  org.label-schema.description="Docker image providing everything to build latex documents based on Debian latest" \
  org.label-schema.vcs-url="https://github.com/shoeper/docker-latex-debian" \
  org.label-schema.schema-version="1.0"

RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula \
    select true | debconf-set-selections && \
    echo "deb http://deb.debian.org/debian testing contrib" >> /etc/apt/sources.list && \
    apt-get update && \
    # prevent "/usr/bin/bash: warning: setlocale: LC_ALL: cannot change locale (en_US.UTF-8)"
    apt-get install -y \
        apt-utils \
        locales && \
    locale-gen en_US.UTF-8 && \
    dpkg-reconfigure -f noninteractive locales && \
    apt-get install -y \
        wget \
        git \
        make \
        texlive-full \
        ttf-mscorefonts-installer && \
    # Removing documentation packages *after* installing them is kind of hacky,
    # but it only adds some overhead while building the image.
    apt-get --purge remove -y .\*-doc$ && \
    # Remove more unnecessary stuff
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
  
