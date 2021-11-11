FROM ruby:2.3.0-alpine
MAINTAINER Roman Messer <rms@gotocloud.net>
ENV RACK_ENV production
WORKDIR /var/www
EXPOSE 80

# Update system
RUN apk update && apk upgrade

# Install dependencies and gems with cleanup
COPY Gemfile* ./
RUN apk add build-base sqlite-dev \
    && bundle install --without development test \
    && apk del build-base \
    && rm -rf /var/cache/apk/*

# Copy and run app
COPY README.md Rakefile config.ru license.txt ./
COPY admin/     admin/
COPY app/       app/
COPY bin/       bin/
COPY config/    config/
COPY db/        db/
COPY lib/       lib/
COPY models/    models/
COPY public/    public/

ENTRYPOINT ["bin/get-volunteers"]
CMD ["--host=0.0.0.0", "--port=80"]
