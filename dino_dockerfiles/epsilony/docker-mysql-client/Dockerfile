FROM epsilony/baseimage

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# gpg: key 5072E1F5: public key "MySQL Release Engineering <mysql-build@oss.oracle.com>" imported
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys A4A9406876FCBD3C456770C88C718D3B5072E1F5

COPY mysql.list /etc/apt/sources.list.d/

RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold" && apt-get install -y mysql-client
# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
