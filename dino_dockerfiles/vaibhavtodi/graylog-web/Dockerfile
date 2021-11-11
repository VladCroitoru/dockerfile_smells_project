# Specifing the base image
FROM            vaibhavtodi/java:1.0

# Maintainer
MAINTAINER      "Vaibhav Todi"    <vaibhavtodi1989@gmail.com>

# Specifing the Label
LABEL           Description="DOCKER IMAGE WHERE GRAYLOG-WEB INTERFACE IS SETUP"                                      \
                Version="1.3"

# Setting the ENV variable
ENV             JAVA              /usr/lib/jvm/java-7-oracle

# Downloading & Installing the Graylog-Server
RUN             wget     https://packages.graylog2.org/repo/packages/graylog-1.3-repository-ubuntu14.04_latest.deb   \
     &&         dpkg     -i       graylog-1.3-repository-ubuntu14.04_latest.deb                                      \
     &&         apt-get  update                                                                                      \
     &&         apt-get  install  -y   graylog-web                                                                   \
     &&         rm       -f       graylog-1.3-repository-ubuntu14.04_latest.deb

# Copying the Graylog Server configuration file
COPY            web.conf          /etc/graylog/web/web.conf

# Copying the entrypoint.sh for running the service
COPY            entrypoint.sh        /entrypoint.sh

# Setting up the Graylog Server Configuration
RUN         sed -i 's/gw_graylog_server_uri/"http:\/\/0\.0\.0\.0:12900\/"/'              /etc/graylog/web/web.conf \
      &&    sed -i 's/gw_application_secret/"lGOVlXDzWwfkvyjwiYgN11ASGxBJpX0VWpLTiDrDVfOHdx2nOa3bplnNTHt1hx8PRfs2CjAfrlwPFBHHwrJFPNVTTjeUS9qZ"/' /etc/graylog/web/web.conf

# Cleaning the Docker image
RUN         apt-get   -y    clean                                                                                   \
       &&   rm        -rf   /var/lib/apt/lists/*                                                                    \
       &&   rm        -rf   /var/cache/*

# Exposing the Ports
EXPOSE      9000

# Mounting the Volumes
VOLUME ["/var/log/graylog-web", "/etc/graylog"]

# Specifing the CMD instruction
CMD    ["/entrypoint.sh"]
