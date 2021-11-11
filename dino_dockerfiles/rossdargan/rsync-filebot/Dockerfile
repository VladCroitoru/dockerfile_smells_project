FROM rednoah/filebot
MAINTAINER Ross Dargan

RUN apt-get update \
    && apt-get install -y rsync openssh-client sudo cron

# Transfer entrypoint script
ADD entry.sh /usr/bin/entry

# Change working directory
WORKDIR /var/

# Entrypoint script
ENTRYPOINT ["/usr/bin/entry"]
