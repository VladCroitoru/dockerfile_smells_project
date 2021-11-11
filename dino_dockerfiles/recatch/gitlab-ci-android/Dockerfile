FROM jangrewe/gitlab-ci-android

RUN apt-get -qq update \
    && curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash \ 
    && apt-get -qq update \
    && apt-get install -qqy --no-install-recommends \
      ruby \
      ruby-dev \
      libcurl4-openssl-dev \
      build-essential \
      imagemagick \
      librsvg2-2 \
      git \
      git-lfs \
      locales \
      librsvg2-bin \
      openssh-client \
    && git lfs install \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && gem install bundler:1.17.3 bundler fastlane --no-rdoc --no-ri \
    && locale-gen en_US.UTF-8

ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

WORKDIR /data
