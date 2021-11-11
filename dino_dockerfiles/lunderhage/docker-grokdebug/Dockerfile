FROM ruby:2.4.1-alpine3.6

ENV GROK_DIR=/opt/grokdebug
ENV GIT_COMMIT=7e108f4b0469adebea158ab68956f84b273629b6
ENV BUILD_PACKAGES="git make gcc musl-dev linux-headers"

RUN apk update && apk add $BUILD_PACKAGES && \
	git clone https://github.com/nickethier/grokdebug.git $GROK_DIR && \
	cd $GROK_DIR && \
	git checkout $GIT_COMMIT && \
	sed -i 's/gem '"'"'haml'"'"'/gem '"'"'haml'"'"', '"'"'4.0.7'"'"'/g' Gemfile && \
 	gem update && \
 	gem install json -v '2.1.0' && \
 	gem install raindrops -v '0.19.0' && \
 	gem install haml -v '~>4.0.0' && \
 	bundle update && \
 	apk del $BUILD_PACKAGES --purge

WORKDIR $GROK_DIR

CMD ["rackup", "-o", "0.0.0.0", "-p", "80"]