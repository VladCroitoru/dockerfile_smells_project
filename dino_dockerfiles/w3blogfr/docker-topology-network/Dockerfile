FROM ubuntu

RUN apt-get update \
	 &&  apt-get install -y net-tools nmap \
	 &&  rm -rf /var/lib/apt/lists/*

ADD start.sh /start.sh

RUN chmod +x /start.sh

CMD ["/start.sh"]

