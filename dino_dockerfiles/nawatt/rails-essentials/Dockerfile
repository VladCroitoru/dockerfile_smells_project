# Use the barebones version of Ruby 2.2.3.
FROM ruby:2.2.5-slim

# Optionally set a maintainer name to let people know who made this image.
MAINTAINER Muhammad Al-Syrwan <mhdsyrwan@gmail.com>

RUN apt-get update && apt-get install -yq git curl build-essential \
                                          postgresql-client-9.4 imagemagick \
                                          libxml2-dev libxslt1-dev libgmp3-dev \
                                          nodejs libpq-dev \
                                          --fix-missing --no-install-recommends
