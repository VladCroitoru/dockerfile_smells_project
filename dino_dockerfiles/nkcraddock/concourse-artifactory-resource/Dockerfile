FROM golang:1.6-alpine
MAINTAINER Nathan Craddock <nkcraddock@gmail.com>

RUN set -ex \
	&& apk update \
	&& apk add --no-cache \
			tar \
			curl \
			git \
			jq 

# This prevents re-cloning unless the master branch has changed
ADD https://api.github.com/repos/jfrogdev/jfrog-cli-go/compare/master...HEAD /dev/null
# Download and build jfrog
RUN git clone git://github.com/jfrogdev/jfrog-cli-go /go/src/github.com/jfrogdev/jfrog-cli-go && go install github.com/jfrogdev/jfrog-cli-go/jfrog

ADD assets/ /opt/resource/
