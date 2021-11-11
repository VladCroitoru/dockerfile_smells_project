FROM ubuntu:trusty

MAINTAINER Jaroslav Kuchar - https://github.com/jaroslav-kuchar

# install dependencies
RUN apt-get update && apt-get install -y \
	git \
	curl \
	software-properties-common 

# install chef-solo
RUN curl -L https://www.opscode.com/chef/install.sh | bash

# prepare structure
RUN mkdir -p /var/www
WORKDIR /var/www

# clone
RUN git clone https://github.com/KIZI/InBeat.git

# install
WORKDIR InBeat
RUN sudo chef-solo -c ./solo.rb

# configure start script
RUN touch /root/start.sh
RUN echo "#!/bin/bash" >> /root/start.sh
RUN echo "/usr/bin/mongod -f /etc/mongod.conf &" >> /root/start.sh
RUN echo "service nginx start" >> /root/start.sh
RUN echo "sleep 10" >> /root/start.sh
RUN echo "( cd /var/www/InBeat/inbeat && ./start.sh )" >> /root/start.sh
RUN chmod 755 /root/start.sh

EXPOSE 80

ENTRYPOINT ["/root/start.sh"]