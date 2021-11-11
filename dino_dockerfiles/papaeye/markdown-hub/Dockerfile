FROM ruby:2.2-onbuild
MAINTAINER papaeye@gmail.com

ENV GITHUB_MARKDOWN_CSS_VERSION 2.0.9

RUN mkdir -p /usr/src/app/public/bower_components/github-markdown-css \
	&& curl -sSL https://github.com/sindresorhus/github-markdown-css/archive/$GITHUB_MARKDOWN_CSS_VERSION.tar.gz \
		| tar -xzC /usr/src/app/public/bower_components/github-markdown-css --strip-components=1

RUN bundle exec rake emoji

EXPOSE 9292

CMD ["bundle", "exec", "rackup", "-o", "0.0.0.0"]
