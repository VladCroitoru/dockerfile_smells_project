FROM registry.access.redhat.com/ubi8/ubi:8.4-206

RUN dnf -y --disableplugin=subscription-manager module enable ruby:2.6 && \
    dnf -y --disableplugin=subscription-manager --setopt=tsflags=nodocs install \
      ruby-devel \
      # To compile native gem extensions
      gcc-c++ make redhat-rpm-config \
      # For git based gems
      git \
      # For the rdkafka gem
      cyrus-sasl-devel zlib-devel openssl-devel diffutils \
      && \
    dnf --disableplugin=subscription-manager clean all

ENV WORKDIR /opt/satellite-operations/
WORKDIR $WORKDIR

COPY Gemfile $WORKDIR
RUN echo "gem: --no-document" > ~/.gemrc && \
    gem install bundler --conservative --without development:test && \
    bundle install --jobs 8 --retry 3 && \
    rm -rvf $(gem env gemdir)/cache/* && \
    rm -rvf /root/.bundle/cache

COPY . $WORKDIR

RUN chgrp -R 0 $WORKDIR && \
    chmod -R g=u $WORKDIR && \
    curl -L -o /usr/bin/haberdasher \
    https://github.com/RedHatInsights/haberdasher/releases/latest/download/haberdasher_linux_amd64 && \
    chmod 755 /usr/bin/haberdasher

ENTRYPOINT ["/usr/bin/haberdasher"]
CMD ["bin/satellite-operations"]
