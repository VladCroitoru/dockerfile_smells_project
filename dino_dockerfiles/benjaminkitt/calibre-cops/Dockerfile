FROM python:2.7

# Install dependencies and create directories
RUN apt-get update && apt-get install -y git cron xvfb imagemagick php5-fpm php5-gd php5-sqlite php5-intl && \
    mkdir /data && \
    mkdir /scripts

# Install nginx
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 && \
    echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list && \
    apt-get install -y ca-certificates nginx && \
    rm -rf /var/lib/apt/lists/*

# Install Calibre
RUN wget -nv -O- https://raw.githubusercontent.com/kovidgoyal/calibre/master/setup/linux-installer.py | python -c "import sys; main=lambda:sys.stderr.write('Download failed\n'); exec(sys.stdin.read()); main()"

# Install cops
RUN mkdir /usr/share/nginx/html/apps && git clone https://github.com/benjaminkitt/cops.git /usr/share/nginx/html/apps/

# Add Locale
RUN apt-get update -qq && apt-get install -y locales -qq && \
    locale-gen en_US.UTF-8 && \
    localedef -f UTF-8 -i en_US en_US.UTF-8

# Add configurations
ADD config_local.php /usr/share/nginx/html/apps/config_local.php
ADD cops.conf /etc/nginx/conf.d/cops.conf
RUN rm /etc/nginx/sites-enabled/default

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/opds.access.log && \
    ln -sf /dev/stderr /var/log/nginx/opds.error.log

# Add scripts
ADD add-books.sh /scripts/add-books.sh
ADD startup.sh /scripts/startup.sh
ADD crontab /scripts/crontab

RUN chmod 755 /scripts/*
EXPOSE 8080

CMD ["/scripts/startup.sh"]