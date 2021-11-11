FROM ruby:2.1-onbuild

ENV APT_PACKAGES " \
  git libmagickwand-dev imagemagick libcurl3 \
  gcc g++ make patch binutils libc6-dev \
  libjemalloc-dev libffi-dev libssl-dev libyaml-dev zlib1g-dev libgmp-dev \
  libxml2-dev libxslt1-dev libpq-dev libreadline-dev libsqlite3-dev libmysqlclient-dev \
"

ENV APT_REMOVE_PACKAGES "anacron cron openssh-server postfix"

# COPY apt.conf /etc/apt/apt.conf.d/local
RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get install -y $APT_PACKAGES
RUN apt-get remove --purge -y $APT_REMOVE_PACKAGES
RUN apt-get autoremove --purge -y

RUN gem install google-map-stitch

CMD ["/usr/src/app/map-maker.rb"]
