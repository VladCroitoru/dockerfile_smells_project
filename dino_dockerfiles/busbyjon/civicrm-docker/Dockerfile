FROM wordpress:4-apache

RUN apt-get update && apt-get install -y unzip && rm -rf /var/lib/apt/lists/* 

RUN docker-php-ext-install zip

WORKDIR /usr/src/wordpress/wp-content/plugins

RUN curl -O https://download.civicrm.org/civicrm-4.7.16-wordpress.zip?src=donate

RUN unzip civicrm-4.7.16-wordpress.zip\?src\=donate 

RUN curl -O https://codeload.github.com/drastik/com.drastikbydesign.stripe/zip/4.7.1

RUN mkdir -p ../uploads/civicrm/ext/

RUN unzip 4.7.1 -d ../uploads/civicrm/ext/

RUN mv ../uploads/civicrm/ext/com.drastikbydesign.stripe-4.7.1/ ../uploads/civicrm/ext/com.drastikbydesign.stripe 

RUN curl -O https://downloads.wordpress.org/plugin/civicrm-wp-member-sync.0.3.1.zip

RUN unzip civicrm-wp-member-sync.0.3.1.zip 

RUN chown -R www-data:www-data /usr/src/wordpress

WORKDIR /var/www/html/
