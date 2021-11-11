FROM amazonlinux:2017.09

RUN echo "OS dependencies" && \
    yum -y install \
      git \
      unzip && \
    echo "NETWORKING=yes" > /etc/sysconfig/network && \
    echo "Supervisord dependencies" && \
    curl https://bootstrap.pypa.io/ez_setup.py | /usr/bin/python && \
    easy_install pip && \
    pip install supervisor && \
    echo "Apache and MySQL dependencies" && \
    yum -y install \
      httpd24 \
      mod24_ssl \
      mysql \
      mysql-server && \
    echo "Start mysqld to create initial tables" && \
    service mysqld start && \
    echo "PHP dependencies" && \
    yum install -y \
      php71 \
      php71-cli \
      php71-dbg \
      php71-gd \
      php71-intl \
      php71-json \
      php71-mbstring \
      php71-mcrypt \
      php71-mysqlnd \
      php71-opcache \
      php71-pdo \
      php71-pecl-redis \
      php71-zip && \
    echo "Install composer" && \
    curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer && \
    echo "Install prestissimo to speed up composer installation" && \
    composer global require hirak/prestissimo && \
    echo "NodeJS dependencies" && \
    curl --silent --location https://rpm.nodesource.com/setup_9.x | bash - && \
    yum -y install \
      nodejs \
      npm && \
    echo "Directory setup" && \
    mkdir -p /home/develop/logs && \
    mkdir -p /home/develop/apps/htdocs && \
    mkdir -p /etc/httpd/certs
