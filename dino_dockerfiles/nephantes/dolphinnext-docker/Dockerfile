FROM ubuntu:xenial
MAINTAINER Alper Kucukural <alper.kucukural@umassmed.edu>
RUN echo "start"
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get dist-upgrade
 
# Install apache, PHP, and supplimentary programs. curl and lynx-cur are for debugging the container.
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 \
                    curl mysql-server libreadline-dev libsqlite3-dev libbz2-dev libssl-dev python python-dev \
                    libmysqlclient-dev python-pip git expect default-jre default-jdk \
                    libxml2-dev software-properties-common gdebi-core wget \
                    tree vim libv8-dev subversion g++ gcc gfortran zlib1g-dev libreadline-dev \
                    libx11-dev xorg-dev libbz2-dev liblzma-dev libpcre3-dev libcurl4-openssl-dev \
                    bzip2 ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 sendmail \
                    mercurial subversion libarchive-dev uuid-dev squashfs-tools build-essential \
                    libgpgme11-dev libseccomp-dev pkg-config 


RUN apt-get clean
RUN pip install simple-crypt mysql-connector
RUN add-apt-repository -y ppa:opencpu/opencpu-2.1
RUN LC_ALL=C.UTF-8 apt-add-repository ppa:ondrej/php
RUN apt-get update
RUN apt-get -y install php7.2 ssh openssh-server \
    php-pear php7.2-curl php7.2-dev php7.2-gd php7.2-mbstring php7.2-zip php7.2-mysql \ 
    php7.2-xml php7.2-ldap s3cmd

# Enable apache mods.
RUN a2enmod rewrite

# Update the PHP.ini file, enable <? ?> tags and quieten logging.
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php/7.2/apache2/php.ini
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING | E_PARSE/" /etc/php/7.2/apache2/php.ini
 
# Manually set up the apache environment variables
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

# Update the default apache site with the config we created.
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf

RUN echo "ServerName localhost" | tee /etc/apache2/conf-available/fqdn.conf
RUN a2enconf fqdn

RUN echo "locale-gen en_US.UTF-8"
RUN echo "dpkg-reconfigure locales"
 
# Copy site into place.

RUN find /var/lib/mysql -type f -exec touch {} \; && service mysql start && \ 
    service apache2 start && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install phpmyadmin php-mbstring php-gettext && \ 
    zcat /usr/share/doc/phpmyadmin/examples/create_tables.sql.gz|mysql -uroot

RUN usermod -d /var/lib/mysql/ mysql

RUN sed -i "s#// \$cfg\['Servers'\]\[\$i\]\['AllowNoPassword'\] = TRUE;#\$cfg\['Servers'\]\[\$i\]\['AllowNoPassword'\] = TRUE;#g" /etc/phpmyadmin/config.inc.php 
RUN ln -s /etc/phpmyadmin/apache.conf /etc/apache2/conf-enabled/phpmyadmin.conf

RUN sed -i "s/|\s*\((count(\$analyzed_sql_results\['select_expr'\]\)/| (\1)/g" /usr/share/phpmyadmin/libraries/sql.lib.php

RUN apt-get -y autoremove

# Define working directory.
WORKDIR /data

RUN curl -s https://get.nextflow.io | bash 
RUN mv /data/nextflow /usr/bin/.
RUN chmod 755 /usr/bin/nextflow
RUN mkdir /.nextflow
RUN chmod 777 /.nextflow
                     
RUN wget https://phar.phpunit.de/phpunit-7.0.2.phar
RUN chmod +x phpunit-7.0.2.phar
RUN mv phpunit-7.0.2.phar /usr/local/bin/phpunit

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

ENV GITUSER=UMMS-Biocore
RUN git clone https://github.com/${GITUSER}/dolphinnext.git /var/www/html/dolphinnext

RUN chown -R ${APACHE_RUN_USER}:${APACHE_RUN_GROUP} /var/www/html/dolphinnext

RUN find /var/lib/mysql -type f -exec touch {} \; && service mysql start && \  
    mysql -u root -e 'CREATE DATABASE dolphinnext;' && \
    cat /var/www/html/dolphinnext/db/dolphinnext.sql|mysql -uroot dolphinnext && \
    python /var/www/html/dolphinnext/scripts/updateDN.py

RUN cd /usr/local/share && wget https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/edirect.tar.gz && \
    tar xvfz edirect.tar.gz && \
    rm edirect.tar.gz && \
    cd edirect && ./setup.sh
RUN mv /usr/local/share/edirect/* /usr/local/sbin/.

RUN wget https://dl.google.com/go/go1.12.7.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.12.7.linux-amd64.tar.gz && \
    export PATH=$PATH:/usr/local/go/bin && \
    export VERSION=3.2.1 && \ 
    wget https://github.com/sylabs/singularity/releases/download/v${VERSION}/singularity-${VERSION}.tar.gz && \
    tar -xzf singularity-${VERSION}.tar.gz && \ 
    cd singularity && ./mconfig && make -C ./builddir && make -C ./builddir install

ADD bin /usr/local/bin


# Downloading gcloud package
RUN curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz
RUN mkdir -p /usr/local/gcloud \
  && tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz \
  && /usr/local/gcloud/google-cloud-sdk/install.sh
ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin

RUN echo "DONE!"

