# Version modified from driket54/glpi

FROM monsantoco/min-jessie:latest
MAINTAINER SJACOUTY

# Installation d'Apache
RUN apt-get update && apt-get install -y apache2 \
	&& rm -rf /var/lib/apt/lists/*

# Installation de PHP et des extensions nécessaires
RUN apt-get update && apt-get install -y \
  wget \
  php5 \
  php5-mysql \
  php5-ldap \
  php5-xmlrpc \
  curl \
  php5-curl \
  php5-gd \
  php5-snmp \
  && rm -rf /var/lib/apt/lists/*
  
# Activation module rewrite et arrêt d'Apache
RUN a2enmod rewrite && service apache2 stop

WORKDIR /var/www/html

# Exécution de script d'installation et paramétrage de GLPI
COPY start.sh /opt/
RUN chmod +x /opt/start.sh
CMD /opt/start.sh

RUN usermod -u 1000 www-data

EXPOSE 80
