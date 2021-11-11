FROM circleci/ruby:2.4.2-node
MAINTAINER patorash <chariderpato@gmail.com>
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add - \
  && sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" >> /etc/apt/sources.list.d/postgresql.list' \
  && sudo apt-get update \
  && sudo apt-get install -y \
       postgresql-client-9.5 \
       ghostscript \
       fontconfig \
       fonts-migmix \
  && sudo apt-get clean \
  && sudo rm -rf /var/lib/apt/lists/* \
  && wget --quiet -O - https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 | tar xj -C /tmp --strip-components=1 \
  && sudo mv /tmp/bin/phantomjs /usr/local/bin \
  && rm -rf /tmp/*