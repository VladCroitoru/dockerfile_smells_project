FROM ruby:2-slim

MAINTAINER Thomas Parisot <hi@oncletom.io>

ENV BACKENDS /asciidoctor-backends

WORKDIR /tmp

COPY Gemfile /tmp/Gemfile
RUN echo 'gem: --no-document' | tee -a ~/.gemrc \
  && apt-get update \
  && apt-get install -y --no-install-recommends make gcc libxml2-dev libxslt-dev \
  && bundle config build.json --use-system-libraries \
  && bundle config build.nokogiri --use-system-libraries --with-xml2-include=/usr/include/libxml2 \
  && bundle install \
  && mkdir -p /documents \
  && mkdir -p "${BACKENDS}" \
  && (curl -LkSs https://api.github.com/repos/asciidoctor/asciidoctor-backends/tarball | tar xfz - -C $BACKENDS --strip-components=1)

WORKDIR /documents
VOLUME /documents

ENTRYPOINT ["asciidoctor"]

CMD ["--help"]
