FROM ubuntu:16.04  
RUN  apt-get update && \
 	apt-get install   -y  apt-transport-https     ca-certificates     curl     software-properties-common && \
	apt-get   clean
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN apt-get update && \
 	    apt-key fingerprint 0EBFCD88 && \
 	    add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable" 
RUN apt-get update && \
	apt-get install -y docker-ce && \
 	 apt-get   clean
VOLUME /var/lib/docker	 
CMD dockerd -H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock
