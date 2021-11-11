# Web development environment in node et. al.

# Build: sudo docker build -t peenuty/nodej-npm-sass-docker .


FROM peenuty/rails-passenger-nginx-docker-i:1.0.1
MAINTAINER Richard Gill <peenuty@gmail.com>

# Install Node

	# GET NODE INSTALL DEPS
	RUN       apt-get update --fix-missing
	RUN       apt-get install -y build-essential python wget

	ENV 			NODE_VERSION 0.10.26

	RUN       wget http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.gz
	RUN       tar -zxvf node-v$NODE_VERSION.tar.gz
	RUN       rm node-v$NODE_VERSION.tar.gz
	WORKDIR   node-v0.10.26

	# INSTALL NODE
	RUN       ./configure
	RUN       make
	RUN       make install

	# CLEAN UP
	WORKDIR   ..
	RUN       rm -r node-v$NODE_VERSION
	RUN       apt-get remove -y build-essential python wget

# Grunt needs git
	RUN apt-get -y install git 

# Install Sass

	RUN bash -l -c "gem install sass"

# Install grunt
	RUN npm install -g grunt-cli

# Install Bower
	RUN npm install -g bower

# Install Karma
  RUN npm install -g karma

# Install protractor 
	RUN npm install -g protractor

# Intstall JFK which protractor needs to work
	RUN apt-get -y install openjdk-7-jre-headless

# Setup firefox + a display to run tests.
run     apt-get install -y x11vnc xvfb firefox
run     mkdir ~/.vnc
# Setup a password
run     x11vnc -storepasswd 1234 ~/.vnc/passwd

run 		echo "Xvfb -ac :99 &" > ~/startXserver.sh 
RUN     chmod u+x ~/startXserver.sh

ENV DISPLAY :99



