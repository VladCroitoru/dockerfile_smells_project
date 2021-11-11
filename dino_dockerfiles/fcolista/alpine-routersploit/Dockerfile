FROM alpine:latest
MAINTAINER Francesco Colista <fcolista@alpinelinux.org>
ENV PATH=$PATH:/usr/share/routersploit
RUN echo "http://nl.alpinelinux.org/alpine/v3.6/community" >> /etc/apk/repositories && \
    echo "http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
	apk add -U \
		git \
		build-base \
		bash \
		python \
		py-pip \
		python-dev \
		ncurses-dev \
		libffi-dev \
		libressl-dev \
		py-setuptools \
		readline-dev && \
	cd /usr/share && \
    	git clone https://github.com/reverse-shell/routersploit && \
	pip install -r /usr/share/routersploit/requirements.txt && \
	apk del git \
		build-base \
		python-dev \
		readline-dev \
		libffi-dev \
		openssl-dev \
		ncurses-dev \
	&& rm -rf /var/cache/apk/*

WORKDIR /usr/share/routersploit
ENTRYPOINT [ "./rsf.py" ]
