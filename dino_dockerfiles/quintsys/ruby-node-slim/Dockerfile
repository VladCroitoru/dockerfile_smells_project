FROM ruby:2.6.1-slim

ENV NODE_VERSION='6.x' \
    YARN_VERSION='latest'

RUN export DEBIAN_FRONTEND=noninteractive \
  && apt-get update \
  && apt-get install -y --no-install-recommends apt-utils \
    curl \
    build-essential \
    libxml2-dev \
    libxslt1-dev \
    libcurl4-openssl-dev \
    gnupg \
    dirmngr \
  && curl -sL https://deb.nodesource.com/setup_${NODE_VERSION} | bash \
  && apt-get install -y --no-install-recommends nodejs \
  && apt-get upgrade -y \
  && npm install -g -s --no-progress yarn \
  && apt-get purge -y --auto-remove \
  && rm -rf /var/lib/apt/lists/*

CMD ["bash"]    
