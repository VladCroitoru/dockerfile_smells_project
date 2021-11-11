FROM ruby:3.0.2-alpine

ENV APP_ROOT /app

RUN apk add --update \
            make \
            gcc \
            musl-dev \
            g++ \
            pcre-dev \
            libxml2-dev \
            libxslt-dev \
            tzdata \
            nodejs \
            npm \
            mariadb-dev

RUN mkdir $APP_ROOT
WORKDIR $APP_ROOT

RUN echo 'gem: --no-document' >> ~/.gemrc && \
    bundle config build.nokogiri --use-system-libraries

CMD ["ash"]

COPY entrypoint.sh /usr/bin/
ENTRYPOINT ["entrypoint.sh"]
