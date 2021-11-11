FROM alpine:3.3

RUN apk add --no-cache \
	build-base \
	ca-certificates \
	libffi-dev \
	nodejs \
	ruby-dev \
	ruby-nokogiri \
	zlib-dev \
        git

RUN addgroup -g 433 runner \
    && adduser -u 431 -G runner -h /home/runner -D -s /sbin/nologin runner

USER runner

WORKDIR /home/runner

RUN	gem install --user-install \
	bundler \
	github-pages \
	io-console \
	--no-rdoc --no-ri

ENV PATH="/home/runner/.gem/ruby/2.2.0/bin:${PATH}"

RUN git clone https://github.com/kubernetes/kubernetes.github.io.git \
    && cd kubernetes.github.io \
    && bundle install --path ~/.gem

EXPOSE 8080

CMD cd kubernetes.github.io && bundle exec jekyll serve -H 0.0.0.0 -P 8080
