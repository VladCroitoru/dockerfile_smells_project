FROM icedream/debian-i386:jessie

RUN apt-get update &&\
	apt-get install -y wget tar wine32 build-essential &&\
	wget https://github.com/Yelp/dumb-init/archive/master.tar.gz -O- |\
		tar xz -C /tmp &&\
	cd /tmp/dumb-init* &&\
	make &&\
	mv dumb-init /sbin/dumb-init &&\
	apt-get autoremove --purge -y wget build-essential &&\
	apt-get clean &&\
	adduser --disabled-password --uid 9999 --home /app --gecos "" app &&\
	cd / &&\
	rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*

USER app
WORKDIR /app
ENV WINEPREFIX /app/wine32
ENV WINEARCH win32
RUN /sbin/dumb-init wine wineboot

ENTRYPOINT [ "/sbin/dumb-init", "wine" ]


