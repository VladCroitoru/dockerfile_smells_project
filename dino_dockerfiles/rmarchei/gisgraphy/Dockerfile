# Gisgraphy - http://www.gisgraphy.com
#
# docker run -d \
#      --restart on-failure \
#      -p 8080:8080 \
#      --link gisgraphy-db:postgres \
#      --name gisgraphy \
#      rmarchei/gisgraphy
#

FROM centos:latest
MAINTAINER Ruggero Marchei <ruggero.marchei@daemonzone.net>


RUN yum install -y java-1.7.0-openjdk-headless \
  unzip \
  bsdtar \
  && yum clean -q all

ENV GISGRAPHY_USER gisgraphy
ENV GISGRAPHY_UID 9432
ENV GISGRAPHY_HOME /opt/gisgraphy
ENV GISGRAPHY_VERSION 4.0-beta1
ENV GISGRAPHY_MD5 2bc368aee43c6b02b4e415cbf15edb88

RUN groupadd -r $GISGRAPHY_USER -o -g $GISGRAPHY_UID \
  && useradd -r -u $GISGRAPHY_UID -o -g $GISGRAPHY_USER -m -d $GISGRAPHY_HOME $GISGRAPHY_USER

# Download and unpack the Gisgraphy distribution
RUN cd /tmp \
  && curl -s -O http://download.gisgraphy.com/releases/gisgraphy-$GISGRAPHY_VERSION.zip \
  && echo "$GISGRAPHY_MD5  gisgraphy-$GISGRAPHY_VERSION.zip" > gisgraphy-$GISGRAPHY_VERSION.zip.md5 \
  && md5sum -c gisgraphy-$GISGRAPHY_VERSION.zip.md5 \
  && bsdtar -C $GISGRAPHY_HOME -x -f /tmp/gisgraphy-$GISGRAPHY_VERSION.zip --strip-components=1 \
  && rm -f /tmp/gisgraphy* \
  && chown -R $GISGRAPHY_USER. $GISGRAPHY_HOME


COPY configure-postgres.sh /usr/local/bin/configure-postgres.sh
COPY configure-solr.sh /usr/local/bin/configure-solr.sh
COPY configure-gisgraphy.sh /usr/local/bin/configure-gisgraphy.sh
COPY docker-entrypoint.sh /

# Make each gisgraphy script executable
RUN chmod +x /opt/gisgraphy/*.sh \
  && chmod +x /docker-entrypoint.sh \
  && chmod +x /usr/local/bin/configure*

EXPOSE 8080
WORKDIR $GISGRAPHY_HOME
USER $GISGRAPHY_USER


ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/opt/gisgraphy/launch.sh"]
