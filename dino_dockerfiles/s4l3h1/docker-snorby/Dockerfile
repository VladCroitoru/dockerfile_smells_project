FROM s4l3h1/docker-barnyard
MAINTAINER Muhammad Salehi <salehi1994@gmail.com>
ENV DEBIAN_FRONTEND noninteractive
ENV COVERALLS_TOKEN [secure]
ENV CXX g++
ENV CC gcc
ADD snorby.zip /opt/
ADD ruby-1.9.3-p551.tar.gz /opt/
WORKDIR /opt/
RUN apt-get update ;\
apt-get install -y libgdbm-dev libncurses5-dev apache2-dev git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties libffi-dev imagemagick apache2 libyaml-dev libxml2-dev libxslt-dev git libssl-dev imagemagick apache2 libyaml-dev libxml2-dev libxslt-dev git postgresql-server-dev-all libpq-dev vim wget libmysqlclient-dev unzip libmysqlclient-dev ;\
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* ;\
tar -xvzf ruby-1.9.3-p551.tar.gz ;\
cd ruby-1.9.3-p551 ;\
./configure ;\
make -j32 ;\
make install ;\
echo "gem: --no-rdoc --no-ri" > ~/.gemrc ;\ 
echo "gem: --no-rdoc --no-ri" > /etc/gemrc ;\
gem install wkhtmltopdf ;\
gem install bundler ;\
gem install rails -v '3.2.13' ;\
gem install passenger -v '5.1.4' ;\
gem install public_suffix -v '1.4.6' ;\
cd /opt ;\
unzip snorby.zip ;\
mkdir /var/www/html/snorby/ ;\
mv snorby-master/* /var/www/html/snorby/
WORKDIR /var/www/html/snorby 
ADD Gemfile /var/www/html/snorby/
ADD Gemfile.lock /var/www/html/snorby/
RUN bundle install --full-index --with=production --without=development test ;\
echo -en "\n\n\n\n" | passenger-install-apache2-module 
RUN cp -fv /var/www/html/snorby/config/snorby_config.yml.example /var/www/html/snorby/config/snorby_config.yml ;\
cp -fv /var/www/html/snorby/config/database.yml.example /var/www/html/snorby/config/database.yml ;\
ln -s /etc/apache2/conf-available/passenger.conf /etc/apache2/conf-enabled/ ;\
rm -fv /etc/apache2/sites-enabled/* ;\
ln -s /etc/apache2/sites-available/snorby.conf /etc/apache2/sites-enabled/ 
ADD entrypoint.sh /opt/
COPY apache-virtualhost-snorby.conf /etc/apache2/sites-available/snorby.conf
COPY apache-passenger.conf /etc/apache2/conf-available/passenger.conf
RUN chmod +x /opt/entrypoint.sh
ENTRYPOINT [""]
CMD ["/opt/entrypoint.sh"]
