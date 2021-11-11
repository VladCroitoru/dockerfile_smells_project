FROM alpine:3.4
MAINTAINER Chris Stretton <chris.stretton@fasthosts.com>

RUN apk --no-cache add \
                   build-base \
                   ca-certificates \
                   ruby \
                   ruby-irb \
                   ruby-dev && \
    echo 'gem: --no-document' >> /etc/gemrc && \
    gem install oj && \
    gem install json && \
    gem install fluentd -v 0.12.31 && \
    apk del build-base ruby-dev && \
    rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem && \
    mkdir -p \
      /fluentd/log \
      /fluentd/etc \
      /fluentd/plugins \
      /home/fluent
    

RUN echo "gem: --user-install --no-document" >> /home/fluent/.gemrc
ENV PATH /home/fluent/.gem/ruby/2.3.0/bin:$PATH
ENV GEM_PATH /home/fluent/.gem/ruby/2.3.0:$GEM_PATH

COPY fluent.conf /fluentd/etc/
ONBUILD COPY fluent.conf /fluentd/etc/
ONBUILD COPY plugins /fluentd/plugins/

ENV FLUENTD_OPT=""
ENV FLUENTD_CONF="fluent.conf"

EXPOSE 24224 5140

CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins $FLUENTD_OPT
