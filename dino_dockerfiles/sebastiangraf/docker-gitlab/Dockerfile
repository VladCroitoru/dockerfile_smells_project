FROM debian:8.0
MAINTAINER sebastian.graf@konschtanz.de

RUN apt-get update \
 && apt-get install -y supervisor logrotate locales \
      vim.tiny wget sudo net-tools ca-certificates unzip \
      nginx openssh-server mysql-client postgresql-client redis-tools \
      git-core ruby2.1 python2.7 python-docutils nodejs \
      libmysqlclient18 libpq5 zlib1g libyaml-0-2 libssl1.0.0 \
      libgdbm3 libreadline6 libncurses5 libffi6 \
      libxml2 libxslt1.1 libcurl3 libicu52 ruby \
 && update-locale LANG=C.UTF-8 LC_MESSAGES=POSIX \
 && locale-gen en_US.UTF-8 \
 && dpkg-reconfigure locales \
 && gem install --no-document bundler \
 && rm -rf /var/lib/apt/lists/* # 20150504

COPY assets/setup/ /app/setup/
RUN chmod 755 /app/setup/install
RUN /app/setup/install

COPY assets/config/ /app/setup/config/
COPY assets/init /app/init
RUN chmod 755 /app/init

EXPOSE 22
EXPOSE 80
EXPOSE 443

VOLUME ["/home/git/data"]
VOLUME ["/var/log/gitlab"]

WORKDIR /home/git/gitlab
ENTRYPOINT ["/app/init"]
CMD ["app:start"]
