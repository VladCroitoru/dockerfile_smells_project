FROM node:6.9.2-wheezy

RUN set -x \
    && apt-get update --quiet \
    && apt-get install --quiet --yes --no-install-recommends rubygems-integration inotify-tools libc6 libgmp3-dev ruby-dev \
    && apt-get clean \
    && gem install --no-ri --no-rdoc sass -v 3.4.22 \
    && gem install --no-ri --no-rdoc bundler \
    && bundle config --global frozen 1 \
    && bundle config --global silence_root_warning 1 \
    && bundle config --global without "development:test" \
    && bundle config --global build.nokogiri  "--use-system-libraries" \
    && rm -rf /var/lib/gems/*/cache/*


WORKDIR /data

ONBUILD ADD ["package.json", "npm-shrinkwrap.json", "Gemfile", "Gemfile.lock", "/data/"]
ONBUILD RUN rm -rf /data/node_modules && npm cache clean && npm install --global grunt-cli && npm install && npm cache clean
ONBUILD RUN bundle install && rm -rf /var/lib/gems/*/cache/*
