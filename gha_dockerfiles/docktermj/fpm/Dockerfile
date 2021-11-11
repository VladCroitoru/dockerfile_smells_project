ARG BASE_IMAGE=ruby:3.0.2-buster
FROM ${BASE_IMAGE}
ENV REFRESHED_AT 2021-10-06
LABEL Name="dockter/fpm" \
      Maintainer="nemo@dockter.com" \
      Version="1.0.0"

# Install packages via apt.

RUN apt-get -y update \
 && apt-get -y install \
      yum \
 && rm -rf /var/lib/apt/lists/*

# Install packages via gem. https://rubygems.org/gems/

RUN gem install --no-document \
      fpm --version 1.13.1

# Runtime execution.

ENTRYPOINT ["fpm"]
