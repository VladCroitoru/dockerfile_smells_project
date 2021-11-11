############################################################
# nginx-passenger
############################################################

FROM ubuntu
MAINTAINER Daniel Bidulock

#
# Installation
#
RUN apt-get update

# Install git
RUN apt-get install -y git python-virtualenv


# Install latest ruby
RUN apt-get install -y git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties libffi-dev

#
# 2015-12-18 
# rbenv/ruby install adapted from https://gist.github.com/deepak/5925003
#
# Install rbenv
RUN git clone https://github.com/sstephenson/rbenv.git /usr/local/rbenv
RUN echo '# rbenv setup' > /etc/profile.d/rbenv.sh
RUN echo 'export RBENV_ROOT=/usr/local/rbenv' >> /etc/profile.d/rbenv.sh
RUN echo 'export PATH="$RBENV_ROOT/bin:$PATH"' >> /etc/profile.d/rbenv.sh
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh
RUN chmod +x /etc/profile.d/rbenv.sh

# install ruby-build
RUN mkdir /usr/local/rbenv/plugins
RUN git clone https://github.com/sstephenson/ruby-build.git /usr/local/rbenv/plugins/ruby-build

ENV RBENV_ROOT /usr/local/rbenv

ENV PATH "$RBENV_ROOT/bin:$RBENV_ROOT/shims:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
# does not work. PATH is set to
# $RBENV_ROOT/shims:$RBENV_ROOT/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# install ruby2
RUN rbenv install 2.2.3
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc
RUN rbenv global 2.2.3
RUN gem install bundler


#
# Nginx and Passenger
#

# Install our PGP key and add HTTPS support for APT
RUN sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 561F9B9CAC40B2F7
RUN sudo apt-get install -y apt-transport-https ca-certificates

# Add our APT repository
RUN sudo sh -c 'echo deb https://oss-binaries.phusionpassenger.com/apt/passenger trusty main > /etc/apt/sources.list.d/passenger.list'
RUN sudo apt-get update

# Install Passenger + Nginx
RUN sudo apt-get install -y nginx-extras passenger

#
# Configuration
#

# Enable Passenger
RUN sed -i -e 's/# passenger_root \/usr\/lib\/ruby\/vendor_ruby\/phusion_passenger\/locations.ini;/passenger_root \/usr\/lib\/ruby\/vendor_ruby\/phusion_passenger\/locations.ini;/g' /etc/nginx/nginx.conf
# The path to ruby is set above
RUN sed -i -e 's/# passenger_ruby \/usr\/bin\/passenger_free_ruby;/passenger_ruby \/usr\/local\/rbenv\/shims\/ruby;/g' /etc/nginx/nginx.conf

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

VOLUME ["/var/cache/nginx"]

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]

