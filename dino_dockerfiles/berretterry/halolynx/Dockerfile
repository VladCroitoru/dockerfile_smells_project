FROM ubuntu:14.04
MAINTAINER berretterry@gmail.com
# add CloudPassage repository
RUN echo 'deb http://packages.cloudpassage.com/debian debian main' | tee /etc/apt/sources.list.d/cloudpassage.list > /dev/null
# install curl
RUN apt-get -y install curl
# import CloudPassage public key
RUN curl http://packages.cloudpassage.com/cloudpassage.packages.key | apt-key add -
# update apt repositories
RUN apt-get update > /dev/null
# install the daemon
RUN apt-get -y install cphalo

#install gosu
RUN curl -o /usr/local/bin/gosu -sSL "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture)" && chmod +x /usr/local/bin/gosu

#this is the lynx install
RUN apt-get update && apt-get install -y \
	lynx \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*

#change working directory
WORKDIR /root
#introduce environment variables
#add halo registry script to run to run in the lynx script
ADD halo.sh /root/halo.sh
#add the lynx script that will run halo registration as well as start lynx
ADD lynx.sh /root/lynx.sh
#create entrypoint which should run every time this image is used
ENTRYPOINT ["/root/lynx.sh"]
#command to run lynx which will hopefully be tracked as main PID
#CMD ["./halo.sh"]
