FROM alpine:latest

LABEL maintainer="Michele Adduci <adduci.michele@gmail.com>"

VOLUME ["/document"]

RUN apk update && \
    apk --update add \
    ruby \
    ruby-dev \
    ruby-irb \
    ruby-rake \
    ruby-io-console \
    ruby-bigdecimal \
    ruby-json \
    ruby-bundler \
    libstdc++ \
    curl \
    tzdata \
    build-base \
    libxml2-dev \
    libxslt-dev \
    postgresql-dev \
    bash && \
    echo 'gem: --no-document' > /etc/gemrc && \
    gem install nokogiri && \
    gem install asciidoctor-diagram && \
    gem install asciidoctor-pdf --version 1.6.1 && \
    gem install asciidoctor-pdf-cjk && \
    gem install coderay pygments.rb thread_safe && \
    gem install slim && \
    gem install concurrent-ruby && \
    gem install haml tilt && \
    apk del curl ruby-bundler postgresql-dev build-base make gcc g++ && \
    rm -rf /var/cache/apk/*

ENTRYPOINT ["asciidoctor-pdf"]
