FROM ruby:2-alpine
MAINTAINER Jens Kohl <jens.kohl@milchundzucker.de>

RUN gem install --no-document \
    danger \
    danger-commit_lint \
    danger-prose \
    danger-changelog \
    danger-mention \
    danger-jenkins \
    danger-gitlab
    
RUN apk update && apk upgrade && \
    apk add --no-cache \
    bash \
    git

ENTRYPOINT danger
