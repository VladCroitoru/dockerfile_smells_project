FROM ruby:alpine
LABEL maintainer 'Juracy Filho <juracy@gmail.com>'

# Based on https://hub.docker.com/r/asciidoctor/docker-asciidoctor
ENV ASCIIDOCTOR_VERSION "1.5.5"
ENV ASCIIDOCTOR_PDF_VERSION "1.5.0.alpha.15"
ENV BACKENDS /backends
ENV BACKENDS_URL https://api.github.com/repos/asciidoctor/asciidoctor-backends/tarball

RUN apk update && apk --update add bash python curl tar && \
    rm -rf /var/cache/apk/* && \
    gem install --no-ri --no-rdoc rake && \
    gem install --no-ri --no-rdoc asciidoctor --version $ASCIIDOCTOR_VERSION && \
    gem install --no-ri --no-rdoc asciidoctor-diagram && \
    gem install --no-ri --no-rdoc asciidoctor-pdf --version $ASCIIDOCTOR_PDF_VERSION && \
    gem install --no-ri --no-rdoc rouge coderay pygments.rb thread_safe && \
    gem install --no-ri --no-rdoc slim haml tilt asciidoctor-revealjs && \
    mkdir $BACKENDS && \
    (curl -LkSs $BACKENDS_URL | tar xfz - -C $BACKENDS --strip-components=1)

WORKDIR /docs
VOLUME /docs

CMD ["/bin/bash"]
