# Base system is the LTS version of Ubuntu.
FROM   ubuntu:16.04


# Make sure we don't get notifications we can't answer during building.
ENV    DEBIAN_FRONTEND noninteractive

ENV    VIRTUAL_HOST localhost
ENV    VIRTUAL_PORT 80

ENV    ADMIN_NAME root
ENV    ADMIN_PW toor
ENV    ADMIN_EMAIL root@localhost.net


# Download and install everything from the repos.
RUN    apt-get --yes update; apt-get --yes upgrade; apt-get --yes install software-properties-common

RUN    apt-get --yes install openssl curl openjdk-8-jdk tar python lib32gcc1 lib32tinfo5 lib32z1 lib32stdc++6 \
       nginx mysql-client mysql-server php-fpm php-cli php-curl php-mysql php-mcrypt ssh expect git && \
       phpenmod mcrypt unzip

# Download PufferPannel

RUN    mkdir -p /srv && cd /srv && \
       curl -L -o pufferpanel.tar.gz https://git.io/vbp3k && \
       tar -xf pufferpanel.tar.gz && \
       cd pufferpanel  && \
       chmod +x pufferpanel

# Install Pufferd
#RUN    curl -s https://packagecloud.io/install/repositories/pufferpanel/pufferd/script.deb.sh | bash && \
#       apt install pufferd

# Load in all script files.
ADD    ./scripts/start /start
ADD    ./scripts/install.exp /srv/install


# Fix all permissions
RUN    chmod +x /start
RUN    chmod +x /srv/install

# Configure Nginx
RUN    rm /etc/nginx/sites-enabled/default
ADD    ./config/pufferpanel.conf /etc/nginx/sites-enabled/pufferpanel.conf

# 5657 for SFTP
EXPOSE 5657

# 80 for Webserver
EXPOSE 80

# 25565 is for minecraft
EXPOSE 25565

# /start runs it.
CMD    ["/start"]