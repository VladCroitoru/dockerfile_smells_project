FROM mhart/alpine-node-auto:0.10

ENV \
  HOME="/root" \
  LC_CTYPE="C.utf8" \
  PATH="/root/node_modules/.bin:$PATH"
WORKDIR $HOME

# for Ruby gem
ADD gemrc /etc/
# pre install
ADD Gemfile $HOME/
ADD package.json $HOME/

# bash and curl needed by the steps on Wercker CI
# ruby, ruby-dev, and ruby-io-console needed by gem
RUN apk --no-cache --update add \
  bash \
  curl \
  git \
  make \
  python \
  python-dev \
  rsync \
  ruby \
  ruby-dev \
  ruby-io-console \
  sudo \
# for Python PIP
  && curl -s https://bootstrap.pypa.io/get-pip.py | python \
# for Ruby gem
  && gem install \
  bundler \
  && rm -r $HOME/.gem \
  && find / -type f -name "*.gem" -delete \
# gcc and libc-dev libffi-dev needed by gem install ffi
  && apk --no-cache --update add --virtual=build-time-only \
  gcc \
  libc-dev \
  libffi-dev \
  && gem install \
  ffi \
  && rm -r $HOME/.gem \
  && find / -type f -name "*.gem" -delete \
  && apk del build-time-only \
# pre install
  && npm instal \
  && rm package.json \
  && bundle install \
  && rm Gemfile* \
  ;

CMD echo "print versions..."\
  && coffee --version \
  && compass --version \
  && haml --version \
  && sass --version \
  && uglifyjs --version \
  ;
