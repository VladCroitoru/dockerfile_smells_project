FROM mhart/alpine-node:6.17.1
ENV \
  LC_CTYPE="en_US.utf8"
# Install commands.
# bash needed by the some steps on Wercker CI
# convert in imagemagick and librsvg needed by something
# font-jis-misc needed by Japanese
# gcc and libc-dev libffi-dev needed by gem install ffi
# nproc in coreutils and GNU xargs in findutils needed by UglifyJS
# ruby, ruby-dev, and ruby-io-console needed by gem
# ssh in openssh-client needed by git
RUN apk --no-cache --update add \
  bash \
  coreutils \
  curl \
  findutils \
  font-jis-misc \
  gcc \
  git \
  imagemagick \
  libc-dev \
  libffi-dev \
  librsvg \
  make \
  openssh-client \
  py-pip \
  python \
  python-dev \
  rsync \
  ruby \
  ruby-dev \
  ruby-io-console \
  sudo \
  zip \
  ;
RUN pip install --upgrade setuptools==44.1.1
RUN echo 'gem: --no-rdoc --no-ri' > /etc/gemrc \
  && gem install \
  bundler \
  ffi \
  && rm -r /root/.gem \
  && find / -name '*.gem' | xargs rm
RUN curl -s https://bootstrap.pypa.io/get-pip.py | python
