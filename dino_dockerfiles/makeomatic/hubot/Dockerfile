FROM makeomatic/node:6.2.1-ruby

WORKDIR /src

# cache gem files
COPY Gemfile* /src/
RUN apk add --no-cache --update --virtual .ruby-buildDeps build-base \
  && bundle install \
  && runDeps="$( \
    scanelf --needed --nobanner --recursive /usr/local \
      | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
      | sort -u \
      | xargs -r apk info --installed \
      | sort -u \
  )" \
  && apk add --virtual .ruby-rundeps $runDeps \
  && apk del .ruby-buildDeps

# cache npm modules
COPY package.json /src/
RUN npm install --production

# move source code
COPY ./ /src/
