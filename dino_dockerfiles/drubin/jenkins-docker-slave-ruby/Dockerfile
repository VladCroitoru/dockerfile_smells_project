# Use phusion/baseimage as base image
FROM phusion/baseimage:0.9.15 

MAINTAINER David Rubin <davidrub@gmail.com>

# Set correct environment variables
ENV HOME /root
# Create the ssh host keys needed for sshd
RUN ssh-keygen -A

# Fix sshd's configuration for use within the container. See VW-10576 for details.
RUN sed -i -e 's/^UsePAM .*/UsePAM no/' /etc/ssh/sshd_config
RUN sed -i -e 's/^PasswordAuthentication .*/PasswordAuthentication yes/' /etc/ssh/sshd_config

ENV DEBIAN_FRONTEND noninteractive

# Install postgres
RUN locale-gen en_US.UTF-8
RUN apt-get update
RUN apt-get install -y --force-yes postgresql-9.3 postgresql-client-9.3

# Configure postgres
RUN mkdir -p /usr/local/pgsql/data
RUN chown postgres:postgres /usr/local/pgsql/data
RUN su - postgres -c '/usr/lib/postgresql/9.3/bin/initdb -D /usr/local/pgsql/data/'

# Adjust PostgreSQL configuration so that remote connections to the
# database are possible
# VERY INSECURE! Configure your own users for a production app
RUN echo "host all  all    0.0.0.0/0  trust" >> /usr/local/pgsql/data/pg_hba.conf

# And add ``listen_addresses`` to ``/usr/local/pgsql/data/postgresql.conf``
RUN echo "listen_addresses='*'" >> /usr/local/pgsql/data/postgresql.conf

# Add Postgres to runit
RUN mkdir /etc/service/postgres
ADD run_postgres.sh /etc/service/postgres/run
RUN chown root /etc/service/postgres/run


RUN apt-get -y install wget git

# Install packages for building ruby
RUN apt-get update
RUN apt-get install -y --force-yes build-essential curl git
RUN apt-get install -y --force-yes zlib1g-dev libssl-dev libreadline-dev libyaml-dev libxml2-dev libxslt-dev
RUN apt-get clean

# Install rbenv and ruby-build
RUN git clone https://github.com/sstephenson/rbenv.git /root/.rbenv
RUN git clone https://github.com/sstephenson/ruby-build.git /root/.rbenv/plugins/ruby-build
RUN ./root/.rbenv/plugins/ruby-build/install.sh
ENV PATH /root/.rbenv/bin:$PATH
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh # or /etc/profile
RUN echo 'eval "$(rbenv init -)"' >> .bashrc

# Install multiple versions of ruby
ENV CONFIGURE_OPTS --disable-install-doc
ADD ./versions.txt /root/versions.txt
RUN xargs -L 1 rbenv install < /root/versions.txt

# Install Bundler for each version of ruby
RUN echo 'gem: --no-rdoc --no-ri' >> /.gemrc
RUN bash -l -c 'for v in $(cat /root/versions.txt); do rbenv global $v; gem install bundler; done'


# Clean up APT when done
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Spin-docker currently supports exposing port 22 for SSH and
# one additional application port (Postgres runs on 5432)
EXPOSE 22 5432

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]
