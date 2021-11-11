FROM ruby:3.0.2-alpine3.13
MAINTAINER Ministry of Justice, Apply service <apply@digital.justice.gov.uk>

# fail early and print all commands
RUN set -ex

# build dependencies:
# -virtual: create virtual package for later deletion
# - build-base for alpine fundamentals
RUN apk --no-cache add --virtual build-dependencies build-base curl openssl bash postgresql-dev
RUN apk --no-cache add postgresql-client


# add non-root user and group with alpine first available uid, 1000
RUN addgroup -g 1000 -S appgroup \
&& adduser -u 1000 -S appuser -G appgroup

RUN curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
RUN chmod +x ./kubectl
RUN mv ./kubectl /usr/local/bin/kubectl
RUN curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
RUN chmod +x get_helm.sh && ./get_helm.sh
RUN ./get_helm.sh

## create app directory in conventional, existing dir /usr/src
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

######################
# DEPENDENCIES START #
######################
COPY Gemfile* ./

# only install production dependencies,
# build nokogiri using libxml2-dev, libxslt-dev
# note: installs bundler version used in Gemfile.lock
#
RUN gem install bundler -v $(cat Gemfile.lock | tail -1 | tr -d " ") \
&& bundle config --global without test development \
&& bundle install

####################
# DEPENDENCIES END #
####################
COPY . .

# tidy up installation
RUN apk update && apk del build-dependencies curl openssl bash

# expect ping environment variables
ARG BUILD_DATE
ARG BUILD_TAG
# set ping environment variables
ENV BUILD_DATE=${BUILD_DATE}
ENV BUILD_TAG=${BUILD_TAG}

USER 1000
CMD "./scripts/docker-startup.sh"
