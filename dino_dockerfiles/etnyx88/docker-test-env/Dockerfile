FROM debian:stable
RUN apt-get update -y && apt-get upgrade -y && \
 DEBIAN_FRONTEND=noninteractive apt-get install -y locales && \
 sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
 dpkg-reconfigure --frontend=noninteractive locales && \
 update-locale LANG=en_US.UTF-8 && \
 apt-get install -y \
  git curl gnupg imagemagick \
  apache2 libapache2-mod-php \
  php-cli php-curl php-mysql php-xml php-zip php-gd php-mbstring php-bz2 \
  mariadb-server mariadb-client openssh-client \
  composer yarnpkg build-essential ruby ruby-dev grunt && \
 alias yarn=yarnpkg && \
 gem install sass compass && \
 curl -sS -L https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
 ls -la /etc/apt/sources.list.d/ && \
 echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
 apt-get update -y && \
 apt-get install -y google-chrome-stable && \
 ln -s $(which yarnpkg) /usr/bin/yarn && \
 printf "<VirtualHost *:80>\nServerName project.lc\nServerAlias www.project.lc en.project.lc ru.project.lc de.project.lc es.project.lc prc.project.lc\nDocumentRoot /builds/project.lc/www/doc_root\nRewriteEngine On\nphp_admin_value open_basedir /builds/project.lc/www:/tmp\nLimitInternalRecursion 20\n<Directory /builds/project.lc/www>\nAllowOverride All\nRequire all granted\n</Directory>\n</VirtualHost>\n<VirtualHost *:443>\nServerName project.lc\nServerAlias www.project.lc en.project.lc ru.project.lc de.project.lc es.project.lc prc.project.lc\nDocumentRoot /builds/project.lc/www/doc_root\nRewriteEngine On\nphp_admin_value open_basedir /builds/project.lc/www:/tmp\nLimitInternalRecursion 20\n<Directory /builds/project.lc/www>\nAllowOverride All\nRequire all granted\n</Directory>\nSSLEngine on\nSSLCertificateFile /etc/ssl/certs/ssl-cert-snakeoil.pem\nSSLCertificateKeyFile /etc/ssl/private/ssl-cert-snakeoil.key\n</VirtualHost>" > /etc/apache2/sites-enabled/project.lc.conf && \
 a2enmod rewrite && \
 a2enmod ssl && \
 service mysql restart && \
 service apache2 restart && \
 touch db.sql && \
 printf "CREATE DATABASE \`project\`;\nCREATE USER project@localhost IDENTIFIED VIA mysql_native_password USING '*23AE809DDACAF96AF0FD78ED04B6A265E05AA257';\nGRANT ALL PRIVILEGES ON * . * TO 'project'@'localhost';\nFLUSH PRIVILEGES;\n" > db.sql && \
 mysql < db.sql

ENV LANG en_US.UTF-8
