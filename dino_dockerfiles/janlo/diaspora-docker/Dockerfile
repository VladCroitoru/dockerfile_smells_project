FROM debian:jessie

RUN apt-get update && \
	apt-get -y install --no-install-recommends \
		ca-certificates \
		curl \
		ghostscript \
		git \
		imagemagick \
		mysql-client \
		net-tools \
		nodejs \
		sqlite3 \
		ruby \
		&& \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN groupadd diaspora && \
	useradd --uid 1000 --create-home --home-dir /home/diaspora -g diaspora diaspora

WORKDIR /home/diaspora

ADD ./install_diaspora /home/diaspora/install_diaspora
ADD ./diaspora_dependencies /home/diaspora/diaspora_dependencies

RUN apt-get update && \
	./diaspora_dependencies install && \
	su diaspora -c ./install_diaspora && \
	./diaspora_dependencies remove && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

USER diaspora
ADD database.yml diaspora/config/database.yml
ADD diaspora.yml diaspora/config/diaspora.yml
ADD startit.sh /home/diaspora/startit.sh
 
ENTRYPOINT ["/home/diaspora/startit.sh"]
