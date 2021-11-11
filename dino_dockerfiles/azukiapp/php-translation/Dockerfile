FROM azukiapp/php-fpm
MAINTAINER Azuki <support@azukiapp.com>

# Install phd
RUN git clone https://git.php.net/repository/phd.git \
  && cd phd \
  && sudo pear install package.xml package_generic.xml package_php.xml

# Install web-php-master
RUN cd / \
  && curl -L https://github.com/php/web-php/archive/master.zip -o master.zip \
  && unzip master.zip \
  && rm -Rf /var/www/* \
  && rsync -avzC --timeout=600 --delete --delete-after --exclude='distributions/**' \
     --exclude='extra/**' --exclude='backend/notes/**' \
     -- /web-php-master/ /var/www/ \
  && rm -Rf master.zip web-php-master

EXPOSE 80
