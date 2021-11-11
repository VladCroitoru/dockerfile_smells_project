FROM elixir:1.2.3

# install depencies
RUN set -xe \
    && buildDeps=' \
      ca-certificates \
      wget \
      debconf-utils \
    ' \
    && apt-get update \
    && apt-get install -y --no-install-recommends $buildDeps

# install mysql server
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections \
    && echo 'mysql-server mysql-server/root_password password' | debconf-set-selections \
    && echo 'mysql-server mysql-server/root_password_again password' | debconf-set-selections \
    && apt-get install -y mysql-server

# cleanup
RUN apt-get purge -y --auto-remove $buildDeps \
    && rm -rf /var/lib/apt/lists/*
