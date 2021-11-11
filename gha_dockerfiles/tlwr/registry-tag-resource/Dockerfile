ARG ruby_version
FROM ruby:$ruby_version

RUN apk add --no-cache build-base ruby-dev

RUN mkdir /registry-tag-resource
WORKDIR /registry-tag-resource

COPY $PWD/Gemfile .
COPY $PWD/Gemfile.lock .

RUN bundle install

COPY $PWD /registry-tag-resource

RUN mkdir -p /opt/resource && \
    ln -s /registry-tag-resource/bin/check /opt/resource/check && \
    ln -s /registry-tag-resource/bin/in /opt/resource/in
