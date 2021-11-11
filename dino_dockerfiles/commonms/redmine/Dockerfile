# Common MS - Redmine (with Git Hosting)
FROM redmine
MAINTAINER Jose M. Fernandez-Alba <jm.fernandezalba@commonms.com>

# Git ssh
EXPOSE 22

# Redmine root directory
ENV REDMINE_ROOT /usr/src/redmine

# Install dependencies
RUN apt-get update && apt-get install -y \
	sudo \
	pkg-config \
	openssh-server \
	build-essential \
	libssh2-1 \
	libssh2-1-dev \
	cmake \
	libgpg-error-dev \
	&& rm -rf /var/lib/apt/lists/*

# Prepare home and permissions
COPY redmine_sudoers /etc/sudoers.d/redmine

RUN mkhomedir_helper redmine \
	&& usermod -a -G staff redmine

RUN chown redmine:redmine -R $REDMINE_ROOT \
	&& chmod 775 -R /usr/local/bundle \
	&& chmod 440 /etc/sudoers.d/redmine

# Plugin installation
WORKDIR $REDMINE_ROOT/plugins
RUN gosu redmine git clone https://github.com/jbox-web/redmine_bootstrap_kit.git \
	&& cd redmine_bootstrap_kit \
	&& git checkout 0.2.4

RUN gosu redmine git clone https://github.com/jbox-web/redmine_git_hosting.git \
	&& cd redmine_git_hosting \
	&& git checkout 1.2.1

# Install Gitolite
RUN useradd -m git

WORKDIR /home/git
RUN gosu git git clone git://github.com/sitaramc/gitolite \
	&& gosu git mkdir bin \
	&& gosu git mkdir repositories
RUN sudo -HEu git gitolite/install -to /home/git/bin

# Set repositories directory as volume
VOLUME /home/git/repositories

# Prepare the entry point
COPY entrypoint_gitolite.sh /sbin/
RUN chmod 755 /sbin/entrypoint_gitolite.sh

WORKDIR $REDMINE_ROOT

ENTRYPOINT ["/sbin/entrypoint_gitolite.sh"]

CMD ["rails", "server", "-b", "0.0.0.0"]
