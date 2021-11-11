FROM phusion/passenger-ruby23

# use korean mirror
# RUN sed -i 's#archive\.ubuntu\.com#kr.archive.ubuntu.com#' /etc/apt/sources.list

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs

RUN apt-get update && \
      apt-get install -y curl \
      wget \
      make \
      git \
      parallel \
      build-essential \
      libpq-dev \
      qt5-default \
      libqt5webkit5-dev \
      nodejs \
      xvfb \
      passenger \
      ttf-wqy-microhei \
      imagemagick \
      postgresql-contrib-9.5 \
      graphviz

RUN npm install -g phantomjs-prebuilt grunt yarn

RUN mkdir /app

WORKDIR /app

RUN mkdir -p log tmp/cache

RUN echo 'gem: --no-document' > ~/.gemrc
RUN gem install bundler git-autobisect passenger
