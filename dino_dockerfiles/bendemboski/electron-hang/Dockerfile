FROM markadams/chromium-xvfb

# Node 6 repo
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -

# Yarn repo
RUN curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN dpkg --add-architecture i386 && \
  apt-get update && \
  apt-get install -y --no-install-recommends \
  build-essential \
  strace \
  openssh-client \
  vim \
  git \
  nodejs \
  yarn \
  libgconf-2-4

ADD . /electron-hang
WORKDIR /electron-hang
RUN yarn
