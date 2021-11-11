# Use an old distro for fun
FROM centos:centos6

# install npm
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm \
	&& yum install -y npm

# copy our stuff into /src
COPY . /src

# install dependencies
RUN cd /src && npm install

# expose the port on which our app is gonna run
EXPOSE 8000

# start our app by running entrypoint file
CMD cd /src && node ./blah.js
