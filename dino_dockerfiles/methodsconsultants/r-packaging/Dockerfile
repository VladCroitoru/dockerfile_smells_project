FROM r-base:latest

RUN apt-get update -qq && apt-get -y --no-install-recommends install \
  libssl-dev \
  libcurl4-openssl-dev \
  libssh2-1-dev \
  libxml2-dev \
  && install2.r --error \
    devtools \
    roxygen2
