# Based on the GitHub pages stack (Ruby, Jekyll, Liquid, Sass)
# Includes additional Jekyll plugins.

FROM ruby:2.5.0

LABEL author="Lakruzz <lars@lakruzz.com>"
LABEL maintainer="Lakruzz <lars@lakruzz.com>"

WORKDIR /app
EXPOSE 4000

# Liquid must run in UTF-8 env to support BOM characters
RUN apt-get update && \
    apt-get install -y locales && \
    echo "en_US UTF-8" > /etc/locale.gen && \
    locale-gen en_US UTF-8

ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_CTYPE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8


# github-pages gem.
#   https://github.com/github/pages-gem
#   https://pages.github.com/versions/
# jekyll-responsive-image
#   https://github.com/wildlyinaccurate/jekyll-responsive-image

RUN gem install \
      github-pages \
      jekyll-responsive-image
