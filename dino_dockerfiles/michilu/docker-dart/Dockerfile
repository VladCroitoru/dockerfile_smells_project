FROM node:0.10.48-slim
RUN sed -i '/jessie-updates/d' /etc/apt/sources.list  # Now archived

ENV \
  LANG="C" \
  LANGUAGE="C" \
  LC_ALL="C" \
  LC_CTYPE="C" \
  PATH="/usr/lib/dart/bin:$HOME/node_modules/.bin:$PATH"

WORKDIR $HOME/

ADD gemrc /etc/
ADD Gemfile $HOME/
ADD package.json $HOME/

# bash and curl needed by the steps on Wercker CI
RUN apt-get -q update && apt-get install --no-install-recommends -y -q \
  apt-transport-https \
  git \
  make \
  python \
  rsync \
  ruby-coffee-script \
  ruby-coffee-script-source \
  ruby-compass \
  ruby-json \
  ruby-sass \
  sudo \
  zip \
  && rm -rf /var/lib/apt/lists/* \
# for Python PIP
  && curl -s https://bootstrap.pypa.io/get-pip.py | python \
# for Ruby gem
  && gem install \
  bundler -v "~> 1" \
  && rm -r $HOME/.gem \
  && find / -type f -name "*.gem" -delete \
# pre install
  && npm install \
  && rm package.json \
  && bundle install \
  && rm Gemfile* \
# for Dart
  && curl -s https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && (cd /etc/apt/sources.list.d \
  && curl -sO https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list \
  && curl -sO https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_unstable.list \
  ) \
  ;

ARG \
  dart="2.12.1"

RUN apt-get -q update && apt-get install --no-install-recommends -y -q dart=${dart}-1 \
  && rm -rf /var/lib/apt/lists/* \
  ;

CMD echo "Versions..."\
  && type coffee && coffee --version \
  && type compass && compass --version \
  && type sass && sass --version \
  && type slimrb && slimrb --version \
  && type uglifyjs && uglifyjs --version \
  && type dart && dart --version \
  && type pub && pub --version \
  && echo "OK." \
  ;
