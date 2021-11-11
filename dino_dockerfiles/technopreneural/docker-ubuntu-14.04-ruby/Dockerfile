FROM		ubuntu:14.04
MAINTAINER	technopreneural@yahoo.com

#VOLUME		[""]

#EXPOSE		3000

RUN		apt-get update \
		&& DEBIAN_FRONTEND=noninteractive apt-get install -y \
			git-core \
			curl \
			zlib1g-dev \
			build-essential \
			libssl-dev \
			libreadline-dev \
			libyaml-dev \
			libsqlite3-dev \
			sqlite3 \
			libxml2-dev \
			libxslt1-dev \
			libcurl4-openssl-dev \
			python-software-properties \
			libffi-dev

# Install NodeJS
RUN		curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - \
		&& sudo apt-get install -y nodejs

# Install rbenv
RUN		cd \
		&& git clone https://github.com/rbenv/rbenv.git ~/.rbenv \
		&& echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc \
		&& echo 'eval "$(rbenv init -)"' >> ~/.bashrc \
		&& exec $SHELL

RUN		git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build \
		&& echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bashrc \
		&& exec $SHELL

RUN		rbenv install 2.3.1 \
		&& rbenv global 2.3.1 \
		&& ruby -v \

# Install bundler
		&& gem install bundler
