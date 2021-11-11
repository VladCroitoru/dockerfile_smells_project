FROM samos123/drupal
MAINTAINER Frédéric Vachon <frederic.vachon@savoirfairelinux.com>

RUN apt-get update && apt-get install -y vim sudo openssh-server wget

RUN apt-get update && \
	apt-get install -y subversion python-setuptools && \
	svn checkout https://github.com/savoirfairelinux/monitoring-tools/branches/drupal/plugins/check-drupal-cache /opt/drupal_cache && \
	svn checkout https://github.com/savoirfairelinux/monitoring-tools/branches/drupal/plugins/check-drupal-codebase /opt/drupal_codebase && \
	svn checkout https://github.com/savoirfairelinux/monitoring-tools/branches/drupal/plugins/check-drupal-cron /opt/drupal_cron && \
	svn checkout https://github.com/savoirfairelinux/monitoring-tools/branches/drupal/plugins/check-drupal-database /opt/drupal_database && \
	svn checkout https://github.com/savoirfairelinux/monitoring-tools/branches/drupal/plugins/check-drupal-extensions /opt/drupal_extensions && \
	svn checkout https://github.com/savoirfairelinux/monitoring-tools/branches/drupal/plugins/check-drupal-logging /opt/drupal_logging && \
	svn checkout https://github.com/savoirfairelinux/monitoring-tools/branches/drupal/plugins/check-drupal-security /opt/drupal_security && \
	svn checkout https://github.com/savoirfairelinux/monitoring-tools/branches/drupal/plugins/check-drupal-status /opt/drupal_status && \
	svn checkout https://github.com/savoirfairelinux/monitoring-tools/branches/drupal/plugins/check-drupal-views /opt/drupal_views && \
	chmod +x /opt/drupal_cache/shinkenplugins/plugins/drupal_cache/drupal_cache.py && \
	chmod +x /opt/drupal_codebase/shinkenplugins/plugins/drupal_codebase/drupal_codebase.py && \
	chmod +x /opt/drupal_cron/shinkenplugins/plugins/drupal_cron/drupal_cron.py && \
	chmod +x /opt/drupal_database/shinkenplugins/plugins/drupal_database/drupal_database.py && \
	chmod +x /opt/drupal_extensions/shinkenplugins/plugins/drupal_extensions/drupal_extensions.py && \
	chmod +x /opt/drupal_logging/shinkenplugins/plugins/drupal_logging/drupal_logging.py && \
	chmod +x /opt/drupal_security/shinkenplugins/plugins/drupal_security/drupal_security.py && \
	chmod +x /opt/drupal_status/shinkenplugins/plugins/drupal_status/drupal_status.py && \
	chmod +x /opt/drupal_views/shinkenplugins/plugins/drupal_views/drupal_views.py && \
	apt-get remove -y subversion && \
	cd /opt/drupal_cache && \
	python setup.py develop

RUN sed -i 's/allow_url_fopen = off/allow_url_fopen = On/g' /usr/local/etc/php/conf.d/drupal-recommends.ini

RUN adduser nagios && adduser nagios www-data
USER nagios

COPY home/nagios/.bashrc /home/nagios/.bashrc

ENV COMPOSER_BIN_DIR=/home/nagios/bin
RUN mkdir /home/nagios/bin
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/home/nagios/bin --filename=composer \
	&& /home/nagios/bin/composer global require drush/drush:7.* \
	&& /home/nagios/bin/drush cc drush

RUN echo 'check_certificate = off' > /home/nagios/.wgetrc
RUN /home/nagios/bin/drush pm-download site_audit

USER root
RUN echo 'check_certificate = off' > /root/.wgetrc

WORKDIR /var/www/html

RUN drush pm-download site_audit
RUN drush pm-download advanced_forum-7.x-2.1
RUN drush pm-download panels-7.x-3.1
RUN drush pm-download views-7.x-3.1

# Install and configure NRPE
RUN apt-get update && apt-get install -y nagios-nrpe-server supervisor
COPY etc/nagios/nrpe.cfg /etc/nagios/nrpe.cfg

COPY entrypoint.sh /
