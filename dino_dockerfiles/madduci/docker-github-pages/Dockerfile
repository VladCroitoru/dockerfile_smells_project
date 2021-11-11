FROM alpine:latest

LABEL maintainer="Michele Adduci <adduci.michele@gmail.com>"

VOLUME /site

EXPOSE 4000

WORKDIR /site

RUN apk update && \
    apk --update add \
    gcc \
    g++ \
    make \
    curl \
    bison \
    ca-certificates \
    tzdata \
    ruby \
    ruby-rdoc \
    ruby-irb \
    ruby-bundler \
    ruby-nokogiri \
    ruby-dev \
    glib-dev \
    zlib-dev \
    libc-dev && \
    echo 'gem: --no-document' > /etc/gemrc && \
    gem install github-pages --version 219 && \
    gem install jekyll-watch && \
    gem install jekyll-admin && \
    apk del gcc g++ binutils bison perl nodejs make curl && \
    rm -rf /var/cache/apk/*

CMD ["exec", "jekyll"]
ENTRYPOINT ["bundle"]
