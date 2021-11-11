FROM itsalgeria/baseits
MAINTAINER m.benyoub@itsolutions.dz

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Add the PostgreSQL PGP key to verify their Debian packages.
# It should be the same key as https://www.postgresql.org/media/keys/ACCC4CF8.asc 
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8

# Add PostgreSQL's repository. It contains the most recent stable release
#     of PostgreSQL, ``9.5``.
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" > /etc/apt/sources.list.d/pgdg.list

# Update the Ubuntu and PostgreSQL repository indexes
RUN locale-gen en_US.UTF-8 && update-locale
RUN echo 'LANG="en_US.UTF-8"' > /etc/default/locale

RUN apt-get update && apt-get -yq install postgresql-9.5 postgresql-contrib-9.5

RUN chown -Rf postgres:postgres /var/lib/postgresql #/9.5/main/base
# stop and clear the database as it is init or mounted on container runtime
RUN /etc/init.d/postgresql stop && \
    rm -rf /var/lib/postgresql/9.5

# Execution environment

ADD source/ /etc/postgresql/9.5/main/

RUN apt-get -y -qq install nano htop
ENV TERM xterm

ENV TZ Africa/Algiers
RUN cp /usr/share/zoneinfo/Africa/Algiers /etc/localtime

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /app
VOLUME ["/var/log/postgresql", "/var/lib/postgresql", "/etc/postgresql"]
# Set the default entrypoint (non overridable) to run when starting the container
ENTRYPOINT ["/app/bin/boot"]
# Expose the PostgreSQL port (this is only so you can run backups,
# not to be exposed to the outside world)
EXPOSE 5432
ADD bin /app/bin/
