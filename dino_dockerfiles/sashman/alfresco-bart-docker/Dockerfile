FROM debian:8

MAINTAINER Sash <sashman90@gmail.com>

# Install packages required
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python-pip python-dev wget python-setuptools python-lockfile rsync librsync-dev \
    lftp ncftp librsync1 libyaml-0-2 libyaml-dev python-boto

# Download and install duplicity
RUN export VERSION=0.6.21 && \
   cd /tmp/ && \
   wget https://code.launchpad.net/duplicity/0.6-series/$VERSION/+download/duplicity-$VERSION.tar.gz && \
   cd /opt/ && \
   tar xzvf /tmp/duplicity-$VERSION.tar.gz && \
   rm /tmp/duplicity-$VERSION.tar.gz && \
   cd duplicity-$VERSION && \
   ./setup.py install

RUN apt-get install -y mysql-client-5.5 postgresql-client

RUN apt-get install -y git-core
RUN git clone https://github.com/sashman/alfresco-backup-and-recovery-tool.git 
RUN cd /alfresco-backup-and-recovery-tool
ENTRYPOINT ["/alfresco-backup-and-recovery-tool/src/alfresco-bart.sh"]
CMD ["--help"]


