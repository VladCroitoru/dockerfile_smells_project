FROM michaelholttech/baseimage:0.0.2
MAINTAINER Michael Holt <mike@holtit.com>
CMD ["/sbin/my_init"]
ADD puppetlabs-release-trusty.deb /root/puppetlabs-release-trusty.deb
RUN dpkg -i /root/puppetlabs-release-trusty.deb && \
  apt-get update -y && apt-get install -y git ruby-dev cron wget build-essential libsqlite3-dev puppetserver && \
  /usr/bin/puppetserver gem install jdbc-sqlite3 && \
  /usr/bin/puppetserver gem install CFPropertyList && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/puppetlabs-release-trusty.deb && \
  mkdir -p /root/bootstrap/modules && \
  mkdir -p /root/bootstrap/hiera/data && \
  mkdir -p /etc/service/puppetserver && \
  mkdir -p /etc/my_init.d


ADD my_init.d/* /etc/my_init.d/
ADD puppetconf/configure.pp /root/bootstrap/configure.pp
ADD conf/hiera.yaml /root/bootstrap/hiera/hiera.yaml
ADD conf/common.yaml /root/bootstrap/hiera/data/common.yaml
ADD puppetserver.sh /etc/service/puppetserver/run
ADD conf/puppet.conf /etc/puppet/puppet.conf
