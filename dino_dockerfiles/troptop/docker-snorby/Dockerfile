FROM ubuntu:latest

ENV MYSQL_ADMIM  ""
ENV MYSQL_ADMINPASS ""
ENV MYSQL_HOST ""
ENV MYSQL_DBNAME ""
ENV MYSQL_PASSWORD ""
ENV MYSQL_USER ""
ENV INSTALLDB "false"
ENV DELETEDB "false"
ENV RESETDB "false"
ENV ADD_DBUSER "false"


WORKDIR /opt
COPY jinja-snorby-conf.py .
COPY database.yml.template .
COPY entrypoint.sh /opt/
COPY snorby_config.yml .
RUN apt-get update -y
RUN apt-get -y install mysql-client ruby-dev ruby-bcrypt ruby-redcloth postgresql-server-dev-all bundler build-essential vim git wget libtool automake gcc flex bison libnet1 libnet1-dev libpcre3 libpcre3-dev autoconf libcrypt-ssleay-perl libwww-perl git zlib1g zlib1g-dev libmysqlclient-dev apache2 imagemagick wkhtmltopdf ruby libyaml-dev libxml2-dev libxslt1-dev openssl libreadline6-dev unzip libapache2-mod-passenger libapr1-dev libaprutil1-dev tzdata python-jinja2 libcurl4-openssl-dev
RUN wget -O snorby.zip --no-check-certificate https://github.com/Snorby/snorby/archive/master.zip
RUN unzip snorby.zip && mv snorby-master/ /var/www/html/snorby
WORKDIR /var/www/html/snorby
# Docker bug with other nokogiri version (can not compile)libcurl4-openssl-dev
RUN apt-get update -y
RUN apt-get install -y ruby-nokogiri ruby-libxml libxml2-dev libxml2 libxslt1.1 libxslt1-dev  liblzma5 liblzma-dev build-essential patch ruby-dev zlib1g-dev liblzma-dev pkg-config
#RUN bundle update nokogiri
#RUN gem install pkg-config -v "~> 1.1" 
#RUN gem install nokogiri -v '1.6.6.2'
COPY envvars  /etc/apache2/envvars
#RUN gem install nokogiri -- --use-system-libraries --with-xml2-include=/usr/include/libxml2/libxml --with-xml2-dir=/usr/lib/x86_64-linux-gnu/
RUN  bundle config build.nokogiri --use-system-libraries  --with-xml2-dir=/usr/lib/x86_64-linux-gnu/
RUN bundle install
#RUN bundle exec rake snorby:setup
RUN echo "<virtualhost *:80> \n\
     DocumentRoot /var/www/html/snorby/public\n\
     <directory '/var/www/html/snorby/public'>\n\
          AllowOverride all\n\
          Order deny,allow\n\
          Allow from all\n\
          Options -MultiViews\n\
          </directory>\n\
        ErrorLog ${APACHE_LOG_DIR}/snorby-error.log\n\
        CustomLog ${APACHE_LOG_DIR}/snorby-access.log combined\n\
</virtualhost>" > /etc/apache2/sites-enabled/000-default.conf
RUN cp -f /opt/snorby_config.yml config/snorby_config.yml
EXPOSE 80
RUN chmod +x /opt/entrypoint.sh
ENTRYPOINT ["/opt/entrypoint.sh"]


