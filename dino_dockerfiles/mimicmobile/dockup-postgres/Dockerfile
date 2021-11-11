FROM mimicmobile/dockup:latest
LABEL maintainer="Jeff Corcoran <jcorcoran+github@gmail.com>"
ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/mimicmobile/dockup-postgres.git" \
      org.label-schema.vcs-ref=$VCS_REF

# install Postgres shell & tools
ENV PG_MAJOR 9.6
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main' $PG_MAJOR > /etc/apt/sources.list.d/pgdg.list
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
RUN apt-get update && apt-get install -y \
    postgresql-client-$PG_MAJOR

ENV PATHS_TO_BACKUP /dockup/pgdump
VOLUME ["/dockup/pgdump"]
ENV POSTGRES_BACKUP_NAME pgdump
ENV BEFORE_BACKUP_CMD ./pgdump.sh
ENV AFTER_BACKUP_CMD ./pgclean.sh
ENV AFTER_RESTORE_CMD ./pgrestore.sh
ENV POSTGRES_USER postgres
ENV POSTGRES_HOST db
ENV POSTGRES_DB postgres
ENV POSTGRES_PORT 5432
COPY /scripts /dockup/
RUN chmod 755 /dockup/*.sh

