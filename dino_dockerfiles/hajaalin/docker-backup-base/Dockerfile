# Use phusion/passenger-full as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/passenger-docker/blob/master/Changelog.md for
# a list of version numbers.
#FROM phusion/passenger-full:<VERSION>
# Or, instead of the 'full' variant, use one of these:
#FROM phusion/passenger-ruby18:<VERSION>
#FROM phusion/passenger-ruby19:<VERSION>
FROM phusion/passenger-ruby20
#FROM phusion/passenger-ruby21:<VERSION>
#FROM phusion/passenger-nodejs:<VERSION>
#FROM phusion/passenger-customizable:<VERSION>

# Set correct environment variables.
ENV HOME /root

# Add MongoDB Repository:
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10
RUN echo 'deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list

# Add postgres 9.3 Repository:
RUN curl -s -O https://www.postgresql.org/media/keys/ACCC4CF8.asc
RUN apt-key add ACCC4CF8.asc
RUN	sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >> /etc/apt/sources.list.d/postgresql.list'


RUN apt-get -qq update
RUN apt-get -yqq install mongodb-org-tools postgresql-client-9.3 vim gnupg && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN gem install backup whenever

# Use baseimage-docker's init process.
CMD ["/sbin/my_init"]