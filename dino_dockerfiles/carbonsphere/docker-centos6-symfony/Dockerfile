############################################################
# Dockerfile: CentOS6 & Symfony Base Container
############################################################
FROM centos:centos6

MAINTAINER CarbonSphere <CarbonSphere@gmail.com>

# Set environment variable
ENV HOME 						/root
ENV TERM 						xterm
ENV SYMFONYPROJECTNAME 			myProject
ENV CARBON_MYSQL_DB_HOST		db
ENV CARBON_MYSQL_DB_PORT		3306
ENV CARBON_APP_NAME				symfonydb
ENV CARBON_MYSQL_DB_USERNAME	symfonyusr
ENV CARBON_MYSQL_DB_PASSWORD	symfonypas
ENV CARBON_MAILER_TRANS			smtp
ENV CARBON_MAILER_HOST			127.0.0.1
ENV CARBON_MAILER_USER			null
ENV CARBON_MAILER_PASS			null
ENV CARBON_SECRET				DEFAULT_SECRET


# Install EPEL repo
RUN yum -y install epel-release

# Install tools
RUN yum -y install vim git openssh-server mysql

# Install Supervisord
RUN yum -y install python-setuptools; easy_install supervisor
ADD supervisor/supervisord.conf /etc/supervisord.conf

# Add Create User & App DB to remote linked DB container
ADD createUserDb.sh /root/createUserDb.sh 		
RUN chmod 755 /root/createUserDb.sh 			# Initialize Remote DB and Account

# Install php 5.4 and install repo
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm; \
    rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm; \
    yum -y --enablerepo=remi,remi-test install httpd php php-common; \
    yum -y --enablerepo=remi,remi-test install php-pecl-apc php-cli php-pear php-pdo php-mysql php-pgsql php-pecl-mongo php-sqlite php-pecl-memcache php-pecl-memcached php-gd php-mbstring php-mcrypt php-xml php-intl

# Modify php.ini
RUN sed -i "s/;date.timezone =.*/date.timezone = Asia\/Taipei/g" /etc/php.ini

# Modify sshd_config
RUN sed -i "s/#PermitRootLogin yes/PermitRootLogin without-password/g" /etc/ssh/sshd_config
RUN sed -i "s/PasswordAuthentication yes/PasswordAuthentication no/g" /etc/ssh/sshd_config

# Help script to auto-generate new keys
ADD changesshkey.sh /root/changesshkey.sh
RUN chmod +x /root/changesshkey.sh

# Add sshd to supervisord
ADD supervisor/sshd.conf /etc/supervisor/conf.d/sshd.conf
ADD supervisor/symfony.conf /etc/supervisor/conf.d/symfony.conf

# Setup root login with ssh-keys, run changesshkey.sh to change your key
RUN mkdir /root/.ssh; \
	chmod 700 /root/.ssh; \
    cd /root/.ssh; \
    ssh-keygen -f docker-server.rsa -t rsa -N ''; \
    cat docker-server.rsa.pub > /root/.ssh/authorized_keys; \
    chmod 600 /root/.ssh/authorized_keys;

# Start SSHD first time to generate RSA & DSA keys
RUN service sshd start

# Add sshd to supervisord
ADD supervisor/sshd.conf /etc/supervisor/conf.d/sshd.conf

# Install composer
RUN cd /root; curl -sS https://getcomposer.org/installer | php; \
    mv composer.phar /usr/local/bin/composer;

# Install Symfony 2.6
RUN curl -LsS http://symfony.com/installer -o /usr/local/bin/symfony; \
    chmod a+x /usr/local/bin/symfony

# Create default symfony project
RUN cd /root; \
	symfony new $SYMFONYPROJECTNAME; \
	chown -R apache:apache $SYMFONYPROJECTNAME; \
	chmod -R 755 $SYMFONYPROJECTNAME; \
	cd $SYMFONYPROJECTNAME; \
	php app/console assets:install --env=dev; \
	php app/console assetic:dump --env=dev;


# Modify symfony.conf to use current default project name
RUN sed -i "s/SYMFONYPROJECTNAME/${SYMFONYPROJECTNAME}/g" /etc/supervisor/conf.d/symfony.conf

# Update Composer -- Removed, You can manually update symfony
# RUN cd /root/$SYMFONYPROJECTNAME; composer update;

# Add Parameter replacer file
ADD symfony/params.php /root/$SYMFONYPROJECTNAME/app/config/params.php

# Change parameter replacer owner and permission
RUN chmod 755 /root/$SYMFONYPROJECTNAME/app/config/params.php; \
	chown apache:apache /root/$SYMFONYPROJECTNAME/app/config/params.php;

# Add params.php to config.yml after parameters.yml
RUN sed -i "s/parameters.yml }/parameters.yml }\n    - { resource: params.php }/g" /root/$SYMFONYPROJECTNAME/app/config/config.yml;

# Initialize git
RUN cd /root/$SYMFONYPROJECTNAME; \
	git init; \
	git add .; \
	git commit -am "Project Initial status "; \
	git config receive.denyCurrentBranch ignore; 

# Add post recieve script to default project
ADD git/post-receive /root/$SYMFONYPROJECTNAME/.git/hooks/post-receive

# Modify post-receive script
RUN sed -i "s/SYMFONYPROJECTNAME/$SYMFONYPROJECTNAME/g" /root/$SYMFONYPROJECTNAME/.git/hooks/post-receive

# Change permission
RUN chmod 755 /root/$SYMFONYPROJECTNAME/.git/hooks/post-receive

# Change timezone to Taipei
RUN echo y | cp -p /usr/share/zoneinfo/Asia/Taipei /etc/localtime

# Display Private Key
RUN cat /root/.ssh/docker-server.rsa

# Generate New Secret Key and insert into environment variable
RUN CARBON_SECRET=`cat /dev/urandom | tr -cd 'a-f0-9' | head -c 40`; \
	echo $CARBON_SECRET;

# 80:Symfony 22:sshd
EXPOSE 80 22

# Display Messages
RUN echo "Once linked with DB container, must run /root/createUserDb.sh to initialize remote DB container"

# Exec supervisord
CMD ["/usr/bin/supervisord","-c","/etc/supervisord.conf"]
