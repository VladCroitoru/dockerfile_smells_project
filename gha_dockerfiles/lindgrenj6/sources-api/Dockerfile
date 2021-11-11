FROM registry.access.redhat.com/ubi8/ubi:8.4-206

RUN dnf -y --disableplugin=subscription-manager module enable ruby:2.6 && \
    dnf -y --disableplugin=subscription-manager --setopt=tsflags=nodocs install \
      ruby-devel \
      # To compile native gem extensions
      gcc-c++ make redhat-rpm-config \
      # For git based gems
      git \
      # For checking service status
      nmap-ncat \
      # Libraries
      postgresql-devel openssl-devel libxml2-devel \
      # For the rdkafka gem
      cyrus-sasl-devel zlib-devel openssl-devel diffutils \
      # For the mimemagic gem (+rails)
      shared-mime-info \
      && \
    dnf --disableplugin=subscription-manager clean all

ENV WORKDIR /opt/sources-api/
ENV RAILS_ROOT $WORKDIR
WORKDIR $WORKDIR

# For the clowder config parser
RUN curl -L https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64 -o jq \
  && chmod +x ./jq && cp jq /usr/bin

RUN touch /opt/rdsca.crt && chmod 666 /opt/rdsca.crt

COPY docker-assets/librdkafka-1.5.0.tar.gz /tmp/librdkafka.tar.gz
RUN cd /tmp && tar -xf /tmp/librdkafka.tar.gz && cd librdkafka-1.5.0 && \
    ./configure --prefix=/usr && \
    make -j2 && make install && \
    rm -rf /tmp/librdkafka*

COPY Gemfile $WORKDIR
RUN echo "gem: --no-document" > ~/.gemrc && \
    gem install bundler --conservative --without development:test && \
    bundle install --jobs 8 --retry 3 && \
    rm -rvf $(gem env gemdir)/cache/* && \
    rm -rvf /root/.bundle/cache

COPY . $WORKDIR

# TODO: find a better way to do this. Image is getting bigger layers. 
COPY docker-assets/entrypoint /usr/bin
COPY docker-assets/run_rails_server /usr/bin
COPY docker-assets/run_sidekiq /usr/bin
COPY docker-assets/seed_database /usr/bin

RUN chgrp -R 0 $WORKDIR && \
    chmod -R g=u $WORKDIR

# for compatibility with CI
EXPOSE 3000 8000

ENTRYPOINT ["entrypoint"]
CMD ["run_rails_server"]
