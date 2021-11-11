FROM sonatype/nexus3:3.12.0

USER root

# Setup gosu for entrypoint execution
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.9/gosu-amd64" \
    && curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.9/gosu-amd64.asc" \
    && gpg --verify /usr/local/bin/gosu.asc \
    && rm /usr/local/bin/gosu.asc \
    && rm -r /root/.gnupg/ \
    && chmod +x /usr/local/bin/gosu

# AWS CLI
ENV container docker
RUN yum -y swap -- remove fakesystemd -- install systemd systemd-libs && \
    yum -y install python epel-release && \
    yum -y install python-pip groff && \
    pip install awscli && \
    yum clean all && rm -rf /tmp/* /var/tmp/*

RUN mkdir -p /opt/s3sync

COPY ./docker-entrypoint.sh /entrypoint.sh

WORKDIR /opt/sonatype/nexus

ENTRYPOINT ["/entrypoint.sh"]
CMD ["bin/nexus", "run"]
