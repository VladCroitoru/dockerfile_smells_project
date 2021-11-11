FROM tutum/apache-php
MAINTAINER cdp181 <chris@smokingcures.com>
ENV DEBIAN_FRONTEND noninteractive

# Set correct environment variables.
ENV HOME /root

RUN apt-get update -q

# Install Dependencies
RUN apt-get install -qy wget nmap sqlite3 wakeonlan php5-sqlite

# Add php files and remove default page
RUN rm -f /var/www/html/index.html
ADD index.php /var/www/html/index.php
ADD wol.php /var/www/html/wol.php
ADD style.css /var/www/html/style.css
ADD font-awesome.min.css /var/www/html/font-awesome.min.css
ADD edit.php /var/www/html/edit.php
ADD adelete.php /var/www/html/adelete.php
ADD ainsert.php /var/www/html/ainsert.php
ADD status_bg.php /var/www/html/status_bg.php
ADD aupdate.php /var/www/html/aupdate.php
ADD sdelete.php /var/www/html/sdelete.php
ADD sinsert.php /var/www/html/sinsert.php
ADD supdate.php /var/www/html/supdate.php
ADD jquery.aCollapTable.js /var/www/html/jquery.aCollapTable.js
ADD darrhax.php /var/www/html/darrhax.php
ADD dbupdate.php /var/www/html/dbupdate.php
ADD dbinsert.php /var/www/html/dbinsert.php
ADD dbdelete.php /var/www/html/dbdelete.php
ADD darrupdate.php /var/www/html/darrupdate.php

# Update apache config
ADD apache-config.conf /etc/apache2/sites-available/000-default.conf
ADD ports.conf /etc/apache2/ports.conf

# Install binaries
RUN mkdir -p /var/www/html/font
RUN mkdir -p /var/www/html/images
ADD up.png /var/www/html/images/up.png
ADD down.png /var/www/html/images/down.png
ADD up.png /var/www/html/images/icon_ipad.png
RUN wget -P /var/www/html/font/ http://www.smokingcures.com/git/font/FontAwesome.otf
RUN wget -P /var/www/html/font/ http://www.smokingcures.com/git/font/fontawesome-webfont.eot
RUN wget -P /var/www/html/font/ http://www.smokingcures.com/git/font/fontawesome-webfont.svg
RUN wget -P /var/www/html/font/ http://www.smokingcures.com/git/font/fontawesome-webfont.ttf
RUN wget -P /var/www/html/font/ http://www.smokingcures.com/git/font/fontawesome-webfont.woff
RUN wget -P /var/www/html/images/ http://www.smokingcures.com/git/images/background.png
RUN wget -P /var/www/html/images/ http://www.smokingcures.com/git/images/glyphicons.png
RUN wget -P /var/www/html/images/ http://www.smokingcures.com/git/images/glyphicons-halflings.png
RUN wget -P /var/www/html/images/ http://www.smokingcures.com/git/images/glyphicons-halflings-white.png
RUN wget -P /var/www/html/images/ http://www.smokingcures.com/git/images/gravatar-default-80x80.png

EXPOSE 21337

# Database directory for config
VOLUME /data
VOLUME /appdata
