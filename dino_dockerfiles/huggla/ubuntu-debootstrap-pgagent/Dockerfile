FROM blitznote/debootstrap-amd64:16.04

RUN apt-get update \
 && apt-get install -y pgagent \
 && rm -rf /var/lib/apt/lists/* \
 && groupadd --gid 70 postgres \
 && useradd --uid 70 --gid 70 postgres \
 && mkdir /run/secrets \
 && touch /run/secrets/.pgpass \
 && chown postgres:postgres /run/secrets/.pgpass \
 && chmod u=r,go= /run/secrets/.pgpass \
 && chown postgres:postgres /usr/bin/pgagent \
 && chmod 6555 /usr/bin/pgagent

VOLUME /run/secrets

ENV PGPASSFILE=/run/secrets/.pgpass
ENV HOSTADDR=''
ENV DBNAME=postgres
ENV USER=postgres

USER nobody

ENTRYPOINT [ "/bin/sh", "-c" ]
CMD [ "/usr/bin/pgagent -f hostaddr=${HOSTADDR} dbname=${DBNAME} user=${USER}" ]
