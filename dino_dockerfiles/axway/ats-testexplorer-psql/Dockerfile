FROM ubuntu:18.04
LABEL maintainer="ats.team__@__axway.com"\
    product="Axway ATS TestExplorer with embeded DB"\
    version="4.0.9-SNAPSHOT"

ARG username=atsuser
ARG password=atspassword
ARG workdir=/home/$username/work

USER root

RUN adduser --disabled-password $username

RUN echo "$username:$password" | chpasswd

RUN usermod -a -G sudo $username

ADD ./docker_files $workdir

RUN apt-get update && apt-get -y install wget unzip openjdk-8-jre-headless zip gnupg2 sudo

# Install PostgreSQL-12 (Default version in 18.04 is Postgre 10)
# Create the file repository configuration: ($(lsb_release -cs) not working for bionic - 18.04)
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt bionic-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
# Import the repository signing key:
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
# Update the package lists, install PostgreSQL 12 and remove caches
RUN apt-get update && DEBIAN_FRONTEND="noninteractive" TZ="UTC" apt-get -y install postgresql-12 postgresql-client-12 && rm -rf /var/lib/apt/lists/*

RUN cd $workdir
RUN chmod +x $workdir/config $workdir/entrypoint

RUN $workdir/config

RUN chown -R $username /home/$username

USER $username

EXPOSE 8080 5432

ENV ENTRYPOINT_SCRIPT=$workdir/entrypoint

CMD ["bash","-c","$ENTRYPOINT_SCRIPT"]

