FROM ruby:2.4-alpine
MAINTAINER DeepMarimba Devops <devops@mailman.deepmarimba.com>

EXPOSE 80

ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 /usr/local/bin/dumb-init
ADD dockerfiles/ /
WORKDIR /wiki

RUN chmod +x /usr/local/bin/dumb-init /entrypoint.sh \
    && apk add --no-cache -t build_util make cmake build-base \
    && apk add --no-cache icu-dev git \
    && gem install github-linguist -v 5.0.10\
    && gem install gollum -v 4.1.1 \
    && gem install github-markdown -v 0.6.9 \
\
    && git init \
    && git config user.name Nobody \
    && git config user.email nobody@example.com \
    && git add Home.md \
    && git commit -m "Default page" \
\
    && apk del build_util

ENTRYPOINT ["/usr/local/bin/dumb-init", "--", "/entrypoint.sh"]
CMD ["run"]
