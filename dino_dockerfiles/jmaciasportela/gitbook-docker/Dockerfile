FROM phusion/baseimage:latest
MAINTAINER Jesus Macias Portela <jmacias@solidgear.es>
ENV DEBIAN_FRONTEND noninteractive

# Set correct environment variables
ENV HOME /root
ENV USER root

# Fix a Debianism of the nobody's uid being 65534
RUN usermod -u 99 nobody
RUN usermod -g 100 nobody

# Activar SSH
RUN rm -fr /etc/service/sshd/down

# Update root password
RUN echo "root:P@ssw0rd" | chpasswd

# Enable ssh for root
RUN sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config
# Enable this option to prevent SSH drop connections
RUN printf "ClientAliveInterval 15\\nClientAliveCountMax 8" >> /etc/ssh/sshd_config

# Install dependencies
RUN apt-get update && apt-get install -y git curl calibre xvfb && \
    curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt-get install -y nodejs && \
    npm install --unsafe-perm -g gitbook-cli gitbook-parsers

# Install latest version
RUN gitbook install 2.6.9

RUN echo '#!/bin/bash' > /usr/local/bin/ebook-convert && \
    echo 'Run xvfb-run /usr/bin/ebook-convert $@' > /usr/local/bin/ebook-convert && \
    echo 'xvfb-run /usr/bin/ebook-convert "$@"'  > /usr/local/bin/ebook-convert && \
    chmod +x /usr/local/bin/ebook-convert

RUN printf "#"'!'"/bin/bash\nrm -f /opt/books/$1/builds/*\ncd /opt/books/\$1/\ngitbook install\ngitbook build\ngitbook pdf . ./\$1.pdf\ntar czvf \$1.tar.gz _book/\ncp \$1.pdf /opt/books/\ncp \$1.tar.gz /opt/books" > /build.sh
RUN chmod +x /build.sh

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Disable security updates
RUN sed -i 's/"${distro_id}:${distro_codename}-security";/\/\/"${distro_id}:${distro_codename}-security";/g' /etc/apt/apt.conf.d/50unattended-upgrades

# Expose ownCloud's data dir
VOLUME ["/opt/books"]

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]
