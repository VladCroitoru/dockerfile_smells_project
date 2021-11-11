FROM fedora

# Setup mysql server

RUN dnf install -y mariadb-server httpd php openssh-server unzip wget java-11-openjdk hostname php-common php-pecl-apcu php-cli php-pear php-pdo php-mysqlnd php-pgsql php-pecl-mongodb php-pecl-memcache php-pecl-memcached php-gd php-mbstring php-mcrypt php-xml iputils iproute

ADD my.cnf /etc/mysql/conf.d/my.cnf

# Remove pre-installed database
RUN rm -rf /var/lib/mysql/*

# Add MySQL utils
ADD create_mysql_admin_user.sh /root/bin/create_mysql_admin_user.sh


#Enviornment variables to configure php
ENV PHP_UPLOAD_MAX_FILESIZE 10M
ENV PHP_POST_MAX_SIZE 10M

# Add volumes for MySQL 
# VOLUME  ["/etc/mysql", "/var/lib/mysql" ]


# install sshd and apache 
RUN useradd -c "Vuln User" -m guest
RUN echo "guest:guest"|chpasswd
RUN echo "root:password" |chpasswd


# Add DVWA
#
RUN mkdir -p /var/www/html/dvwa
ADD https://github.com/ethicalhack3r/DVWA/archive/master.tar.gz /var/www/html/dvwa/
ADD dvwa-install.sh /root/bin/dvwa-install.sh


# Deploy Mutillidae
RUN \
	mkdir /root/mutillidae && \
	cd /root/mutillidae && \
  wget -O /root/mutillidae/mutillidae.zip http://sourceforge.net/projects/mutillidae/files/latest/download && \
  unzip /root/mutillidae/mutillidae.zip && \
  cp -r /root/mutillidae/mutillidae /var/www/html/  && \
  rm -rf /root/mutillidae

RUN \
  sed -i 's/static public \$mMySQLDatabaseUsername =.*/static public \$mMySQLDatabaseUsername = "root";/g' /var/www/html/mutillidae/classes/MySQLHandler.php && \
  echo "sed -i 's/static public \$mMySQLDatabasePassword =.*/static public \$mMySQLDatabasePassword = \\\"'\$PASS'\\\";/g' /var/www/html/mutillidae/classes/MySQLHandler.php" >> //root/bin/create_mysql_admin_user.sh


# Add webgoat
RUN mkdir /root/webgoat
# RUN cd /root/webgoat; curl 'https://github.com/WebGoat/WebGoat/releases/download/7.1/webgoat-container-7.1-exec.jar' -O -J -L
# RUN cd /root/webgoat; curl 'https://github.com/WebGoat/WebGoat/releases/download/v8.0.0.M25/webgoat-server-8.0.0.M25.jar' -O -J -L
RUN cd /root/webgoat; curl 'https://github.com/WebGoat/WebGoat/releases/download/v8.1.0/webgoat-server-8.1.0.jar' -O -J -L

# RUN cd /root/webgoat; curl 'https://github.com/WebGoat/WebGoat/releases/download/v8.0.0.M25/webwolf-8.0.0.M25.jar' -O -J -L
RUN cd /root/webgoat; curl ''https://github.com/WebGoat/WebGoat/releases/download/v8.1.0/webwolf-8.1.0.jar -O -J -L

# Add commix
RUN mkdir /var/www/html/commix
ADD https://github.com/commixproject/commix/archive/master.tar.gz /var/www/html/commix

# Fix mariadb issue
RUN rm -rf /etc/my.cnf.d/auth_gssapi.cnf ; rm -rf /var/lib/mysql; echo -e 'innodb_buffer_pool_size=16M\ninnodb_log_buffer_size=500K\ninnodb_thread_concurrency=2' >>/etc/my.cnf.d/mariadb-server.cnf
RUN  mysql_install_db --user=mysql --ldata=/var/lib/mysql; chown -R mysql /var/lib/mysql/
# RUN mkdir -p /var/lib/mysql/; chown -R mysql /var/lib/mysql/ ;  cd /var/lib/mysql; /usr/libexec/mysqld  --initialize-insecure  --user=mysql --datadir=/var/lib/mysql

# Extract the tar files:
##   <aka> ## RUN dnf install -y tar python2 ; dnf clean all;
##   <aka> ## RUN cd /var/www/html/dvwa/; tar xvf master.tar.gz ; cd DVWA-master; cp config/config.inc.php.dist config/config.inc.php
##   <aka> ## RUN cd /var/www/html/commix/; tar xvf master.tar.gz

## OWASP Bricks
RUN wget -O /var/www/html/bricks.zip 'http://sourceforge.net/projects/owaspbricks/files/Tuivai%20-%202.2/OWASP%20Bricks%20-%20Tuivai.zip/download'
RUN mkdir /var/www/html/owasp-bricks; cd /var/www/html/owasp-bricks; unzip /var/www/html/bricks.zip

RUN dnf install -y php-mysqlnd php-gd && dnf clean all
RUN cd /var/www/html/dvwa; tar xvf master.tar.gz; cd DVWA-master/; mv config/config.inc.php{.dist,}


ADD start.sh /root/bin
# Add index file
ADD index.html /var/www/html

RUN chmod +x /root/bin/*.sh


RUN dnf install procps-ng -y && dnf clean all
# ADD https://github.com/bkimminich/juice-shop/releases/download/v8.6.2/juice-shop-8.6.2_node8_linux_x64.tgz /var/www/html
ADD https://github.com/bkimminich/juice-shop/releases/download/v12.6.1/juice-shop-12.6.1_node14_linux_x64.tgz /var/www/html
RUN cd /var/www/html && tar xvf juice-shop-12.6.1_node14_linux_x64.tgz && mv juice-shop_12.6.1 juice

ADD https://github.com/snoopysecurity/dvws/archive/master.tar.gz /var/www/html
RUN cd /var/www/html; tar xvf master.tar.gz && rm -rf master.tar.gz && mv dvws-master dvws

ADD https://github.com/commixproject/commix-testbed/archive/master.tar.gz /var/www/html
RUN cd /var/www/html; tar xvf master.tar.gz; rm -rf master.tar.gz && mv commix-testbed-master commix-testbed

RUN mkdir /var/www/html/bwapp
ADD https://sourceforge.net/projects/bwapp/files/bWAPP/bWAPP_latest.zip/download  /var/www/html/bwapp/bwapp.zip
RUN cd /var/www/html/bwapp; unzip bwapp.zip; rm -rf bwapp.zip; cd bWAPP; chmod 777 passwords/ images/ documents/ logs/ ;

#XVWA
RUN dnf install git sudo -y && dnf clean all 
ADD https://raw.githubusercontent.com/s4n7h0/Script-Bucket/master/Bash/xvwa-setup.sh /var/www/html
RUN cd /var/www/html; sed -i 's/read uname/uname=root/' xvwa-setup.sh && \
    sed -i "s/read pass/pass=root/" xvwa-setup.sh && \
    sed -i "s;read webroot;webroot=/var/www/html;" xvwa-setup.sh
# sed -i 's/localhost/127.0.0.1/' xvwa/config.php
#  echo root | bash xvwa-setup.sh && \
# wget https://raw.githubusercontent.com/stamparm/DSVW/master/dsvw.py
#
# Fix php-fpm
RUN sed -i 's/^listen =.*/listen = 127.0.0.1:8000/' /etc/php-fpm.d/www.conf ; sed -i 's;.*Handler.*;SetHandler "proxy:fcgi://localhost";' /etc/httpd/conf.d/php.conf


EXPOSE 22 80 8080 3000 3306

CMD "/root/bin/start.sh"
