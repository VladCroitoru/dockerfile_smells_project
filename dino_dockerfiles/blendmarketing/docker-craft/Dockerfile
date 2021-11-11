FROM richarvey/nginx-php-fpm:1.3.10

# Originally From https://github.com/wyveo/craftcms-docker
MAINTAINER Marc Tanis "marc@blendimc.com"

# Set craft cms version
ENV CRAFT_VERSION=2.7 CRAFT_BUILD=3

ENV CRAFT_ZIP=Craft-$CRAFT_VERSION.$CRAFT_BUILD.zip

# Remove default webroot files & set PHP session handler to Redis
RUN sed -i -e "s/memory_limit\s*=\s*.*/memory_limit = 256M/g" ${php_conf}

# Download the latest Craft (https://craftcms.com/support/download-previous-versions)
ADD https://download.buildwithcraft.com/craft/$CRAFT_VERSION/$CRAFT_VERSION.$CRAFT_BUILD/$CRAFT_ZIP /tmp/$CRAFT_ZIP

# Extract craft to webroot & remove default template files
RUN unzip -qqo /tmp/$CRAFT_ZIP 'craft/*' -d /var/www/ && \
    unzip -qqo /tmp/$CRAFT_ZIP 'public/index.php' -d /var/www/ && \
    rm -rf /var/www/craft/templates/*

# Add default craft cms nginx config
RUN mkdir -p /var/www/html/conf/nginx/
ADD ./default.conf /var/www/html/conf/nginx/nginx-site.conf 

# Cleanup
RUN rm /tmp/$CRAFT_ZIP && \
    chown -Rf nginx:nginx /var/www

WORKDIR /var/www

EXPOSE 80
