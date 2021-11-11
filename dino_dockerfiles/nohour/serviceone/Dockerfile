FROM ubuntu:16.04

MAINTAINER vadim


# Install Node...
RUN \
	apt-get update && \
	apt-get -y upgrade && \
	apt-get -y install nodejs && \
	apt-get -y install npm
	
	
# Copy app to /src
COPY . /src

# Install app and dependencies into /src
RUN ln -s /usr/bin/nodejs /usr/bin/node && \ 
     cd /src && \
	 npm install


EXPOSE 3100

CMD cd /src && node ./server.js
