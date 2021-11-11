FROM ruby:3.0.2-slim-buster

LABEL maintainer "gene@technicalissues.us"

ENV GOSU_VERSION 1.11
ENV APP_ROOT /var/www/tree-planter
RUN mkdir -p $APP_ROOT
WORKDIR $APP_ROOT

RUN apt-get update -qq \
  && apt-get upgrade -y \
  && apt-get install -y --no-install-recommends dirmngr gcc git make gnupg2 openssh-client ruby-dev wget sendmail \
  && apt-get clean autoclean \
  && apt-get autoremove -y \
  && rm -rf /var/lib/apt/lists/*

RUN dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
  && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" \
  && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc" \
  && export GNUPGHOME="$(mktemp -d)" \
  && gpg2 --keyserver hkps://keys.openpgp.org --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
  && gpg2 --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
  && rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc \
  && chmod +x /usr/local/bin/gosu \
  && gosu nobody true

ADD Gemfile* $APP_ROOT/

RUN gem install bundler && bundle install --jobs=3 --without development

ADD . $APP_ROOT
COPY config-example.json $APP_ROOT/config.json
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

# SSH Setup
RUN mkdir -p /home/user/.ssh \
  && printf "Host *\n\tStrictHostKeyChecking no\n" >> /home/user/.ssh/config \
  && chmod 700 /home/user/.ssh \
  && chmod 644 /home/user/.ssh/config

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

EXPOSE 8080
CMD ["bundle", "exec", "passenger", "start", "--port", "8080"]

