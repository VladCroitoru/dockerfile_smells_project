FROM phusion/baseimage:0.9.15
MAINTAINER Quang Dinh <ngocquangbb@gmail.com>


# Ensure UTF-8
RUN locale-gen en_US.UTF-8
ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8

# Upgrade for PHP 5.6
# note: triggers non-fatal error due to non-ASCII characters in repo name
#       (gpg: key E5267A6C: public key "Launchpad PPA for Ond\xc5\x99ej Sur�" imported)
# You can safely ignore that error
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C \
 && add-apt-repository -y ppa:ondrej/php5-5.6 \
 && apt-key update \
 && apt-get update -y

# Install base packages
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -yq install \
        vim \
        wget \
        build-essential \
        python-software-properties \
        python-pip \
        python-setuptools \
        supervisor \
        curl \
        php5 \
        apache2 \
        libapache2-mod-php5 \
        php5-json \
        php5-xsl \
        php5-mysql \
        php5-mcrypt \
        php5-gd \
        php5-curl \
        php-pear \
        php5-redis \
        php5-memcached \
        php-apc && \
    rm -rf /var/lib/apt/lists/* && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# apt clean
RUN apt-get clean & rm -rf /var/lib/apt/lists/*


RUN /usr/sbin/php5enmod mcrypt
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \
    sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g" /etc/php5/apache2/php.ini

RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php5/apache2/php.ini
RUN sed -i 's/memory_limit\ =\ 128M/memory_limit\ =\ 2G/g' /etc/php5/apache2/php.ini
RUN sed -i "s/AllowOverride None/AllowOverride All/g" /etc/apache2/apache2.conf
#RUN sed -i 's/\;date\.timezone\ =/date\.timezone\ =\ Asia\/Ho_Chi_Minh/g' /etc/php5/apache2/php.ini
RUN sed -i 's/upload_max_filesize\ =\ 2M/upload_max_filesize\ =\ 200M/g' /etc/php5/apache2/php.ini
RUN sed -i 's/post_max_size\ =\ 8M/post_max_size\ =\ 200M/g' /etc/php5/apache2/php.ini
RUN sed -i 's/max_execution_time\ =\ 30/max_execution_time\ =\ 3600/g' /etc/php5/apache2/php.ini
RUN sed -i 's/\;error_log\ =\ syslog/error_log\ =\ syslog/g' /etc/php5/apache2/php.ini
RUN sed -i 's/short_open_tag\ =\ Off/short_open_tag\ =\ On/g' /etc/php5/apache2/php.ini



# enable apache modules
RUN a2enmod rewrite ssl headers php5 expires

# install envtpl for replace
RUN pip install envtpl

# Copy startup script for getting environment information such as config...
ADD startup.sh      /var/startup.sh
RUN chmod +x /var/startup.sh

#ENV ALLOW_OVERRIDE **False**

# syslog-ng loggly config
ADD logentries.conf.tpl /etc/syslog-ng/conf.d/logentries.conf.tpl

#IF USE host key logentries
#RUN wget https://raw.github.com/logentries/le/master/install/linux/logentries_install.sh && sudo bash logentries_install.sh
#ADD tasks.sh.tpl /var/tasks.sh.tpl

# supervisord config
ADD supervisord.conf /etc/supervisord.conf

RUN rm -fr /var/www/html
ADD www/src /var/www/html
WORKDIR /var/www/html

EXPOSE 80 443
# Create private folder for download config
RUN mkdir /var/www/private

CMD [ "/var/startup.sh" ]
