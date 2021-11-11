# vim: set tabstop=4 shiftwidth=4 expandtab :

# Writing Guidelines:
# * https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/
# * http://docs.projectatomic.io/container-best-practices/#

FROM drupal:8.4-fpm

LABEL name="plainlychrist/site-buildbarbuda" \
      version="1.0"

MAINTAINER Jonah.Beckford@plainlychrist.org

WORKDIR /var/www/html

############# Versions

# NGINX: https://hub.docker.com/_/nginx/ 1.13.3
# DRUPAL_SECURITY_REVIEW: as of 9/8/2016, is a dev dependency (https://packagist.drupal-composer.org/packages/drupal/security_review#dev-8.x-1.x), which needs 'git clone'
# NPS: https://developers.google.com/speed/pagespeed/module/release_notes
ENV NGINX_VERSION="1.13.3-1~jessie" \
    DRUSH_MAJOR_VERSION="8" \
    DRUPAL_BACKUP_DB_VERSION="~1.2" \
    DRUPAL_ADVAGG_VERSION="~3.2" \
    DRUPAL_BOOTSTRAP_VERSION="~3.6" \
    MYSQL2SQLITE_VERSION="1b0b5d610c6090422625a2c58d2c23d2296eab3a" \
    DRUPAL_SECURITY_REVIEW_VERSION="~1.3" \
    NPS_VERSION="1.12.34.2" \
    NPS_STREAM="stable" \
    DRUPAL_GROUP_VERSION="~1.0" \
    DRUPAL_ADMIN_TOOLBAR_VERSION="~1" \
    DRUPAL_PATHAUTO_VERSION="~1.0" \
    DRUPAL_METATAG_VERSION="~1.3" \
    DRUPAL_VIEWS_SLIDESHOW_VERSION="~4.5" \
    DRUPAL_DS_VERSION="~3.1" \
    DRUPAL_ADDTOANY_VERSION="~1.8" \
    DRUPAL_GOOGLE_MAP_FIELD_VERSION="~1.4" \
    DRUPAL_TERMS_OF_USE_VERSION="~2.0@dev" \
    DRUPAL_RECAPTCHA_VERSION="~2.2" \
    DRUPAL_GOOGLE_ANALYTICS_VERSION="~2.2" \
    DRUPAL_WEBFORM_VERSION="~5.0" \
    DRUPAL_CONFIG_IGNORE_VERSION="~2.0" \
    DRUPAL_SLICK_MEDIA_VERSION="~1.0" \
    DRUPAL_VIDEO_EMBED_FIELD_VERSION="~1.5" \
    DRUPAL_FILE_BROWSER_VERSION="1.1" \
    DRUPAL_MEDIA_ENTITY_DOCUMENT_VERSION="~1.1" \
    DRUPAL_MEDIA_ENTITY_SLIDESHOW_VERSION="~1.2" \
    DRUPAL_MEDIA_ENTITY_INSTAGRAM_VERSION="~1.4" \
    DRUPAL_MEDIA_ENTITY_TWITTER_VERSION="~1.3" \
    DRUPAL_IMAGE_WIDGET_CROP_VERSION="~2.0" \
    DRUPAL_INLINE_ENTITY_FORM_VERSION="~1.0" \
    DRUPAL_PAGE_MANAGER_VERSION="~4.0" \
    DRUPAL_TWIG_TWEAK_VERSION="~2.0"

########################
######## ROOT ##########
########################

############## APT

# Install gawk so mysql2sqlite does not Segfault on large bootstrap databases
# Install git so that Composer, when fetching dev dependencies, can do a 'git clone'
# Install a database client, which is used by 'drush up' and 'drush sql-dump'
#   mysql-client or sqlite3
# Install postfix and libsasl2-modules and rsyslog for mail delivery
# Install ruby and ruby-dev for 'gem install sass'
# Install self-signed SSL (auto-generated) for HTTPS
# Install supervisor so we can run multiple processes in one container
# Install unzip so 'drush webform-libraries-download' works
RUN apt-get -y update && \
    echo "postfix postfix/mailname string replaceme.hostname.com" | debconf-set-selections && \
    echo "postfix postfix/main_mailer_type string 'Internet Site'" | debconf-set-selections && \
    apt-get -y install \
        gawk \
        git \
        libsasl2-modules \
        mysql-client \
        rsyslog \
        ruby ruby-dev \
        postfix \
        sqlite3 \
        ssl-cert openssl-blacklist \
        supervisor \
        unzip && \
    gem install sass

############## Nginx 1.13.5
# - skips installing nginx-module-*
# - skips remove /var/lib/apt/lists/*

# mimic: apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
# by placing filesystem/etc/apt/trusted.gpg.d/nginx-org.asc in http://manpages.ubuntu.com/manpages/zesty/man8/apt-key.8.html keyring
COPY filesystem/etc/apt/ /etc/apt/
RUN apt-key add /etc/apt/trusted.gpg.d/nginx-org.asc && \
    echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get install --no-install-recommends --no-install-suggests -y \
						ca-certificates \
						nginx=${NGINX_VERSION} \
						gettext-base

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
  && ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80 443

# Install custom PHP extensions
RUN docker-php-ext-install -j "$(nproc)" exif

# Install Google Page Speed Module for nginx
#    https://developers.google.com/speed/pagespeed/module/build_ngx_pagespeed_from_source
##########

RUN apt-get install --no-install-recommends --no-install-suggests -y build-essential zlib1g-dev libpcre3 libpcre3-dev unzip libssl-dev
RUN set -x \
  && cd \
  && NGINX_VERSION=$(nginx -v 2>&1 | sed 's#.*/##') \
  && PS_NGX_EXTRA_FLAGS=$(nginx -V 2>&1 | awk '/configure arguments:/{$1=""; $2=""; print}') \
  && curl -LO https://github.com/pagespeed/ngx_pagespeed/archive/v${NPS_VERSION}-${NPS_STREAM}.zip \
  && unzip v${NPS_VERSION}-${NPS_STREAM}.zip  \
  && cd ngx_pagespeed-${NPS_VERSION}-${NPS_STREAM}/ \
  && psol_url=https://dl.google.com/dl/page-speed/psol/${NPS_VERSION}-${NPS_STREAM}.tar.gz \
  && [ -e scripts/format_binary_url.sh ] && psol_url=$(scripts/format_binary_url.sh PSOL_BINARY_URL) \
  && curl -LO ${psol_url} \
  && echo curl -LO https://dl.google.com/dl/page-speed/psol/${NPS_VERSION}.tar.gz  \
  && echo tar -xzvf ${NPS_VERSION}.tar.gz  \
  && tar -xzvf $(basename ${psol_url}) \
  && cd  \
  && curl -LO http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz  \
  && tar -xvzf nginx-${NGINX_VERSION}.tar.gz \
  && cd nginx-${NGINX_VERSION}/  \
  && echo ./configure --add-dynamic-module=$HOME/ngx_pagespeed-${NPS_VERSION}-${NPS_STREAM} $PS_NGX_EXTRA_FLAGS > /tmp/runit  \
  && sh /tmp/runit  \
  && rm /tmp/runit \
  && make \
  && install -pv ./objs/ngx_pagespeed.so /etc/nginx/modules/  \
  && cd \
  && rm -rf release-${NPS_VERSION}-${NPS_STREAM}.zip ngx_pagespeed-release-${NPS_VERSION}-${NPS_STREAM}/ nginx-${NGINX_VERSION}.tar.gz nginx-${NGINX_VERSION}/ \
  && apt-get remove -y build-essential zlib1g-dev libpcre3-dev 

# Get rid of PHP extensions we don't need
##########

# We won't use: PostgreSQL (comes from Drupal Dockerfile)
RUN rm -f /usr/local/etc/php/conf.d/docker-php-ext-pdo_pgsql.ini

########################
###### DRUPALADMIN #####
########################

# POSIX permissions: https://www.drupal.org/node/244924
# Keep uid and gid stable across all Docker containers by setting to 200
RUN addgroup --system  --gid 200 drupaladmin
RUN adduser --system  --uid 200 --ingroup drupaladmin --shell /bin/false drupaladmin

# Give it the permissions it needs
RUN chown -R drupaladmin \
        /var/www/html/composer.json \
        /var/www/html/composer.lock \
        /var/www/html/modules \
        /var/www/html/profiles \
        /var/www/html/themes \
        /var/www/html/vendor
RUN chmod o+w \
        /var/www/html/modules \
        /var/www/html/profiles \
        /var/www/html/themes \
        /var/www/html/vendor

# Switch to drupaladmin
USER drupaladmin

############# Composer

# Install Composer with the phar file.
RUN install -d ~/bin
RUN curl -fsSL "https://getcomposer.org/installer" | php -- --install-dir ~/bin --filename=composer && \
        chmod +x ~/bin/composer

# Choose where to install packages from
RUN ~/bin/composer config repositories.drupal composer https://packages.drupal.org/8

############# Drush

# Install Drush with Composer: http://www.whaaat.com/installing-drush-8-using-composer
RUN ~/bin/composer global require \
        drush/drush:${DRUSH_MAJOR_VERSION}.*
RUN ln -s ~/.composer/vendor/bin/drush ~/bin/

# Test your install.
RUN ~/bin/drush core-status

# Install Webform libraries
#  We need a Drupal installation to do this :(
#   https://www.drupal.org/docs/8/modules/webform/webform-libraries
USER root
RUN rsync -ap sites/default/ sites/default-moveback && \
    install -o drupaladmin -g www-data -d /tmp/webform-libraries-sqlite && \
    ~drupaladmin/bin/drush -y site-install standard install_configure_form.enable_update_status_module=NULL install_configure_form.enable_update_status_emails=NULL --db-url="sqlite:///tmp/webform-libraries-sqlite/.ht.sqlite" && \
    ~drupaladmin/bin/drush en webform -y && \
    ~drupaladmin/bin/drush webform-libraries-download && \
    rm -rf /tmp/webform-libraries-sqlite sites/default && \
    mv sites/default-moveback sites/default
USER drupaladmin

# Modules
#   To mitigate docker build running out of memory, we split up the composer require commands
#########

# config_installer: Because of bug https://www.drupal.org/node/1613424, we need this custom install profile
RUN ~/bin/drush dl config_installer

# Install Backup and Migrate
# Install Advanced CSS/JS Aggregation
# Install Security Review
# Install Group
# Install Admin Toolbar
# Install PathAuto
# Install Metatag
# Install Views Slideshow
# Install Display Suite
# Install Google Map Field
# Install AddToAny
# Install Terms of Use
# Install Google Analytics
# Install reCAPTCHA
# Install Webform
# Install Config Ignore
# Install Media (from https://github.com/drupal-media/media pre-8.4)
#   Install Slick Media
#   Install Video Embed Field
#   Install File Browser
#   Install Media Entity Slideshow
#   Install Media Entity Instagram
#   Install Media Entity Twitter
#   Install Media Entity Document
#   Install Image Widget Crop
# Install Inline Entity Form (from https://drupal-media.gitbooks.io/drupal8-guide/content/modules/media/installation.html)
RUN ~/bin/composer require \
        "drupal/backup_db ${DRUPAL_BACKUP_DB_VERSION}" \
        "drupal/advagg ${DRUPAL_ADVAGG_VERSION}" \
        "drupal/security_review ${DRUPAL_SECURITY_REVIEW_VERSION}" \
        "drupal/group ${DRUPAL_GROUP_VERSION}" \
        "drupal/admin_toolbar ${DRUPAL_ADMIN_TOOLBAR_VERSION}" \
        "drupal/pathauto ${DRUPAL_PATHAUTO_VERSION}" \
        "drupal/metatag ${DRUPAL_METATAG_VERSION}" \
        "drupal/views_slideshow ${DRUPAL_VIEWS_SLIDESHOW_VERSION}" \
        "drupal/ds ${DRUPAL_DS_VERSION}" \
        "drupal/google_map_field ${DRUPAL_GOOGLE_MAP_FIELD_VERSION}" \
        "drupal/addtoany ${DRUPAL_ADDTOANY_VERSION}" \
        "drupal/terms_of_use ${DRUPAL_TERMS_OF_USE_VERSION}" \
        "drupal/google_analytics ${DRUPAL_GOOGLE_ANALYTICS_VERSION}" \
        "drupal/recaptcha ${DRUPAL_RECAPTCHA_VERSION}" \
        "drupal/webform ${DRUPAL_WEBFORM_VERSION}" \
        "drupal/config_ignore ${DRUPAL_CONFIG_IGNORE_VERSION}" \
        "drupal/slick_media ${DRUPAL_SLICK_MEDIA_VERSION}" \
        "drupal/video_embed_field ${DRUPAL_VIDEO_EMBED_FIELD_VERSION}" \
        "drupal/file_browser ${DRUPAL_FILE_BROWSER_VERSION}" \
        "drupal/media_entity_document ${DRUPAL_MEDIA_ENTITY_DOCUMENT_VERSION}" \
        "drupal/media_entity_slideshow ${DRUPAL_MEDIA_ENTITY_SLIDESHOW_VERSION}" \
        "drupal/media_entity_instagram ${DRUPAL_MEDIA_ENTITY_INSTAGRAM_VERSION}" \
        "drupal/media_entity_twitter ${DRUPAL_MEDIA_ENTITY_TWITTER_VERSION}" \
        "drupal/image_widget_crop ${DRUPAL_IMAGE_WIDGET_CROP_VERSION}" \
        "drupal/inline_entity_form ${DRUPAL_INLINE_ENTITY_FORM_VERSION}" \
        "drupal/page_manager ${DRUPAL_PAGE_MANAGER_VERSION}" \
        "drupal/twig_tweak ${DRUPAL_TWIG_TWEAK_VERSION}"

# Install Drupal 8 (pre-8.4) media module
RUN cd modules && git clone https://github.com/drupal-media/media.git

# Modify Media so it uses our family permissions
USER root
RUN find . -regex '.*/src/Entity/Media.php' -print0 | xargs --verbose -0 sed -i 's#Drupal\\media_entity\\MediaAccessController#Drupal\\family_organization_permissions\\FamilyOrganizationMediaAccessController#'
USER drupaladmin

# Install Bootstrap base theme
RUN ~/bin/composer require \
        "drupal/bootstrap ${DRUPAL_BOOTSTRAP_VERSION}"

# Install mysql2sqlite
RUN curl "https://raw.githubusercontent.com/dumblob/mysql2sqlite/${MYSQL2SQLITE_VERSION}/mysql2sqlite" > ~/bin/mysql2sqlite && \
        chmod +x ~/bin/mysql2sqlite

# Clean up drupaladmin
##########

RUN ~/bin/composer clear-cache

########################
######## ROOT ##########
########################

USER root

# Clean up space and unneeded packages
##########

RUN apt-get autoremove -y && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Configuration
#########

COPY filesystem/etc/ /etc/
COPY filesystem/usr/local/etc/ /usr/local/etc/
RUN rm -f /usr/local/etc/php-fpm.d/zz-docker.conf

# External libraries
#   http://cgit.drupalcode.org/views_slideshow/tree/README.txt
RUN mkdir -p libraries/jquery.cycle && cd libraries/jquery.cycle && curl -LO https://malsup.github.io/jquery.cycle.all.js \
    && mkdir -p ../../libraries/jquery.hoverIntent && cd ../../libraries/jquery.hoverIntent && curl -LO http://cherne.net/brian/resources/jquery.hoverIntent.js \
    && mkdir -p ../../libraries/json2 && cd ../../libraries/json2 && curl -LO https://raw.githubusercontent.com/douglascrockford/JSON-js/master/json2.js
#   Views Slideshow needs jquery.pause, but it isn't documented except during 'drush en'
RUN cd libraries && git clone https://github.com/tobia/Pause.git jquery.pause
#   https://drupal.org/project/file_browser
RUN cd libraries && git clone https://github.com/enyo/dropzone.git && git clone https://github.com/desandro/imagesloaded.git && git clone https://github.com/desandro/masonry.git
#   https://www.drupal.org/project/slick
RUN cd libraries && git clone https://github.com/kenwheeler/slick.git && git clone https://github.com/gdsmith/jquery.easing.git
#   https://drupal-media.gitbooks.io/drupal8-guide/content/modules/media/installation.html
RUN cd libraries && git clone https://github.com/fengyuanchen/cropper.git && git clone https://github.com/dinbror/blazy.git

# Initial configuration for the 'all' site ...
COPY filesystem/var/www/html/ /var/www/html
RUN chown -R www-data:www-data /var/www/html/sites/all/modules /var/www/html/sites/all/themes && \
    chown www-data:www-data /var/www/html/*

# Compile themes

RUN install -o drupaladmin -g www-data -m 750 -d /var/www/html/sites/all/themes/directjude/css && \
        sass \
            --no-cache \
            --default-encoding UTF-8 \
            /var/www/html/sites/all/themes/directjude/sass/style.scss \
            /var/www/html/sites/all/themes/directjude/css/style.css && \
        test -e /var/www/html/sites/all/themes/directjude/css/style.css

# Clean up space and unneeded packages (we don't need SASS and hence Ruby anymore)

RUN gem cleanup all && \
        apt-get -y remove ruby unzip && \
        apt-get autoremove -y && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Snippets used to build the settings.php and .htacess
COPY settings/ /var/lib/site/settings

# Installation
############

COPY filesystem/var/lib/site/ /var/lib/site/
RUN chmod 500 /var/lib/site/bin/*.sh && \
  chown www-data /var/lib/site/bin/sanitized-backup.sh && \
  install -o drupaladmin -g www-data -m 750 -d /var/www/html/sites/default && \
  install -o drupaladmin -g www-data -m 770 -d /var/www/private && \
  chown -R drupaladmin:www-data /var/lib/site/merge-config

ENTRYPOINT ["/var/lib/site/bin/entry.sh"]
