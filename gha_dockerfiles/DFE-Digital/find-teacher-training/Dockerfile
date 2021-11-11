ARG BASE_RUBY_IMAGE=ruby:2.7.2-alpine3.12

FROM ${BASE_RUBY_IMAGE} AS base-image

RUN apk add --update --no-cache tzdata && \
    cp /usr/share/zoneinfo/Europe/London /etc/localtime && \
    echo "Europe/London" > /etc/timezone

RUN apk add --update --no-cache --virtual runtime-dependances \
    yarn shared-mime-info

WORKDIR /app

COPY Gemfile Gemfile.lock .tool-versions ./

RUN apk add --update --no-cache --virtual build-dependances \
    build-base  && \
    bundle install --jobs=4 && \
    apk del build-dependances

COPY package.json yarn.lock ./

RUN yarn install --frozen-lockfile

COPY . .

RUN bundle exec rake assets:precompile && \
    rm -rf node_modules /usr/local/bundle/cache


FROM ${BASE_RUBY_IMAGE}
ENV FREEDESKTOP_MIME_TYPES_PATH=/usr/share/mime/packages/freedesktop.org.xml
WORKDIR /app

RUN apk add --update --no-cache tzdata && \
    cp /usr/share/zoneinfo/Europe/London /etc/localtime && \
    echo "Europe/London" > /etc/timezone

COPY --from=base-image ${FREEDESKTOP_MIME_TYPES_PATH} ${FREEDESKTOP_MIME_TYPES_PATH}
COPY --from=base-image /app /app
COPY --from=base-image /usr/local/bundle/ /usr/local/bundle/

ARG COMMIT_SHA
ENV SHA=${COMMIT_SHA}

CMD bundle exec rails server -b 0.0.0.0
