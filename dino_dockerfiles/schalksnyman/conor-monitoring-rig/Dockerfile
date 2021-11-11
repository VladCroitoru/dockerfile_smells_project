FROM centos:centos7

MAINTAINER Schalk Snyman <schalksnyman@conor.com>

LABEL   Description="This Dockerfile starts up a Riemann, InfluxDB and Grafana" \
        Vendor="Conor Info Tech" \
        Version="0.1"

# --------------------------
#   Environment variables
# --------------------------
ENV     RIEMANN_VERSION     0.2.11
ENV     INFLUXDB_VERSION    0.13.0
ENV     GRAFANA_VERSION     3.0.2

# These variables are used by set_influxdb.sh and set_grafana.sh
ENV     PRE_CREATE_DB           data grafana
ENV     INFLUXDB_URL            http://localhost:8086
ENV     INFLUXDB_ADMIN_PW       @dmin@cvm
ENV     INFLUXDB_DATA_USER      data
ENV     INFLUXDB_DATA_PW        d@ta@cvm
ENV     INFLUXDB_GRAFANA_USER   grafana
ENV     INFLUXDB_GRAFANA_PW     gr@fana@cvm

# -------------------------------------
#   Increase OS TCP/UDP buffer limits
# -------------------------------------
# 8MB = (8*1024*1024) is starting recommendation to handle higher UDP load
#RUN     echo 'net.core.rmem_max=12582912' >> /etc/sysctl.conf

#RUN     echo 'net.ipv4.tcp_rmem= 10240 87380 12582912' >> /etc/sysctl.conf && \
#        echo 'net.ipv4.tcp_wmem= 10240 87380 12582912' >> /etc/sysctl.conf

# Turn on window scaling
#RUN     echo 'net.ipv4.tcp_window_scaling = 1' >> /etc/sysctl.conf

# -------------------
#   Data Volumes
# -------------------
# All persistent data in this dir
# Mount with docker argument e.g. -v /home/conor/docker_data:/mnt/docker_rig/
# 
#VOLUME  /mnt/docker_rig/riemann
VOLUME  /mnt/docker_rig/influxdb
VOLUME  /var/log/supervisor
#VOLUME  /mnt/docker_rig/grafana
#VOLUME  /mnt/docker_rig/supervisord
#VOLUME  /mnt/docker_rig/docker

# forward request and error logs to docker log collector
#RUN     ln -sf /dev/stdout /mnt/docker_rig/docker/info.log
#RUN     ln -sf /dev/stderr /mnt/docker_rig/docker/error.log

# -------------------------
#   Create users & groups
# -------------------------
#RUN     groupadd -r -g 1200 riemann && useradd -r -g riemann -u 1200 riemann
#RUN     groupadd -r -g 1300 influxdb && useradd -r -g influxdb -u 1300 influxdb
#RUN     groupadd -r -g 1400 grafana && useradd -r -g grafana -u 1400 grafana

## Assign Owners
#RUN     chown riemann:riemann /mnt/docker_rig/riemann
#RUN     chown influxdb:influxdb /mnt/docker_rig/influxdb
#RUN     chown grafana:grafana /mnt/docker_rig/grafana

# --------------------------
#   Install prerequisites
# --------------------------
# - Install epel repository required for nodejs, npm, nginx...
# - Install basic packages (e.g. python-setuptools is required to have python's easy_install)
# - Install inotify, needed to automate daemon restarts after config file changes
# - Install supervisord (via python's easy_install)
# - Install yum-utils so we have yum-config-manager tool available
RUN     yum -y install epel-release && \
        yum -y update && \        
        yum -y groupinstall "Development Tools" && \
        yum -y install fontconfig nodejs npm && \
        yum -y install nginx wget && \
        yum -y install java-1.8.0-openjdk && \        
        yum -y install hostname inotify-tools yum-utils which && \
        yum -y install rubygems ruby-dev && \
        yum -y install python-setuptools && \
        easy_install supervisor

RUN     gem install riemann-client riemann-tools riemann-dash

# -----------------------------------
#   Install Riemann to /src/riemann
# -----------------------------------
RUN     mkdir -p src/riemann && cd src/riemann && \
        wget https://aphyr.com/riemann/riemann-${RIEMANN_VERSION}.tar.bz2 -O riemann.tar.bz2 && \
        tar xvfj riemann.tar.bz2 --strip-components=1 && rm riemann.tar.bz2

# ---------------------
#   Install InfluxDB
# ---------------------
ADD     repo/influxdb.repo /etc/yum.repos.d/influxdb.repo
RUN     yum -y install influxdb

# ---------------------
#   Install Grafana
# ---------------------
RUN     yum -y install https://grafanarel.s3.amazonaws.com/builds/grafana-3.0.2-1463383025.x86_64.rpm

# ---------------------
#   Configure Riemann
# ---------------------
ADD     riemann/riemann.config /src/riemann/etc/riemann.config

# ----------------------
#   Configure InfluxDB
# ----------------------
ADD     influxdb/influxdb.conf /etc/influxdb/influxdb.conf
ADD     influxdb/run.sh /usr/local/bin/run_influxdb
#RUN     chown influxdb:influxdb /etc/influxdb/influxdb.conf

RUN     mkdir /mnt/docker_rig/influxdb/shared/data -p && \
        mkdir /mnt/docker_rig/influxdb/shared/meta -p && \
        mkdir /mnt/docker_rig/influxdb/shared/wal -p
#RUN     chown influxdb:influxdb /mnt/docker_rig/influxdb -R

# ----------------------
#   Configure Grafana
# ----------------------
ADD     grafana/config.js /usr/share/grafana/config.js
ADD     grafana/dash.json /var/lib/grafana/dashboards/dash.json
ADD     grafana/grafana.ini /etc/grafana/grafana.ini
#RUN     chown grafana:grafana /etc/grafana/grafana.ini

ADD     scripts/configure.sh /configure.sh
ADD     scripts/set_grafana.sh /set_grafana.sh
ADD     scripts/set_influxdb.sh /set_influxdb.sh
RUN     /configure.sh

# -------------------------
#   Configure nginx
# -------------------------
ADD     nginx/nginx.conf /etc/nginx/nginx.conf
RUN     mkdir -p /var/www && \
        ln -s /usr/share/grafana -d /var/www/grafana && \
        chown nginx:nginx /var/www/grafana -R && \
        chown nginx:nginx /usr/share/grafana -R && \
        rm -f /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/example_ssl.conf

# -------------------------
#   Configure supervisord
# -------------------------
ADD     supervisor/supervisord.conf /etc/supervisord.d/supervisord.conf

# -----------
#   Cleanup  
# -----------
RUN     yum clean all

# -------------------
#   Expose ports
# -------------------
# Riemann TCP/UDP servers
EXPOSE  5555

# Riemann Websockets server
EXPOSE  5556

# InfluxDB Admin server
EXPOSE  8083

# InfluxDB HTTP API
EXPOSE  8086

# Grafana
EXPOSE  80 

# Supervisord
#EXPOSE  9111

# -------------------
#   Run!
# -------------------
CMD     ["/usr/bin/supervisord", "-c", "/etc/supervisord.d/supervisord.conf"]
