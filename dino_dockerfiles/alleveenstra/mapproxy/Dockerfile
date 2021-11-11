FROM phusion/baseimage:0.9.16
MAINTAINER Alle Veenstra <alle.veenstra@gmail.com>

# Set the locale
ENV LANG C.UTF-8
RUN update-locale LANG=C.UTF-8

RUN apt-get update -y && \
    apt-get install -y libapache2-mod-wsgi python-pip python-pyproj supervisor apache2 python-dev libgeos-dev libjpeg-dev zlib1g-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install Shapely Pillow MapProxy uwsgi webcolors

# Create a `mapproxy` service
RUN mkdir /usr/local/mapproxy
RUN mkdir /usr/local/mapproxy/cache_data
RUN chmod a+rwx /usr/local/mapproxy/cache_data
ADD mapproxy-mapnik.yaml /usr/local/mapproxy/mapproxy-mapnik.yaml
ADD config.py /usr/local/mapproxy/config.py
RUN a2enmod wsgi
RUN a2enmod rewrite
RUN a2dissite 000*
ADD tileserver.conf /etc/apache2/sites-available/tileserver.conf
RUN a2ensite tileserver.conf
RUN a2enmod rewrite

# Configure supervisord
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose the webserver
EXPOSE 80

# Start supervisord
CMD ["/usr/bin/supervisord"]
