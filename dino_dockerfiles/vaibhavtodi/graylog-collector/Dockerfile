# Specifing the base image
FROM            vaibhavtodi/java:1.0

# Maintainer
MAINTAINER      "Vaibhav Todi"    <vaibhavtodi1989@gmail.com>

# Specifing the Label
LABEL           Description="DOCKER IMAGE WHERE GRAYLOG-COLLECTOR IS SETUP"                                                       \
                Version="1.0"

# Setting the ENV variable
ENV             JAVA              /usr/lib/jvm/java-7-oracle

# Downloading & Installing the Graylog-Server
RUN             wget     https://packages.graylog2.org/repo/packages/graylog-collector-latest-repository-ubuntu14.04_latest.deb   \
     &&         dpkg     -i       graylog-collector-latest-repository-ubuntu14.04_latest.deb                                      \
     &&         apt-get  update                                                                                                   \
     &&         apt-get  install  -y   graylog-collector                                                                          \
     &&         rm       -f       graylog-collector-latest-repository-ubuntu14.04_latest.deb

# Copying the Graylog Server configuration file
COPY            collector.conf       /etc/graylog/collector/collector.conf

# Copying the entrypoint.sh for running the service
COPY            entrypoint.sh        /entrypoint.sh

# Cleaning the Docker image
RUN             apt-get   -y    clean                                                                                            \
       &&       rm        -rf   /var/lib/apt/lists/*                                                                             \
       &&       rm        -rf   /var/cache/*

# Exposing the Ports
#EXPOSE          12201

# Mounting the Volumes
VOLUME          ["/etc/graylog"]

# Specifing the CMD instruction
CMD             ["/entrypoint.sh"]
