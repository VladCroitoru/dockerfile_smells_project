FROM fanday/java:latest
MAINTAINER Fanday Dai <fandaydai@live.cn>

# scm-server environment
ENV SCM_VERSION 1.46
ENV SCM_PKG_URL https://maven.scm-manager.org/nexus/content/repositories/releases/sonia/scm/scm-server/${SCM_VERSION}/scm-server-${SCM_VERSION}-app.tar.gz
ENV SCM_HOME /var/lib/scm

# install scm-server
RUN yum install -y mercurial svn git curl
RUN curl -Lks "$SCM_PKG_URL" -o /root/scm-server.tar.gz
RUN /usr/sbin/useradd --create-home --home-dir /opt/scm-server --shell /bin/bash scm
RUN tar zxf /root/scm-server.tar.gz --strip=1 -C /opt/scm-server
RUN rm -f /root/scm-server.tar.gz
RUN chown -R scm:scm /opt/scm-server
RUN mkdir -p /var/lib/scm
RUN chown scm:scm /var/lib/scm

# run scm-manager
WORKDIR /var/lib/scm
VOLUME /var/lib/scm
EXPOSE 8080
USER scm
CMD ["/opt/scm-server/bin/scm-server"]
