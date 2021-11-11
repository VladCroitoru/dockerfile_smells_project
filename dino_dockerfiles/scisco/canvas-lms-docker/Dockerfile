FROM    ubuntu:14.04

RUN     apt-get update -y
RUN     apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 561F9B9CAC40B2F7
RUN     apt-get install --yes software-properties-common python-software-properties \
                              curl apt-transport-https ca-certificates

RUN     add-apt-repository --yes ppa:chris-lea/redis-server
RUN     add-apt-repository --yes ppa:brightbox/ruby-ng
RUN     sh -c 'echo deb https://oss-binaries.phusionpassenger.com/apt/passenger trusty main > /etc/apt/sources.list.d/passenger.list'
RUN     curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN     echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN     curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN     apt-get update -y

# Install dependencies
RUN     apt-get install --yes postgresql-9.3 git-core libapache2-mod-passenger apache2
RUN     apt-get install --yes ruby2.4 ruby2.4-dev zlib1g-dev libxml2-dev \
                              libsqlite3-dev postgresql libpq-dev \
                              libxmlsec1-dev curl make g++ \
                              python python-dev python-pip \
                              redis-server \
                              nodejs yarn

# Enable rewrite and passenger on Apache
RUN     a2enmod rewrite
RUN     a2enmod passenger
RUN     a2enmod ssl

# get canvas and install
RUN     cd /var && git clone https://github.com/instructure/canvas-lms.git canvas
WORKDIR /var/canvas
RUN     git branch --set-upstream-to origin/stable
RUN     git checkout release/2017-04-22.20

ENV     CANVAS_RAILS5 1
ENV     REALLY_GEM_UPDATE_SYSTEM 1
RUN     update-alternatives --install /usr/bin/ruby ruby /usr/bin/ruby2.4 400 \
          --slave /usr/bin/rake rake /usr/bin/rake2.4 \
          --slave /usr/bin/ri ri /usr/bin/ri2.4 \
          --slave /usr/bin/rdoc rdoc /usr/bin/rdoc2.4 \
          --slave /usr/bin/irb irb /usr/bin/irb2.4 \
          --slave /usr/share/man/man1/ruby.1.gz ruby.1.gz /usr/share/man/man1/ruby2.4.1.gz \
          --slave /usr/share/man/man1/rake.1.gz rake.1.gz /usr/share/man/man1/rake2.4.1.gz \
          --slave /usr/share/man/man1/ri.1.gz ri.1.gz /usr/share/man/man1/ri2.4.1.gz \
          --slave /usr/share/man/man1/rdoc.1.gz rdoc.1.gz /usr/share/man/man1/rdoc2.4.1.gz \
          --slave /usr/share/man/man1/irb.1.gz irb.1.gz /usr/share/man/man1/irb2.4.1.gz
RUN     update-alternatives --install /usr/bin/gem gem /usr/bin/gem2.4 400 \
          --slave /usr/share/man/man1/gem.1.gz gem.1.gz /usr/share/man/man1/gem2.4.1.gz
RUN     gem update --system
RUN     gem install bundler
RUN     bundle install --path vendor/bundle --without=sqlite mysql

# Automation jobs
RUN     ln -s /var/canvas/script/canvas_init /etc/init.d/canvas_init
RUN     update-rc.d canvas_init defaults

# copy config files
RUN     for config in amazon_s3 database \
            delayed_jobs domain file_store outgoing_mail security external_migration; \
            do cp config/$config.yml.example config/$config.yml; done
RUN     mkdir -p log tmp/pids public/assets public/stylesheets/compiled
RUN     touch Gemfile.lock

# create canvas user
RUN     adduser --disabled-password --gecos canvas canvasuser
RUN     chown -R canvasuser config/environment.rb log tmp public/assets \
        public/stylesheets/compiled Gemfile.lock config.ru

# install dependencies
RUN     yarn install
ENV     CANVAS_BUILD_CONCURRENCY=1
ENV     RAILS_ENV=production
RUN     locale-gen en_US.UTF-8
RUN     dpkg-reconfigure locales
ENV     LANG en_US.UTF-8
ENV     LANGUAGE en_US:en
ENV     LC_ALL en_US.UTF-8
RUN     bundle exec rake --trace canvas:compile_assets

EXPOSE 80 443
RUN     bundle install --path vendor/bundle --without=sqlite mysql
RUN     unlink /etc/apache2/sites-enabled/000-default.conf
ADD     ./start.sh /var/canvas/start.sh
ADD     ./delayed_workers.sh /var/canvas/delayed_workers.sh
RUN     chown canvasuser:canvasuser log/production.log
RUN     chmod -R 777 app/stylesheets && chmod -R 777 public/assets && chmod -R 777 public/stylesheets
