FROM      martinhoefling/salt-minion:debian
MAINTAINER Martin Hoefling <martin.hoefling@gmx.de>

# push formula
COPY dovecot /srv/salt/dovecot
COPY pillar.example /srv/pillar/example.sls
RUN echo "file_client: local" > /etc/salt/minion.d/local.conf && \
    echo "base:" > /srv/pillar/top.sls  && \
    echo "  '*':" >> /srv/pillar/top.sls  && \
    echo "    - example" >> /srv/pillar/top.sls && \
    salt-call --local --retcode-passthrough state.sls dovecot
