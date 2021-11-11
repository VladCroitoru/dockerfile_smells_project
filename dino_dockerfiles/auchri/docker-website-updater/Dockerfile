FROM auchri/docker-apache-php
MAINTAINER Christoph Auer <auer.chrisi@gmx.net>

RUN apt-get update && apt-get -y install sudo git && apt-get clean && rm -r /var/lib/apt/lists/*

ARG WEB_ROOT=/var/www
ARG HTML_DIR="${WEB_ROOT}/html"
ARG CONFIG_DIR="${WEB_ROOT}/config"

# Add index file
ADD index.php "${HTML_DIR}/index.php"
RUN rm "${HTML_DIR}/index.html"

# Add config file
ADD config/ "${CONFIG_DIR}/"

# Set owner
RUN chown www-data:www-data "${WEB_ROOT}" -R

# Create ssh dir
RUN mkdir -p ~/.ssh

# Link private key
RUN ln -s "${CONFIG_DIR}/private.key" ~/.ssh/id_rsa

# Set ssh config
RUN touch ~/.ssh/config
RUN echo "Host *" >> ~/.ssh/config
RUN echo "    StrictHostKeyChecking  no" >> ~/.ssh/config

ADD start.sh /start.sh
ADD pull.sh /pull.sh

RUN echo "www-data ALL = (root) NOPASSWD: /pull.sh" >> /etc/sudoers

CMD ["/start.sh"]
