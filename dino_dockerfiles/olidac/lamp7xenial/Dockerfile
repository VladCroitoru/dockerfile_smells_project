# Version: 1.0.0
FROM webmaestro365/lamp7xenial
# Based on tutum/lamp maintained by Fernando Mayo <fernando@tutum.co>, Feng Honglin <hfeng@tutum.co>
MAINTAINER A. Datta <intersoftbengal@ymail.com>
# Install packages (Modified by A. Datta)

RUN apt-get update && apt-get -y install php7.0-zip php7.0-mbstring php7.0-sqlite3 php7.0-xml php7.0-imap php7.0-gd php7.0-curl && sed -i 's/AllowOverride FileInfo/AllowOverride All/' /etc/apache2/sites-available/000-default.conf

EXPOSE 80 3306
CMD ["/run.sh"]
