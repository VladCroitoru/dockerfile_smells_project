FROM debian:latest
MAINTAINER Rony Dray <contact@obigroup.fr>

# Install a late version of Nginx
RUN echo 'deb http://http.debian.net/debian wheezy main contrib non-free' >> /etc/apt/sources.list
RUN apt-get -y update
RUN apt-get -y install g++
RUN apt-get install --quiet --assume-yes \
    python-pip \
    nginx \
    libssl-dev \
    curl \
    && apt-get clean

RUN nginx -t

# Install supevisord
RUN pip install supervisor

# Clean APT cache for a lighter image
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Create Cozy users
RUN useradd -M cozy

# Generate the SSL certificate and the DH parameter
RUN mkdir /etc/cozy
RUN chown -hR cozy /etc/cozy
RUN openssl req -x509 -nodes -newkey rsa:2048 -keyout /etc/cozy/server.key -out /etc/cozy/server.crt -days 365 -subj '/CN=localhost'
RUN openssl dhparam -out /etc/cozy/dh2048.pem -outform PEM -2 2048
RUN chown cozy:cozy /etc/cozy/server.key
RUN chmod 600 /etc/cozy/server.key

# Run supervisor
ADD supervisor/supervisord.conf /etc/supervisord.conf
RUN mkdir -p /var/log/supervisor
RUN chmod 774 /var/log/supervisor
RUN /usr/local/bin/supervisord -c /etc/supervisord.conf

# Need ENV VARS:
ENV COZYAPPS_HOST cozyapps
ENV COZYAPPS_PORT 9104
# Set to true if multi cozy cloud intances on a same server
ENV DISABLE_SSL false

# Configure Nginx and check configuration by restarting the service
ADD nginx/nginx.conf /etc/nginx/nginx.conf
ADD nginx/cozy.conf /etc/nginx/sites-available/cozy.conf
ADD nginx/cozy-ssl.conf /etc/nginx/sites-available/cozy-ssl.conf
RUN chmod 0644 /etc/nginx/sites-available/*
RUN rm /etc/nginx/sites-enabled/default

# Copy supervisor configuration files
ADD supervisor/nginx.conf /etc/supervisor/conf.d/nginx.conf
RUN chmod 0644 /etc/supervisor/conf.d/*

EXPOSE 80 443

ADD sh/run.sh /home/run.sh
WORKDIR /home
CMD ["/bin/sh", "run.sh"]