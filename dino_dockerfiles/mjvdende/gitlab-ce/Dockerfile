FROM gitlab/gitlab-ce:8.5.4-ce.0

RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
RUN wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | sudo apt-key add -

RUN apt-get update -q
RUN apt-get install -yq postgresql postgresql-contrib postgresql-client

RUN ln -sf /usr/bin/pg_dump /usr/bin/psql /opt/gitlab/embedded/bin/


