FROM ruby:2.7 AS pdkbase
ENV PDK_DISABLE_ANALYTICS=true
ENV PATH="${PATH}:/opt/puppetlabs/pdk/private/git/bin"

COPY entrypoint.sh /entrypoint.sh
COPY .gemfile /.gemfile

# We have to cp mkdir because it's apparently hardcoded in the nio4r makefile
RUN wget https://apt.puppet.com/puppet-tools-release-bullseye.deb && \
    dpkg -i puppet-tools-release-bullseye.deb && \
    apt-get update && \
    apt-get install -y ruby-dev pdk build-essential patch augeas-tools libaugeas-dev && \
    cp /bin/mkdir /usr/bin/mkdir

ENTRYPOINT ["/entrypoint.sh"]
