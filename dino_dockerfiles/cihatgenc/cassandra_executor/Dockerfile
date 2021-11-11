
# Image with git and cassandra (cqlsh) client.
# Image can be used to run cql scripts against a cassandra container
#
# Usage:
#
#

FROM cassandra

MAINTAINER cihat@catwithboots.com

# Get netcat and git
RUN apt-get update && apt-get install -y netcat git && rm -rf /var/lib/apt/lists/*
ADD entrypoint.sh /usr/local/bin/

RUN ["chmod", "+x", "/usr/local/bin/entrypoint.sh"]

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
