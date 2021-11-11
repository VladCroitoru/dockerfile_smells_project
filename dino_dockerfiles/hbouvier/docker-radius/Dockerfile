From ubuntu:trusty

# Upgrade base system packages
RUN apt-get -y update

# Install freeradius v3
RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:freeradius/stable-3.0
RUN apt-get -y update
RUN apt-get -y install freeradius

# Add startup script
ADD bin/radius /usr/local/bin/radius

# Expose SQLITE3 database
VOLUME /opt/db/

# Expose Certificates
VOLUME /etc/freeradius/certs

# FreeRADIUS Port
EXPOSE 1812/udp

# Run
CMD radius
