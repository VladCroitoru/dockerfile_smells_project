FROM ruby:2.5.1-slim

LABEL maintainer="Nate Morse <nathan@shadyoaksoftware.com>"

ENV S3_WEBSITE_VERSION=3.4.0

RUN apt-get update -qq && apt-get install -y --no-install-recommends \
	openjdk-8-jre-headless && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
	gem install s3_website -v ${S3_WEBSITE_VERSION} && \
	mkdir /app && \
	s3_website install

WORKDIR /app

ENTRYPOINT ["s3_website"]
CMD ["help"]
