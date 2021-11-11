FROM phusion/baseimage:0.9.13
MAINTAINER Michael Williams
ENV REFRESHED_AT 2015-06-14

# Set correct environment variables.
ENV RUBY_MAJOR 2.2
ENV RUBY_VERSION 2.2.1

# ENV HOME does not seem to work currently; HOME is unset in Docker container.
# See discussion at: https://github.com/phusion/baseimage-docker/issues/119
RUN echo /root > /etc/container_environment/HOME

# Regenerate SSH host keys. baseimage-docker does not contain any, so you
# have to do that yourself. You may also comment out this instruction; the
# init system will auto-generate one during boot.
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

# Baseimage-docker enables an SSH server by default, so that you can use SSH
# to administer your container. In case you do not want to enable SSH, here's
# how you can disable it. Uncomment the following:
#RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

# Use phusion/baseimage's init system.
CMD ["/sbin/my_init"]

# Set the locale.
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# See discussion at: https://github.com/phusion/baseimage-docker/issues/58
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Install dependencies and useful tools.
RUN apt-get update \
	&& apt-get install -y autoconf bison build-essential libssl-dev libyaml-dev libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm3 libgdbm-dev \
	&& apt-get install -y sqlite3 libsqlite3-dev \
	&& apt-get install -y libpq-dev

# Bootstrap install MRI.
# TODO(mtwilliams): Use Rubinius instead?
RUN apt-get install -y ruby \
	&& mkdir -p /usr/src/ruby \
	&& curl -SL "http://cache.ruby-lang.org/pub/ruby/2.2/ruby-2.2.1.tar.gz" | tar -xz -f - -C /usr/src/ruby --strip-components=1 \
	&& cd /usr/src/ruby \
	&& autoconf \
	&& ./configure --disable-install-doc \
	&& make -j"$(nproc)" \
	&& make install \
	&& apt-get purge -y --auto-remove ruby \
	&& rm -r /usr/src/ruby

# Never install documentation for Gems; it useless bloat and RDoc is too slow.
RUN echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc"

# Make Gems globally accessable.
ENV GEM_HOME /usr/local/bundle
ENV PATH $GEM_HOME/bin:$PATH
RUN gem install bundler \
	&& bundle config --global path "$GEM_HOME" \
	&& bundle config --global bin "$GEM_HOME/bin"

# Don't create pesky .bundle folders everywhere.
ENV BUNDLE_APP_CONFIG $GEM_HOME

# Clean up.
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Run the service.
RUN mkdir /etc/service/app
ADD app.sh /etc/service/app/run
ONBUILD ADD ./ /app
ONBUILD RUN cd /app && bundle install
