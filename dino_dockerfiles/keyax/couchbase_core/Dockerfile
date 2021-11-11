# FROM ubuntu:14.04
FROM keyax/ubuntu_lts

# MAINTAINER Couchbase Docker Team <docker@couchbase.com>
LABEL maintainer "yones.lebady AT gmail.com"
LABEL keyax.os "ubuntu core"
LABEL keyax.os.ver "14.04 trusty"
LABEL keyax.vendor "Keyax"
LABEL keyax.app "Couchbase 4.5.0"
LABEL keyax.app.ver "2.1"

# Install dependencies:
#  runit: for container process management
#  wget: for downloading .deb
#  python-httplib2: used by CLI tools
#  chrpath: for fixing curl, below
# Additional dependencies for system commands used by cbcollect_info:
#  lsof: lsof
#  lshw: lshw
#  sysstat: iostat, sar, mpstat
#  net-tools: ifconfig, arp, netstat
#  numactl: numactl
RUN apt-get update && \
    apt-get install -yq \
       runit \
#       wget \
#       python-httplib2 \
       chrpath \
       lsof lshw \
# disable transparent hugepages databases couchbase in Ubuntu
       sysfsutils \
       sysstat net-tools \
       numactl \
    && apt-get autoremove && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Create Couchbase user with UID 1000 (necessary to match default boot2docker UID)
RUN groupadd -g 1000 couchbase && useradd couchbase -u 1000 -g couchbase -M

# ARG CB_VERSION=4.5.0
# ARG CB_RELEASE_URL=http://packages.couchbase.com/releases
# ARG CB_PACKAGE=couchbase-server-community_4.5.0-ubuntu14.04_amd64.deb
# ARG CB_SHA256=7682b2c90717ba790b729341e32ce5a43f7eacb5279f48f47aae165c0ec3a633
# ENV PATH=$PATH:/opt/couchbase/bin:/opt/couchbase/bin/tools:/opt/couchbase/bin/install

ENV CB_VERSION="4.5.0" \
    CB_RELEASE_URL="http://packages.couchbase.com/releases" \
    CB_PACKAGE="couchbase-server-community_4.5.0-ubuntu14.04_amd64.deb" \
    CB_SHA256="7682b2c90717ba790b729341e32ce5a43f7eacb5279f48f47aae165c0ec3a633" \
    LD_LIBRARY_PATH=":/opt/couchbase/lib" \
    CB_PATHS=":/opt/couchbase/bin:/opt/couchbase/bin/tools:/opt/couchbase/bin/install"
ENV PATH=${PATH}${CB_PATHS}
#    PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/couchbase/bin:/opt/couchbase/bin/tools:/opt/couchbase/bin/install"
# PATH=$PATH:/opt/couchbase/bin:/opt/couchbase/bin/tools:/opt/couchbase/bin/install

# Install couchbase
RUN wget -N $CB_RELEASE_URL/$CB_VERSION/$CB_PACKAGE && \
    echo "$CB_SHA256  $CB_PACKAGE" | sha256sum -c - && \
    dpkg -i ./$CB_PACKAGE && rm -f ./$CB_PACKAGE

# RedHat Warning: Transparent hugepages looks to be active and should not be.
# Please look at http://bit.ly/1ZAcLjD as for how to PERMANENTLY alter this setting.
# RUN echo never > /sys/kernel/mm/transparent_hugepage/enabled
# Ubuntu disabling transparent hugepages
RUN echo kernel/mm/transparent_hugepage/enabled = never > /etc/sysfs.conf
# Warning: Swappiness is not set to 0.
# Please look at http://bit.ly/1k2CtNn as for how to PERMANENTLY alter this setting.
# RUN sysctl vm.swappiness=0 && echo "vm.swappiness = 0" >> /etc/sysctl.conf
# Ubuntu set swappiness 0
RUN echo 'vm.swappiness = 0' >> /etc/sysctl.conf
# Add runit script for couchbase-server
# RUN touch /etc/service/couchbase-server/run
COPY scripts/run /etc/service/couchbase-server/run

# Add dummy script for commands invoked by cbcollect_info that
# make no sense in a Docker container
COPY scripts/dummy.sh /usr/local/bin/
RUN ln -s dummy.sh /usr/local/bin/iptables-save \
 && ln -s dummy.sh /usr/local/bin/lvdisplay \
 && ln -s dummy.sh /usr/local/bin/vgdisplay \
 && ln -s dummy.sh /usr/local/bin/pvdisplay \
# && echo "export PATH=$PATH:/opt/couchbase/bin:/opt/couchbase/bin/tools:/opt/couchbase/bin/install" >> /root/.bashrc \
# && /root/.bashrc && echo $PATH \
# Fix curl RPATH
 && chrpath -r '$ORIGIN/../lib' /opt/couchbase/bin/curl

# 8091: Couchbase Web console, REST/HTTP interface
# 8092: Views, queries, XDCR
# 8093: Query services (4.0+) Workbench 8094
# 8094: Full-text Serarch (4.5+)  CBFT use Bleve indexer 8095 -----
# 11207: Smart client library data node access (SSL) EE
# 11210: Smart client library/moxi data node access
# 11211: Legacy non-smart client library data node access
# 18091: Couchbase Web console, REST/HTTP interface (SSL) EE
# 18092: Views, query, XDCR (SSL) EE
# 18093: Query services (SSL) (4.0+) EE-----
# EXPOSE 8091 8092 8093 8094 11207 11210 11211 18091 18092 18093
EXPOSE 4984 4985 8091 8092 8093 8094 11210 11211
VOLUME /opt/couchbase/var

# Add bootstrap script
COPY scripts/entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
CMD ["couchbase-server"]


COPY scripts/configure-cluster-node.sh  /
CMD ["/configure-cluster-node.sh"]

# from image arungupta/couchbase-node
# ENTRYPOINT &{["/entrypoint.sh"]}
# CMD ["couchbase-server"]
# EXPOSE 11207/tcp 11210/tcp 11211/tcp 18091/tcp 18092/tcp 8091/tcp 8092/tcp 8093/tcp
# VOLUME /opt/couchbase/var
# COPY scripts/configure-cluster-node.sh /opt/couchbase
# CMD ["/opt/couchbase/configure-cluster-node.sh"]
