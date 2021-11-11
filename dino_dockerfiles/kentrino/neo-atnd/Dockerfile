FROM ruby:2.3.1-alpine

MAINTAINER Kento Haneda <kento@haneda.me>

ENV BUILD_PACKAGES="ruby-dev build-base mysql-dev git" \
    PACKAGES="libxml2-dev zlib-dev linux-headers libxslt-dev tzdata nodejs" \
    RAILS_VERSION="4.2.6" \
    RAILS_ENV=production \
    BUNDLE_GEMFILE=/var/www/app/Gemfile \
    RAILS_ROOT=/var/www/app \
    GROUP_ID=110 \
    APP_USER_ID=1100 \
    NGINX_USER_ID=100

RUN \
  mkdir /var/www && \
  mkdir /var/www/app && \
  apk --update upgrade && \
  apk --no-cache add $BUILD_PACKAGES $PACKAGES $DEV_PACKAGES && \

  # gem no document setting
  echo 'gem: --no-document' >> ~/.gemrc && \
  cp ~/.gemrc /etc/gemrc && \
  chmod uog+r /etc/gemrc  && \

  gem install nokogiri -- --use-system-libraries && \
  gem install rails --version "$RAILS_VERSION" && \
  git clone https://github.com/kentrino/neo-atnd $RAILS_ROOT && \
  bundle install && \
  cd /var/www/app && \
  rake assets:precompile && \

  # cppy static files
  mkdir /var/www/html && \
  cp -R /var/www/app/public/* /var/www/html && \

  # security settings =====================================================
  addgroup nginx -g $GROUP_ID && \
  adduser -D -H -G nginx -u $APP_USER_ID app && \
  adduser -D -H -G nginx -u $NGINX_USER_ID nginx && \
  chown -R app:nginx /var/www/app && \
  chmod -R go-rwx /var/www/app && \

  # socket file
  chown app:nginx /var/run && \

  # public folder
  chown nginx:nginx /var/www && \
  chown -R nginx:nginx /var/www/html && \

  # cleanup ===============================================================
  # mysql
  cp -L /usr/lib/libmysqlclient.so.18 ~/ && \
  apk del $BUILD_PACKAGES && \
  mv ~/libmysqlclient.so.18 /usr/lib && \

  find / -type f -iname \*.apk-new -delete && \
  rm -rf /usr/lib/lib/ruby/gems/*/cache/* && \
  rm -rf ~/.gem

USER app
WORKDIR /var/www/app

ENTRYPOINT ["bundle", "exec"]
CMD ["unicorn", "-c", "./config/unicorn.rb"]
