FROM ubuntu:trusty 

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN groupadd -r atlassian && useradd -r -g atlassian atlassian

# grab gosu for easy step-down from root
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/* \
  && gpg --keyserver pgp.mit.edu --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
  && curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture)" \
  && curl -o /tmp/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture).asc" \
  && gpg --verify /tmp/gosu.asc /usr/local/bin/gosu \
  && rm /tmp/gosu.asc \
  && chmod +x /usr/local/bin/gosu \
  && apt-get purge -y --auto-remove curl

# grab the crowd dependencies
RUN apt-get update && apt-get install -y \
    openjdk-7-jdk \
    libtcnative-1 \
  && rm -rf /var/lib/apt/lists/*

ENV CROWD_VERSION 2.9.1
ENV CROWD_HOME /var/atlassian/crowd

# extract crowd
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/* \
  && mkdir -p /opt/atlassian \
  && curl -o /opt/atlassian/atlassian-crowd.tar.gz -SL 'https://www.atlassian.com/software/crowd/downloads/binary/atlassian-crowd-2.9.1.tar.gz' \
  && tar xf /opt/atlassian/atlassian-crowd.tar.gz -C /opt/atlassian --strip-components=1 \
  && echo "crowd.home=$CROWD_HOME" > /opt/atlassian/crowd-webapp/WEB-INF/classes/crowd-init.properties \
  && rm -f /opt/atlassian/atlassian-crowd.tar.gz \
  && chown -R atlassian /opt/atlassian \
  && apt-get purge -y --auto-remove curl

VOLUME /var/atlassian/crowd

COPY ./docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 8080
CMD ["crowd"]
