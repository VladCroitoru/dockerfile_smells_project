# Folding@home
#
# VERSION               0.1
# Run with: docker run -d -v <path_to_config_xml>:/config:ro bwooce/folding-at-home
# Inspired by magglass1/docker-folding-at-home and
# Inspired by jordan0day/docker-folding-at-home

FROM centos

VOLUME /config

RUN yum -y update
RUN yum -y upgrade
RUN yum -y install bzip2

# Install Folding@home
RUN curl -OL http://fah-web.stanford.edu/file-releases/beta/release/fahclient/centos-5.3-64bit/v7.4/fahclient_7.4.4-64bit-release.tar.bz2
RUN ls -l
RUN tar -jxf fahclient_7.4.4-64bit-release.tar.bz2 

CMD ./fahclient_7.4.4-64bit-release/FAHClient --config=/config/config.xml 
