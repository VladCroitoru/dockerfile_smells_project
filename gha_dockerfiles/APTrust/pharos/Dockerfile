FROM madnight/docker-alpine-wkhtmltopdf as builder

FROM ruby:2.7.2-alpine3.11
LABEL maintainer="Christian Dahlhausen <christian@aptrust.org>"

# Install dependencies
# - build-base: To ensure certain gems can be compiled
# - nodejs: Compile assets
# - libpq-dev: Communicate with postgres through the postgres gem
# - postgresql-client-9.4: In case you want to talk directly to postgres

RUN apk update -qq && apk upgrade && apk add --no-cache build-base libpq \
    nodejs postgresql-client postgresql-dev python py-pip py-argparse \
    libstdc++ tzdata bash ruby-dev ruby-nokogiri ruby-bigdecimal \
	libxml2-dev libxslt-dev readline readline-dev curl \
# Following packages for wkhtmltopdf only
    libgcc libstdc++ libx11 glib libxrender libxext libintl \
    libcrypto1.1 libssl1.1 \
    ttf-dejavu ttf-droid ttf-freefont ttf-liberation ttf-ubuntu-font-family \
	jq py3-configobj py3-pip py3-setuptools python3 python3-dev

# Needed for bin/pharos_notify.py
RUN pip install requests

RUN addgroup -S somegroup -g 1000 && adduser -S -G somegroup somebody -u 1000

RUN mkdir /pharos
WORKDIR /pharos

# Set Timezone & Locale
ENV TZ=UTC
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'
ENV SECRET_KEY_BASE=${SECRET_KEY_BASE:-52517cb1d20063c94605ba51bb5c40c4b0e2dc7d4c37bb506f1288f8976a187a4df1fdd820ad88b8382009c84de50f2d53a09d4c17ff2e64f8a99dc4da6a4987}

# Set Environment
# Environment to be set in .env file and populated by Ansible with correct
# values. Ansible shall start container build and deploy. build script should
# make sure that docker and ansible are installed locally. After build the
# container will be pushed to the server and restarted.

COPY --from=builder /bin/wkhtmltopdf /bin/wkhtmltopdf

COPY Gemfile Gemfile.lock ./
RUN gem update --system && gem install bundler -v 2.1.4
RUN bundle install --jobs=4 --without=["development" "test"] --no-cache

COPY . $WORKDIR

# - load db schema at first deploy
# - migrate db schema
# - pharos setup (create institutions, roles and users)
# --> These should be part of a build script. The only purpose of this image is
# to provide the rails environment and app. It assumes an external db (per env)

# Provide dummy data to Rails so it can pre-compile assets.
#RUN bundle exec rake RAILS_ENV=production DATABASE_URL=postgresql://user:pass@127.0.0.1/dbname SECRET_TOKEN=pickasecuretoken assets:precompile
RUN RAILS_ENV=test bundle exec rake assets:precompile
RUN RAILS_ENV=production bundle exec rake assets:precompile
RUN RAILS_ENV=demo bundle exec rake assets:precompile

# Expose rails server port
EXPOSE 9292

# Cleanup packages we don't need after compilation
RUN apk del build-base postgresql-dev postgresql-client libxml2-dev libxslt-dev \
            ruby-bundler ruby-dev ruby-bigdecimal && \
    rm -rf /usr/lib/ruby/gems/*/cache/* \
           /usr/local/bundle/cache/* \
           /var/cache/apk/* \
           /tmp/* \
           /var/tmp/*

# Expose a volume so that nginx will be able to read in assets in production.
VOLUME ["$WORKDIR/public"]

HEALTHCHECK CMD curl --fail http://localhost:9292/ || exit 1

RUN chown -R somebody:somegroup /pharos
USER somebody

CMD ["bundle", "exec", "puma", "-p9292"]
