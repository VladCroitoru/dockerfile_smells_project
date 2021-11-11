FROM debian:stretch-slim

MAINTAINER Tim Bennett <tim@coderunner.io>

# Add required deps for docker, plus openssh-client
RUN \
  apt-get update && \
  apt-get install -y \
   apt-transport-https \
   ca-certificates \
   curl \
   gnupg2 \
   software-properties-common \
   openssh-client

# Setup docker repository
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/debian \
       $(lsb_release -cs) \
       stable"

# Install docker
RUN \
  apt-get update && \
  apt-get install -y docker-ce

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# -----------------------
# Default configuration
# ----------------------- 
# Location of ghost files to sync (on the local host)
ENV GHOST_CONTENT_LOCAL "/var/lib/ghost/content"

# Location to sync local ghost files to on the remote host
ENV GHOST_CONTENT_REMOTE "/var/lib/ghost/content"

# Location of backup log (written after each automated backup)
ENV LOG_LOCATION "/var/log/ghost-sync.log"

# The name of a linked ghost-backup container (required if you want to sync the database)
ENV GHOST_BACKUP_CONTAINER "ghost-backup"

# Prefix to put before the synced DB archive so that it is recognised by the remote ghost-backup container
ENV BACKUP_FILE_PREFIX="backup"

# -----------------------

# Add the sync script
COPY sync.sh /bin/sync
RUN chmod +x /bin/sync

ENTRYPOINT ["/bin/sync"]
CMD ["-i"]