FROM debian:wheezy

ADD package.zip.enc entrypoint.sh /home/

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 && \
	echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.2 main" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list && \
	apt-get update -y && \
	apt-get install less lftp ssh s3cmd wget curl telnet dnsutils net-tools zip unzip vim openssl mongodb-org-shell mongodb-org-tools mysql-client -y && \
	apt-get clean

ENTRYPOINT ["/home/entrypoint.sh"]
	
	