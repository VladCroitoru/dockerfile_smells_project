# Pull base image
FROM debian:stable
ENV DEBIAN_FRONTEND noninteractive
ENV TIMEZONE Europe/Paris
ENV LC_ALL C.UTF-8
ENV LANG fr_FR.UTF-8
ENV LANGUAGE fr_FR.UTF-8

# Change locale 
RUN apt-get update -y && apt-get install -y locales
RUN echo 'fr_FR.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen

# Timezone
RUN echo $TIMEZONE > /etc/timezone && dpkg-reconfigure tzdata

# Update & install packages
RUN apt-get install -y \
    python3-pip \
    python3-dev \
    python3-virtualenv \
    python3-venv \
    libpq-dev \
    postgresql-client \
    libjpeg-dev \
    libxml2-dev \ 
    libxslt1-dev \
    libfreetype6-dev \
    zlib1g-dev \
    g++ \
    build-essential \
    openssh-client \
    wget \
  && apt-get clean -y \
  && apt-get autoclean -y \
  && apt-get autoremove -y \
  && rm -rf /usr/share/locale/* \
  && rm -rf /var/cache/debconf/*-old \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /usr/share/doc/*

# Geckodriver pour selenium
RUN wget -qO- \
  https://github.com/mozilla/geckodriver/releases/download/v0.19.0/geckodriver-v0.19.0-linux64.tar.gz | \
  tar xvz -C /usr/local/bin
