# Postgresql (http://www.postgresql.org/)

FROM phusion/baseimage:0.9.13
MAINTAINER Ryan Seto <ryanseto@yak.net>

# Ensure we create the cluster with UTF-8 locale
RUN locale-gen en_US.UTF-8 && \
    echo 'LANG="en_US.UTF-8"' > /etc/default/locale

# Disable SSH (Not using it at the moment).
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

# Install the latest postgresql
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --force-yes \
        postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3 && \
    /etc/init.d/postgresql stop

# Install wal-e
RUN apt-get install -y --force-yes \
    python-pip python-dev \
    libxml2-dev libxslt-dev \
    zlib1g-dev lzop pv
RUN pip install wal-e envdir
RUN pip install "six>=1.7.0"
ADD scripts/init_wale.py /etc/my_init.d/50_init_wale.py
RUN chmod +x /etc/my_init.d/50_init_wale.py

# Install other tools.
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y pwgen inotify-tools

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Cofigure the database to use our data dir.
RUN sed -i -e"s/data_directory =.*$/data_directory = '\/data'/" /etc/postgresql/9.3/main/postgresql.conf
# Allow connections from anywhere.
RUN sed -i -e"s/^#listen_addresses =.*$/listen_addresses = '*'/" /etc/postgresql/9.3/main/postgresql.conf
RUN echo "host    all    all    0.0.0.0/0    md5" >> /etc/postgresql/9.3/main/pg_hba.conf

EXPOSE 5432
ADD scripts /scripts
RUN chmod +x /scripts/start.sh
RUN touch /firstrun

# Add daemon to be run by runit.
RUN mkdir /etc/service/postgresql
RUN ln -s /scripts/start.sh /etc/service/postgresql/run

# Expose our data, log, and configuration directories.
VOLUME ["/data", "/var/log/postgresql", "/etc/postgresql", "/etc/wal-e.d/env"]

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]
