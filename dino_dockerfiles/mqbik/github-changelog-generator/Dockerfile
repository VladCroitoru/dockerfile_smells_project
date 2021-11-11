FROM ruby:2.4.1-alpine

RUN apk add --no-cache git

ENV GCG_VERSION 1.14.3
RUN gem install github_changelog_generator -v $GCG_VERSION

# Set up the application directory
VOLUME ["/app"]
WORKDIR /app

CMD ["--help"]
ENTRYPOINT ["github_changelog_generator"]
