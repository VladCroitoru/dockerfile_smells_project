FROM alpine:latest

RUN mkdir -p /var/www/
WORKDIR /var/www/

COPY Gemfile* /var/www/

RUN apk add --update --no-cache \
            ruby \
            ruby-rdoc \
            ruby-dev \
            sqlite-dev \
            gcc \
            libc-dev \
            make \
            apache2 && \
    gem install bundler -v "1.16.1" && \
    bundle install -j4

COPY . /var/www/

RUN mv httpd.conf /etc/apache2/

CMD ["httpd", "-D", "FOREGROUND"]
