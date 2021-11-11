# Use phusion/baseimage as base image. To make your builds
# reproducible, make sure you lock down to a specific version, not
# to `latest`! See
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md
# for a list of version numbers.
FROM phusion/baseimage:0.10.1

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# add wget and mysq-client for admin interface.
RUN apt-get update && apt-get install -y wget mysql-client

RUN wget https://github.com/sysown/proxysql/releases/download/v1.4.8/proxysql_1.4.8-ubuntu16_amd64.deb -O /opt/proxysql_1.4.8-ubuntu16_amd64.deb
RUN dpkg -i /opt/proxysql_1.4.8-ubuntu16_amd64.deb

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /opt/proxysql_1.4.8-ubuntu16_amd64.deb

ENTRYPOINT ["proxysql", "-f"]
