FROM madnight/docker-alpine-wkhtmltopdf as wkhtmltopdf_image

# Builder stage
#FROM ruby:2.4.4-alpine3.7 as builder
FROM ruby:2.5-alpine as builder

ENV PATH /root/.yarn/bin:$PATH

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh build-base nodejs nodejs-npm tzdata mysql-dev

RUN apk update \
  && apk add curl bash binutils tar gnupg \
  && rm -rf /var/cache/apk/* \
  && /bin/bash \
  && touch ~/.bashrc \
  && curl -o- -L https://yarnpkg.com/install.sh | bash \
  && apk del curl tar binutils

RUN apk add --update --no-cache \
    libgcc libstdc++ libx11 glib libxrender libxext libintl \
    libcrypto1.1 libssl1.1 \
    ttf-dejavu ttf-droid ttf-freefont ttf-liberation ttf-ubuntu-font-family 

# Configure the main working directory. This is the base
# directory used in any further RUN, COPY, and ENTRYPOINT
# commands.
WORKDIR /usr/src/app

# Copy the Gemfile as well as the Gemfile.lock and install
# the RubyGems. This is a separate step so the dependencies
# will be cached unless changes to one of those two files
# are made.
COPY Gemfile Gemfile.lock ./
RUN gem install bundler && \
    gem install nokogiri -v 1.8.5 && \
    gem install listen -v 3.1.5 && \
    bundle install -j "$(getconf _NPROCESSORS_ONLN)" --retry 5 --without development,test

RUN apk add --update --no-cache wkhtmltopdf
RUN which wkhtmltopdf

# Copy dependencies for Node.js and instance the packages.
# Again, being separate means this will cache.
COPY package.json yarn.lock ./
RUN yarn install
RUN npm rebuild node-sass --force

FROM ruby:2.5-alpine

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh build-base nodejs nodejs-npm tzdata mysql-dev

RUN apk add --update --no-cache \
    libgcc libstdc++ libx11 glib libxrender libxext libintl \
    libcrypto1.1 libssl1.1 \
    ttf-dejavu ttf-droid ttf-freefont ttf-liberation ttf-ubuntu-font-family \
    imagemagick nfs-utils


COPY --from=builder /usr/local/bundle/ /usr/local/bundle/
RUN which wkhtmltopdf
#COPY /usr/bin/wkhtmltopdf /usr/local/bundle/bin/
RUN /usr/local/bundle/bin/wkhtmltopdf --version

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY --from=builder /usr/src/app/ /usr/src/app/
COPY --from=builder /usr/src/app/ /usr/src/app/
#COPY --from=builder /app/config/gpg/ /root/.gnupg/

# Set Rails to run in production
ENV RAILS_ENV production 
ENV RACK_ENV production
ENV RAILS_ROOT /usr/src/app
# Use Rails for static files in public
ENV RAILS_SERVE_STATIC_FILES 1
# You must pass environment variable SECRET_KEY_BASE
ARG SECRET_KEY_BASE
ENV SECRET_KEY_BASE $SECRET_KEY_BASE

# Copy the main application.
COPY . ./

# Precompile Rails assets (plus Webpack)
RUN bundle exec rake DATABASE_URL=mysql2:does_not_exist SECRET_KEY_BASE=dummytoken assets:precompile

# Will run on port 3000 by default
EXPOSE 3000
COPY docker-entrypoint.sh /usr/local/bin
COPY database.yml.prod config/database.yml

RUN mkdir -p /usr/src/app/storage
RUN chown -R root:root /usr/src/app
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
