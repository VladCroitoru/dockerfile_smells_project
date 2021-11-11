FROM ubuntu

# Add the PostgreSQL PGP key to verify their Debian packages.
# It should be the same key as https://www.postgresql.org/media/keys/ACCC4CF8.asc
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8

# Add PostgreSQL repository containing the most recent stable release (9.4)
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list

RUN apt-get update

RUN apt-get install -y build-essential python-software-properties software-properties-common postgresql-9.4 postgresql-client-9.4 postgresql-contrib-9.4 libpq-dev

RUN apt-get install -y curl git vim nano

RUN apt-get install -y python-dev python-setuptools

RUN easy_install pip



####################
# PostgreSQL stuff #
####################

# run these commands as user postgres to create databases etc
USER postgres

# Create psql user 'docker' with password 'docker' and have him own a database 'docker'
# which will be the universal database credentials for each application image
RUN /etc/init.d/postgresql start && psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" && createdb -O docker docker

RUN sed -i '1s/^/local all docker trust\n/' /etc/postgresql/9.4/main/pg_hba.conf

##################
# End PostgreSQL #
##################



USER root

ENV PYTHONUNBUFFERED 1
ADD requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt


WORKDIR /srv/www/emissary/emissary

ADD start.sh /root/start.sh
RUN chmod +x /root/start.sh

ENTRYPOINT ["/root/start.sh"]
