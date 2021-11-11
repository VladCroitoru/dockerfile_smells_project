FROM ubuntu:trusty
MAINTAINER MindSwap <mindswap@ro.ru>

RUN echo "deb     http://deb.torproject.org/torproject.org trusty main" >> /etc/apt/sources.list && \
	gpg --keyserver keys.gnupg.net --recv 886DDD89 && \
	gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | apt-key add - && \
	apt-get -y  update && \
	apt-get -y --no-install-recommends install deb.torproject.org-keyring tor && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

RUN mv /var/lib/tor / && \
	ln -s /tor /var/lib/

COPY torrc /etc/tor/	

VOLUME /tor

EXPOSE 9050

CMD ["/usr/bin/tor"]	
