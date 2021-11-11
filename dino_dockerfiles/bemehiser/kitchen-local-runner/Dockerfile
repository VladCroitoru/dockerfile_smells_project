FROM ubuntu:16.04

RUN apt-get update && \
	apt-get install -y \
	build-essential \
	bzip2 \
	docker.io \
    git \
    iproute2 \
    libssl-dev \
    libreadline-dev \
    ruby-dev \
    sudo \
    zlib1g-dev

ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/chef/bin:/opt/chef/embedded/bin \
    CHEF_REPO_PATH=/tmp/chef
ENV COOKBOOK_PATH=$CHEF_REPO_PATH/cookbooks

# Install chef-client
RUN apt-get install -y \
    ca-certificates \
    curl && \
    curl -L --progress-bar https://www.chef.io/chef/install.sh | bash -s -- -P chefdk

# Configure Chef Client
RUN mkdir -p $COOKBOOK_PATH && \
    mkdir -p /etc/chef ~/.chef && \
    echo "cookbook_path %w($COOKBOOK_PATH)" > /etc/chef/client.rb && \
    echo "local_mode true" >> /etc/chef/client.rb && \
    echo "chef_zero.enabled true" >> /etc/chef/client.rb && \
    ln /etc/chef/client.rb ~/.chef/config.rb

# Install rbenv and ruby-build
RUN git clone https://github.com/sstephenson/rbenv.git /usr/local/rbenv && \
	git clone git://github.com/sstephenson/ruby-build.git /usr/local/rbenv/plugins/ruby-build && \
	echo 'export RBENV_ROOT=/usr/local/rbenv' >> /etc/profile.d/rbenv.sh  && \
	echo 'export PATH="$RBENV_ROOT/bin:$PATH"' >> /etc/profile.d/rbenv.sh  && \
	echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh  && \
	chmod +x /etc/profile.d/rbenv.sh && \
	. /etc/profile.d/rbenv.sh
ENV RBENV_ROOT /usr/local/rbenv
ENV PATH "$RBENV_ROOT/bin:$RBENV_ROOT/shims:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

RUN git clone git://github.com/sstephenson/rbenv.git ~/.rbenv && \
	echo 'export PATH=$HOME/.rbenv/bin:$PATH' >> ~/.profile && \
	echo 'eval "$(rbenv init -)"' >> ~/.profile && \
	git clone git://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build

# Install Ruby
RUN rbenv install 2.4.2 && \
	rbenv global 2.4.2 && \
	# Ruby gems
	gem install bundler

RUN mkdir /src
WORKDIR /src

CMD ["bash"]
