FROM debian:stable
MAINTAINER Florenz A. P. Hollebrandse
LABEL description="Build and deploy Hugo static websites" \
      version="0.23"

ENV HUGO_URL "https://github.com/gohugoio/hugo/releases/download/v0.23/hugo_0.23_Linux-64bit.deb"

# Install required packages
RUN  apt-get --assume-yes --quiet update \
  && apt-get install --assume-yes --quiet --no-install-recommends \
    git \
    openssh-client \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Configure git so it's ready to be used.
RUN  git config --system user.name "Hugo Box (Docker container)" \
  && git config --system user.email docker@users.noreply.github.com 

# Install Hugo
ADD $HUGO_URL hugo.deb
RUN dpkg --install hugo.deb \
  && rm hugo.deb
