FROM tutum/lamp:latest
MAINTAINER Bo Qi <simble1986@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# Preparation
RUN apt-get update && apt-get install -yqq wget unzip php5-curl dnsutils default-jre && \
  rm -rf /var/lib/apt/lists/*
COPY ./mutillidae-2.6.58.zip mutillidae.zip
# Deploy Mutillidae
RUN \
  unzip /mutillidae.zip && \
  rm -rf /app/* && \
  cp -r /mutillidae /app  && \
  rm /app/mutillidae/.htaccess && \
  rm -rf /mutillidae  && \
  wget -O dvwa.zip https://github.com/RandomStorm/DVWA/archive/v1.0.8.zip  && \
  unzip /dvwa.zip && \
  cp -r /DVWA-1.0.8 /app/dvwa && \
  rm /app/dvwa/.htaccess && \
  rm -rf /DVWA-1.0.8 && \
  wget -O webgoat.jar https://github.com/WebGoat/WebGoat/releases/download/7.1/webgoat-container-7.1-exec.jar && \
  sed -i 's/DirectoryIndex index.html.*/DirectoryIndex index.php index.html index.cgi index.pl index.xhtml index.htm/g' /etc/apache2/mods-enabled/dir.conf&& \
  sed -i 's/static public \$mMySQLDatabaseUsername =.*/static public \$mMySQLDatabaseUsername = "admin";/g' /app/mutillidae/classes/MySQLHandler.php && \
  echo "sed -i 's/static public \$mMySQLDatabasePassword =.*/static public \$mMySQLDatabasePassword = \\\"'\$PASS'\\\";/g' /app/mutillidae/classes/MySQLHandler.php" >> /create_mysql_admin_user.sh && \
  sed -i "s/^\$_DVWA\[ 'db_user' \] = 'root'/\$_DVWA[ 'db_user' ] = 'admin'/g" /app/dvwa/config/config.inc.php && \
  echo "sed -i \"s/p@ssw0rd/\$PASS/g\" /app/dvwa/config/config.inc.php" >> /create_mysql_admin_user.sh  && \
  echo 'session.save_path = "/tmp"' >> /etc/php5/apache2/php.ini && \
  sed -i '$i\echo "=> Starting WebGoat..."\njava -jar webgoat.jar &' /run.sh

EXPOSE 80 3306 8080
CMD ["/run.sh"]
