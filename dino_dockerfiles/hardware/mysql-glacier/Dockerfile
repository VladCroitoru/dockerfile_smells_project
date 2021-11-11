FROM debian:jessie
MAINTAINER Hardware <contact@meshup.net>

ENV GLACIER_VAULT_NAME=default DBHOST=mysql DBPORT=3306 DBSITE=main

RUN export DEBIAN_FRONTEND=noninteractive \
  && apt-get update && apt-get install -y --no-install-recommends --no-install-suggests \
    mysql-client-5.5 python-pip python-iso8601 python-sqlalchemy git \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN pip install boto && mkdir /tmp/glacier \
  && git clone git://github.com/basak/glacier-cli.git /tmp/glacier \
  && cp /tmp/glacier/glacier.py /usr/local/bin/glacier \
  && rm -rf /tmp/glacier

COPY backup.sh /usr/local/bin/backup.sh
COPY vault.sh /usr/local/bin/vault.sh

RUN chmod +x /usr/local/bin/backup.sh /usr/local/bin/vault.sh

ENTRYPOINT ["/usr/local/bin/backup.sh"]