# Specifing the base image
FROM            debian:8.3

# Maintainer
MAINTAINER      "Vaibhav Todi"      <vaibhavtodi1989@gmail.com>

# Specifing the Label
LABEL           Description="Roundcube Docker image"                                                         \
                Version="1.0"

# Setting the working directory
ENV             home                /root
WORKDIR         $home

# Setting up the ENV variables for Apache2
ENV             APACHE_RUN_USER  = www-data               \
                APACHE_RUN_GROUP = www-data               \
                APACHE_PID_FILE  = /var/run/apache2.pid   \
                APACHE_RUN_DIR   = /var/run/apache2       \
                APACHE_LOCK_DIR  = /var/lock/apache2      \
                APACHE_LOG_DIR   = /var/log/apache2       \

# Downloading & Installing the Roundcube Package
RUN             apt-get             update                                                                   \
        &&      DEBIAN_FRONTEND=noninteractive apt-get   install  -y  wget  curl  vim  apache2               \
                                                                      libapache2-mod-php5                    \
        &&      mkdir               /var/lock/apache2                                                        \
        &&      wget                https://downloads.sourceforge.net/project/roundcubemail/roundcubemail/1.1.4/roundcubemail-1.1.4-complete.tar.gz       \
        &&      tar                 -xvzf      roundcubemail-1.1.4-complete.tar.gz                           \
        &&      rm                  -f         roundcubemail-1.1.4-complete.tar.gz                           \
        &&      mv                  /root/roundcubemail-1.1.4           /root/roundcube                      \
        &&      mv                  /root/roundcube                     /etc                                 \
        &&      touch               /etc/apache2/sites-enabled/roundcube.conf                                \
        &&      ln                  -s         /etc/apache2/sites-enabled/roundcube.conf      roundcube.conf

# Clearing the Docker image
RUN             apt-get             -y         clean                                                         \
        &&      rm                  -rf        /var/lib/apt/lists/*                                          \
        &&      rm                  -rf        /var/cache/*

# Copying the roundcube apache2 config file
COPY            roundcube.conf      /etc/apache2/sites-enabled/roundcube.conf

# Copying the entrypoint.sh
COPY            entrypoint.sh       /entrypoint.sh

# Exposing the Ports
EXPOSE          80

# Mounting the log & data directory
VOLUME          ["/etc/roundcube, /etc/apache2, /var/log/apache2, /var/log/roundcube"]

# Specifing the entrypoint
CMD             ["/entrypoint.sh"]
