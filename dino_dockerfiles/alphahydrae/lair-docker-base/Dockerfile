FROM ruby:2.3

LABEL maintainer="docker@alphahydrae.com"

ENV NODE_VERSION="6.10.3" \
    S6_OVERLAY_VERSION="1.17.2.0" \
    SERF_VERSION="0.8.1"

# Install curl and postgresql
RUN apt-get update \
    && apt-get install -q -y curl postgresql-client

# Install Node.js
RUN curl -sSLo /tmp/node.tar.xz https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.xz \
    && tar -C /usr/local --strip-components 1 -xf /tmp/node.tar.xz \
    && rm -f /tmp/node.tar.xz

# Install s6 for service supervision (https://github.com/just-containers/s6-overlay)
RUN curl -sSLo /tmp/s6.tar.gz https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-amd64.tar.gz \
    && tar xzf /tmp/s6.tar.gz -C / \
    && rm -f /tmp/s6.tar.gz

# Install serf
RUN mkdir -p /usr/local/bin \
    && curl -sSLo /tmp/serf.gz https://releases.hashicorp.com/serf/${SERF_VERSION}/serf_${SERF_VERSION}_linux_amd64.zip \
    && gunzip -c /tmp/serf.gz > /usr/local/bin/serf \
    && chmod 755 /usr/local/bin/serf \
    && rm -f /tmp/serf.gz

# Install gems
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY Gemfile Gemfile.lock /usr/src/app/
RUN bundle install --without development test

# Clean up
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Set s6 as the entrypoint
ENTRYPOINT ["/init"]
