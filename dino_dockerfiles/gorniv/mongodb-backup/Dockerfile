FROM ubuntu:14.04
MAINTAINER Tutum Labs <support@tutum.co>

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 && \ 
   	echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list && \ 
    apt-get update && \    
    apt-get install -y mongodb-org-shell && \ 
	apt-get install -y mongodb-org-tools && \    
	echo "mongodb-org-shell hold" | dpkg --set-selections && \ 
	echo "mongodb-org-tools hold" | dpkg --set-selections && \   
	mkdir /backup

ENV CRON_TIME="0 0 * * *"

ADD run.sh /run.sh
VOLUME ["/backup"]
CMD ["/run.sh"]
