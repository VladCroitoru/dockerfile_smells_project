FROM java:8u40-jre

# Download and unzip Stash Backup Client

ENV BITBUCKET_BACKUP_CLIENT_VERSION 2000000

RUN curl -Lks https://marketplace.atlassian.com/download/plugins/com.atlassian.stash.backup.client/version/${BITBUCKET_BACKUP_CLIENT_VERSION} -o /root/stash-backup-client.zip
RUN mkdir /opt/stash
RUN unzip /root/stash-backup-client.zip -d /opt/stash
RUN mv /opt/stash/bitbucket-backup-client-* /opt/stash/bitbucket-backup-client

## Lets install the necessities to compress, encrypt, and send to s3

RUN apt-get update && \ 
     apt-get install -y -q gnupg xz-utils python-setuptools ca-certificates && \ 
     easy_install pip && \ 
     pip install awscli 

## Add in our init script

ADD run.sh /run.sh
RUN chmod +x /run.sh

## Setup dirs
#
WORKDIR /opt/stash
#VOLUME /opt/atlassian-home

## Setup a volume and var for the default backup output location
VOLUME /opt/backup
ENV BACKUP_HOME /opt/backup

ENTRYPOINT ["/run.sh"]
