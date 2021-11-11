FROM centos/s2i-core-centos7

# PostgreSQL image for OpenShift.
# Volumes:
#  * /var/lib/psql/data   - Database cluster for PostgreSQL
# Environment:
#  * $POSTGRESQL_USER     - Database user name
#  * $POSTGRESQL_PASSWORD - User's password
#  * $POSTGRESQL_DATABASE - Name of the database to create
#  * $POSTGRESQL_ADMIN_PASSWORD (Optional) - Password for the 'postgres'
#                           PostgreSQL administrative account

ENV POSTGRESQL_VERSION=9.6 \
    POSTGRESQL_PREV_VERSION=9.5 \
    HOME=/var/lib/pgsql \
    PGUSER=postgres \
    APP_DATA=/opt/app-root

ENV SUMMARY="PostgreSQL is an advanced Object-Relational database management system" \
    DESCRIPTION="PostgreSQL is an advanced Object-Relational database management system (DBMS). \
The image contains the client and server programs that you'll need to \
create, run, maintain and access a PostgreSQL DBMS server."

LABEL summary="$SUMMARY" \
      description="$DESCRIPTION" \
      io.k8s.description="$DESCRIPTION" \
      io.k8s.display-name="PostgreSQL 9.6" \
      io.openshift.expose-services="5432:postgresql" \
      io.openshift.tags="database,postgresql,postgresql96,rh-postgresql96" \
      name="centos/postgresql-96-centos7" \
      com.redhat.component="rh-postgresql96-docker" \
      version="9.6" \
      usage="docker run -d --name postgresql_database -e POSTGRESQL_USER=user -e POSTGRESQL_PASSWORD=pass -e POSTGRESQL_DATABASE=db -p 5432:5432 centos/postgresql-96-centos7" \
      maintainer="SoftwareCollections.org <sclorg@redhat.com>"

COPY root /
COPY ./s2i/bin/ $STI_SCRIPTS_PATH
RUN chmod +x -R /usr
    
# This image must forever use UID 26 for postgres user so our volumes are
# safe in the future. This should *never* change, the last test is there
# to make sure of that.

RUN yum install -y centos-release-scl-rh && \
    rpm -Uvh http://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm && \
    yum -y update && yum -y install epel-release && \
    yum -y update glibc-common && \
    yum -y install bind-utils gettext hostname nss_wrapper &&\
    #yum -y install bind-utils gettext hostname nss_wrapper openssh-server procps-ng rsync &&\
    #yum -y install postgresql96-server postgresql96-contrib postgresql96 plr96 pgaudit_96 pgbackrest postgis24_96 postgis24_96-client && \
    yum -y install rh-postgresql96 rh-postgresql96-postgresql-contrib rh-postgresql95-postgresql-server  plr96 pgaudit_96 pgbackrest postgis24_96 postgis24_96-client && \
    yum -y clean all && \
    rm -rf /var/cache/yum && \
    cp /usr/pgsql-9.6/share/extension/* /opt/rh/rh-postgresql96/root/usr/share/pgsql/extension && \
    cp /usr/pgsql-9.6/lib/* /opt/rh/rh-postgresql96/root/usr/lib64/pgsql && \
    localedef -f UTF-8 -i en_US en_US.UTF-8 && \
    test "$(id postgres)" = "uid=26(postgres) gid=26(postgres) groups=26(postgres)" && \
    mkdir -p /var/lib/pgsql/data && \
    /usr/libexec/fix-permissions /var/lib/pgsql && \
    /usr/libexec/fix-permissions /var/run/postgresql

# Get prefix path and path to scripts rather than hard-code them in scripts
ENV CONTAINER_SCRIPTS_PATH=/usr/share/container-scripts/postgresql \
    ENABLED_COLLECTIONS=rh-postgresql96
    
# When bash is started non-interactively, to run a shell script, for example it
# looks for this variable and source the content of this file. This will enable
# the SCL for all scripts without need to do 'scl enable'.
ENV BASH_ENV=${CONTAINER_SCRIPTS_PATH}/scl_enable \
    ENV=${CONTAINER_SCRIPTS_PATH}/scl_enable \
    PROMPT_COMMAND=". ${CONTAINER_SCRIPTS_PATH}/scl_enable"

VOLUME ["/var/lib/pgsql/data"]

# {APP_DATA} needs to be accessed by postgres user while s2i assembling
# postgres user changes permissions of files in APP_DATA during assembling
RUN /usr/libexec/fix-permissions ${APP_DATA} && usermod -a -G root postgres

EXPOSE 5432

USER 26

ENTRYPOINT ["container-entrypoint"]
CMD ["run-postgresql"]
