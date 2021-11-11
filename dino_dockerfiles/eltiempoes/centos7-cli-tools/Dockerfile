FROM centos:7
ENV REFRESHED_AT 2021-08-24
LABEL maintainer "it@eltiempo.es"
LABEL version "1.4"
LABEL description "Image with some cli tools for dev environment"
ENV container docker

RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
    rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm && \
    rpm -Uvh https://rpms.remirepo.net/enterprise/remi-release-7.rpm && \
    rpm -Uvh http://www.city-fan.org/ftp/contrib/yum-repo/rhel7/x86_64/city-fan.org-release-2-1.rhel7.noarch.rpm && \
    yum -y --setopt=tsflags=nodocs update && \
    yum -y --setopt=tsflags=nodocs upgrade && \
    yum -y install yum-utils && \
    yum-config-manager --enable remi-php74 && \
    yum -y --setopt=tsflags=nodocs install epel-release && \
    yum -y --setopt=tsflags=nodocs install nginx net-tools vim mariadb wget curl && \
    yum -y --setopt=tsflags=nodocs install php php-cli php-gd php-mbstring php-mysqlnd php-opcache php-pdo php-xml php-pecl-xdebug php-imap php-tidy php-xmlrpc php-soap php-mcrypt php-intl php-pecl-zip && \
    yum -y --setopt=tsflags=nodocs groupinstall 'Development Tools' && \
    yum -y --setopt=tsflags=nodocs --enablerepo=city-fan.org install libcurl && \
    yum clean all

RUN yum -y --setopt=tsflags=nodocs install grib_api && \
    yum clean all

RUN php -r "readfile('http://getcomposer.org/installer');" | php -- --install-dir=/usr/bin/ --filename=composer --version=2.0.12 

RUN curl -L -s https://cs.symfony.com/download/php-cs-fixer-v3.phar -o /usr/local/bin/php-cs-fixer && \
    chmod +x /usr/local/bin/php-cs-fixer

RUN curl -L -s https://phar.phpunit.de/phpunit.phar -o /usr/local/bin/phpunit && \
    chmod +x /usr/local/bin/phpunit

RUN curl -L -s https://codeception.com/codecept.phar -o /usr/local/bin/codecept && \
    chmod +x /usr/local/bin/codecept

RUN groupadd --gid 1000 cli-user && \
	adduser -u 1000 -g 1000 cli-user 

RUN yum -y --setopt=tsflags=nodocs install sudo

RUN echo "cli-user ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/cli-user && \
    chmod 0440 /etc/sudoers.d/cli-user

USER cli-user
RUN mkdir /home/cli-user/nvm
ENV NVM_DIR /home/cli-user/nvm
ENV NODE_VERSION v11.10.0
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash && \
	source $NVM_DIR/nvm.sh && \
	nvm install $NODE_VERSION && \
	nvm alias default $NODE_VERSION && \
    nvm use default && \
	npm install -g bower && \
	npm install gulp-cli -g

ENV NODE_PATH $NVM_DIR/$NODE_VERSION/lib/node_modules
ENV PATH      $NVM_DIR/$NODE_VERSION/bin:$PATH

WORKDIR /home/cli-user