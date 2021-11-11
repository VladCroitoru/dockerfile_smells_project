# Dockerfile for the HDC's OSCAR-to-E2E exporter
#
#
FROM phusion/baseimage
MAINTAINER derek.roberts@gmail.com


################################################################################
# System and packages
################################################################################


# Environment variables
#
ENV TERM xterm
ENV DEBIAN_FRONTEND noninteractive


# Update system, and install packages
#
RUN apt-get update; \
    apt-get install -y --no-install-recommends \
      default-jdk \
      maven \
      mysql-server \
      sudo; \
    apt-get autoclean; \
    apt-get clean; \
    rm -rf \
      /var/tmp/* \
      /var/lib/apt/lists/* \
      /tmp/* \
      /usr/share/doc/ \
      /usr/share/doc-base/ \
      /usr/share/man/


################################################################################
# Setup
################################################################################


# Build
#
WORKDIR /app/
COPY . .
RUN mvn clean package

# Disable strict mode and all ACID requirements
#
COPY ./config/my.cnf-mysqld .
RUN cat ./my.cnf-mysqld >> /etc/mysql/my.cnf; \
    rm ./my.cnf-mysqld


# Setup database
#
RUN service mysql start; \
    mysqladmin -u root password superInsecure; \
    mysql --user=root --password=superInsecure -e 'CREATE DATABASE oscar_12_1;'



# Entrypoint
#
COPY ./config/entrypoint.sh /


################################################################################
# Volumes, ports and start command
################################################################################


# Initialize
#
VOLUME /import/
CMD ["/entrypoint.sh"]
