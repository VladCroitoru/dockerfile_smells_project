FROM node:6.10.0 
MAINTAINER Thore Sünert <mail@thoresuenert.de> 

RUN \
  apt-get update -y &&\
  apt-get install openssh-client -y

# Note: npm is v3.10.10
RUN \
	yarn global add ember-cli@2.12.1 &&\
	yarn global add bower &&\
	yarn global add phantomjs-prebuilt &&\
  yarn global add node-sass@3.13.1

# install watchman
# Note: See the README.md to find out how to increase the
# fs.inotify.max_user_watches value so that watchman will 
# work better with ember projects.
RUN \
	git clone https://github.com/facebook/watchman.git &&\
	cd watchman &&\
	git checkout v3.5.0 &&\
	./autogen.sh &&\
	./configure &&\
	make &&\
	make install
