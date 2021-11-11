#----------------------------------------------------------------------
# gollum - a Gollum webapp on Debian 8 Docker Container
#
# For usage info, just run the image without a command:
#   $ docker run --rm genebarker/gollum
#
# For a rack application, see the example (config.ru), and be sure
# to append its required packages and gems to the respective RUN
# commands below.
#----------------------------------------------------------------------

FROM debian:8.5

MAINTAINER Eugene F. Barker <genebarker@gmail.com>

# install dependencies
RUN apt-get update && apt-get install -y \
    apache2 \
    build-essential \
    git \
    libicu-dev \
    libz-dev \
    ruby \
    ruby-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists

# install gollum & GitHub Flavored Markdown
RUN gem install gollum github-markdown

# initialize wiki content
RUN mkdir /root/wiki && \
    git init /root/wiki

# copy initial apache2 SSL key and cert
# (to avoid their use by --hsts option)
RUN mkdir /root/oldfiles && \
    cd /root/oldfiles && \
    cp /etc/ssl/private/ssl-cert-snakeoil.key . && \
    cp /etc/ssl/certs/ssl-cert-snakeoil.pem .

# set apache env variables
# note: apache proxy / SSL setup is configured at runtime via
#       entrypoint.sh script
ENV APACHE_RUN_USER www-data \
    APACHE_RUN_GROUP www-data \
    APACHE_LOG_DIR /var/log/apache2

# copy in entrypoint script
COPY ./entrypoint.sh /

# set entry point
ENTRYPOINT ["/entrypoint.sh"]

# expose default webapp ports
EXPOSE 80 443
